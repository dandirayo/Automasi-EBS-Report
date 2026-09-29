import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# I need to insert [1A] ✨ Daily: H-1 (Dengan Analisis AI) back into the menu string.
search_str = 'print("  │ [1]  📄 Daily: H-1 (Kemarin)                                             │")'

if search_str in text:
    # 74 width inside box.
    # length of `[1A] ✨ Daily: H-1 (Dengan Analisis AI)` -> 5 chars + 2(emoji) + 33 chars = 40.
    # 74 - 40 = 34 spaces. Let's compute exact pad for 1A just like others.
    # Ref: `[1]  📄 Daily: H-1 (Kemarin)` had 43 pad.
    # `[1]  📄 Daily: H-1 (Kemarin)` length is 31 in python. 31 + 43 = 74.
    # `[1A] ✨ Daily: H-1 (Dengan Analisis AI)` length is 39 in python. 74 - 39 = 35.
    
    replace_str = search_str.replace('Daily: H-1 (Kemarin)', 'Daily: H-1 (Offline / Tanpa AI)')
    # wait, earlier length: `[1]  📄 Daily: H-1 (Offline / Tanpa AI)` is 39 in python. 74 - 39 = 35.
    
    line1 = '        print("  │ [1]  📄 Daily: H-1 (Offline / Tanpa AI)                          │")\n'
    line1A = '        print("  │ [1A] ✨ Daily: H-1 (API / Pakai AI)                              │")\n'
    
    text = text.replace(search_str, line1 + line1A)
    
    # Also fix the input loop options if 1A is missing from valid choices
    text = text.replace('if pilihan in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16"]:',
                        'if pilihan in ["1", "1A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16"]:')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed menu 1A")
else:
    print("Could not find search str")
