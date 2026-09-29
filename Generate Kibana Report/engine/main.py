import os
import sys
import json
import time
import shutil
import re
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# ==========================================
# 1. KONFIGURASI PATH & ENV
# ==========================================
ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ENGINE_DIR)
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
CONFIG_FILE = os.path.join(ENGINE_DIR, 'config.json')

os.makedirs(OUTPUT_DIR, exist_ok=True)
load_dotenv(os.path.join(ROOT_DIR, '.env'))

KIBANA_USERNAME = os.getenv("KIBANA_USERNAME", "")
KIBANA_PASSWORD = os.getenv("KIBANA_PASSWORD", "")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

CONFIG = load_config()
URLS = CONFIG.get("urls", {})

# ==========================================
# 2. LOGO & UTILS
# ==========================================
def print_logo():
    logo = """
\033[96m
  ██╗  ██╗██╗██████╗  █████╗ ███╗   ██╗ █████╗ 
  ██║ ██╔╝██║██╔══██╗██╔══██╗████╗  ██║██╔══██╗
  █████╔╝ ██║██████╔╝███████║██╔██╗ ██║███████║
  ██╔═██╗ ██║██╔══██╗██╔══██║██║╚██╗██║██╔══██║
  ██║  ██╗██║██████╔╝██║  ██║██║ ╚████║██║  ██║
  ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
\033[0m
================================================================================
  KIBANA AUTOMATION REPORT ENGINE
================================================================================
"""
    print(logo)

def set_kibana_time(url, timeframe):
    return re.sub(r'time:\(from:.*?,to:.*?\)', f'time:(from:{timeframe},to:now)', url)

def auto_login(page):
    print("  \033[93m[INFO] Mendeteksi halaman login. Melakukan Auto-Login...\033[0m")
    try:
        page.wait_for_selector('input[name="username"]', timeout=10000)
        page.fill('input[name="username"]', KIBANA_USERNAME)
        page.fill('input[name="password"]', KIBANA_PASSWORD)
        try:
            page.click('button[type="submit"]', timeout=3000)
        except:
            page.click('button:has-text("Log In")', timeout=3000)
            
        print("  \033[92m[SUCCESS] Berhasil submit form login!\033[0m")
        page.wait_for_url("**/app/dashboards**", timeout=30000)
        print("  \033[92m[SUCCESS] Masuk ke Dashboard Kibana.\033[0m")
    except Exception as e:
        print(f"  \033[91m[ERROR] Gagal auto-login: {e}\033[0m")

# ==========================================
# 3. CORE LOGIC: SCREENSHOT & EXCEL
# ==========================================
def run_automation(mode):
    date_str = datetime.now().strftime("%Y%m%d")
    ts = datetime.now().strftime("%H%M%S")
    out_folder = os.path.join(OUTPUT_DIR, date_str)
    os.makedirs(out_folder, exist_ok=True)
    
    run_prefix = f"Run_{ts}"
    timeframe = "now-24h" # Bisa diganti dari argumen CLI nantinya
    
    if not KIBANA_USERNAME or "isi_dengan" in KIBANA_USERNAME:
        print("\n\033[91m[ERROR] Anda belum mengisi Username/Password di file .env!\033[0m")
        return

    print("\n\033[93m[INFO] Menyiapkan Robot Browser Edge...\033[0m")
    
    with sync_playwright() as p:
        user_data_dir = os.path.join(ROOT_DIR, "edge_bot_profile")
        os.makedirs(user_data_dir, exist_ok=True)
        
        is_headless = CONFIG.get("browser", {}).get("headless", False)
        
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=is_headless,
            viewport={'width': 1920, 'height': 1080},
            args=['--start-maximized']
        )
        
        page = browser.pages[0] if browser.pages else browser.new_page()

        # --- TAHAP 1 & 2: SCREENSHOT DASHBOARD ---
        if mode in [1, 3]:
            print("\n\033[96m[1/2] Mengambil Screenshots (Timeframe: 24h)...\033[0m")
            
            for key, original_url in URLS.items():
                target_url = set_kibana_time(original_url, timeframe)
                print(f"\n  📸 Memproses: {key}...")
                
                try:
                    page.goto(target_url, timeout=60000)
                except Exception as e:
                    print(f"  \033[91m[WARN] Timeout load awal, lanjut... ({e})\033[0m")
                
                page.wait_for_timeout(3000)
                
                if "login" in page.url.lower() or "sso" in page.url.lower():
                    auto_login(page)
                
                print("  ⏳ Menunggu rendering grafik Kibana...")
                try:
                    page.wait_for_load_state("networkidle", timeout=60000)
                except:
                    pass
                time.sleep(8) # Extra wait for charts
                
                ss_path = os.path.join(out_folder, f"{run_prefix}_{key}.png")
                try:
                    # Dashboard pertama panjang, sisanya top viewport saja sesuai desain engine
                    if key == "web1_full":
                        page.screenshot(path=ss_path, full_page=True)
                    else:
                        page.screenshot(path=ss_path, full_page=False)
                    print(f"  \033[92m[SUCCESS] Disimpan: {os.path.basename(ss_path)}\033[0m")
                except Exception as e:
                    print(f"  \033[91m[ERROR] Gagal screenshot {key}: {e}\033[0m")

        # --- TAHAP 3: EXTRACT DATA (EXCEL) ---
        if mode in [2, 3]:
            print("\n\033[96m[2/2] Mengekstrak Data ke Excel (Simulasi)...\033[0m")
            excel_path = os.path.join(out_folder, f"{run_prefix}_Kibana_Data.xlsx")
            try:
                dummy_data = {
                    'Metric': ['CPU Usage', 'Memory Usage', 'Error Rate', 'Total Hits'],
                    'Value': ['85%', '92%', '1.2%', '45,210'],
                    'Status': ['Warning', 'Critical', 'Healthy', 'Healthy']
                }
                df = pd.DataFrame(dummy_data)
                df.to_excel(excel_path, index=False)
                print(f"  📊 Berhasil membuat Excel: {os.path.basename(excel_path)}")
            except Exception as e:
                print(f"  \033[91m[ERROR] Gagal mengekstrak Excel: {e}\033[0m")

        browser.close()
        
    print("\n\033[92m" + "=" * 80)
    print(f"  ✨ SELESAI! Hasil disimpan di folder:")
    print(f"  📂 {out_folder}")
    print("=" * 80 + "\033[0m\n")


# ==========================================
# 4. ENTRY POINT
# ==========================================
if __name__ == "__main__":
    os.system('color')
    print_logo()

    print("  \033[96mPilih Mode Eksekusi:\033[0m")
    print("  ┌───────────────────────────────────────────────┐")
    print("  │  [1]  📸 Screenshot Saja (4 SS)               │")
    print("  │  [2]  📊 Excel Saja (Ekstrak Data)            │")
    print("  │  [3]  📸 + 📊 Screenshot & Excel Lengkap      │")
    print("  └───────────────────────────────────────────────┘")
    
    while True:
        pilihan = input("  Pilihan [1-3]: ").strip()
        if pilihan in ["1", "2", "3"]:
            run_automation(int(pilihan))
            break
        else:
            print("  \033[91m❌ Pilihan tidak valid!\033[0m")
