import re
import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\template.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

# The exact block I injected was:
# {% if chart_cpu or chart_memory or chart_disk %}
# <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">
# ...
# </div>
# {% endif %}

pattern = re.compile(r'\{% if chart_cpu or chart_memory or chart_disk %\}.*?<div style="grid-column: 1 / -1; max-width: 50%; margin: 0 auto;">.*?</div>\s*</div>\s*\{% endif %\}', re.DOTALL)
text, count = pattern.subn('', text)
print(f'Removed {count} full blocks')

# Also remove any stranded elements
text = re.sub(r'<div><img src="file:///\{\{\s*chart_cpu\s*\|\s*replace[^\}]+\}\}"[^>]+></div>', '', text)
text = re.sub(r'<div><img src="file:///\{\{\s*chart_memory\s*\|\s*replace[^\}]+\}\}"[^>]+></div>', '', text)
text = re.sub(r'<div[^>]*><img src="file:///\{\{\s*chart_disk\s*\|\s*replace[^\}]+\}\}"[^>]+></div>', '', text)
text = re.sub(r'\{% if chart_cpu %\}', '', text)
text = re.sub(r'\{% if chart_memory %\}', '', text)
text = re.sub(r'\{% if chart_disk %\}', '', text)
text = re.sub(r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">\s*</div>', '', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
