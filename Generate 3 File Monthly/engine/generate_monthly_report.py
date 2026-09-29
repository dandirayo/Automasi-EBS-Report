import sys
import os
import shutil
from docx import Document
from pptx import Presentation
import win32com.client

# Import engine dari Automasi Daily
sys.path.append(r"C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly")
from engine import main as engine_main

def replace_text_in_docx(doc_path, output_path, mapping):
    doc = Document(doc_path)
    for p in doc.paragraphs:
        for key, val in mapping.items():
            if key in p.text:
                for run in p.runs:
                    if key in run.text:
                        run.text = run.text.replace(key, val)
                if key in p.text:
                    p.text = p.text.replace(key, val)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for key, val in mapping.items():
                        if key in p.text:
                            for run in p.runs:
                                if key in run.text:
                                    run.text = run.text.replace(key, val)
                            if key in p.text:
                                p.text = p.text.replace(key, val)
    doc.save(output_path)
    print(f"[+] Berhasil membuat Notin DOCX: {output_path}")

def replace_text_in_pptx(ppt_path, output_path, mapping):
    prs = Presentation(ppt_path)
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                for key, val in mapping.items():
                    if key in shape.text:
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                if key in run.text:
                                    run.text = run.text.replace(key, val)
                        if key in shape.text:
                            shape.text = shape.text.replace(key, val)
            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        for key, val in mapping.items():
                            if key in cell.text:
                                for paragraph in cell.text_frame.paragraphs:
                                    for run in paragraph.runs:
                                        if key in run.text:
                                            run.text = run.text.replace(key, val)
                                if key in cell.text:
                                    cell.text = cell.text.replace(key, val)
    prs.save(output_path)
    print(f"[+] Berhasil membuat PPTX: {output_path}")



def parse_month_input(user_input):
    """Parse 'agustus 2026', '0826', dll"""
    user_input = user_input.lower().strip().replace(" ", "")
    
    # Mapping ID to EN for processing
    months_id = ["januari", "februari", "maret", "april", "mei", "juni", 
                 "juli", "agustus", "september", "oktober", "november", "desember"]
    months_en = ["January", "February", "March", "April", "May", "June", 
                 "July", "August", "September", "October", "November", "December"]
    
    # Very basic parsing
    target_month_en = None
    target_month_id = None
    target_year = "2026"
    month_idx = -1
    
    for i, m in enumerate(months_id):
        if m in user_input:
            month_idx = i
            # try to extract year, e.g. "agustus2026"
            rem = user_input.replace(m, "")
            if "2026" in rem or "26" in rem: target_year = "2026"
            elif "2025" in rem or "25" in rem: target_year = "2025"
            break
            
    if month_idx == -1:
        # Check by English month
        for i, m in enumerate(months_en):
            if m.lower() in user_input:
                month_idx = i
                break
                
    if month_idx == -1:
        print("Format bulan tidak dikenali! Harap gunakan format seperti 'Agustus 2026'")
        sys.exit(1)
        
    target_month_id = months_id[month_idx].capitalize()
    target_month_en = months_en[month_idx]
    
    # Prev month logic
    prev_idx = (month_idx - 1) % 12
    prev_month_id = months_id[prev_idx].capitalize()
    prev_month_en = months_en[prev_idx]
    
    return target_month_en, target_month_id, target_year, prev_month_en, prev_month_id, f"{month_idx+1:02d}"

def main():
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input("Masukkan bulan & tahun (contoh: Agustus 2026): ")
        
    month_en, month_id, year, prev_en, prev_id, month_num = parse_month_input(user_input)
    yyyymm = f"{year}{month_num}"
    
    print(f"\n[*] Target: {month_id} {year} ({month_en})")
    
    # Sync and copy files directly from OneDrive using engine logic
    engine_main.setup_monthly(month_en, int(year))
    download_dir = os.path.join(engine_main.ROOT_DIR, ".cache", "monthly_downloads", yyyymm)
    print("\n[*] Menarik data dari OneDrive...")
    local_paths = engine_main.copy_monthly_files(month_en, year, download_dir)
    
    # Check if files exist
    missing = [k for k, v in local_paths.items() if not v]
    if missing:
        print(f"\n[!] ERROR: File sumber untuk {month_en} {year} belum lengkap di OneDrive!")
        print(f"    Missing: {', '.join(missing)}")
        print("    Mohon pastikan file sudah di-upload ke Teams/OneDrive.")
        sys.exit(1)
        
    print("\n[*] Memproses Metrik Data (XLA, Infra, Transactions, GL)...")
    all_data = {}
    
    # Kumpulkan semua data untuk rendering PDF
    all_data.update(engine_main.process_xla(local_paths['XLA']))
    all_data.update(engine_main.process_infra(local_paths['Infrastructures']))
    all_data.update(engine_main.process_transactions(local_paths['Transactions']))
    all_data.update(engine_main.process_gl(local_paths['GL']))
    
    # Generate Charts required for the PDF
    all_data.update(engine_main.generate_charts(all_data))
    
    # Alias variables for mapping
    xla_data = all_data
    infra_data = all_data
    
    # --- Ekstrak P99 untuk Tabel Notin DOCX ---
    print("[*] Memetakan P99 Concurrent Job untuk Notin...")
    import pandas as pd
    try:
        df_trx = pd.read_excel(local_paths['Transactions'], sheet_name='Summary', header=2)
        prog_dict = {}
        for _, row in df_trx.iterrows():
            name = str(row.get('Program Name', '')).strip().lower()
            val = row.get('P99 (min)', 0)
            if pd.isna(val): val = 0
            p99 = f"{float(val):.2f}".replace('.', ',')
            prog_dict[name] = p99
    except Exception as e:
        print(f"[-] Gagal membaca sheet Summary: {e}")
        prog_dict = {}

    def find_p99(search_str):
        search_str = search_str.lower()
        # Exact match first
        if search_str in prog_dict:
            return prog_dict[search_str]
        # Partial match
        for k, v in prog_dict.items():
            if search_str in k or k in search_str:
                return v
        return "-"

    
    # Construct mappings for the template tags
    mapping = {
        "{{BULAN_TAHUN}}": f"{month_id} {year}",
        "{{MONTH_YEAR}}": f"{month_en} {year}",
        "{{MONTH_YEAR_UPPER}}": f"{month_en.upper()} {year}",
        "{{BULAN}}": month_id,
        "{{MONTH}}": month_en,
        "{{MONTH_UPPER}}": month_en.upper(),
        "{{BULAN_LALU}}": prev_id,
        "{{MONTH_PREV}}": prev_en,
        "{{YYYYMM}}": yyyymm,
        
        "{{XLA_SUCCESS_PCT}}": f"{xla_data.get('xla_success_pct', '0')}%".replace(".", ","),
        "{{XLA_PROCESSED}}": str(xla_data.get('xla_processed', '0')).replace(",", "."),
        "{{XLA_TOTAL_JUTA}}": f"{float(str(xla_data.get('xla_total','0')).replace(',',''))/1000000:.1f} juta".replace(".", ","),
        "{{XLA_UNPROCESSED}}": str(xla_data.get('xla_unprocessed', '0')).replace(",", "."),
        "{{XLA_ERROR}}": str(xla_data.get('xla_e', '0')).replace(",", "."),
        
        "{{INFRA_CRITICAL}}": str(infra_data.get('infra_critical_count', '0')),
        
        # P99 Concurrent Jobs Mapping
        "{{P99_PROG_1}}": find_p99("BNI GL Laporan Trial Balance Per Currency V2"),
        "{{P99_PROG_2}}": find_p99("BNI GL Laporan Trial Balance"),
        "{{P99_PROG_3}}": find_p99("Gather Schema Statistic"),
        "{{P99_PROG_4}}": find_p99("Accounting Program"),
        "{{P99_PROG_5}}": find_p99("FAH Process"),
        "{{P99_PROG_6}}": find_p99("Create Accounting"),
        "{{P99_PROG_7}}": find_p99("Transfer Journal Entries to GL"),
        "{{P99_PROG_8}}": find_p99("Program - Import Journals") if find_p99("Program - Import Journals") != "-" else find_p99("Journal Import"),
        "{{P99_PROG_9}}": find_p99("Report Set"),
        "{{P99_PROG_10}}": find_p99("BNI FAH Journal Reversal"),
        "{{P99_PROG_11}}": find_p99("Validate App Acct Definitions") if find_p99("Validate App Acct Definitions") != "-" else find_p99("Validate Application Accounting Definitions"),
        "{{P99_PROG_12}}": find_p99("BNI GL Lap Jurnal Trx Entity"),
        "{{P99_PROG_13}}": find_p99("Subledger Period Close Exceptions"),
        "{{P99_PROG_14}}": find_p99("Update Subledger Acct Balances") if find_p99("Update Subledger Acct Balances") != "-" else find_p99("Update Subledger Accounting Balances"),
        "{{P99_PROG_15}}": find_p99("Posting: Single Ledger"),
        "{{P99_PROG_16}}": find_p99("OAM Dashboard Collection"),
        "{{P99_PROG_17}}": find_p99("Workflow Background Process"),
        "{{P99_PROG_18}}": find_p99("BNI GL Interface Kurs Harian"),
    }
    
    # Define output files
    template_dir = r"C:\Users\901191\Music\Automasi EFS\Generate 3 File Monthly\engine\Template_Master"
    output_dir = r"C:\Users\901191\Music\Automasi EFS\Generate 3 File Monthly\Output"
    
    template_docx = os.path.join(template_dir, "Master_Template_Notin.docx")
    template_pptx = os.path.join(template_dir, "Master_Template_Presentation.pptx")
    
    output_docx = os.path.join(output_dir, f"Draft Notin Penyampaian Monthly Report CBS {month_id} - Enterprise Financial System (EFS).docx")
    output_pptx = os.path.join(output_dir, f"{yyyymm} - EFS Monthly Report - {month_en} {year}.pptx")
    output_pdf = os.path.join(output_dir, f"{yyyymm} - EFS Monthly Report - {month_en} {year}.pdf")
    
    print("\n[*] Men-generate File Laporan...")
    replace_text_in_docx(template_docx, output_docx, mapping)
    replace_text_in_pptx(template_pptx, output_pptx, mapping)
    
    # Generate HTML-based PDF using the daily engine
    print("[*] Merender PDF Laporan Vertikal (seperti format Daily)...")
    generated_engine_pdf = engine_main.generate_pdf(all_data)
    if generated_engine_pdf and os.path.exists(generated_engine_pdf):
        try:
            shutil.copy2(generated_engine_pdf, output_pdf)
            print(f"[+] Berhasil membuat PDF: {output_pdf}")
        except PermissionError:
            fallback_pdf = output_pdf.replace(".pdf", "_baru.pdf")
            shutil.copy2(generated_engine_pdf, fallback_pdf)
            print(f"[!] File utama sedang dibuka. Menyimpan sebagai: {fallback_pdf}")
    else:
        print("[-] Gagal membuat PDF melalui Engine.")
    print("\n[+] Selesai! Seluruh 3 file berhasil di-generate secara otomatis.")

if __name__ == "__main__":
    main()
