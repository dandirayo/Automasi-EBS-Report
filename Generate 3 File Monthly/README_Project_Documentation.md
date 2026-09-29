# Automasi EFS Monthly Report (Generator)

## 1. Latar Belakang & Tujuan
Proses pelaporan bulanan (Monthly Report) untuk **Enterprise Financial System (EFS)** secara rutin membutuhkan pembuatan dokumen turunan, seperti presentasi (.pptx) dan Nota Intern (Notin) (.docx), yang datanya bersumber dari rekapitulasi harian/bulanan. 

**Tujuan pembuatan project ini adalah:**
* **Efisiensi Waktu:** Mengotomatiskan pembuatan 3 file turunan wajib (DOCX, PPTX, PDF) hanya dengan satu kali klik.
* **Minimalisasi Human Error:** Menghindari kelalaian saat harus mengubah teks repetitif (misal: "Juli" menjadi "Agustus") atau menyalin data angka (seperti persentase kesuksesan XLA, jumlah _record_, status _server_ Critical/Warning).
* **Standarisasi Format:** Memastikan dokumen yang dihasilkan (_output_) selalu mengikuti struktur dan desain laporan bulan sebelumnya sebagai _template_ acuan baku.

## 2. Struktur Direktori
Project ini diletakkan berdampingan dengan Automasi EFS Daily, dengan fokus pada pengolahan laporan bulanan.
```text
C:\Users\901191\Music\Automasi EFS\Generate 3 File Monthly\
│
├── run.bat                         # User Interface (CMD Menu) untuk menjalankan automasi
├── generate_monthly_report.py      # Core script Python yang melakukan Find & Replace data
├── PPT_Kosongan.pptx               # (Opsional) File presentasi kosong yang di-generate via Menu 2
└── (Output Files)                  # File hasil (Contoh: 202608 - EFS Monthly Report - August 2026.pdf)
```

## 3. Komponen Utama
### A. `run.bat` (Interactive Menu)
File ini dirancang agar automasi bisa dijalankan dengan mudah oleh _user_ tanpa harus berurusan dengan _command line_. Menu yang tersedia mirip dengan _Automasi Daily_, yaitu:
1. **Generate 3 File Monthly:** Mengeksekusi script utama Python.
2. **Generate PPT Kosongan:** Mem-build file PPT murni (blank) yang bisa digunakan jika user membutuhkan wadah desain dari awal.

### B. `generate_monthly_report.py` (Script Python)
Script utama yang menggunakan pustaka `python-pptx`, `python-docx`, dan `pywin32` (via COM `win32com`). Tugasnya adalah:
1. Membaca _template_ DOCX dan PPTX dari folder referensi bulan sebelumnya (misal: Juli).
2. Melakukan *Find and Replace* otomatis secara menyeluruh, baik pada paragraf biasa, *text box*, maupun tabel.
3. Menyimpan hasil _replace_ menjadi file bulan yang dituju (misal: Agustus).
4. Khusus untuk presentasi, script akan otomatis memanggil *Microsoft PowerPoint* di _background_ untuk mengekspor (Save As) file PPTX ke format PDF.

## 4. Mekanisme Data (Mapping)
Karena *template* yang digunakan bukanlah _template_ kosong (melainkan laporan bulan sebelumnya), script menggunakan sistem _dictionary mapping_ di dalam Python. 
Jika terjadi perubahan angka/data bulan berikutnya, _user_ dapat memperbarui data di baris kode ini:
```python
    mapping = {
        "Juli 2026": "Agustus 2026",
        "July 2026": "August 2026",
        "Juni": "Juli",
        # Data Kustom Bulanan
        "99,51%": "94,76%",
        "70.091.415": "76.013.071",
        "449.109": "1.034.245",
        "137.003": "0",
        "5 / 8": "7 / 8",
        # dst...
    }
```
*Note: Script akan mendeteksi teks di sebelah kiri pada template lama, dan mengubahnya menjadi teks di sebelah kanan.*

## 5. Panduan Penggunaan Lengkap
1. **Persiapan Data:** Buka file `generate_monthly_report.py` dan sesuaikan daftar kata/angka di dalam variabel `mapping` (jika ada data metrik bulan baru yang perlu di-_update_ dari file Markdown laporan bulanan).
2. **Jalankan Menu:** Klik ganda (Double-Click) pada file `run.bat`.
3. **Pilih Opsi:** Ketik `1` lalu tekan `Enter` untuk men-generate laporan.
4. **Validasi:** Tunggu beberapa detik (layar tidak akan langsung menutup). Setelah pesan sukses muncul, file DOCX, PPTX, dan PDF siap digunakan di dalam folder yang sama.
