import re
import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\template.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

infra_chart_html = r"""
{% if chart_cpu or chart_memory or chart_disk %}
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">
    {% if chart_cpu %}
    <div><img src="file:///{{ chart_cpu | replace('\\', '/') }}" style="width: 100%; height: auto; display: block; border-radius: 8px;" /></div>
    {% endif %}
    {% if chart_memory %}
    <div><img src="file:///{{ chart_memory | replace('\\', '/') }}" style="width: 100%; height: auto; display: block; border-radius: 8px;" /></div>
    {% endif %}
    {% if chart_disk %}
    <div style="grid-column: 1 / -1; max-width: 50%; margin: 0 auto;"><img src="file:///{{ chart_disk | replace('\\', '/') }}" style="width: 100%; height: auto; display: block; border-radius: 8px;" /></div>
    {% endif %}
</div>
{% endif %}
</section>
"""
text = re.sub(r'</thead><tbody>\s*\{\%\s*for host, metrics in infra_hosts_summary\.items\(\)\s*\%\}.*?</tbody></table></div></section>',
              lambda m: m.group(0).replace('</section>', infra_chart_html), text, flags=re.DOTALL)

concurrent_chart_html = r"""
{% if chart_concurrent %}
<div style="margin-bottom: 24px;">
    <img src="file:///{{ chart_concurrent | replace('\\', '/') }}" style="width: 100%; height: auto; display: block; border-radius: 8px;" />
</div>
{% endif %}
<div class="grid-2">
"""
text = text.replace('<div class="grid-2">', concurrent_chart_html, 1)

xla_chart_html = r"""
{% if chart_xla %}
<div style="margin-top: 16px; margin-bottom: 24px;">
    <img src="file:///{{ chart_xla | replace('\\', '/') }}" style="width: 100%; height: auto; display: block; border-radius: 8px;" />
</div>
{% endif %}
<div class="table-wrap"><table><thead><tr><th>Periode</th>
"""
text = text.replace('<div class="table-wrap"><table><thead><tr><th>Periode</th>', xla_chart_html, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Inserted clean charts!")
