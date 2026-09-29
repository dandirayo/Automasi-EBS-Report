import os
import re

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

new_logo = r"""def print_logo():
    print("\033[96m" + r'''
  ██████╗  █████╗ ██╗██╗     ██╗   ██╗    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
  ██╔══██╗██╔══██╗██║██║     ╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
  ██║  ██║███████║██║██║      ╚████╔╝     ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
  ██║  ██║██╔══██║██║██║       ╚██╔╝      ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
  ██████╔╝██║  ██║██║███████╗   ██║       ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    ''' + "\033[0m")
    print("  \033[90mby dandirayo\033[0m\n")
    print("=" * 80)
    print("  \033[97m\033[1mEFS DAILY & MONTHLY HEALTH REPORT ENGINE\033[0m")
    print("  \033[92m[\u2713] Auto-Sync OneDrive (Departemen CBS - EFS): Terhubung & Sinkron\033[0m")
    print("=" * 80)
    print()"""

# Manual replacement without re.sub
idx1 = text.find("def print_logo():")
idx2 = text.find("print()", idx1) + 7
if idx1 != -1 and idx2 != -1:
    text = text[:idx1] + new_logo + text[idx2:]

menu_regex = r'print\("  \\033\[96mPilih Mode Generate:\\033\[0m"\).*?print\("  └──────────────────────────────────────────────────────────────────────────┘"\)'
new_menu = r"""print("  \033[96mPilih Mode Generate:\033[0m")
        print("  ┌── DAILY ─────────────────────────────────────────────────────────────────┐")
        print("  │                                                                          │")
        print("  │ [1]  📄 Generate H-1 (Kemarin)                                           │")
        print("  │ [2]  📅 Generate tanggal tertentu (Manual)                               │")
        print("  │ [3]  📦 Batch: 3 hari terakhir                                           │")
        print("  │ [4]  📦 Batch: 7 hari terakhir (1 Minggu)                                │")
        print("  │ [5]  📦 Batch: Dari awal bulan sampai H-1                                │")
        print("  │ [6]  📦 Batch: Custom range                                              │")
        print("  │ [7]  📦 Batch: 1 Bulan Penuh (Misal: agustus 2026)                       │")
        print("  │ [8]  📁 Tarik Excel Mentah Saja (H-1)                                    │")
        print("  │ [9]  📁 Tarik Excel Mentah Saja (Batch 3 hari)                           │")
        print("  │ [10] 📁 Tarik Excel Mentah Saja (1 Bulan Penuh)                          │")
        print("  │                                                                          │")
        print("  ├── MONTHLY ───────────────────────────────────────────────────────────────┤")
        print("  │                                                                          │")
        print("  │ [11] 📄 Generate Monthly (Misal: agustus2026)                            │")
        print("  │ [12] 📁 Tarik Excel Mentah Monthly Saja                                  │")
        print("  │                                                                          │")
        print("  ├── ONEDRIVE / TEAMS ──────────────────────────────────────────────────────┤")
        print("  │ [13] 🔄 Sync / Update Folder OneDrive Manual                             │")
        print("  ├── PENGATURAN SISTEM ─────────────────────────────────────────────────────┤")
        print("  │ [14] ⚙️  Auto-Nyala & Auto-Sync saat Komputer Nyala                       │")
        print("  ├── LAINNYA ───────────────────────────────────────────────────────────────┤")
        print("  │ [16] 🎭 Generate Laporan Dummy H-1 (Tanpa Branding)                      │")
        print("  │                                                                          │")
        print("  │ [15] ❌ Keluar / Exit                                                    │")
        print("  └──────────────────────────────────────────────────────────────────────────┘")"""

text = re.sub(menu_regex, new_menu, text, flags=re.DOTALL)

text = text.replace('global date_str, month_str, year_str, report_date_display, is_monthly_mode, current_output_dir', 
                    'global date_str, month_str, year_str, report_date_display, is_monthly_mode, current_output_dir, is_dummy_mode\n    is_dummy_mode = False')
if 'is_dummy_mode = False' not in text[:2000]:
    text = text.replace('is_monthly_mode = False', 'is_monthly_mode = False\nis_dummy_mode = False')

confirm_logic = r"""pilihan = input("  Pilihan [1-16]: ").strip()
        
        if pilihan == "15":
            print("\n  \033[92m Sampai jumpa!\033[0m\n")
            break

        if pilihan in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16"]:
            konfirmasi = input("\n  Eksekusi pilihan ini? (Y/N): ").strip().upper()
            if konfirmasi != 'Y':
                print("  \033[93mDibatalkan. Kembali ke menu utama...\033[0m")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue"""

text = re.sub(r'pilihan = input\("  Pilihan \[1-15\]: "\)\.strip\(\)\s+if pilihan == "15":\s+print\("\\n  \\033\[92m Sampai jumpa!\\033\[0m\\n"\)\s+break', confirm_logic, text)

opt_1_regex = r'elif pilihan == "1":\s+if not args\.silent:\s+gen_email = input\("Generate draf email summary \(Y/N\)\? "\)\.strip\(\)\.lower\(\) == \'y\'\s+run_report_for_date\(default_date, generate_email=gen_email\)'
opt_1_new = r"""elif pilihan == "1":
            if not args.silent:
                gen_email = input("  Generate draf email summary (Y/N)? ").strip().lower() == 'y'
            else:
                gen_email = False
            run_report_for_date(default_date, generate_email=gen_email)

        elif pilihan == "16":
            is_dummy_mode = True
            gen_email = input("  Generate draf email summary (Y/N)? ").strip().lower() == 'y'
            run_report_for_date(default_date, generate_email=gen_email)
            is_dummy_mode = False"""

text = re.sub(opt_1_regex, opt_1_new, text)

text = text.replace("template = env.get_template('template.html')\n    html_out = template.render(all_data)", 
                    "template = env.get_template('template.html')\n    all_data['is_dummy_mode'] = globals().get('is_dummy_mode', False)\n    html_out = template.render(all_data)")

# We should scrub 'BNI' from top slowest strings if is_dummy_mode is True
# But I can just do it in template.html for easier rendering logic!
# Wait, for dummy mode, the user also mentioned "Kantor" or "BNI". 
# The HTML template uses "PT Bank Negara Indonesia (Persero) Tbk", "Departemen CBS - EFS", and "EFS Daily Health Report"

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Main menu fixed!")
