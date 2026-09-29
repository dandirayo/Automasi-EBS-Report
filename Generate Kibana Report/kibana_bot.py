import os
import re
import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Load konfigurasi dari file .env
load_dotenv()
KIBANA_USERNAME = os.getenv("KIBANA_USERNAME", "")
KIBANA_PASSWORD = os.getenv("KIBANA_PASSWORD", "")

DASHBOARDS = {
    "L1_Transaction_EFS": "https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/09f9a35d-ee51-4290-9a98-2b4729f5ec85?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-24h%2Fh,to:now))",
    "L2_Infra_EFS_DB": "https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/74f6689c-3120-4ef6-842b-0fd06f7327ad?_g=(filters:!(),refreshInterval:(pause:!f,value:300000),time:(from:now-1d,to:now))",
    "L2_Infra_EFS_App": "https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/9ba19c88-763e-4c5f-a95d-86fea0fe09d8?_g=(filters:!(),refreshInterval:(pause:!f,value:300000),time:(from:now-8h,to:now))",
    "L1_EFS_Availability": "https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/96e8bce1-f494-4df6-a5fb-c7a9fe34ddf2?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-24h%2Fh,to:now))"
}

def set_kibana_time(url, timeframe):
    return re.sub(r'time:\(from:.*?,to:.*?\)', f'time:(from:{timeframe},to:now)', url)

def auto_login(page):
    """Fungsi khusus untuk mengisi form login secara otomatis"""
    print("[INFO] Mencoba login otomatis menggunakan kredensial di .env...")
    try:
        # Menunggu kotak input username muncul
        page.wait_for_selector('input[name="username"]', timeout=10000)
        
        # Ketik username & password
        page.fill('input[name="username"]', KIBANA_USERNAME)
        page.fill('input[name="password"]', KIBANA_PASSWORD)
        
        # Klik tombol Log In
        # Mencari tombol yang mengandung teks 'Log In' atau 'Login' atau type submit
        try:
            page.click('button[type="submit"]', timeout=3000)
        except:
            page.click('button:has-text("Log In")', timeout=3000)
            
        print("[SUCCESS] Form login berhasil diisi dan disubmit!")
        
        # Tunggu sampai URL berubah dari halaman login (maksimal 30 detik)
        page.wait_for_url("**/app/dashboards**", timeout=30000)
        print("[SUCCESS] Berhasil masuk ke Kibana Dashboard!")
        
    except Exception as e:
        print(f"[ERROR] Gagal melakukan auto-login: {e}")
        print("[WARN] Pastikan username & password di file .env sudah benar.")

def main(timeframe):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    user_data_dir = os.path.join(base_dir, "edge_bot_profile")
    os.makedirs(user_data_dir, exist_ok=True)
    report_dir = os.path.join(base_dir, "Hasil_Report")
    os.makedirs(report_dir, exist_ok=True)

    print(f"[INFO] Folder kerja aktif: {base_dir}")
    print(f"[INFO] Memulai automasi untuk rentang waktu: {timeframe}")
    
    if not KIBANA_USERNAME or "isi_dengan" in KIBANA_USERNAME:
        print("[ERROR] Anda belum mengisi Username dan Password di file .env!")
        return

    with sync_playwright() as p:
        print("[INFO] Meluncurkan browser Edge bawaan...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False,
            viewport={'width': 1920, 'height': 1080},
            args=['--start-maximized']
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        for name, original_url in DASHBOARDS.items():
            target_url = set_kibana_time(original_url, timeframe)
            print(f"\n[INFO] Membuka dashboard: {name}...")
            
            try:
                page.goto(target_url, timeout=60000)
            except Exception as e:
                print(f"[WARN] Batas waktu tunggu load awal halaman habis, mencoba lanjut... ({e})")
            
            # Beri sedikit waktu agar halaman benar-benar memutuskan apakah harus redirect ke login
            page.wait_for_timeout(3000)
            
            if "login" in page.url.lower() or "sso" in page.url.lower():
                print("\n" + "="*50)
                print("[WARNING] TERDETEKSI HALAMAN LOGIN!")
                auto_login(page)
                print("="*50 + "\n")
            
            print("[INFO] Menunggu dashboard selesai memuat data...")
            try:
                page.wait_for_load_state("networkidle", timeout=60000)
            except Exception as e:
                print("[WARN] Peringatan: Loading jaringan lambat, memaksa lanjut ambil gambar...")
            
            # Waktu ekstra untuk render grafik
            time.sleep(8)
            
            safe_timeframe = timeframe.replace("-", "_").replace("/", "_")
            filename = os.path.join(report_dir, f"{name}_{safe_timeframe}.png")
            
            try:
                page.screenshot(path=filename, full_page=True)
                print(f"[SUCCESS] Berhasil! Screenshot full-page tersimpan di: {filename}")
            except Exception as e:
                print(f"[WARN] Screenshot full-page gagal ({e}). Mencoba screenshot biasa...")
                try:
                    page.screenshot(path=filename, full_page=False)
                    print(f"[SUCCESS] Berhasil! Screenshot biasa tersimpan di: {filename}")
                except Exception as e2:
                    print(f"[ERROR] Screenshot gagal sama sekali: {e2}")

        browser.close()
        print("\n[INFO] Proses ambil gambar selesai semuanya!")

if __name__ == "__main__":
    # Eksekusi untuk 24 jam terakhir (H-1)
    waktu_pilihan = "now-24h" 
    main(waktu_pilihan)
