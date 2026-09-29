import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

idx = text.find('elif pilihan == "3":')
end_idx = text.find('elif pilihan == "8":')

print(text[idx:end_idx].encode('utf-8', 'ignore').decode('ascii', 'ignore'))
