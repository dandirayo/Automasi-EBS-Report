import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Find the confirm execution part
find_str = """konfirmasi = input("\\n  Eksekusi pilihan ini? (Y/N): ").strip().lower()
            if konfirmasi != 'y':
                continue"""

replace_str = """konfirmasi = input("\\n  Eksekusi pilihan ini? (Y/N): ").strip().lower()
            if konfirmasi != 'y':
                continue
            
            # Khusus untuk pilihan generate (selain 1 dan 1A yang sudah ter-define), tanyakan AI
            if pilihan in ["2", "3", "4", "5", "6", "7", "11"]:
                tanya_ai = input("  Gunakan Analisis AI (API)? Proses akan lebih lama (Y/N): ").strip().lower()
                if tanya_ai != 'y':
                    os.environ['SKIP_AI'] = '1'
                elif 'SKIP_AI' in os.environ:
                    del os.environ['SKIP_AI']
"""

if find_str in text:
    text = text.replace(find_str, replace_str)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected AI prompt for batch successfully!")
else:
    print("Could not find the confirm prompt.")
