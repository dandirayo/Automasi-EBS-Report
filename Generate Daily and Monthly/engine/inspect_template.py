import re
with open(r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\template.html', encoding='utf-8') as f:
    text = f.read()

infra_idx = text.find('id="infra"')
print("Infra:")
print(text[max(0, infra_idx-100):infra_idx+800])

slo_idx = text.find('id="slo"')
print("\nSLO:")
print(text[max(0, slo_idx-100):slo_idx+800])

trx_idx = text.find('id="transactions"')
print("\nTransactions:")
print(text[max(0, trx_idx-100):trx_idx+800])
