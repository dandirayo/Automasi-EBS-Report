# EFS Daily Health Report Engine - Guidance & Notes

Dokumen ini berisi panduan singkat mengenai batasan sistem (exceptions) dan cara berinteraksi dengan AI (Antigravity/Gemini) jika di masa depan Anda ingin melakukan update pada report ini.

---

## 1. Exception & Batasan (Jika File Excel Berubah)

Engine ini (Python Pandas) membaca file Excel berdasarkan **struktur yang baku**. Program akan mengalami *error* atau gagal membaca data jika terjadi perubahan struktur dari Oracle/Teams seperti berikut:

*   **Nama Sheet Berubah:** Contoh, sheet `Status Overview` berubah menjadi `Overview`.
*   **Nama Kolom Berubah:** Contoh, kolom `Total` berubah nama menjadi `Jumlah Records`.
*   **Struktur Tabel Bergeser:** Contoh, pada file XLA, tabel data yang biasanya dimulai di baris ke-1 tiba-tiba tergeser karena ada *header* tambahan di atasnya.
*   **Penamaan File Berubah:** Program mencari file dengan format baku, contoh `EFS_GL_YYYYMMDD.xlsx`. Jika format penamaan dari tim berubah, program tidak akan mendeteksi file tersebut.

**Catatan:** Jika yang berubah **hanya isi angkanya atau jumlah baris datanya**, program 100% aman dan akan tetap berjalan dengan normal.

---

## 2. Cara Update / Prompting AI di Masa Depan

Jika di kemudian hari ada perubahan struktur Excel, atau Anda ingin mendesain ulang tampilan PDF-nya, Anda cukup memanggil saya (AI) dengan melampirkan file yang relevan.

Berikut adalah contoh *prompt* (perintah) yang bisa Anda gunakan:

### Skenario A: Ada Perubahan Format Excel dari Oracle
> *"Tolong update EFS Engine. File Excel XLA sekarang formatnya berubah. Nama sheet-nya ganti jadi 'Detail XLA' dan kolom 'Total' sekarang namanya 'Total Transaksi'. Tolong sesuaikan logic python-nya dengan file Excel terbaru yang saya lampirkan ini."*
> **(Pastikan untuk melampirkan/upload file Excel versi terbaru ke dalam chat).**

### Skenario B: Ingin Menambah KPI/Grafik Baru
> *"Saya ingin menambahkan satu metrik KPI baru di bagian atas (Hero Section) PDF. Datanya diambil dari file EFS_Transactions, sheet 'Summary', kolom 'Failed Jobs'. Tolong update `main.py` untuk logic tarikan datanya, dan update `template.html` untuk memunculkan kotak KPI barunya."*

### Skenario C: Ingin Mengubah Desain / Warna PDF
> *"Tolong redesain bagian Footer dan Header di PDF. Saya mau warnanya diganti jadi hijau tua, dan font-nya diperbesar sedikit. Coba update `template.html` dan settingan Playwright di `main.py`."*

### Skenario D: Ingin Menambah Opsi Menu Baru di `run.bat`
> *"Tolong tambahkan opsi nomor 7 di menu interaktif CLI untuk melakukan generate report khusus di hari libur/weekend saja."*

---

## 3. Struktur Folder Terkini

Sebagai pengingat, berikut adalah letak file-file penting Anda:
*   **`engine/main.py`**: Otak utama program. Berisi logic untuk membaca Excel, membuat grafik, dan merender PDF.
*   **`engine/template.html`**: Kerangka desain/layout PDF. Jika ingin mengubah warna, ukuran font, atau letak kotak, ubahnya di sini.
*   **`engine/config.json`**: Berisi batasan batas persentase (threshold) untuk warna merah/kuning/hijau pada indikator KPI.
*   **`.cache/`**: Folder tersembunyi tempat program menyimpan hasil download dari Teams sementara dan foto grafik (*jangan dihapus secara manual*).
*   **`output/`**: Folder tempat PDF dan Markdown hasil akhir disimpan, dikelompokkan per tanggal.
