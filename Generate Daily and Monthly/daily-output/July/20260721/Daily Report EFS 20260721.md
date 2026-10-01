# EFS DAILY HEALTH REPORT
**Periode:** 21 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260721.xlsx, EFS_Infrastructures_20260721.xlsx, EFS_XLA_20260721.xlsx, EFS_GL_20260721.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,457,951
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,120
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,120 records. GL Posted mencapai 217,161 (99.82% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | PASS |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | PASS |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.82% | PASS |

### Alur Pemrosesan Akuntansi End-to-End (Data Pipeline)
1. **Source Apps:** Aplikasi hulu (ICONS, Credit Card, Cross Border, Joint Finance) mentransfer file transaksi harian.
2. **FAH & XLA Intake:** Validasi kelayakan format file sumber dan pendaftaran event transaksi di Subledger.
3. **Create Accounting:** Penerjemahan event transaksi menjadi entri jurnal debit/kredit standar (Accounting Program).
4. **Transfer to GL:** Pengiriman jurnal accounted ke antarmuka buku besar (Journal Import).
5. **GL Posting:** Pembukuan resmi jurnal ke saldo buku besar (GL_BALANCES).

### Glosari Istilah Kunci
- **XLA (Subledger Accounting):** Modul akuntansi sentral Oracle yang memetakan transaksi bisnis hulu menjadi jurnal standar.
- **FAH (Financial Accounting Hub):** Gerbang penerima data aplikasi eksternal untuk memvalidasi format data sebelum diproses akuntansi.
- **Accounted vs Not Accounted:** *Accounted* = jurnal DR/CR berhasil terbentuk; *Not Accounted* = data valid namun jurnal belum terbentuk (menunggu sweep/rule).
- **XLA Error vs Event Unprocessed:** *XLA Error* = transaksi gagal akuntansi (kurs closing belum ada/selisih intercompany); *Unprocessed* = antrean antrean harian wajar.
- **Posted vs Unposted GL:** *Posted* = resmi mengupdate saldo neraca; *Unposted* = jurnal sudah masuk ke GL tapi belum diposting (tertunda).
- **P95 / P99 Latency:** 95% atau 99% request selesai di bawah durasi tersebut. P99 adalah tolok ukur utama durasi terburuk (*worst-case*).
- **CPU Saturation:** Utilisasi prosesor server >80% (Warning) atau >90% (Critical) yang berpotensi memperlambat antrean Concurrent Manager.

---

## 03. Concurrent Job dan Latency Program
### Monitoring Program Utama EFS (Accounting & GL)
| Program Name | Total Hit | Normal | Warning | Error | P95 (min) | P99 (min) | Status | Detail Pesan (Warning / Error) |
|---|---|---|---|---|---|---|---|---|
| Create Accounting | 2,459 | 2,370 | 83 | 6 | 1.92 | 7.56 | CRITICAL | - |
| Accounting Program | 272 | 162 | 110 | 0 | 33.44 | 36.95 | WARNING | - |
| Journal Import | 2,379 | 2,376 | 3 | 0 | 0.42 | 1.45 | WARNING | - |
| Posting | 6 | 6 | 0 | 0 | 0.68 | 0.78 | HEALTHY | - |
| Posting: Single Ledger | 2,379 | 2,379 | 0 | 0 | 0.40 | 0.45 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 6 | 0 | 0 | 7.03 | 7.81 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.32 | 0.32 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 23.52 | 23.52 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 20 | 20 | 0 | 0 | 31.48 | 32.27 | HEALTHY | - |
| BNI FAH Laporan Konfigurasi | 1 | 1 | 0 | 0 | 0.67 | 0.67 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 18 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 3 | 1.31 | Healthy |
| BNI GL KLN Load File to Table | 3 | 0.18 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,457,951 | Volume total harian |
| Processed (P / XLA=S) | 2,453,831 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,120 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 217,554
- **2. FAH Processing (FAH Success / Error):** 217,552 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 217,161 / 391
- **4. Transfer to GL (Transferred):** 217,161
- **5. GL Posting (Posted / Unposted):** 217,161 (99.82% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 216,914 | 2 | 370 | 216,542 | 0 |
| CROSS BORDER PAYMENT Custom Application | 377 | 0 | 0 | 377 | 0 |
| TRADE FINANCE Custom Application | 178 | 0 | 0 | 178 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 19 | 31 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,346,154 | 1,345,516 | 638 | 0.05% | 172,091,237,128,254.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 486,420 | 486,420 | 0 | 0.00% | 14,249,742,083,071.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 218,300 | 218,300 | 0 | 0.00% | 42,298,267,553,125.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,726 | 182,726 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 86,578 | 86,578 | 0 | 0.00% | 1,515,644,398.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,026 | 68,026 | 0 | 0.00% | 2,056,704,125.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,330 | 42,330 | 0 | 0.00% | 53,345,726,721,127.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,236 | 7,236 | 0 | 0.00% | 57,343,192,282,442.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,875 | 5,875 | 0 | 0.00% | -39,794,268,581,739.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,018 | 4,018 | 0 | 0.00% | 2,668,791,272,745.00 | Healthy |

### Glosarium Alur Akuntansi End-to-End (Data Pipeline EFS)
- **1. FAH Interface / Intake:** Masuk FAH (staging transaksi sumber).
- **2. FAH Processing:** Validasi struktur file (FAH Success vs FAH Error).
- **3. XLA Event Processing:** Registrasi event akuntansi (Entities Invalid / Stuck in XLA).
- **4. SLA Accounting:** Create Accounting untuk membentuk jurnal debit-kredit (Accounted vs Not Accounted).
- **5. Transfer to GL:** Pemindahan batch jurnal accounted ke GL Interface.
- **6. GL Journal Import:** Pembentukan entri jurnal di General Ledger.
- **7. GL Posting:** Pembukuan final saldo jurnal ke buku besar (Posted vs Unposted).

---

## 07. Financial Footprint (Distribusi Currency)
| Currency | Count | Amount | Base Amount |
|---|---|---|---|
| USD | 17,699 | -23,486,136.87 | 4,620,821,992.85 |
| SGD | 2,492 | 116,544.57 | 873,114,877.55 |
| HKD | 301 | 331,694.27 | 713,506,842.16 |
| JPY | 340 | 7,523,297.00 | 459,769,945.48 |
| AUD | 100 | 51,756.95 | 282,603,559.83 |
| EUR | 235 | 23,701.80 | 280,223,208.96 |
| IDR | 2,043,234 | -1,860,571,765,233.00 | -1,860,571,765,233.00 |
| BNI_LEDGER_IDR | 2,065,025 | -1,860,584,417,103.10 | -1,853,031,138,234.78 |

---

## 08. Infrastructure Health (Utilisasi Server)
| Host / Server | Peran | CPU Min | CPU Avg | CPU Max | Mem Min | Mem Avg | Mem Max | Disk Min | Disk Avg | Disk Max | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ebsintsdr01 | App | 1.7% | 2.3% | 9.9% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 23.1% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.4% | 9.1% | 0.0% | 0.0% | 0.0% | 12.6% | 12.6% | 14.2% | Healthy |
| ebsintslp01 | App | 4.4% | 16.6% | 47.9% | 0.0% | 0.0% | 0.0% | 17.9% | 18.0% | 18.0% | Healthy |
| ebsintslp02 | App | 4.7% | 15.3% | 52.0% | 0.0% | 0.0% | 0.0% | 9.9% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 35.2% | 41.2% | 61.2% | 0.0% | 0.0% | 0.0% | 67.7% | 67.8% | 67.9% | Warning |
| efsdbsdr02 | Database | 3.4% | 6.1% | 19.4% | 0.0% | 0.0% | 0.0% | 46.5% | 46.6% | 46.7% | Healthy |
| efsdbslp01 | Database | 18.9% | 42.8% | 74.9% | 0.0% | 0.0% | 0.0% | 57.9% | 61.1% | 65.0% | Warning |
| efsdbslp02 | Database | 19.3% | 30.6% | 63.8% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,120 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.82%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

---

## 10. Prioritas Perbaikan dan Action Items
- **P1 (Segera):** Drain residual queue XLA (DEP-NQ_ED2P_INVV, LON-NQ_ED2P_BORV, CTA-NQ_ED2P_CTAV).
- **P1 (Segera):** RCA latency Report Set, FAH Process, dan Create Accounting terhadap CPU contention.
- **P2 (Hari ini):** Rekonsiliasi GL leak (79 FAH Error dan 88 Not Accounted).
- **P3 (Mingguan):** Capacity hygiene pada node disk dan memory database.

---

## 11. Rekonsiliasi dan Kualitas Data
| Pemeriksaan | Hasil |
|---|---|
| XLA status components vs source totals | PASS |
| GL Accounted + Not Accounted vs FAH Success | PASS |
| GL Transferred + Stuck vs Accounted | PASS |
| GL Posted + Unposted vs Transferred | PASS |
| GL Accounted DR = CR | PASS |
| GL Blocking Not Accounted vs funnel | CHECK |
