import os

path = r'C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\engine\main.py'
with open(path, encoding='utf-8') as f:
    text = f.read()

# 1. Update _make_infra_chart to Bar Chart and Navy color scheme
old_infra = """def _make_infra_chart(df, title, ylabel, filename, threshold_line=None):
    \"\"\"Helper: membuat line chart infrastruktur per server.\"\"\"
    fig, ax = plt.subplots(figsize=(12, 5))
    time_col = df.columns[0]  # Kolom pertama = Time
    x_labels = df[time_col].astype(str).tolist()

    for server in SERVERS:
        if server in df.columns:
            values = pd.to_numeric(df[server], errors='coerce').fillna(0)
            ax.plot(x_labels, values, label=server, color=SERVER_COLORS.get(server, '#666'),
                    linewidth=1.2, markersize=2)

    if threshold_line:
        ax.axhline(y=threshold_line, color='red', linestyle='--', linewidth=0.8, alpha=0.7, label=f'Threshold {threshold_line}%')

    ax.set_title(title, fontsize=11, fontweight='bold', color='#1a365d')
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=45, labelsize=7)
    ax.tick_params(axis='y', labelsize=8)
    ax.legend(fontsize=6, ncol=4, loc='upper right')
    ax.grid(True, alpha=0.2)
    ax.set_ylim(bottom=0)

    # Kurangi jumlah label X agar tidak terlalu ramai
    step = max(1, len(x_labels) // 12)
    ax.set_xticks(range(0, len(x_labels), step))
    ax.set_xticklabels([x_labels[i] for i in range(0, len(x_labels), step)])

    plt.tight_layout()
    chart_path = os.path.join(TEMP_DIR, filename)
    plt.savefig(chart_path, dpi=150)
    plt.close()
    return chart_path"""

new_infra = """def _make_infra_chart(df, title, ylabel, filename, threshold_line=None):
    \"\"\"Helper: membuat bar chart infrastruktur max per jam.\"\"\"
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
    return chart_path"""

if old_infra in text:
    text = text.replace(old_infra, new_infra)
    print("Replaced _make_infra_chart")
else:
    print("Could not find old_infra")

# 2. Update XLA chart colors
old_xla = """    # --- XLA Hourly Trend ---
    if 'xla_hourly_data' in data:
        hd = data['xla_hourly_data']
        fig, ax = plt.subplots(figsize=(10, 3.5))
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
        plt.close()"""

new_xla = """    # --- XLA Hourly Trend ---
    if 'xla_hourly_data' in data:
        hd = data['xla_hourly_data']
        fig, ax = plt.subplots(figsize=(12, 5))
        fig.patch.set_facecolor('#06152D')
        ax.set_facecolor('#06152D')
        
        hours = [str(h) for h in hd['hours']]
        ax.bar(hours, hd['completed'], label='Completed', color='#22c55e', edgecolor='#0f172a', linewidth=1.2)
        if any(v > 0 for v in hd['unprocessed']):
            ax.bar(hours, hd['unprocessed'], bottom=hd['completed'], label='Unprocessed', color='#f59e0b', edgecolor='#0f172a', linewidth=1.2)
        if any(v > 0 for v in hd['error']):
            ax.bar(hours, hd['error'], bottom=[c + u for c, u in zip(hd['completed'], hd['unprocessed'])],
                   label='Error', color='#ef4444', edgecolor='#0f172a', linewidth=1.2)
        ax.set_title(f'XLA Volume {freq_en} Trend', fontsize=11, fontweight='bold', color='#D4AF37')
        ax.set_ylabel('Count', color='#e2e8f0')
        ax.legend(fontsize=8, facecolor='#06152D', edgecolor='#D4AF37', labelcolor='#e2e8f0')
        ax.grid(True, alpha=0.2, axis='y', color='#e2e8f0')
        ax.tick_params(axis='x', rotation=45, labelsize=7.5, colors='#e2e8f0')
        ax.tick_params(axis='y', labelsize=7.5, colors='#e2e8f0')
        
        def million_formatter(x, pos):
            if x >= 1e6:
                return f"{x*1e-6:,.1f} jt".replace('.', ',').replace(',0 jt', ' jt')
            return f"{x:,.0f}".replace(',', '.')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(million_formatter))
        
        plt.tight_layout()
        chart_paths['chart_xla'] = os.path.join(TEMP_DIR, 'chart_xla.png')
        plt.savefig(chart_paths['chart_xla'], dpi=150)
        plt.close()"""

if old_xla in text:
    text = text.replace(old_xla, new_xla)
    print("Replaced xla chart")
else:
    print("Could not find old_xla")

# 3. Update Concurrent chart colors & type to Bar
old_conc = """    # --- Concurrent Programs per Hour ---
    if 'trx_concurrent_hourly' in data:
        ch = data['trx_concurrent_hourly']
        if ch['hours']:
            fig, ax = plt.subplots(figsize=(10, 3.5))
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
            plt.close()"""

new_conc = """    # --- Concurrent Programs per Hour ---
    if 'trx_concurrent_hourly' in data:
        ch = data['trx_concurrent_hourly']
        if ch['hours']:
            fig, ax = plt.subplots(figsize=(12, 5))
            fig.patch.set_facecolor('#06152D')
            ax.set_facecolor('#06152D')
            
            hours = [str(h) for h in ch['hours']]
            ax.bar(range(len(hours)), ch['hits'], color='#D4AF37', edgecolor='#0f172a', linewidth=1.2)
            
            title_c = 'Distribusi Concurrent Request Per Hari' if is_monthly_mode else 'Distribusi Concurrent Request Per Jam'
            ax.set_title(title_c, fontsize=11, fontweight='bold', color='#D4AF37')
            ax.set_ylabel('Total Hits', color='#e2e8f0')
            ax.set_xticks(range(len(hours)))
            ax.set_xticklabels(hours, rotation=45, fontsize=7.5, colors='#e2e8f0')
            ax.tick_params(axis='y', labelsize=7.5, colors='#e2e8f0')
            ax.grid(True, alpha=0.2, color='#e2e8f0')
            ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'.replace(',', '.')))
            plt.tight_layout()
            chart_paths['chart_concurrent'] = os.path.join(TEMP_DIR, 'chart_concurrent.png')
            plt.savefig(chart_paths['chart_concurrent'], dpi=150)
            plt.close()"""

if old_conc in text:
    text = text.replace(old_conc, new_conc)
    print("Replaced conc chart")
else:
    print("Could not find old_conc")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

