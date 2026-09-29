import os
import json
import time
from datetime import datetime, timedelta
import glob
import threading
import subprocess
import sys

try:
    import telebot
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
except ImportError:
    print("Modul pyTelegramBotAPI belum terinstall. Sedang menginstall...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])
    import telebot
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load config
ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(ENGINE_DIR, 'config.json')

with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)

BOT_TOKEN = CONFIG.get('telegram_bot_token', '').strip()
ALLOWED_USER_ID = str(CONFIG.get('telegram_allowed_userid', '')).strip()

if not BOT_TOKEN:
    print("ERROR: telegram_bot_token di config.json belum diisi!")
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# Import main.py logic softly so we can call it
import main

def is_allowed(user_id):
    user_id_str = str(user_id)
    if not ALLOWED_USER_ID:
        return True
    if user_id_str != ALLOWED_USER_ID:
        print(f"[BLOCKED] Pesan dari user ID tidak dikenal: {user_id_str}")
        return False
    return True

@bot.message_handler(commands=['my_id'])
def send_id(message):
    bot.reply_to(message, f"🆔 User/Chat ID Anda adalah:\n`{message.chat.id}`\n\nSilakan copy angka di atas dan masukkan ke dalam `telegram_allowed_userid` di config.json agar lebih aman.")

@bot.message_handler(commands=['start', 'menu', 'generate_daily'])
def send_menu(message):
    if not is_allowed(message.chat.id):
        bot.reply_to(message, "⛔ Akses Ditolak. Anda tidak terdaftar sebagai admin bot ini.")
        return
        
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    btn1 = InlineKeyboardButton("📄 Tarik PDF H-1 (Kemarin)", callback_data="gen_h1")
    btn2 = InlineKeyboardButton("📦 Tarik PDF Batch (3 Hari Terakhir)", callback_data="gen_3days")
    markup.add(btn1, btn2)
    
    msg_text = "👋 Halo! Silakan pilih menu Laporan EFS di bawah ini:"
    if not ALLOWED_USER_ID:
         msg_text += "\n\n⚠️ PERINGATAN: `telegram_allowed_userid` belum diset di config.json!"
         
    bot.send_message(message.chat.id, msg_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if not is_allowed(call.message.chat.id):
        bot.answer_callback_query(call.id, "Akses Ditolak!")
        return

    # Acknowledge button press
    bot.answer_callback_query(call.id, "Perintah diterima! Sedang diproses...")

    if call.data == "gen_h1":
        bot.send_message(call.message.chat.id, "⏳ Memproses Laporan H-1... Mohon tunggu (biasanya 10-30 detik).")
        threading.Thread(target=run_report_job, args=(call.message.chat.id, 1)).start()
        
    elif call.data == "gen_3days":
        bot.send_message(call.message.chat.id, "⏳ Memproses Laporan 3 Hari Terakhir... Ini akan memakan waktu sekitar 1-2 menit.")
        threading.Thread(target=run_report_job, args=(call.message.chat.id, 3)).start()


def run_report_job(chat_id, days_to_run):
    try:
        if 'SKIP_AI' in os.environ:
            del os.environ['SKIP_AI']
        
        main.ensure_onedrive_running()
        main.sync_onedrive(interactive=False)
        
        # Loop over the number of days backwards (e.g. if 3: H-3, H-2, H-1)
        for i in range(days_to_run, 0, -1):
            target_dt = datetime.now() - timedelta(days=i)
            date_str = target_dt.strftime("%Y%m%d")
            bot.send_message(chat_id, f"🔄 Sedang menyusun laporan tanggal {date_str}...")
            
            success = main.run_report_for_date(target_dt, generate_email=False)
            
            if success:
                month_str = target_dt.strftime("%B")
                out_dir = os.path.join(main.DAILY_OUTPUT_DIR, month_str, date_str)
                pdf_files = glob.glob(os.path.join(out_dir, "*.pdf"))
                
                if pdf_files:
                    pdf_files.sort(key=os.path.getmtime, reverse=True)
                    latest_pdf = pdf_files[0]
                    with open(latest_pdf, 'rb') as doc:
                        bot.send_document(chat_id, doc, caption=f"✅ Laporan EFS {date_str} Berhasil!")
                else:
                    bot.send_message(chat_id, f"⚠️ Proses {date_str} berhasil, tapi file PDF tidak ditemukan.")
            else:
                bot.send_message(chat_id, f"❌ Gagal men-generate laporan {date_str} (File Excel di Teams mungkin belum lengkap).")
                
    except Exception as e:
        bot.send_message(chat_id, f"💥 Terjadi kesalahan sistem: {str(e)}")

print("="*60)
print("🤖 TELEGRAM BOT LISTENER BERJALAN 🤖")
print("="*60)
print("Menunggu perintah dari Telegram...")
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except Exception as e:
    print(f"Error: {e}")
