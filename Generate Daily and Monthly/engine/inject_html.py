import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\template.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

# I want to inject after the top 10 fastest and slowest programs grid-2
# Let's find the closing div of grid-2 inside the transactions section.

inject_html = r"""
        {% if trx_watchlist_errors %}
        <div style="margin-top: 32px; background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 16px;">
            <h3 style="margin-top: 0; color: #e11d48; margin-bottom: 12px; font-size: 14px; display: flex; align-items: center; gap: 8px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                Critical Programs Error Watchlist
            </h3>
            <p style="margin: 0 0 12px 0; font-size: 12px; color: #9f1239;">Menangkap error detail (termasuk parameter jika tercatat) dari program utama EFS.</p>
            <div class="table-wrap">
                <table class="wide" style="background: white; margin: 0;">
                    <thead>
                        <tr style="background: #ffe4e6;">
                            <th style="width: 25%; color: #be123c;">Program Name</th>
                            <th style="width: 10%; color: #be123c; text-align: center;">Error Count</th>
                            <th style="width: 65%; color: #be123c;">Error Message / Parameter</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in trx_watchlist_errors %}
                        <tr>
                            <td style="color: #881337; font-weight: 500;">{{ item.program }}</td>
                            <td style="text-align: center;"><span class="badge critical">{{ item.count }}</span></td>
                            <td style="font-family: monospace; font-size: 11px; white-space: pre-wrap; color: #9f1239; background: #fff5f5; padding: 8px;">{{ item.message }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        {% endif %}
"""

# In template.html, the transaction section ends with:
# </div> </div> </section><section class="section" id="xla">
idx_section_end = text.find('</section><section class="section" id="xla">')

# Wait, let's find the closing tag of the transactions section
# </div>
#         {% endif %}
#     </div>
# </div>
# </section>

if "Critical Programs Error Watchlist" not in text:
    text = text[:idx_section_end] + inject_html + text[idx_section_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected HTML logic.")
