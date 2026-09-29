from playwright.sync_api import sync_playwright
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
user_data_dir = os.path.join(base_dir, "edge_bot_profile")
# Pakai URL Dashboard 1 sebagai pancingan
url = "https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/09f9a35d-ee51-4290-9a98-2b4729f5ec85"

def main():
    print("="*60)
    print("Mempersiapkan Tahap 1: PANCINGAN LOGIN...")
    print("="*60)
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge",
            headless=False, # Harus False agar user bisa interaksi
            viewport={'width': 1920, 'height': 1080},
            args=['--start-maximized']
        )
        
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        try:
            print("\n[INFO] Membuka halaman login Kibana...")
            page.goto(url, timeout=60000)
        except Exception as e:
            print(f"[WARN] Timeout saat load awal, tapi kita abaikan. ({e})")
            
        print("\n\n" + "!"*60)
        print("[ACTION REQUIRED] (TINDAKAN DIBUTUHKAN):")
        print("1. Silakan login pada browser Edge yang baru saja terbuka.")
        print("2. Jika Anda sudah berhasil masuk dan melihat grafik Kibana...")
        print("3. TUTUP BROWSER TERSEBUT (Klik Tanda Silang/X di pojok kanan atas).")
        print("!"*60 + "\n")
        print("Menunggu Anda menyelesaikan login dan menutup browser... (Waktu tidak terbatas)")
        
        # Script akan terus berhenti (pause) di sini SAMPAI pengguna menekan tombol X pada browser.
        try:
            page.wait_for_event("close", timeout=0)
        except Exception as e:
            pass # Abaikan error jika tertutup paksa
            
        browser.close()
        print("\n[SUCCESS] BROWSER DITUTUP! Sesi login Anda telah berhasil direkam dan disimpan!")
        print("[SUCCESS] Tahap 1 SELESAI.")

if __name__ == "__main__":
    main()
