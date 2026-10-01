with open(r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\template.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="gl"')
idx_end = text.find('</section>', idx)
print(text[idx:idx_end+10].encode('ascii', 'backslashreplace').decode('ascii'))
