import re
import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Replace menu 1
pattern = re.compile(r'print\("  \u2502 \[1\]  \U0001f4c4 Daily: H-1 \(Kemarin\).*?\u2502"\)\n')
replacement = '        print("  \u2502 [1]  \U0001f4c4 Daily: H-1 (Offline / Tanpa AI)                          \u2502")\n'
replacement += '        print("  \u2502 [1A] ✨ Daily: H-1 (API / Pakai AI)                              \u2502")\n'

text, count = pattern.subn(replacement, text)
print(f"Replaced {count} times.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
