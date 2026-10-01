import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# find where df_hourly is loaded
idx_load = text.find("df_hourly = pd.read_excel(path, sheet_name='EFS Programs Hourly', header=2)")
idx_end_load = text.find("\n", idx_load)

inject_load = """
    try:
        df_err_msg = pd.read_excel(path, sheet_name='Trx by Error Type Msg', header=2)
        clean_cols(df_err_msg, ['Count'])
        watchlist = [
            "FAH Process", "Report Set", "Create Accounting", "Accounting Program",
            "Journal Import", "Posting", "Transfer Journal to GL", "Interface Kurs Harian",
            "BNI FAH Journal Reversal", "BNI GL Jurnal Trx Entity V2", "BNI FAH Laporan Konfigurasi"
        ]
        watchlist_err = []
        for _, row in df_err_msg.iterrows():
            prog_name = str(row.get('Program Name', ''))
            if prog_name in watchlist:
                msg = str(row.get('Message', '')).strip()
                # filter out 'completed normal' type messages
                if 'completed normal' not in msg.lower() and msg.lower() != 'normal' and 'completed warning' not in msg.lower():
                    watchlist_err.append({
                        'program': prog_name,
                        'message': msg,
                        'count': int(row.get('Count', 0))
                    })
    except Exception:
        watchlist_err = []
"""

# inject loading logic
if "df_err_msg = pd.read_excel" not in text:
    text = text[:idx_end_load] + "\n" + inject_load + text[idx_end_load:]

# find return dict
idx_return = text.find("return {", text.find("def process_transactions("))
idx_end_return = text.find("}", idx_return)

inject_return = "        'trx_watchlist_errors': watchlist_err,\n    "

if "'trx_watchlist_errors'" not in text:
    text = text[:idx_end_return] + inject_return + text[idx_end_return:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected Python logic.")
