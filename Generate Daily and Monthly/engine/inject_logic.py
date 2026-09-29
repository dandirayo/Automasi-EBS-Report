import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

find_str = """
        dates_to_run = []
        is_download_only = False
"""

replace_str = """
        valid_choices = ["1", "1a", "1A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16", ""]
        if pilihan not in valid_choices:
            print("  \033[91mPilihan tidak valid!\033[0m")
            import time
            time.sleep(1)
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
            
        if pilihan != "":
            konfirmasi = input("\\n  Eksekusi pilihan ini? (Y/N): ").strip().lower()
            if konfirmasi != 'y':
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

        # Tanya AI untuk batch/manual
        if pilihan in ["2", "3", "4", "5", "6", "7", "11"]:
            tanya_ai = input("  Gunakan Analisis AI (API)? Proses ini akan memakan waktu lebih lama (Y/N): ").strip().lower()
            if tanya_ai != 'y':
                os.environ['SKIP_AI'] = '1'
            elif 'SKIP_AI' in os.environ:
                del os.environ['SKIP_AI']

        dates_to_run = []
        is_download_only = False
"""

if find_str in text:
    text = text.replace(find_str, replace_str)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected logic successfully!")
else:
    print("Could not find anchor string.")
