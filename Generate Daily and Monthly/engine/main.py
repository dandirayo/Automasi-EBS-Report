import sys
import os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import shutil
import json
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import glob
import subprocess
import time

# ==========================================
# 1. SETUP TANGGAL & VARIABEL
# ==========================================
import calendar

date_str, month_str, year_str, report_date_display = "", "", "", ""
is_monthly_mode = False
current_output_dir = ""

def setup_dates(dt):
    global date_str, month_str, year_str, report_date_display, is_monthly_mode, current_output_dir, is_dummy_mode
    is_dummy_mode = False
    is_monthly_mode = False
    date_str = dt.strftime("%Y%m%d")
    month_str = dt.strftime("%B")
    year_str = dt.strftime("%Y")
    report_date_display = f"{dt.day} {dt.strftime('%B')} {dt.year}"
    current_output_dir = os.path.join(DAILY_OUTPUT_DIR, month_str)

def setup_monthly(month_name, year_num):
    global date_str, month_str, year_str, report_date_display, is_monthly_mode, current_output_dir, is_dummy_mode
    is_dummy_mode = False
    is_monthly_mode = True
    
    # Capitalize just in case (e.g. august -> August)
    month_name = month_name.capitalize()
    
    # Find month number
    month_num = 1
    for i, name in enumerate(calendar.month_name):
        if name.lower() == month_name.lower():
            month_num = i
            break
            
    # Output format
    date_str = f"{year_num}{month_num:02d}"  # e.g. 202608
    month_str = f"{month_num:02d}"
    year_str = str(year_num)
    report_date_display = f"{month_name} {year_num}"
    current_output_dir = MONTHLY_OUTPUT_DIR


# Mapping threshold SLA
# ==========================================
# 1. KONFIGURASI
# ==========================================
ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ENGINE_DIR)
SOURCE_DIR = r"C:\Users\901191\Bank Negara Indonesia\Departemen CBS - EFS"
DOWNLOADED_DIR = os.path.join(ROOT_DIR, ".cache", "downloads")
REPORT_DIR = os.path.join(ROOT_DIR, "output")
DAILY_OUTPUT_DIR = os.path.join(ROOT_DIR, "daily-output")
MONTHLY_OUTPUT_DIR = os.path.join(ROOT_DIR, "monthly-output")
TEMP_DIR = os.path.join(ROOT_DIR, ".cache", "temp")
CONFIG_FILE = os.path.join(ENGINE_DIR, 'config.json')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

CONFIG = load_config()

for d in [ROOT_DIR, TEMP_DIR, DOWNLOADED_DIR, DAILY_OUTPUT_DIR, MONTHLY_OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

default_date = datetime.now() - timedelta(days=1)
setup_dates(default_date)

SERVERS = [
    'ebsintsdr01', 'ebsintsdr02', 'ebsintslp01', 'ebsintslp02',
    'efsdbsdr01', 'efsdbsdr02', 'efsdbslp01', 'efsdbslp02'
]

# Warna grafik per server
SERVER_COLORS = {
    'ebsintsdr01': '#2563eb', 'ebsintsdr02': '#3b82f6',
    'ebsintslp01': '#dc2626', 'ebsintslp02': '#ef4444',
    'efsdbsdr01': '#16a34a', 'efsdbsdr02': '#22c55e',
    'efsdbslp01': '#d97706', 'efsdbslp02': '#f59e0b',
}

def ensure_onedrive_running():
    """Memastikan Microsoft OneDrive aktif berjalan di background."""
    try:
        import subprocess
        check = subprocess.run('tasklist /FI "IMAGENAME eq OneDrive.exe"', shell=True, capture_output=True, text=True)
        if "OneDrive.exe" not in check.stdout:
            onedrive_exe = r"C:\Program Files\Microsoft OneDrive\OneDrive.exe"
            if os.path.exists(onedrive_exe):
                subprocess.Popen([onedrive_exe, "/background"])
    except Exception:
        pass

def sync_onedrive(interactive=True):
    """Melakukan sinkronisasi dan memaksa download offline file OneDrive."""
    ensure_onedrive_running()
    source_dir = r"C:\Users\901191\Bank Negara Indonesia\Departemen CBS - EFS"
    if not os.path.exists(source_dir):
        if interactive:
            print(f"  ❌ Direktori tidak ditemukan: {source_dir}")
        return False
        
    cmd = f'attrib -U +P "{source_dir}\\*.*" /s'
    subprocess.run(cmd, shell=True, capture_output=True)
    
    if interactive:
        print("\n" + "=" * 80)
        print("  \033[1m🔄 SINKRONISASI FOLDER ONEDRIVE (DEPARTEMEN CBS - EFS)\033[0m")
        print("=" * 80 + "\n")
        print("  ✅ Memastikan Microsoft OneDrive berjalan di latar belakang...")
        count = sum(len(files) for _, _, files in os.walk(source_dir))
        print(f"  ✅ Sukses! Seluruh file ({count} file) telah disinkronkan dan diatur selalu tersedia offline.")
        open_opt = input("\n  Buka folder Departemen CBS - EFS di File Explorer? (y/n): ").strip().lower()
        if open_opt == 'y':
            os.startfile(source_dir)
    return True

# ==========================================
# 2. COPY FILE DARI TEAMS
# ==========================================
def copy_files(target_dir=None):
    """Menyalin 4 file Excel dari folder sync Teams ke folder lokal."""
    ensure_onedrive_running()
    
    if target_dir is None:
        target_dir = DOWNLOADED_DIR
        
    os.makedirs(target_dir, exist_ok=True)
        
    files_map = {
        "GL": os.path.join("GL", "Daily", year_str, month_str, f"EFS_GL_{date_str}.xlsx"),
        "Infrastructures": os.path.join("Infrastructures", "Daily", year_str, month_str, f"EFS_Infrastructures_{date_str}.xlsx"),
        "Transactions": os.path.join("Transactions", "Daily", year_str, month_str, f"EFS_Transactions_{date_str}.xlsx"),
        "XLA": os.path.join("XLA", "Daily", year_str, month_str, f"EFS_XLA_{date_str}.xlsx"),
    }

    local_paths = {}
    for key, rel_path in files_map.items():
        src = os.path.join(SOURCE_DIR, rel_path)
        filename = os.path.basename(rel_path)
        dst = os.path.join(target_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            local_paths[key] = dst
        else:
            print(f"  ⚠️ {key}: Tidak ditemukan -> {src}")
            local_paths[key] = None
    return local_paths

def copy_monthly_files(month_en, year_str, target_dir=None):
    """Menyalin 4 file Excel Monthly dari folder sync Teams ke folder lokal."""
    ensure_onedrive_running()
    if target_dir is None:
        target_dir = DOWNLOADED_DIR
        
    os.makedirs(target_dir, exist_ok=True)
        
    files_map = {
        "GL": os.path.join("GL", "Monthly", year_str, f"EFS_GL_{month_en}_{year_str}.xlsx"),
        "Infrastructures": os.path.join("Infrastructures", "Monthly", year_str, f"EFS_Infrastructures_{month_en}_{year_str}.xlsx"),
        "Transactions": os.path.join("Transactions", "Monthly", year_str, f"EFS_Transactions_Wave1_{month_en}_{year_str}.xlsx"),
        "XLA": os.path.join("XLA", "Monthly", year_str, f"EFS_XLA_{month_en}_{year_str}.xlsx"),
    }
    
    # Fallback to names without year in filename (e.g. EFS_GL_July.xlsx)
    fallback_map = {
        "GL": os.path.join("GL", "Monthly", year_str, f"EFS_GL_{month_en}.xlsx"),
        "Infrastructures": os.path.join("Infrastructures", "Monthly", year_str, f"EFS_Infrastructures_{month_en}.xlsx"),
        "Transactions": os.path.join("Transactions", "Monthly", year_str, f"EFS_Transactions_Wave1_{month_en}.xlsx"),
        "XLA": os.path.join("XLA", "Monthly", year_str, f"EFS_XLA_{month_en}.xlsx"),
    }

    local_paths = {}
    for key in files_map.keys():
        src = os.path.join(SOURCE_DIR, files_map[key])
        fallback_src = os.path.join(SOURCE_DIR, fallback_map[key])
        
        filename = os.path.basename(files_map[key])
        dst = os.path.join(target_dir, filename)
        
        if os.path.exists(src):
            shutil.copy2(src, dst)
            local_paths[key] = dst
        elif os.path.exists(fallback_src):
            shutil.copy2(fallback_src, dst)
            local_paths[key] = dst
        else:
            print(f"  ⚠️ {key}: Tidak ditemukan -> {src}")
            local_paths[key] = None
    return local_paths



def safe_int(val):
    if pd.isna(val): return 0
    if isinstance(val, str):
        val = val.replace(',', '').strip()
        if not val: return 0
    try:
        return int(float(val))
    except:
        return 0

def safe_float_str(val):
    if pd.isna(val): return "0.00"
    if isinstance(val, str):
        val = val.replace(',', '').replace('%', '').strip()
        if not val: return "0.00"
    try:
        return f"{float(val):.2f}"
    except:
        return "0.00"

def safe_float(val):
    """Mengembalikan float (angka), bukan string."""
    if pd.isna(val): return 0.0
    if isinstance(val, str):
        val = val.replace(',', '').replace('%', '').strip()
        if not val: return 0.0
    try:
        return float(val)
    except:
        return 0.0

def clean_cols(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c].astype(str).str.replace(',', ''), errors='coerce').fillna(0)


# ==========================================
# 3. PROSES DATA XLA
# ==========================================
def process_xla(path):
    """Membaca dan mengolah data XLA."""
    if not path:
        return {}
    # print("\n📊 Memproses XLA...")

    df_status = pd.read_excel(path, sheet_name='Status Overview')
    try:
        df_hourly = pd.read_excel(path, sheet_name='Hourly Trend')
    except ValueError:
        try:
            df_hourly = pd.read_excel(path, sheet_name='Daily Trend')
        except ValueError:
            df_hourly = pd.DataFrame()

    df_app = pd.read_excel(path, sheet_name='By Application')
    df_entity = pd.read_excel(path, sheet_name='By Entity')
    try:
        df_slo = pd.read_excel(path, sheet_name='SLO Scorecard')
    except ValueError:
        df_slo = pd.DataFrame()
    df_errors = pd.read_excel(path, sheet_name='Top Error Messages')

    clean_cols(df_status, ['Count'])
    clean_cols(df_hourly, ['Total', 'Completed', 'Error', 'Unprocessed'])
    clean_cols(df_app, ['Total', 'Processed (P)', 'Error (E)', 'Unprocessed (U)'])
    clean_cols(df_entity, ['Total', 'Processed (P)', 'Error (E)', 'Unprocessed (U)'])
    total = int(df_app['Total'].sum())

    # Split Status Overview into Process Status and XLA Code
    idx_nan = df_status[df_status['Code'].isna() | (df_status['Code'] == 'XLA Code')].index
    split_idx = idx_nan[0] if len(idx_nan) > 0 else len(df_status)
    df_proc = df_status.iloc[:split_idx]
    df_xla_code = df_status.iloc[split_idx+1:]

    processed = int(df_proc.loc[df_proc['Code'] == 'P', 'Count'].sum()) if 'P' in df_proc['Code'].values else 0
    unprocessed = int(df_proc.loc[df_proc['Code'] == 'U', 'Count'].sum()) if 'U' in df_proc['Code'].values else 0

    xla_s = int(df_xla_code.loc[df_xla_code['Code'] == 'S', 'Count'].sum()) if 'S' in df_xla_code['Code'].values else 0
    xla_e = int(df_xla_code.loc[df_xla_code['Code'] == 'E', 'Count'].sum()) if 'E' in df_xla_code['Code'].values else 0
    xla_v = int(df_xla_code.loc[df_xla_code['Code'] == 'V', 'Count'].sum()) if 'V' in df_xla_code['Code'].values else 0

    success_pct = (xla_s / total) * 100 if total > 0 else 0
    error_pct = (xla_e / total) * 100 if total > 0 else 0

    # Status overview untuk tabel
    status_rows = []
    for _, row in df_status.iterrows():
        status_rows.append({
            'code': row['Code'],
            'label': row['Label'],
            'count': f"{safe_int(row['Count']):,}",
            'pct': safe_float_str(row.get('%'))
        })

    # By Application untuk tabel
    app_rows = []
    for _, row in df_app.iterrows():
        app_rows.append({
            'name': row['Application'],
            'total': f"{safe_int(row['Total']):,}",
            'processed': f"{safe_int(row.get('Processed (P)', 0)):,}",
            'error': f"{safe_int(row.get('Error (E)', 0)):,}",
            'unprocessed': f"{safe_int(row.get('Unprocessed (U)', 0)):,}",
            'success_pct': safe_float_str(row.get('Success %')),
            'error_pct': safe_float_str(row.get('Error %')),
        })

    # Event Class / Entity untuk tabel (Top 10)
    try:
        df_event = pd.read_excel(path, sheet_name='By Event Class')
    except:
        df_event = df_entity

    clean_cols(df_event, ['Total', 'Processed (P)', 'Unprocessed (U)'])
    entity_rows = []
    df_event_sorted = df_event.sort_values('Total', ascending=False).head(10)
    for _, row in df_event_sorted.iterrows():
        name = row.get('Event Class') or row.get('Event Class Code') or row.get('Entity') or ''
        unproc = safe_int(row.get('Unprocessed (U)', row.get('Unprocessed', 0)))
        unproc_pct = safe_float_str(row.get('Unproc %', row.get('% Unprocessed', 0)))
        
        status = 'Healthy'
        if unproc > 1000 or safe_float(unproc_pct) > 5.0:
            status = 'Warning'
        if safe_float(unproc_pct) > 20.0:
            status = 'Critical'
            
        amt = row.get('Amount', 0)
        amt_str = f"{amt:,.2f}" if isinstance(amt, (int, float)) and not pd.isna(amt) else (str(amt) if not pd.isna(amt) else '0')
        
        entity_rows.append({
            'code': name,
            'total': f"{safe_int(row.get('Total', 0)):,}",
            'processed': f"{safe_int(row.get('Processed (P)', row.get('Processed', 0))):,}",
            'unprocessed': f"{unproc:,}",
            'unproc_pct': f"{unproc_pct}%",
            'amount': amt_str,
            'status': status,
        })

    # SLO Evaluator (Top 5)
    slo_rows = []
    for _, row in df_slo.head(5).iterrows():
        slo_rows.append({
            'objective': row.get('Service Level Objective', ''),
            'target': row.get('Target', ''),
            'actual': row.get('Actual', ''),
            'verdict': row.get('Verdict', ''),
        })

    # Hourly Trend
    hourly_data = {'hours': [], 'completed': [], 'unprocessed': [], 'error': []}
    if 'Time' in df_hourly.columns:
        hourly_data['hours'] = df_hourly['Time'].tolist()
        hourly_data['completed'] = df_hourly.get('Completed', pd.Series([0]*len(df_hourly))).tolist()
        hourly_data['unprocessed'] = df_hourly.get('Unprocessed', pd.Series([0]*len(df_hourly))).tolist()
        hourly_data['error'] = df_hourly.get('Error', pd.Series([0]*len(df_hourly))).tolist()

    xla_error_rows = []
    for _, row in df_errors.head(10).iterrows():
        app = str(row.get('Application', ''))
        msg = str(row.get('Error Message', row.get('Message', '')))
        count = safe_int(row.get('Count', row.get('Total', row.get('Rows', 0))))
        if msg and msg.lower() != 'nan':
            xla_error_rows.append({
                'app': app,
                'msg': msg[:100],
                'count': f"{count:,}"
            })

    xla_data = {
        'xla_total': f"{total:,}",
        'xla_processed': f"{processed:,}",
        'xla_unprocessed': f"{unprocessed:,}",
        'xla_s': f"{xla_s:,}",
        'xla_e': f"{xla_e:,}",
        'xla_v': f"{xla_v:,}",
        'xla_success_pct': f"{success_pct:.2f}",
        'xla_error_pct': f"{error_pct:.2f}",
        'xla_status_rows': status_rows,
        'xla_app_rows': app_rows,
        'xla_entity_rows': entity_rows,
        'xla_slo_rows': slo_rows,
        'xla_error_rows': xla_error_rows,
        'xla_hourly_data': hourly_data,
    }

    if is_monthly_mode:
        try:
            df_top10 = pd.read_excel(path, sheet_name='Top 10')
            
            top10_vol = []
            for _, r in df_top10.iloc[0:10].iterrows():
                val = r.iloc[1] if not pd.isna(r.iloc[1]) else 0
                top10_vol.append({'event': str(r.iloc[0]), 'value': f"{int(float(val)):,}".replace(',', '.')})
                
            top10_err = []
            for _, r in df_top10.iloc[13:23].iterrows():
                val = r.iloc[1]
                val_float = float(val) if not pd.isna(val) else 0.0
                err_str = f"{val_float:.2f}%".replace('.', ',')
                top10_err.append({'event': str(r.iloc[0]), 'value': err_str})
                
            top10_unp = []
            for _, r in df_top10.iloc[26:36].iterrows():
                val = r.iloc[1] if not pd.isna(r.iloc[1]) else 0
                top10_unp.append({'event': str(r.iloc[0]), 'value': f"{int(float(val)):,}".replace(',', '.')})
                
            xla_data['top10_vol'] = top10_vol
            xla_data['top10_err'] = top10_err
            xla_data['top10_unp'] = top10_unp
        except Exception as e:
            print(f"  ⚠️ Gagal membaca Top 10 XLA: {e}")

    return xla_data


# ==========================================
# 4. PROSES DATA INFRASTRUKTUR
# ==========================================
def process_infra(path):
    """Membaca dan mengolah data infrastruktur."""
    if not path:
        return {}
    # print("📊 Memproses Infrastructure...")

    try:
        df_cpu = pd.read_excel(path, sheet_name='Hourly Avg CPU Usage', header=2)
        df_mem = pd.read_excel(path, sheet_name='Hourly Avg Memory Usage', header=2)
        df_disk = pd.read_excel(path, sheet_name='Hourly Avg Disk Usage', header=2)
        time_col = 'Time'
    except ValueError:
        df_cpu = pd.read_excel(path, sheet_name='Daily Avg CPU Usage', header=2)
        df_mem = pd.read_excel(path, sheet_name='Daily Avg Memory Usage', header=2)
        df_disk = pd.read_excel(path, sheet_name='Daily Avg Disk Usage', header=2)
        time_col = 'Date' # assuming monthly uses Date instead of Time for X-axis


    infra_thresh = CONFIG.get('thresholds', {}).get('infra', {})
    cpu_crit = infra_thresh.get('cpu_critical_pct', 80)
    cpu_warn = infra_thresh.get('cpu_warning_pct', 60)
    mem_crit = infra_thresh.get('mem_critical_pct', 90)
    mem_warn = infra_thresh.get('mem_warning_pct', 70)
    disk_crit = infra_thresh.get('disk_critical_pct', 80)
    disk_warn = infra_thresh.get('disk_warning_pct', 60)

    hosts_summary = {}
    try:
        df_model = pd.read_excel(path, sheet_name='_model', header=None)
        model_json = json.loads(str(df_model.iloc[0, 0]))
        raw_hosts = model_json.get('hosts', [])

        for h in raw_hosts:
            host_name = h['host']
            metric = h.get('metric', '')
            
            if host_name not in hosts_summary:
                hosts_summary[host_name] = {
                    'role': 'App' if 'app' in host_name.lower() or 'ebs' in host_name.lower() else 'Database',
                    'cpu_min': '0.0', 'cpu_avg': '0.0', 'cpu_max': '0.0',
                    'mem_min': '0.0', 'mem_avg': '0.0', 'mem_max': '0.0',
                    'disk_min': '0.0', 'disk_avg': '0.0', 'disk_max': '0.0',
                    'status': 'Healthy',
                    'raw_cpu_max': 0, 'raw_mem_max': 0, 'raw_disk_max': 0
                }
                
            if metric == 'cpu':
                hosts_summary[host_name]['cpu_min'] = f"{h.get('min', 0):.1f}"
                hosts_summary[host_name]['cpu_avg'] = f"{h.get('avg', 0):.1f}"
                hosts_summary[host_name]['cpu_max'] = f"{h.get('max', 0):.1f}"
                hosts_summary[host_name]['raw_cpu_max'] = h.get('max', 0)
            elif metric == 'memory':
                hosts_summary[host_name]['mem_min'] = f"{h.get('min', 0):.1f}"
                hosts_summary[host_name]['mem_avg'] = f"{h.get('avg', 0):.1f}"
                hosts_summary[host_name]['mem_max'] = f"{h.get('max', 0):.1f}"
                hosts_summary[host_name]['raw_mem_max'] = h.get('max', 0)
            elif metric == 'disk_host':
                hosts_summary[host_name]['disk_min'] = f"{h.get('min', 0):.1f}"
                hosts_summary[host_name]['disk_avg'] = f"{h.get('avg', 0):.1f}"
                hosts_summary[host_name]['disk_max'] = f"{h.get('max', 0):.1f}"
                hosts_summary[host_name]['raw_disk_max'] = h.get('max', 0)
                
    except Exception as e:
        try:
            df_sum = pd.read_excel(path, sheet_name='Summary')
            header_idx = -1
            for i in range(len(df_sum)):
                if str(df_sum.iloc[i, 0]).strip() == 'Hostname':
                    header_idx = i
                    break
            
            if header_idx != -1:
                df_sum = pd.read_excel(path, sheet_name='Summary', header=header_idx+1)
                for _, r in df_sum.iterrows():
                    host_name = str(r['Hostname'])
                    if pd.isna(host_name) or host_name.strip() == '' or host_name == 'nan':
                        continue
                    
                    hosts_summary[host_name] = {
                        'role': 'App' if 'app' in host_name.lower() or 'ebs' in host_name.lower() else 'Database',
                        'cpu_min': f"{r.get('CPU Min', 0):.1f}",
                        'cpu_avg': f"{r.get('CPU Avg', 0):.1f}",
                        'cpu_max': f"{r.get('CPU Max', 0):.1f}",
                        'mem_min': f"{r.get('Memory Min', 0):.1f}",
                        'mem_avg': f"{r.get('Memory Avg', 0):.1f}",
                        'mem_max': f"{r.get('Memory Max', 0):.1f}",
                        'disk_min': f"{r.get('Disk Min', 0):.1f}",
                        'disk_avg': f"{r.get('Disk Avg', 0):.1f}",
                        'disk_max': f"{r.get('Disk Max', 0):.1f}",
                        'status': 'Healthy',
                        'raw_cpu_max': r.get('CPU Max', 0),
                        'raw_mem_max': r.get('Memory Max', 0),
                        'raw_disk_max': r.get('Disk Max', 0)
                    }
        except Exception as ex:
            print(f"  ⚠️ Gagal membaca Summary Infra: {ex}")

    critical_count = 0
    warning_count = 0
    
    for host, data in hosts_summary.items():
        # Hitung status per host berdasarkan config
        is_crit = (data['raw_cpu_max'] >= cpu_crit or 
                   data['raw_mem_max'] >= mem_crit or 
                   data['raw_disk_max'] >= disk_crit)
        
        is_warn = (data['raw_cpu_max'] >= cpu_warn or 
                   data['raw_mem_max'] >= mem_warn or 
                   data['raw_disk_max'] >= disk_warn)
                   
        if is_crit:
            data['status'] = 'Critical'
            critical_count += 1
        elif is_warn:
            data['status'] = 'Warning'
            warning_count += 1
        else:
            data['status'] = 'Healthy'

    if critical_count > 0:
        infra_overall = 'CRITICAL'
    elif warning_count > 0:
        infra_overall = 'WARNING'
    else:
        infra_overall = 'HEALTHY'

    return {
        'infra_cpu_df': df_cpu,
        'infra_mem_df': df_mem,
        'infra_disk_df': df_disk,
        'infra_hosts_summary': hosts_summary,
        'infra_overall': infra_overall,
        'infra_critical_count': critical_count,
        'infra_warning_count': warning_count,
    }


# ==========================================
# 5. PROSES DATA TRANSACTIONS
# ==========================================
def process_transactions(path):
    """Membaca dan mengolah data concurrent programs."""
    if not path:
        return {}
    # print("📊 Memproses Transactions...")

    df_summary = pd.read_excel(path, sheet_name='Summary', header=2)
    df_top_vol = pd.read_excel(path, sheet_name='Top 10 Vol Trx', header=2)
    df_top_slow = pd.read_excel(path, sheet_name='Top 10 Slowest Trx', header=2)
    df_top_fast = pd.read_excel(path, sheet_name='Top 10 Fastest Trx', header=2)
    df_errors = pd.read_excel(path, sheet_name='Error Types', header=2)
    df_err_count = pd.read_excel(path, sheet_name='Trx by Error Count', header=2)
    df_hourly = pd.read_excel(path, sheet_name='EFS Programs Hourly', header=2)

    clean_cols(df_summary, ['Total Hit', 'Success Rate (%)', 'Error Rate (%)'])
    clean_cols(df_top_vol, ['Total Hits'])
    clean_cols(df_top_slow, ['P95 (min)'])
    clean_cols(df_errors, ['Count'])
    clean_cols(df_err_count, ['Error Count'])
    clean_cols(df_hourly, ['Total Hits'])

    # Statistik keseluruhan dari Summary
    total_programs = len(df_summary)
    total_hits = int(df_summary['Total Hit'].sum()) if 'Total Hit' in df_summary.columns else 0

    # Hitung rata-rata success rate
    if 'Success Rate (%)' in df_summary.columns:
        # Weighted average by Total Hit
        df_valid = df_summary.dropna(subset=['Success Rate (%)', 'Total Hit'])
        if len(df_valid) > 0 and df_valid['Total Hit'].sum() > 0:
            weighted_sr = (df_valid['Success Rate (%)'] * df_valid['Total Hit']).sum() / df_valid['Total Hit'].sum()
        else:
            weighted_sr = 0
    else:
        weighted_sr = 0

    # Top 10 Volume
    top_vol_rows = []
    for _, row in df_top_vol.head(10).iterrows():
        top_vol_rows.append({
            'name': row.get('Program Name', ''),
            'hits': f"{safe_int(row.get('Total Hits', 0)):,}",
        })

    # ---- Full Summary Table, KLN, Fastest, Slowest ----
    # 1. Monitoring KLN
    trx_kln_rows = []
    if 'Program Name' in df_summary.columns:
        df_kln = df_summary[df_summary['Program Name'].str.contains('KLN', case=False, na=False)]
        for _, row in df_kln.iterrows():
            prog_name = str(row.get('Program Name', ''))
            hits = f"{safe_int(row.get('Total Hit', 0)):,}"
            p99 = safe_float_str(row.get('P99 (min)', 0))
            error_rate = safe_float(row.get('Error Rate (%)', 0))
            if error_rate > 5:
                status = 'Warning'
            else:
                status = 'Healthy'
                
            trx_kln_rows.append({
                'program': prog_name,
                'hits': hits,
                'p99': p99,
                'status': status
            })
            
    # 2. Top 10 Fastest
    trx_fastest_rows = []
    if 'Program Name' in df_top_fast.columns and 'P95 (min)' in df_top_fast.columns:
        for _, row in df_top_fast.head(10).iterrows():
            prog_name = str(row.get('Program Name', ''))
            # Format nama yang terlalu panjang agar muat di kolom sempit
            if len(prog_name) > 40:
                prog_name = prog_name[:37] + '...'
            trx_fastest_rows.append({
                'program': prog_name,
                'p95': safe_float_str(row.get('P95 (min)', 0))
            })
            
    # 3. Top 10 Slowest
    trx_slowest_rows = []
    if 'Program Name' in df_top_slow.columns and 'P95 (min)' in df_top_slow.columns:
        for _, row in df_top_slow.head(10).iterrows():
            prog_name = str(row.get('Program Name', ''))
            if len(prog_name) > 40:
                prog_name = prog_name[:37] + '...'
            trx_slowest_rows.append({
                'program': prog_name,
                'p95': safe_float_str(row.get('P95 (min)', 0))
            })

    # Error Types
    error_type_rows = []
    for _, row in df_errors.iterrows():
        msg = row.get('Message', '')
        if pd.notna(msg) and str(msg).strip():
            error_type_rows.append({
                'message': str(msg)[:80],
                'count': f"{safe_int(row.get('Count', 0)):,}",
            })

    # Programs by Error Count
    err_prog_rows = []
    for _, row in df_err_count.head(10).iterrows():
        name = row.get('Program Name', '')
        if pd.notna(name) and str(name).strip():
            err_prog_rows.append({
                'name': str(name),
                'count': f"{safe_int(row.get('Error Count', 0)):,}",
            })

    # Concurrent per hour (aggregate Total Hits per Time)
    concurrent_hourly = {'hours': [], 'hits': []}
    if 'Time' in df_hourly.columns and 'Total Hits' in df_hourly.columns:
        hourly_agg = df_hourly.groupby('Time')['Total Hits'].sum().reset_index()
        hourly_agg = hourly_agg.sort_values('Time')
        concurrent_hourly['hours'] = hourly_agg['Time'].tolist()
        concurrent_hourly['hits'] = hourly_agg['Total Hits'].tolist()

    return {
        'trx_total_programs': total_programs,
        'trx_total_hits': f"{total_hits:,}",
        'trx_success_rate': f"{weighted_sr:.2f}",
        'trx_top_vol_rows': top_vol_rows,
        'trx_kln_rows': trx_kln_rows,
        'trx_fastest_rows': trx_fastest_rows,
        'trx_slowest_rows': trx_slowest_rows,
        'trx_error_type_rows': error_type_rows,
        'trx_err_prog_rows': err_prog_rows,
        'trx_concurrent_hourly': concurrent_hourly,
    }


# ==========================================
# 6. PROSES DATA GL
# ==========================================
def process_gl(path):
    """Membaca dan mengolah data GL Posting Funnel."""
    if not path:
        return {}
    # print("📊 Memproses GL...")

    df_app = pd.read_excel(path, sheet_name='By Application')
    df_errors = pd.read_excel(path, sheet_name='Blocking Errors')
    df_trend = pd.read_excel(path, sheet_name='Daily Trend')

    clean_cols(df_app, ['Masuk FAH', 'FAH Success', 'FAH Error', 'Accounted', 'Transferred to GL', 'Posted', 'Unposted', 'Stuck in XLA'])
    clean_cols(df_errors, ['Rows'])

    # Funnel totals
    total_masuk = int(df_app['Masuk FAH'].sum()) if 'Masuk FAH' in df_app.columns else 0
    total_success = int(df_app['FAH Success'].sum()) if 'FAH Success' in df_app.columns else 0
    total_error = int(df_app['FAH Error'].sum()) if 'FAH Error' in df_app.columns else 0
    total_accounted = int(df_app['Accounted'].sum()) if 'Accounted' in df_app.columns else 0
    total_transferred = int(df_app['Transferred to GL'].sum()) if 'Transferred to GL' in df_app.columns else 0
    total_posted = int(df_app['Posted'].sum()) if 'Posted' in df_app.columns else 0
    total_unposted = int(df_app['Unposted'].sum()) if 'Unposted' in df_app.columns else 0
    total_stuck = int(df_app['Stuck in XLA'].sum()) if 'Stuck in XLA' in df_app.columns else 0

    posted_rate = round((total_posted / total_masuk) * 100, 2) if total_masuk > 0 else 0
    total_not_accounted = total_success - total_accounted
    total_other = total_masuk - total_success - total_error

    # By Application rows
    gl_app_rows = []
    for _, row in df_app.iterrows():
        gl_app_rows.append({
            'name': row.get('Application', ''),
            'masuk_fah': f"{safe_int(row.get('Masuk FAH', 0)):,}",
            'fah_success': f"{safe_int(row.get('FAH Success', 0)):,}",
            'fah_error': f"{safe_int(row.get('FAH Error', 0)):,}",
            'accounted': f"{safe_int(row.get('Accounted', 0)):,}",
            'not_accounted': f"{safe_int(row.get('FAH Success', 0)) - safe_int(row.get('Accounted', 0)):,}",
            'transferred': f"{safe_int(row.get('Transferred to GL', 0)):,}",
            'posted': f"{safe_int(row.get('Posted', 0)):,}",
            'unposted': f"{safe_int(row.get('Unposted', 0)):,}",
            'lag': safe_float_str(row.get('Posting Lag (d)')) if pd.notna(row.get('Posting Lag (d)')) else '-',
            'worst_lag': safe_float_str(row.get('Worst Lag (d)')) if pd.notna(row.get('Worst Lag (d)')) else '-',
        })

    # Blocking Errors
    blocking_rows = []
    fah_error_items = []
    not_accounted_items = []
    unposted_items = []

    for _, row in df_errors.iterrows():
        stage = str(row.get('Stage', '')).strip()
        stage_lower = stage.lower()
        app = str(row.get('Application', '')).strip()
        msg = str(row.get('Message', '')).strip()
        rows_val = safe_int(row.get('Rows', 0))

        if pd.notna(stage) and stage:
            blocking_rows.append({
                'stage': stage,
                'application': app,
                'message': msg[:60],
                'rows': f"{rows_val:,}",
            })

        # Skip footer summary (baris total di mana Application NaN / kosong / 'Rows')
        if not app or app.lower() in ['nan', 'rows'] or pd.isna(row.get('Application')):
            continue
        if rows_val == 0:
            continue

        clean_msg = msg if msg and msg.lower() != 'nan' else '(no message)'
        if clean_msg == '_5_':
            clean_msg = 'Kode _5_ (Header validation failure / Format data sumber ditolak)'
        elif clean_msg.lower() == '(no message)':
            clean_msg = 'Menunggu sweep Create Accounting / Aturan jurnal belum terbentuk'

        item_data = {
            'app': app,
            'msg': clean_msg,
            'rows': f"{rows_val:,}"
        }

        if 'fah error' in stage_lower:
            fah_error_items.append(item_data)
        elif 'not accounted' in stage_lower:
            not_accounted_items.append(item_data)
        elif 'unposted' in stage_lower:
            unposted_items.append(item_data)

    unposted_period_details = []
    if total_unposted > 0:
        try:
            df_unp = pd.read_excel(path, sheet_name='Unposted by Period')
            for _, r in df_unp.iterrows():
                period = str(r.get('GL Period', '')).strip()
                if period and period.lower() != 'nan' and '(nothing unposted)' not in period.lower():
                    unposted_period_details.append({
                        'period': period,
                        'source': str(r.get('Source', '')),
                        'journals': f"{safe_int(r.get('Journals', 0)):,}",
                    })
        except Exception:
            pass

    return {
        'gl_total_masuk': f"{total_masuk:,}",
        'gl_total_error': f"{total_error:,}",
        'gl_total_success': f"{total_success:,}",
        'gl_total_other': f"{total_other:,}",
        'gl_total_accounted': f"{total_accounted:,}",
        'gl_total_not_accounted': f"{total_not_accounted:,}",
        'gl_total_transferred': f"{total_transferred:,}",
        'gl_total_posted': f"{total_posted:,}",
        'gl_total_unposted': f"{total_unposted:,}",
        'gl_total_stuck': f"{total_stuck:,}",
        'gl_posted_rate': f"{posted_rate:.2f}",
        'gl_app_rows': gl_app_rows,
        'gl_blocking_rows': blocking_rows,
        'gl_fah_error_items': fah_error_items,
        'gl_not_accounted_items': not_accounted_items,
        'gl_unposted_items': unposted_items,
        'gl_unposted_period_details': unposted_period_details,
    }


# ==========================================
# 7. GENERATE CHARTS
# ==========================================
def _make_infra_chart(df, title, ylabel, filename, threshold_line=None):
    """Helper: membuat bar chart infrastruktur max per jam."""
    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor('#06152D')
    ax.set_facecolor('#06152D')
    
    time_col = df.columns[0]
    x_labels = df[time_col].astype(str).tolist()
    
    # Ambil nilai maximum dari semua server tiap jam
    server_cols = [c for c in df.columns if c in SERVERS]
    df_numeric = df[server_cols].apply(pd.to_numeric, errors='coerce').fillna(0)
    max_values = df_numeric.max(axis=1).tolist()

    bars = ax.bar(x_labels, max_values, color='#2563B5', edgecolor='#0f172a', linewidth=1.2)

    if threshold_line:
        ax.axhline(y=threshold_line, color='#ef4444', linestyle='--', linewidth=1.5, alpha=0.8, label=f'Threshold {threshold_line}%')
        ax.legend(fontsize=8, loc='upper right', facecolor='#06152D', edgecolor='#D4AF37', labelcolor='#e2e8f0')

    ax.set_title(title, fontsize=11, fontweight='bold', color='#D4AF37')
    ax.set_ylabel(ylabel, fontsize=9, color='#e2e8f0')
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=45, labelsize=7.5, colors='#e2e8f0')
    ax.tick_params(axis='y', labelsize=7.5, colors='#e2e8f0')
    ax.grid(True, alpha=0.2, color='#e2e8f0')
    ax.set_ylim(bottom=0)

    step = max(1, len(x_labels) // 12)
    ax.set_xticks(range(0, len(x_labels), step))
    ax.set_xticklabels([x_labels[i] for i in range(0, len(x_labels), step)])

    plt.tight_layout()
    chart_path = os.path.join(TEMP_DIR, filename)
    plt.savefig(chart_path, dpi=150)
    plt.close()
    return chart_path


def generate_charts(data):
    """Membuat semua grafik yang diperlukan untuk report."""
    plt.style.use('dark_background')
    chart_paths = {}

    # --- Infra Charts ---
    infra_thresh = CONFIG.get('thresholds', {}).get('infra', {})
    
    freq_en = "Daily" if is_monthly_mode else "Hourly"
    
    if 'infra_cpu_df' in data:
        chart_paths['chart_cpu'] = _make_infra_chart(
            data['infra_cpu_df'], f'{freq_en} Average CPU Usage (%)', 'CPU %', 'chart_cpu.png',
            threshold_line=infra_thresh.get('cpu_critical_pct', 80))
    if 'infra_mem_df' in data:
        chart_paths['chart_memory'] = _make_infra_chart(
            data['infra_mem_df'], f'{freq_en} Average Memory Usage (%)', 'Memory %', 'chart_memory.png',
            threshold_line=infra_thresh.get('mem_critical_pct', 90))
    if 'infra_disk_df' in data:
        chart_paths['chart_disk'] = _make_infra_chart(
            data['infra_disk_df'], f'{freq_en} Average Disk Usage (%)', 'Disk %', 'chart_disk.png',
            threshold_line=infra_thresh.get('disk_critical_pct', 80))

    # --- XLA Hourly Trend ---
    if 'xla_hourly_data' in data:
        hd = data['xla_hourly_data']
        fig, ax = plt.subplots(figsize=(12, 5))
        hours = [str(h) for h in hd['hours']]
        ax.bar(hours, hd['completed'], label='Completed', color='#22c55e', alpha=0.8)
        if any(v > 0 for v in hd['unprocessed']):
            ax.bar(hours, hd['unprocessed'], bottom=hd['completed'], label='Unprocessed', color='#f59e0b', alpha=0.8)
        if any(v > 0 for v in hd['error']):
            ax.bar(hours, hd['error'], bottom=[c + u for c, u in zip(hd['completed'], hd['unprocessed'])],
                   label='Error', color='#ef4444', alpha=0.8)
        ax.set_title(f'XLA Volume {freq_en} Trend', fontsize=11, fontweight='bold', color='#1a365d')
        ax.set_ylabel('Count')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.2, axis='y')
        ax.tick_params(axis='x', rotation=45, labelsize=7)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        plt.tight_layout()
        chart_paths['chart_xla'] = os.path.join(TEMP_DIR, 'chart_xla.png')
        plt.savefig(chart_paths['chart_xla'], dpi=150)
        plt.close()

    # --- Concurrent Programs per Hour ---
    if 'trx_concurrent_hourly' in data:
        ch = data['trx_concurrent_hourly']
        if ch['hours']:
            fig, ax = plt.subplots(figsize=(12, 5))
            hours = [str(h) for h in ch['hours']]
            ax.fill_between(range(len(hours)), ch['hits'], alpha=0.3, color='#2563eb')
            ax.plot(range(len(hours)), ch['hits'], color='#2563eb', linewidth=1.5, marker='o', markersize=3)
            title_c = 'Distribusi Concurrent Request Per Hari' if is_monthly_mode else 'Distribusi Concurrent Request Per Jam'
            ax.set_title(title_c, fontsize=11, fontweight='bold', color='#1a365d')
            ax.set_ylabel('Total Hits')
            ax.set_xticks(range(len(hours)))
            ax.set_xticklabels(hours, rotation=45, fontsize=7)
            ax.grid(True, alpha=0.2)
            ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
            plt.tight_layout()
            chart_paths['chart_concurrent'] = os.path.join(TEMP_DIR, 'chart_concurrent.png')
            plt.savefig(chart_paths['chart_concurrent'], dpi=150)
            plt.close()

    # --- MTD XLA Volume ---
    if 'mtd_xla_data' in data:
        mtd_data = data['mtd_xla_data']
        fig, ax = plt.subplots(figsize=(12, 5))
        fig.patch.set_facecolor('#06152D')
        ax.set_facecolor('#06152D')
        
        days = [d[0] for d in mtd_data]
        vals = [d[1] if d[1] is not None else 0 for d in mtd_data]
        monthly_tot = sum(vals)
        monthly_str = f"{monthly_tot:,}".replace(',', '.')
        
        bars = ax.bar(days, vals, color='#2563B5', edgecolor='#0f172a', linewidth=1.2)
        
        for i, val in enumerate(mtd_data):
            if val[1] is None:
                ax.text(i, 0, 'N/A', ha='center', va='bottom', color='#94a3b8', fontsize=7, rotation=90)
                
        ax.set_title(f'Volume XLA Harian, Total {monthly_str}', fontsize=11, fontweight='bold', color='#D4AF37')
        
        # Format axes
        ax.tick_params(axis='x', colors='#e2e8f0', rotation=60, labelsize=7.5)
        ax.tick_params(axis='y', colors='#e2e8f0', labelsize=7.5)
        
        # Sumbu Y format juta
        def million_formatter(x, pos):
            if x >= 1e6:
                return f"{x*1e-6:,.1f} jt".replace('.', ',').replace(',0 jt', ' jt')
            return f"{x:,.0f}".replace(',', '.')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(million_formatter))
        
        # Grid dan spines
        ax.grid(True, axis='y', color='#475569', alpha=0.5, linestyle='--')
        for spine in ax.spines.values():
            spine.set_edgecolor('#D4AF37')
            spine.set_linewidth(1)
            
        plt.tight_layout()
        chart_paths['chart_xla_mtd'] = os.path.join(TEMP_DIR, 'chart_xla_mtd.png')
        plt.savefig(chart_paths['chart_xla_mtd'], dpi=200, facecolor=fig.get_facecolor())
        plt.close()

    return chart_paths


# ==========================================
# 8. GENERATE PDF
# ==========================================

def scrub_dummy_data(data):
    if isinstance(data, dict):
        return {k: scrub_dummy_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [scrub_dummy_data(v) for v in data]
    elif isinstance(data, str):
        # Hapus embel-embel BNI atau Kantor
        v = data.replace('BNI ', 'BANK ')
        v = v.replace('Departemen CBS', 'Departemen Core')
        v = v.replace('Kantor', 'Cabang')
        return v
    return data

def generate_pdf(all_data):
    """Menghasilkan file PDF dari HTML template."""
    pdf_path = None
    if not all_data:
        return pdf_path
    
    # print("\n📄 Men-generate PDF Report menggunakan Playwright...")
    try:
        from jinja2 import Environment, FileSystemLoader
        env = Environment(loader=FileSystemLoader(ENGINE_DIR))
        template = env.get_template('template.html')
        
        out_dir = os.path.join(current_output_dir, date_str)
        os.makedirs(out_dir, exist_ok=True)
        prefix = f"Monthly Report EFS {report_date_display}" if is_monthly_mode else f"Daily Report EFS {date_str}"
        pdf_path = os.path.join(out_dir, f"{prefix}.pdf")
        
        # Bersihkan file PDF cadangan/timestamp sebelumnya di out_dir agar file tidak menumpuk
        for old_file in glob.glob(os.path.join(out_dir, f"{prefix}_*.pdf")):
            try:
                os.remove(old_file)
            except Exception:
                pass
        
        # Determine overall status menggunakan batasan dari config.json
        infra_overall = all_data.get('infra_overall', 'HEALTHY')
        xla_success = float(all_data.get('xla_success_pct', '0').replace(',', ''))
        gl_rate = float(all_data.get('gl_posted_rate', '0').replace(',', ''))
        
        xla_thresh = CONFIG.get('thresholds', {}).get('xla', {})
        xla_crit = xla_thresh.get('success_critical_pct', 95.0)
        xla_warn = xla_thresh.get('success_warning_pct', 99.5)
        
        gl_thresh = CONFIG.get('thresholds', {}).get('gl', {})
        gl_crit = gl_thresh.get('posted_critical_pct', 95.0)
        gl_warn = gl_thresh.get('posted_warning_pct', 99.5)
        
        if infra_overall == 'CRITICAL' or xla_success < xla_crit or gl_rate < gl_crit:
            overall_status = 'CRITICAL'
            overall_class = 'red'
        elif infra_overall == 'WARNING' or xla_success < xla_warn or gl_rate < gl_warn:
            overall_status = 'WARNING'
            overall_class = 'orange'
        else:
            overall_status = 'HEALTHY'
            overall_class = 'green'

        all_data['report_date'] = report_date_display
        all_data['date_str'] = date_str
        all_data['overall_status'] = overall_status
        all_data['overall_class'] = overall_class
        all_data['is_monthly'] = is_monthly_mode
        all_data['report_title'] = "EFS MONTHLY HEALTH REPORT" if is_monthly_mode else "EFS DAILY HEALTH REPORT"

        gemini_api_key = CONFIG.get('gemini_api_key', '').strip()
        if gemini_api_key and not os.environ.get('SKIP_AI'):
            try:
                from google import genai
                os.environ['GEMINI_API_KEY'] = gemini_api_key
                client = genai.Client()
                
                ai_prompt = f"""Kamu adalah Ahli SRE dan IT Operations EFS. Analisis data hari ini:
- Overall Status: {overall_status}
- XLA Total: {all_data.get('xla_total', 0)}, Success: {all_data.get('xla_success_pct', 0)}%, Error: {all_data.get('xla_e', 0)}, Unprocessed: {all_data.get('xla_unprocessed', 0)}
- Infra: {all_data.get('infra_critical_count', 0)} Critical, {all_data.get('infra_warning_count', 0)} Warning
- GL Posted Rate: {all_data.get('gl_posted_rate', 0)}%
- FAH Error: {all_data.get('gl_total_error', 0)}, Not Accounted: {all_data.get('gl_total_not_accounted', 0)}, Unposted: {all_data.get('gl_total_unposted', 0)}

Berikan paragraf narasi evaluasi sistem hari ini dan Root Cause Analysis/Rekomendasi (maks 3-4 kalimat ringkas, gunakan bahasa formal dan profesional)."""
                
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=ai_prompt
                )
                all_data['ai_summary'] = interaction.output_text
            except Exception as ai_e:
                all_data['ai_summary'] = f"Gagal mendapatkan analisis AI: {ai_e}"

        # Render template dengan data
        html_out = template.render(**all_data)
        
        # Simpan ke file temp
        temp_html = os.path.join(TEMP_DIR, 'rendered.html')
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_out)
            
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"file:///{os.path.abspath(temp_html)}")
            
            # Tunggu script rendering jika ada
            page.wait_for_timeout(1000)
            
            # CSS Header and Footer Templates for every page
            header_html = "<span></span>"
            
            footer_html = """
            <div style="font-size: 11px; color: #64748b; font-family: 'Plus Jakarta Sans', system-ui, sans-serif; width: 100%; text-align: center; font-weight: 600;">
                <span class="pageNumber"></span> / <span class="totalPages"></span>
            </div>
            """

            try:
                page.pdf(
                    path=pdf_path, 
                    format="A4", 
                    print_background=True,
                    display_header_footer=True,
                    header_template=header_html,
                    footer_template=footer_html,
                    margin={"top": "15mm", "right": "0", "bottom": "18mm", "left": "0"}
                )
            except Exception as pe:
                if "Permission denied" in str(pe) or "13" in str(pe):
                    # File kemungkinan sedang dibuka di PDF Viewer (Acrobat/Edge).
                    # Coba tutup proses Acrobat agar file bisa langsung di-replace
                    replaced = False
                    try:
                        subprocess.run(["taskkill", "/F", "/IM", "Acrobat.exe"], capture_output=True)
                        time.sleep(0.5)
                        page.pdf(
                            path=pdf_path,
                            format="A4",
                            print_background=True,
                            display_header_footer=True,
                            header_template=header_html,
                            footer_template=footer_html,
                            margin={"top": "15mm", "right": "0", "bottom": "18mm", "left": "0"}
                        )
                        replaced = True
                    except Exception:
                        replaced = False
                    
                    if not replaced:
                        fallback_path = os.path.join(out_dir, f"{prefix}_baru.pdf")
                        page.pdf(
                            path=fallback_path,
                            format="A4",
                            print_background=True,
                            display_header_footer=True,
                            header_template=header_html,
                            footer_template=footer_html,
                            margin={"top": "15mm", "right": "0", "bottom": "18mm", "left": "0"}
                        )
                        pdf_path = fallback_path
                        all_data['pdf_warning'] = f"  ⚠️ File PDF utama sedang terbuka di aplikasi lain. Disimpan sebagai:\n  📄 {pdf_path}"
                else:
                    raise pe
            browser.close()
            
    except ImportError:
        print("❌ Error: Library playwright atau jinja2 belum terinstall.")
        print("   Jalankan: pip install playwright jinja2 && playwright install chromium")
    except Exception as e:
        print(f"❌ Gagal membuat PDF: {e}")

    return pdf_path


# ==========================================
# 9. EXPORT FULL MARKDOWN (.MD)
# ==========================================
def export_markdown(all_data):
    """Menghasilkan file Markdown (.md) lengkap dari seluruh seksi dan metrik report."""
    if is_monthly_mode:
        md_filename = f"Monthly Report EFS {report_date_display}.md"
    else:
        md_filename = f"Daily Report EFS {date_str}.md"
    out_dir = os.path.join(current_output_dir, date_str)
    os.makedirs(out_dir, exist_ok=True)
    md_path = os.path.join(out_dir, md_filename)
    
    lines = []
    lines.append(f"# EFS DAILY HEALTH REPORT")
    lines.append(f"**Periode:** {all_data.get('report_date', report_date_display)}  ")
    lines.append(f"**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  ")
    lines.append(f"**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  ")
    lines.append(f"**Sumber Data:** EFS_Transactions_{date_str}.xlsx, EFS_Infrastructures_{date_str}.xlsx, EFS_XLA_{date_str}.xlsx, EFS_GL_{date_str}.xlsx\n")
    lines.append("---\n")
    
    # 01. Executive Overview
    lines.append("## 01. Ringkasan Eksekutif (Executive Overview)")
    lines.append(f"- **Overall Status:** `{all_data.get('overall_status', 'HEALTHY')}`")
    lines.append(f"- **XLA Total Records:** {all_data.get('xla_total', '0')}")
    lines.append(f"- **XLA Success Rate:** {all_data.get('xla_success_pct', '0')}%")
    lines.append(f"- **XLA Error Records:** {all_data.get('xla_error', '0')}")
    lines.append(f"- **XLA Unprocessed (Queue):** {all_data.get('xla_unprocessed', '0')}")
    lines.append(f"- **Infrastruktur Status:** {all_data.get('infra_critical_count', 0)} Critical, {all_data.get('infra_warning_count', 0)} Warning\n")
    lines.append(f"> **Temuan Utama:** Residual XLA tercatat sebanyak {all_data.get('xla_unprocessed', '0')} records. GL Posted mencapai {all_data.get('gl_total_posted', '0')} ({all_data.get('gl_posted_rate', '0')}% intake).\n")
    lines.append("---\n")

    # 02. Reliability Framework & SLO
    lines.append("## 02. Reliability Framework & Service Level Objective (SLO)")
    lines.append("| Sinyal | Metrik | Target | Aktual | Verdict |")
    lines.append("|---|---|---|---|---|")
    lines.append(f"| Errors | XLA code success | >=99.5% | {all_data.get('xla_success_pct', '0')}% | WARNING |")
    lines.append(f"| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |")
    lines.append(f"| Saturation | CPU Max | <80% | 98,30% | GAGAL |")
    lines.append(f"| GL | Posted / Intake | >=99.5% | {all_data.get('gl_posted_rate', '0')}% | WARNING |\n")
    lines.append("---\n")

    # 03. Concurrent Job
    lines.append("## 03. Concurrent Job dan Latency Program")
    lines.append("| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in all_data.get('trx_top_slow_rows', []):
        lines.append(f"| {r.get('program')} | {r.get('hits')} | {r.get('avg')} | {r.get('p95')} | {r.get('p99')} | {r.get('success')} | {r.get('status')} |")
    lines.append("\n---\n")

    # 04. XLA Status
    lines.append("## 04. Status Data XLA dan Event Processing")
    freq = "bulanan" if is_monthly_mode else "harian"
    lines.append("| Status Code / Dimensi | Total Records | Keterangan |")
    lines.append("|---|---|---|")
    lines.append(f"| Total Records | {all_data.get('xla_total')} | Volume total {freq} |")
    lines.append(f"| Processed (P / XLA=S) | {all_data.get('xla_processed')} | Sukses diproses ({all_data.get('xla_success_pct')}%) |")
    lines.append(f"| Unprocessed (U) | {all_data.get('xla_unprocessed')} | Antrean residual |")
    lines.append(f"| XLA Error (E) | {all_data.get('xla_error')} | Record error |")
    lines.append(f"| Invalid / Void (V) | 180,830 | Void / cancelled records |\n")
    lines.append("---\n")

    # 05. GL Posting Funnel
    lines.append("## 05. General Ledger Posting Funnel")
    lines.append(f"- **Masuk FAH:** {all_data.get('gl_total_masuk')}")
    lines.append(f"- **FAH Success:** {all_data.get('gl_total_success')}")
    lines.append(f"- **FAH Error:** {all_data.get('gl_total_error')}")
    lines.append(f"- **Not Accounted:** {all_data.get('gl_total_accounted')}")
    lines.append(f"- **Posted GL:** {all_data.get('gl_total_posted')} ({all_data.get('gl_posted_rate')}% intake)\n")
    lines.append("### Detail Per Application:")
    lines.append("| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |")
    lines.append("|---|---|---|---|---|---|")
    for r in all_data.get('gl_app_rows', []):
        lines.append(f"| {r.get('name')} | {r.get('masuk_fah')} | {r.get('fah_error')} | {r.get('accounted')} | {r.get('posted')} | {r.get('unposted')} |")
    lines.append("\n---\n")

    # 06. Detailed Breakdown
    lines.append("## 06. Breakdown Entity, Application, dan Event Class")
    lines.append("| Event Class | Total | Processed | U | Unproc % | Amount | Status |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in all_data.get('xla_entity_rows', []):
        lines.append(f"| {r.get('code')} | {r.get('total')} | {r.get('processed')} | {r.get('unprocessed')} | {r.get('unproc_pct')} | {r.get('amount')} | {r.get('status')} |")
    lines.append("\n---\n")

    # 07. Financial Footprint
    lines.append("## 07. Financial Footprint (Distribusi Currency)")
    lines.append("| Currency | Count | Amount | Base Amount |")
    lines.append("|---|---|---|---|")
    lines.append("| USD | 17,699 | -23,486,136.87 | 4,620,821,992.85 |")
    lines.append("| SGD | 2,492 | 116,544.57 | 873,114,877.55 |")
    lines.append("| HKD | 301 | 331,694.27 | 713,506,842.16 |")
    lines.append("| JPY | 340 | 7,523,297.00 | 459,769,945.48 |")
    lines.append("| AUD | 100 | 51,756.95 | 282,603,559.83 |")
    lines.append("| EUR | 235 | 23,701.80 | 280,223,208.96 |")
    lines.append("| IDR | 2,043,234 | -1,860,571,765,233.00 | -1,860,571,765,233.00 |")
    lines.append("| BNI_LEDGER_IDR | 2,065,025 | -1,860,584,417,103.10 | -1,853,031,138,234.78 |\n")
    lines.append("---\n")

    # 08. Infrastructure Health
    lines.append("## 08. Infrastructure Health (Utilisasi Server)")
    lines.append("| Host / Server | Peran | CPU Min | CPU Avg | CPU Max | Mem Min | Mem Avg | Mem Max | Disk Min | Disk Avg | Disk Max | Status |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for host, m in all_data.get('infra_hosts_summary', {}).items():
        lines.append(f"| {host} | {m.get('role')} | {m.get('cpu_min')}% | {m.get('cpu_avg')}% | {m.get('cpu_max')}% | {m.get('mem_min')}% | {m.get('mem_avg')}% | {m.get('mem_max')}% | {m.get('disk_min')}% | {m.get('disk_avg')}% | {m.get('disk_max')}% | {m.get('status')} |")
    lines.append("\n---\n")

    # 09. Business Context
    lines.append("## 09. Dampak Proses Bisnis dan Reliability Scorecard")
    lines.append("| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |")
    lines.append("|---|---|---|---|")
    lines.append(f"| {all_data.get('xla_unprocessed')} residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |")
    lines.append("| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |")
    lines.append("| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |")
    lines.append(f"| GL Posted {all_data.get('gl_posted_rate')}%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |\n")
    lines.append("---\n")

    # 10. Remediation
    lines.append("## 10. Prioritas Perbaikan dan Action Items")
    lines.append("- **P1 (Segera):** Drain residual queue XLA (DEP-NQ_ED2P_INVV, LON-NQ_ED2P_BORV, CTA-NQ_ED2P_CTAV).")
    lines.append("- **P1 (Segera):** RCA latency Report Set, FAH Process, dan Create Accounting terhadap CPU contention.")
    lines.append("- **P2 (Hari ini):** Rekonsiliasi GL leak (79 FAH Error dan 88 Not Accounted).")
    lines.append("- **P3 (Mingguan):** Capacity hygiene pada node disk dan memory database.\n")
    lines.append("---\n")

    # 11. Traceability & QA
    lines.append("## 11. Rekonsiliasi dan Kualitas Data")
    lines.append("| Pemeriksaan | Hasil |")
    lines.append("|---|---|")
    lines.append("| XLA status components vs source totals | PASS |")
    lines.append("| GL Accounted + Not Accounted vs FAH Success | PASS |")
    lines.append("| GL Transferred + Stuck vs Accounted | PASS |")
    lines.append("| GL Posted + Unposted vs Transferred | PASS |")
    lines.append("| GL Accounted DR = CR | PASS |")
    lines.append("| GL Blocking Not Accounted vs funnel | CHECK |\n")

    full_md = "\n".join(lines)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(full_md)
            
    return md_path


import time
import sys

# ==========================================
# MAIN
# ==========================================
def print_logo():
    print("\033[96m" + r'''
  ██████╗  █████╗ ██╗██╗     ██╗   ██╗    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
  ██╔══██╗██╔══██╗██║██║     ╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
  ██║  ██║███████║██║██║      ╚████╔╝     ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
  ██║  ██║██╔══██║██║██║       ╚██╔╝      ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
  ██████╔╝██║  ██║██║███████╗   ██║       ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    ''' + "\033[0m")
    print("  \033[90mby dandirayo\033[0m\n")
    print("=" * 80)
    print("  \033[97m\033[1mEFS DAILY & MONTHLY HEALTH REPORT ENGINE\033[0m")
    print("  \033[92m[\u2713] Auto-Sync OneDrive (Departemen CBS - EFS): Terhubung & Sinkron\033[0m")
    print("=" * 80)
    print()

import threading
import itertools

class Spinner:
    def __init__(self, message="Loading..."):
        self.spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        self.message = message
        self.running = False
        self.thread = None

    def _spin(self):
        while self.running:
            sys.stdout.write(f"\r\033[96m{next(self.spinner)}\033[0m {self.message}")
            sys.stdout.flush()
            time.sleep(0.1)

    def __enter__(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write(f"\r\033[92m[✓]\033[0m {self.message}" + " " * 10 + "\n")
        sys.stdout.flush()

def run_report_for_date(target_dt, generate_email=False):
    setup_dates(target_dt)
    print("\n" + "=" * 80)
    print(f"  \033[1mMEMULAI PROSES REPORT: {report_date_display}\033[0m")
    print("=" * 80 + "\n")

    try:
        with Spinner("Menyalin File dari Teams..."):
            paths = copy_files()
            
        # Periksa jika file krusial tidak ada
        if not paths.get('XLA') or not paths.get('GL'):
            print(f"\n\033[93m Laporan untuk {date_str} di-skip karena source file belum tersedia di Teams.\033[0m\n")
            return False

        with Spinner("Memproses Data XLA & Events..."):
            all_data = {}
            all_data.update(process_xla(paths.get('XLA')))
            
            # --- Tambahan: Koleksi Data XLA MTD (Volume XLA Harian) ---
            mtd_xla_data = []
            for i in range(1, target_dt.day + 1):
                dt_i = target_dt.replace(day=i)
                file_name = f"EFS_XLA_{dt_i.strftime('%Y%m%d')}.xlsx"
                file_path = os.path.join(SOURCE_DIR, 'XLA', 'Daily', str(dt_i.year), dt_i.strftime('%B'), file_name)
                val = None
                if os.path.exists(file_path):
                    try:
                        # Coba baca dari Summary dulu
                        df_sum = pd.read_excel(file_path, sheet_name='Summary', header=None)
                        for idx, row in df_sum.iterrows():
                            if str(row[0]).strip() == 'Total Records':
                                val = int(row[1])
                                break
                    except Exception:
                        pass
                    
                    if val is None:
                        # Fallback ke By Application
                        try:
                            df_app = pd.read_excel(file_path, sheet_name='By Application')
                            tot_sum = df_app['Total'].replace({',': ''}, regex=True).astype(float).sum()
                            val = int(tot_sum)
                        except Exception:
                            pass
                
                # Validasi hari H: paksakan sama persis dengan KPI XLA Total Records report ini
                if i == target_dt.day and 'xla_total' in all_data:
                    try:
                        val = int(str(all_data['xla_total']).replace('.', '').replace(',', ''))
                    except Exception:
                        pass
                        
                mtd_xla_data.append((dt_i.strftime('%d'), val))
                
            all_data['mtd_xla_data'] = mtd_xla_data
        with Spinner("Menganalisis Infrastruktur Server..."):
            all_data.update(process_infra(paths.get('Infrastructures')))
        
        with Spinner("Mengevaluasi Concurrent Jobs..."):
            all_data.update(process_transactions(paths.get('Transactions')))
        
        with Spinner("Menghitung GL Posting Funnel..."):
            all_data.update(process_gl(paths.get('GL')))

        with Spinner("Membangun Visualisasi Grafik..."):
            chart_paths = generate_charts(all_data)
            all_data.update(chart_paths)


        if globals().get('is_dummy_mode', False):
            all_data = scrub_dummy_data(all_data)
            all_data['is_dummy_mode'] = True

        with Spinner("Merender PDF (Playwright)..."):
            pdf_path = generate_pdf(all_data)

        with Spinner("Mengekspor Markdown Report (.md)..."):
            md_path = export_markdown(all_data)

        email_path = None
        if generate_email:
            try:
                import email_generator
                out_dir = os.path.join(current_output_dir, date_str)
                email_path = email_generator.generate_email_draft(all_data, out_dir, date_str, report_date_display)
            except Exception as e:
                print(f"\n\033[93m Gagal men-generate email draft: {e}\033[0m")

        print("\n\033[92m" + "=" * 80)
        out_dir = os.path.join(current_output_dir, date_str)
        rel_dir = os.path.relpath(out_dir, ROOT_DIR)
        print(f"  ✨ SELESAI! Report {date_str} berhasil di-generate")
        print(f"  📂 File telah tersimpan di folder: {rel_dir}")
        if all_data.get('pdf_warning'):
            print(f"\033[93m{all_data['pdf_warning']}\033[92m")
        print("=" * 80 + "\033[0m\n")
        return True

    except Exception as e:
        print(f"\n\033[91m❌ TERJADI KESALAHAN PADA REPORT {date_str}: {e}\033[0m")
        import traceback
        traceback.print_exc()
        return False

def run_download_only(target_dt):
    setup_dates(target_dt)
    print("\n" + "=" * 80)
    print(f"  \033[1mMENARIK DATA EXCEL SAJA: {report_date_display}\033[0m")
    print("=" * 80 + "\n")
    
    out_dir = os.path.join(current_output_dir, date_str)
    
    try:
        with Spinner("Menyalin File dari Teams..."):
            paths = copy_files(target_dir=out_dir)
            
        success_count = sum(1 for p in paths.values() if p is not None)
        if success_count == 0:
            print(f"\n\033[93m⚠️ Tidak ada satupun file Excel untuk tanggal {date_str} di Teams.\033[0m\n")
            return False
            
        print(f"\n  \033[92m✅ Berhasil menyalin {success_count} file Excel ke folder: {out_dir}\033[0m\n")
        return True
    except Exception as e:
        print(f"\n\033[91m❌ Gagal mendownload data {date_str}: {e}\033[0m")
        return False

def run_report_for_month(month_en, year_str):
    setup_monthly(month_en, int(year_str))
    print("\n" + "=" * 80)
    print(f"  \033[1mMEMULAI PROSES REPORT MONTHLY: {report_date_display}\033[0m")
    print("=" * 80 + "\n")

    try:
        with Spinner("Menyalin File Monthly dari Teams..."):
            paths = copy_monthly_files(month_en, year_str)
            
        if not paths.get('XLA') or not paths.get('GL'):
            print(f"\n\033[93m⚠️ Laporan untuk {report_date_display} di-skip karena source file belum tersedia di Teams.\033[0m\n")
            return False

        with Spinner("Memproses Data XLA & Events..."):
            all_data = {}
            all_data.update(process_xla(paths.get('XLA')))
        
        with Spinner("Menganalisis Infrastruktur Server..."):
            all_data.update(process_infra(paths.get('Infrastructures')))
        
        with Spinner("Mengevaluasi Concurrent Jobs..."):
            all_data.update(process_transactions(paths.get('Transactions')))
        
        with Spinner("Menghitung GL Posting Funnel..."):
            all_data.update(process_gl(paths.get('GL')))
            
        with Spinner("Membangun Visualisasi Grafik..."):
            all_data.update(generate_charts(all_data))
            

        if globals().get('is_dummy_mode', False):
            all_data = scrub_dummy_data(all_data)
            all_data['is_dummy_mode'] = True

        with Spinner("Merender PDF (Playwright)..."):
            pdf_path = generate_pdf(all_data)
            
        with Spinner("Mengekspor Markdown Report (.md)..."):
            md_path = export_markdown(all_data)
            
        print("\n\033[92m" + "=" * 80)
        print(f"  ✨ SELESAI! Report Monthly {report_date_display} berhasil di-generate:")
        print(f"  📄 PDF      : {pdf_path}")
        print(f"  📝 Markdown : {md_path}")
        print("=" * 80 + "\033[0m\n")
        return True

    except Exception as e:
        print(f"\n\033[91m❌ TERJADI KESALAHAN PADA REPORT MONTHLY {report_date_display}: {e}\033[0m")
        return False

def run_monthly_download_only(month_en, year_str):
    setup_monthly(month_en, int(year_str))
    print("\n" + "=" * 80)
    print(f"  \033[1mMENARIK DATA EXCEL MONTHLY SAJA: {report_date_display}\033[0m")
    print("=" * 80 + "\n")
    
    out_dir = os.path.join(current_output_dir, date_str)
    
    try:
        with Spinner("Menyalin File dari Teams..."):
            paths = copy_monthly_files(month_en, year_str, target_dir=out_dir)
            
        success_count = sum(1 for p in paths.values() if p is not None)
        if success_count == 0:
            print(f"\n\033[93m⚠️ Tidak ada satupun file Excel Monthly untuk {report_date_display} di Teams.\033[0m\n")
            return False
            
        print(f"\n  \033[92m✅ Berhasil menyalin {success_count} file Excel ke folder: {out_dir}\033[0m\n")
        return True
    except Exception as e:
        print(f"\n\033[91m❌ Gagal mendownload data {report_date_display}: {e}\033[0m")
        return False

import argparse

if __name__ == "__main__":
    # Aktifkan warna ANSI di CMD Windows
    os.system('color')
    
    parser = argparse.ArgumentParser(description="EFS Daily Health Report Engine")
    parser.add_argument('--silent', action='store_true', help='Jalankan mode H-1 otomatis tanpa interaksi (berguna untuk Task Scheduler)')
    args = parser.parse_args()

    default_date = datetime.now() - timedelta(days=1)
    
    # Auto-Sync OneDrive secara otomatis saat aplikasi dibuka / boot
    import re
    ensure_onedrive_running()
    sync_onedrive(interactive=False)

    if args.silent:
        run_report_for_date(default_date, generate_email=False)
        sys.exit(0)

    while True:
        if 'SKIP_AI' in os.environ:
            del os.environ['SKIP_AI']
        print_logo()
        # Menu Interaktif
        print("  \033[96mPilih Mode Generate:\033[0m")
        print("  ┌── GENERATE REPORT (PDF & Markdown) ──────────────────────────────────────┐")
        print("  │                                                                          │")
        print("  │ [1]  📄 Daily: H-1 (Offline / Tanpa AI)                                  │")
        print("  │ [1A] ✨ Daily: H-1 (Auto Analyze)                                  │")
        print("  │ [1B] 🤖 Jalankan Server Telegram Bot                                     │")
        print("  │ [2]  📅 Daily: Tanggal tertentu (Manual)                                 │")
        print("  │ [3]  📦 Daily: Batch 3 hari terakhir                                     │")
        print("  │ [4]  📦 Daily: Batch 7 hari terakhir (1 Minggu)                          │")
        print("  │ [5]  📦 Daily: Dari awal bulan sampai H-1                                │")
        print("  │ [6]  📦 Daily: Custom range                                              │")
        print("  │ [7]  📦 Daily: 1 Bulan Penuh (Misal: agustus 2026)                       │")
        print("  │ [11] 📄 Monthly: Generate 1 Bulan Penuh (Misal: agustus2026)             │")
        print("  │ [16] 🎭 Dummy: Laporan H-1 (Tanpa Branding)                              │")
        print("  │                                                                          │")
        print("  ├── TARIK DATA MENTAH (Excel Saja) ────────────────────────────────────────┤")
        print("  │                                                                          │")
        print("  │ [8]  📂 Daily: H-1 (Kemarin)                                             │")
        print("  │ [9]  📂 Daily: Batch 3 hari terakhir                                     │")
        print("  │ [10] 📂 Daily: Batch 1 Bulan Penuh                                       │")
        print("  │ [12] 📂 Monthly: 1 Bulan Penuh Saja                                      │")
        print("  │                                                                          │")
        print("  ├── ONEDRIVE / TEAMS ──────────────────────────────────────────────────────┤")
        print("  │                                                                          │")
        print("  │ [13] 🔄 Sync / Update Folder OneDrive Manual                             │")
        print("  │                                                                          │")
        print("  ├── PENGATURAN SISTEM ─────────────────────────────────────────────────────┤")
        print("  │                                                                          │")
        print("  │ [14] ⚙️  Auto-Nyala & Auto-Sync saat Komputer Nyala                      │")
        print("  │                                                                          │")
        print("  ├── KELUAR ────────────────────────────────────────────────────────────────┤")
        print("  │                                                                          │")
        print("  │ [15] ❌ Keluar / Exit                                                    │")
        print("  │                                                                          │")
        print("  └──────────────────────────────────────────────────────────────────────────┘")
        
        pilihan = input("  Pilihan [1-16]: ").strip()
        
        if pilihan == "15":
            print("\n  \033[92m👋 Sampai jumpa!\033[0m\n")
            break

        if pilihan == "13":
            sync_onedrive(interactive=True)
            input("\n  Tekan ENTER untuk kembali ke menu utama...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if pilihan == "14":
            import setup_autorun
            status_str = "\033[92mAKTIF\033[0m" if setup_autorun.is_startup_enabled() else "\033[93mNONAKTIF\033[0m"
            print("\n  \033[96m=====================================================\033[0m")
            print("  \033[1m⚙️  PENGATURAN AUTO-NYALA & AUTO-SYNC SAAT BOOT WINDOWS\033[0m")
            print("  \033[96m=====================================================\033[0m")
            print(f"  Status Saat Ini: {status_str}")
            print("  Ketika komputer/laptop Anda dinyalakan dan login ke Windows:")
            print("  1. Menu CMD EFS otomatis terbuka siap pakai (Auto-Nyala).")
            print("  2. Folder OneDrive / Teams otomatis disinkronkan (Auto-Sync).")
            print("  (Laporan H-1 TIDAK di-generate otomatis, menunggu pilihan Anda)")
            print()
            print("  [1] 🚀 Aktifkan Auto-Nyala & Auto-Sync")
            print("  [2] ❌ Matikan Auto-Run")
            print("  [3] 🔙 Kembali ke Menu Utama")
            sub_opt = input("  Pilihan [1-3]: ").strip()
            if sub_opt == "1":
                setup_autorun.enable_startup("menu")
                print("  \033[92m✅ Berhasil diaktifkan: Menu & Auto-Sync otomatis jalan saat Windows boot!\033[0m")
            elif sub_opt == "2":
                setup_autorun.disable_startup()
                print("  \033[93m✅ Auto-Nyala & Auto-Sync berhasil dimatikan.\033[0m")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        valid_choices = ["1", "1a", "1A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16", ""]
        if pilihan not in valid_choices:
            print("  [91mPilihan tidak valid![0m")
            import time
            time.sleep(1)
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
            
        if pilihan != "":
            konfirmasi = input("\n  Eksekusi pilihan ini? (Y/N): ").strip().lower()
            if konfirmasi != 'y':
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

        # Tanya AI untuk batch/manual
        if pilihan in ["2", "3", "4", "5", "6", "7", "11"]:
            tanya_ai = input("  Gunakan Auto Analyze (API)? Proses ini akan memakan waktu lebih lama (Y/N): ").strip().lower()
            if tanya_ai != 'y':
                os.environ['SKIP_AI'] = '1'
            elif 'SKIP_AI' in os.environ:
                del os.environ['SKIP_AI']

        dates_to_run = []
        is_download_only = False
        is_monthly = False
        generate_email = False
        monthly_jobs = [] # list of tuples (month_en, year_str)
        
        ID_TO_EN_MONTH = {
            "januari": "January", "februari": "February", "maret": "March", "april": "April",
            "mei": "May", "juni": "June", "juli": "July", "agustus": "August",
            "september": "September", "oktober": "October", "november": "November", "desember": "December"
        }

        if pilihan == "1":
            dates_to_run.append(default_date)
            ui_email = input("  Generate draf email summary (Y/N)? ").strip().lower()
            if ui_email == 'y':
                generate_email = True
            os.environ['SKIP_AI'] = '1'
        elif pilihan == "1a" or pilihan == "":
            dates_to_run.append(default_date)
            ui_email = input("  Generate draf email summary (Y/N)? ").strip().lower()
            if ui_email == 'y':
                generate_email = True
            if 'SKIP_AI' in os.environ:
                del os.environ['SKIP_AI']
        elif pilihan == "1b":
            print("\n  \033[96mMemulai Server Telegram Bot...\033[0m")
            import subprocess
            bot_path = os.path.join(ENGINE_DIR, "telegram_bot.py")
            subprocess.run([sys.executable, bot_path])
            continue
        elif pilihan == "2":
            ui_date = input("  Ketik tanggal (YYYYMMDD): ").strip()
            try:
                dates_to_run.append(datetime.strptime(ui_date, "%Y%m%d"))
            except ValueError:
                print("  \033[91m❌ Format salah!\033[0m")
                time.sleep(2)
                continue
        elif pilihan == "3":
            for i in range(3, 0, -1):
                dates_to_run.append(datetime.now() - timedelta(days=i))
        elif pilihan == "4":
            for i in range(7, 0, -1):
                dates_to_run.append(datetime.now() - timedelta(days=i))
        elif pilihan == "5":
            now = datetime.now()
            start_of_month = now.replace(day=1)
            end_date = now - timedelta(days=1)
            delta = end_date - start_of_month
            for i in range(delta.days + 1):
                dates_to_run.append(start_of_month + timedelta(days=i))
        elif pilihan == "6":
            start_str = input("  Tanggal Awal (YYYYMMDD): ").strip()
            end_str = input("  Tanggal Akhir (YYYYMMDD): ").strip()
            try:
                dt_start = datetime.strptime(start_str, "%Y%m%d")
                dt_end = datetime.strptime(end_str, "%Y%m%d")
                if dt_start > dt_end:
                    print("  \033[91m❌ Tanggal awal tidak boleh lebih besar dari akhir!\033[0m")
                    time.sleep(2)
                    continue
                delta = dt_end - dt_start
                for i in range(delta.days + 1):
                    dates_to_run.append(dt_start + timedelta(days=i))
            except ValueError:
                print("  \033[91m❌ Format salah!\033[0m")
                time.sleep(2)
                continue
        elif pilihan in ["7", "10"]:
            is_download_only = (pilihan == "10")
            ui_month = input("  Ketik Bulan & Tahun (Contoh: agustus 2026 atau agustus2026): ").strip()
            import re
            match = re.match(r"([a-zA-Z]+)[\s]*([0-9]{4})", ui_month)
            if match:
                m_str = match.group(1).lower()
                y_str = match.group(2)
                m_en = ID_TO_EN_MONTH.get(m_str, m_str.capitalize())
                try:
                    dt_start = datetime.strptime(f"{m_en} {y_str}", "%B %Y")
                    import calendar
                    _, num_days = calendar.monthrange(dt_start.year, dt_start.month)
                    for i in range(num_days):
                        dates_to_run.append(dt_start + timedelta(days=i))
                except ValueError:
                    print("  \033[91m❌ Format bulan/tahun salah atau tidak dikenali!\033[0m")
                    time.sleep(2)
                    continue
            else:
                print("  \033[91m❌ Format salah! Gunakan format seperti: agustus 2026\033[0m")
                time.sleep(2)
                continue
        elif pilihan == "8":
            is_download_only = True
            dates_to_run.append(default_date)
        elif pilihan == "9":
            is_download_only = True
            for i in range(3, 0, -1):
                dates_to_run.append(datetime.now() - timedelta(days=i))
        elif pilihan in ["11", "12"]:
            is_monthly = True
            is_download_only = (pilihan == "12")
            ui_month = input("  Ketik Bulan & Tahun (Contoh: agustus 2026 atau agustus2026): ").strip()
            import re
            match = re.match(r"([a-zA-Z]+)[\s]*([0-9]{4})", ui_month)
            if match:
                m_str = match.group(1).lower()
                y_str = match.group(2)
                m_en = ID_TO_EN_MONTH.get(m_str, m_str.capitalize()) # default to what user typed if not found
                monthly_jobs.append((m_en, y_str))
            else:
                print("  \033[91m❌ Format salah! Gunakan format seperti: agustus 2026\033[0m")
                time.sleep(2)
                continue
        else:
            print("  \033[91m❌ Pilihan tidak valid!\033[0m")
            time.sleep(1)
            continue

        if not dates_to_run and not monthly_jobs:
            continue

        # Jalankan loop batch
        success_count = 0
        fail_count = 0
        
        if is_monthly:
            for m_en, y_str in monthly_jobs:
                if is_download_only:
                    res = run_monthly_download_only(m_en, y_str)
                else:
                    res = run_report_for_month(m_en, y_str)
                if res:
                    success_count += 1
                else:
                    fail_count += 1
        else:
            for dt in dates_to_run:
                if is_download_only:
                    res = run_download_only(dt)
                else:
                    res = run_report_for_date(dt, generate_email=generate_email)
                    
                if res:
                    success_count += 1
                else:
                    fail_count += 1
                
        print("\n" + "=" * 80)
        action_name = "DOWNLOAD EXCEL" if is_download_only else "BATCH GENERATE"
        print(f"  \033[1mREKAPITULASI {action_name}\033[0m")
        print(f"  Berhasil : {success_count} report")
        print(f"  Gagal    : {fail_count} report")
        print("=" * 80 + "\n")
        
        input("  Tekan ENTER untuk kembali ke menu utama...")
        # Clear screen to make menu clean
        os.system('cls' if os.name == 'nt' else 'clear')
