# 📘 DOKUMENTASI SPESIFIKASI SISTEM: AUTOMATION KIBANA REPORT & TELEGRAM BOT

Dokumen ini disusun sebagai cetak biru (*blueprint*) dan spesifikasi teknis lengkap untuk pengembangan program **Automasi Monitoring, Screenshot Dashboard Kibana, Ekstraksi Data ke Excel, dan Integrasi Telegram Bot**. Dokumen ini siap digunakan sebagai referensi pengembang maupun sebagai konteks *prompting* ke model AI.

---

## 🎯 1. LATAR BELAKANG & TUJUAN PEMBUATAN PROGRAM

### 1.1 Masalah Operasional
1. **Beban Kerja Manual yang Repetitif:** Tim operasional/monitoring (SRE / DevOps / IT Ops) harus memantau 4 dashboard Kibana berukuran panjang secara berkala setiap hari dan setiap kali terjadi insiden (*incident response*).
2. **Proses Pengambilan Data Lambat:** Pengambilan *screenshot* manual (termasuk *scroll* dari atas sampai bawah) dan ekspor tabel satu per satu memakan waktu 15–30 menit per siklus pelaporan.
3. **Kebutuhan Respon Cepat saat Insiden:** Ketika terjadi degradasi performa atau transaksi anjlok, tim membutuhkan visibilitas data dalam rentang waktu spesifik (misal: 10 menit, 40 menit, 1 jam, atau 24 jam terakhir) secara instan tanpa harus membuka laptop dan login VPN/Kibana manual.
4. **Batasan Keamanan Korporat (Corporate Security & IT Policy):** Komputer kerja berada dalam domain korporat (Bank BNI) dengan kebijakan keamanan ketat (EDR, antivirus, pemblokiran unduhan binary eksternal, firewall). Solusi harus **ringan, gratis, dan tidak melanggar security**.

### 1.2 Maksud & Tujuan Utama
1. **Otomatisasi Penuh (End-to-End Automation):** Mengambil *screenshot full-page* dari 4 dashboard Kibana utama secara otomatis.
2. **Ekstraksi Data Terstruktur ke Excel:** Mengambil data tabular (Error Jobs, Running Jobs, All Jobs, Raw Log, Resource Usage) dan menyatukannya ke dalam satu file Excel multi-sheet.
3. **Fleksibilitas Rentang Waktu (Dynamic Time Range):** Mampu menarik data berdasarkan kebutuhan:
   - Laporan Harian H-1 (00:00 s.d. 23:59 kemarin).
   - Laporan Insidental: 10 menit, 40 menit, 1 jam, 2 jam, 4 jam, 8 jam, 12 jam, hingga 24 jam ke belakang.
4. **Pelaporan Terpusat via Telegram Bot:** Pengguna cukup mengirim perintah atau menekan tombol interaktif (*inline keyboard*) di Telegram untuk meminta laporan, dan bot langsung membalas dengan foto screenshot + file Excel.
5. **Aman & Ringan (Living off the Land):** Memanfaatkan browser Microsoft Edge bawaan OS Windows (`msedge.exe`) dan profil sesi lokal sehingga tidak memicu alarm keamanan/antivirus serta tidak memerlukan lisensi berbayar.

---

## 🏗️ 2. ARSITEKTUR & ALUR KERJA SISTEM (WORKFLOW)

```
                 +-----------------------------------+
                 |    User / Tim Monitoring via      |
                 |      Telegram Chat / Grup         |
                 +-----------------+-----------------+
                                   |
                  (1) Perintah: /report atau tombol
                                   v
                 +-----------------------------------+
                 |         TELEGRAM BOT CORE         |
                 |    (Menerima Request & Timeframe) |
                 +-----------------+-----------------+
                                   |
                    (2) Trigger Script Automation
                                   v
                 +-----------------------------------+
                 |    PLAYWRIGHT BROWSER ENGINE      |
                 |  - Edge Bawaan (msedge.exe)       |
                 |  - Persistent Context Profile     |
                 +--------+-----------------+--------+
                          |                 |
         (3) Inject URL Timeframe     (4) Sesi Login Tersimpan
                          v                 v
           +-----------------------------------------------+
           |         KIBANA DASHBOARD (4 TARGETS)          |
           | 1. L1 Transaction EFS                         |
           | 2. L2 Infra EFS DB                            |
           | 3. L2 Infra EFS App                           |
           | 4. L1 EFS Availability                        |
           +-----------------------+-----------------------+
                                   |
           +-----------------------+-----------------------+
           |                                               |
           v                                               v
+---------------------+                         +---------------------+
| SCREENSHOT MODULE   |                         | DATA EXTRACT MODULE |
| - Lazy-load scroll  |                         | - Export / Query    |
| - Full-page capture |                         | - Multi-sheet Excel |
+----------+----------+                         +----------+----------+
           |                                               |
           +-----------------------+-----------------------+
                                   |
                     (5) Kumpul File Output
                                   v
                 +-----------------------------------+
                 |     TELEGRAM DISPATCH MODULE      |
                 | Mengirim 4 Gambar + 1 File Excel  |
                 +-----------------+-----------------+
                                   |
                                   v
                 +-----------------------------------+
                 | User Menerima Laporan Lengkap     |
                 +-----------------------------------+
```

---

## 📋 3. DETAIL 4 TARGET DASHBOARD KIBANA

Sistem mengelola 4 URL dashboard utama pada Kibana BNI (`kbnhub.bni.co.id`):

| No | Nama Dashboard | Tipe Konten Utama | Kebutuhan Output |
|:--:|:---|:---|:---|
| **1** | **[Centralized] L1 - Transaction EFS** | Success Rate, Total Hit/Request, Response Time, RPM, Error Rate, Chart Time Series, Tabel All Jobs (25k+ docs), On Running Jobs, On Error Jobs, EFS Raw Log | Screenshot Full-Page + Excel Sheet (Error Jobs, Running Jobs, All Jobs Summary) |
| **2** | **[Centralized] L2 - Infrastruktur EFS DB** | CPU Usage Per Hostname, Memory Usage, Disk Free/Usage per Mount Point (`/`, `/boot`, `/data`), Top Process CPU/Memory, Chart Utilisasi Database | Screenshot Full-Page + Excel Sheet (Host Resource Matrix) |
| **3** | **[Centralized] L2 - Infrastruktur EFS App** | CPU & Memory App Node, Top Process Java/Python, Disk Usage per Mount Point Server App, Status Ketersediaan Node | Screenshot Full-Page + Excel Sheet (App Nodes Matrix) |
| **4** | **[Centralized Log] - EFS Availability** | Availability Metric, Service Uptime, Log Error/Warning agregat | Screenshot Full-Page / Top Viewport |

### Format URL Asli:
- **L1 Transaction EFS:**
  `https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/09f9a35d-ee51-4290-9a98-2b4729f5ec85?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-24h%2Fh,to:now))`
- **L2 Infra EFS DB:**
  `https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/74f6689c-3120-4ef6-842b-0fd06f7327ad?_g=(filters:!(),refreshInterval:(pause:!f,value:300000),time:(from:now-1d,to:now))`
- **L2 Infra EFS App:**
  `https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/9ba19c88-763e-4c5f-a95d-86fea0fe09d8?_g=(filters:!(),refreshInterval:(pause:!f,value:300000),time:(from:now-8h,to:now))`
- **L1 EFS Availability:**
  `https://kbnhub.bni.co.id/s/cbs/app/dashboards#/view/96e8bce1-f494-4df6-a5fb-c7a9fe34ddf2?_g=(filters:!(),refreshInterval:(pause:!t,value:60000),time:(from:now-24h%2Fh,to:now))`

---

## ⚙️ 4. SPESIFIKASI FITUR & LOGIKA TEKNIS

### 4.1 Logika Manipulasi Waktu Dinamis (URL Time Injection)
Kibana menyimpan status waktu global pada parameter URL query `_g`. Script memanipulasi rentang waktu tanpa menyentuh UI date-picker:

| Label Menu / Telegram | String Parameter Kibana | Keterangan |
|:---|:---|:---|
| **10 Menit Lalu** | `time:(from:now-10m,to:now)` | Quick check saat lonjakan insiden |
| **40 Menit Lalu** | `time:(from:now-40m,to:now)` | Cek tren setelah deployment/patching |
| **1 Jam Lalu** | `time:(from:now-1h,to:now)` | Monitoring berkala |
| **2 Jam Lalu** | `time:(from:now-2h,to:now)` | Evaluasi insiden sedang berjalan |
| **4 Jam Lalu** | `time:(from:now-4h,to:now)` | Evaluasi shift kerja |
| **8 Jam Lalu** | `time:(from:now-8h,to:now)` | Laporan pergantian shift (8 jam) |
| **12 Jam Lalu** | `time:(from:now-12h,to:now)` | Setengah hari operasional |
| **24 Jam Lalu** | `time:(from:now-24h,to:now)` | 24 jam berjalan |
| **H-1 (Full Day Kemarin)** | `time:(from:now-1d%2Fd,to:now-1d%2Fd)` | 00:00 s.d. 23:59 kemarin (Laporan Harian) |

*Logika Regex Penggantian URL:*
```python
import re
def set_kibana_time(url, timeframe_str):
    # Mengganti parameter waktu lama dengan yang baru
    return re.sub(r'time:\(from:.*?,to:.*?\)', f'time:(from:{timeframe_str},to:now)', url)
```

---

### 4.2 Mekanisme Otentikasi & Bypass Security
1. **Engine Browser:** Menggunakan `playwright` Python dengan opsi `channel="msedge"` (memanggil Microsoft Edge resmi yang terpasang di sistem operasi Windows).
2. **Persistent Session Context:** Menggunakan direktori profil khusus `edge_bot_profile`. 
   - Pada eksekusi perdana: Script membuka browser dengan `headless=False`, mendeteksi halaman SSO/Login, lalu memberikan jeda (`input()` prompt) agar pengguna memasukkan kredensial dan menyelesaikan 2FA/MFA.
   - Pada eksekusi berikutnya: Cookie, localStorage, dan token SSO tersimpan di direktori profil, sehingga browser **langsung masuk ke dashboard tanpa login ulang**.
3. **Tab Grouping / Single Session:** Sesi autentikasi dibagikan ke seluruh tab/halaman baru dalam konteks browser yang sama.

---

### 4.3 Logika Pengambilan Screenshot Full-Page & Lazy Loading
Dashboard Kibana berukuran panjang dan menggunakan teknik *lazy-rendering* (grafik di bagian bawah hanya digambar saat pengguna menggulir layar).
*Langkah pengambilan gambar:*
1. Buka URL target dengan parameter waktu yang sudah diatur.
2. Tunggu status jaringan tenang: `page.wait_for_load_state("networkidle", timeout=60000)`.
3. Lakukan injeksi JavaScript auto-scroll ke bawah dan kembali ke atas:
   ```javascript
   window.scrollTo(0, document.body.scrollHeight);
   // tunggu 2 detik
   window.scrollTo(0, 0);
   // tunggu render visual selesai
   ```
4. Ambil tangkapan layar penuh: `page.screenshot(path=filename, full_page=True)`.
5. Dilengkapi mekanisme *fallback*: Jika `full_page=True` gagal karena halaman melampaui batas canvas memori, otomatis beralih ke tangkapan layar `full_page=False` (top viewport).

---

### 4.4 Logika Ekstraksi Data ke Excel Multi-Sheet
1. **Format Output:** File `.xlsx` tunggal dengan nama terformat: `Kibana_Report_[Timeframe]_[YYYYMMDD_HHMMSS].xlsx`.
2. **Struktur Sheet:**
   - **Sheet 1 (`Summary & KPIS`):** Success Rate, Error Rate, Total Hits, RPM.
   - **Sheet 2 (`On Error Jobs`):** Request ID, Program Name, Error Message, Timestamp.
   - **Sheet 3 (`On Running Jobs`):** Status proses yang sedang berjalan, durasi.
   - **Sheet 4 (`Infra DB Resources`):** Hostname, CPU %, Memory %, Disk Free GB.
   - **Sheet 5 (`Infra App Resources`):** Top Process, Memory Usage per node.
3. **Metode Penarikan Data:**
   - *Opsi 1 (Automasi UI):* Klik otomatis tombol inspect panel ➡️ trigger download CSV ➡️ gabung menggunakan pustaka `pandas`.
   - *Opsi 2 (Elasticsearch Proxy/API Intercept):* Menangkap *response JSON* dari panggilan network `_msearch` Kibana saat halaman dibuka, lalu di-*parse* langsung ke DataFrame.

---

### 4.5 Desain Antarmuka Bot Telegram (Interactive UX)
1. **Perintah Utama:**
   - `/start` atau `/menu`: Menampilkan menu tombol interaktif.
   - `/report`: Menampilkan pilihan rentang waktu.
   - `/harian`: Langsung mengeksekusi laporan H-1 (00:00 s.d. 23:59 kemarin).
2. **Inline Keyboard Buttons (Pilihan Rentang Waktu):**
   ```
   [ ⚡ 10 Menit ]   [ ⏱️ 40 Menit ]
   [ 🕐 1 Jam    ]   [ 🕑 2 Jam    ]
   [ 🕓 4 Jam    ]   [ 🕗 8 Jam    ]
   [ 🕛 12 Jam   ]   [ 📅 24 Jam   ]
   [      📆 Rekap Harian (H-1)    ]
   ```
3. **Respon Status Real-time:**
   - Bot membalas instan: *"⏳ Sedang memproses dashboard Kibana (Rentang: 40 Menit). Mohon tunggu..."*
   - Setelah selesai, bot mengirimkan album foto (4 screenshot) + dokumen file Excel dengan ringkasan status dalam pesan (Success Rate, Total Error, dsb.).

---

## 📂 5. STRUKTUR DIREKTORI PROYEK

```
C:\Users\901191\Music\Automasi EFS\Generate Kibana Report\
│
├── engine/
│   ├── config.json             # Konfigurasi URL dashboard, credentials, path
│   ├── requirements.txt        # Daftar dependency Python
│   ├── main.py                 # Core engine automasi (Playwright & Pandas)
│   ├── telegram_bot.py         # Service Bot Telegram listener & sender
│   └── excel_generator.py      # Modul pembentukan file Excel multi-sheet
│
├── edge_bot_profile/           # Direktori penyimpanan cache, cookie, & sesi login Edge
│
├── Hasil_Report/               # Direktori penyimpanan screenshot gambar (.png)
│   └── YYYYMMDD/
│
├── output/                     # Direktori penyimpanan file Excel (.xlsx) hasil generate
│   └── YYYYMMDD/
│
├── kibana_bot.py               # Script standalone cepat untuk pengujian lokal
├── run.bat                     # Runner sekali-klik (One-click batch script)
└── PROJECT_SPEC.md             # Dokumen spesifikasi teknis (File ini)
```

---

## 🛠️ 6. TECH STACK & PRASYARAT (100% FREE & RINGAN)

1. **Bahasa Pemrograman:** Python 3.10+ (Terpasang pada komputer pengguna).
2. **Library Utama:**
   - `playwright`: Automasi browser modern berbasis event (ringan dan cepat).
   - `pandas` & `openpyxl`: Pemrosesan tabel data dan pembuatan file spreadsheet Excel berformat rapi.
   - `python-telegram-bot` (atau `requests` via Telegram Bot API): Komunikasi bot dua arah.
3. **Aplikasi Pendukung:**
   - Microsoft Edge (Browser bawaan Windows OS - tidak memerlukan driver eksternal manual).
   - Akun Telegram & Bot Token (diperoleh secara gratis melalui `@BotFather`).

---

## 🤖 7. MASTER PROMPT UNTUK AI (PROMPT TEMPLATE)

Jika Anda ingin memberikan spesifikasi ini ke model AI lain untuk membuat kode baru, silakan gunakan format *prompt* berikut:

> **Copy & Paste Prompt Berikut ke AI:**
> 
> *"Bertindaklah sebagai Senior Python Automation Engineer dan DevOps Specialist. Tolong buatkan kode produksi lengkap berdasarkan dokumen spesifikasi teknis berikut:*
> 
> *1. Gunakan Python dengan Playwright (`sync_api`) yang menjalankan Microsoft Edge lokal (`channel='msedge'`) dengan profil persisten (`edge_bot_profile`) agar sesi login tersimpan dan tidak terblokir firewall korporat.*
> *2. Program harus memproses 4 dashboard Kibana (L1 Transaction EFS, L2 Infra EFS DB, L2 Infra EFS App, L1 EFS Availability) dan mampu mengganti parameter waktu URL secara dinamis (`now-10m`, `now-40m`, `now-1h`, `now-2h`, `now-4h`, `now-8h`, `now-12h`, `now-24h`, dan H-1 `now-1d/d`).*
> *3. Implementasikan auto-scroll untuk memicu lazy-loaded charts sebelum mengambil full-page screenshot berkualitas tinggi.*
> *4. Buat modul penarikan data tabel (All Jobs, Running, Error Jobs, Raw Log, Resource Host) yang dikonversi menjadi file Excel `.xlsx` multi-sheet menggunakan Pandas dan Openpyxl.*
> *5. Integrasikan dengan bot Telegram menggunakan tombol inline keyboard untuk pemilihan rentang waktu, indikator loading proses, dan pengiriman otomatis file gambar serta Excel.*
> *6. Kode harus memiliki struktur rapi, error handling tangguh (try-except-fallback), tanpa karakter emoji yang merusak terminal Windows cp1252, dan siap dijalankan melalui file batch `run.bat`."*

---
*Dokumen ini diperbarui secara otomatis pada direktori proyek:*  
`C:\Users\901191\Music\Automasi EFS\Generate Kibana Report\PROJECT_SPEC.md`
