import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Current menu string for 1:
search_str = '        print("  │ [1]  📄 Daily: H-1 (Kemarin)                                             │")\n'

if search_str in text:
    replace_str = '        print("  │ [1]  📄 Daily: H-1 (Offline / Tanpa AI)                          │")\n'
    replace_str += '        print("  │ [1A] ✨ Daily: H-1 (API / Pakai AI)                              │")\n'
    
    text = text.replace(search_str, replace_str)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Re-added 1A successfully!")
else:
    print("Search string for 1A not found.")
