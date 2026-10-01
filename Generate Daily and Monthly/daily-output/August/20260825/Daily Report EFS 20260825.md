# EFS DAILY HEALTH REPORT
**Periode:** 25 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260825.xlsx, EFS_Infrastructures_20260825.xlsx, EFS_XLA_20260825.xlsx, EFS_GL_20260825.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,411,347
- **XLA Success Rate:** 99.13%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,443
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,443 records. GL Posted mencapai 202,953 (99.55% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.13% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.55% | PASS |

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
| Create Accounting | 166 | 43 | 121 | 0 | 38.32 | 59.58 | WARNING | - |
| Accounting Program | 255 | 111 | 144 | 0 | 55.39 | 58.24 | WARNING | [Warning] [144x] (no completion text) |
| Journal Import | 137 | 137 | 0 | 0 | 3.62 | 15.64 | HEALTHY | - |
| Posting: Single Ledger | 137 | 137 | 0 | 0 | 0.69 | 0.88 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 6.61 | 7.00 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.47 | 1.47 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 19.20 | 19.20 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 16 | 16 | 0 | 0 | 14.58 | 18.32 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,411,347 | Volume total harian |
| Processed (P / XLA=S) | 2,388,948 | Sukses diproses (99.13%) |
| Unprocessed (U) | 1,443 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 203,865
- **2. FAH Processing (FAH Success / Error):** 203,140 / 713
- **3. SLA Accounting (Accounted / Not Accounted):** 202,956 / 184
- **4. Transfer to GL (Transferred):** 202,953
- **5. GL Posting (Posted / Unposted):** 202,953 (99.55% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 202,860 | 636 | 165 | 202,044 | 0 |
| CROSS BORDER PAYMENT Custom Application | 651 | 1 | 0 | 650 | 0 |
| TRADE FINANCE Custom Application | 195 | 0 | 0 | 195 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 17 | 35 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 4 | 0 | 0 | 4 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 0 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,338,113 | 1,335,781 | 1,329 | 0.10% | 28,561,690,076,197.87 | Warning |
| DEP-NQ_ED2P_SC_BFST | 479,678 | 479,678 | 0 | 0.00% | 13,092,037,800,775.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 213,694 | 213,667 | 0 | 0.00% | 6,348,640,395,948.95 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,654 | 176,756 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,362 | 93,328 | 0 | 0.00% | 1,973,815,852.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,954 | 72,664 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 5,962 | 5,312 | 0 | 0.00% | 89,527,030,203.11 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,924 | 5,906 | 0 | 0.00% | -37,174,275,764,267.67 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,280 | 4,280 | 0 | 0.00% | 55,761,842,499.78 | Healthy |
| BRA-NQ_ED2P_ELOG | 857 | 837 | 0 | 0.00% | 387,347,267,721.00 | Healthy |

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
| efsdbslp02 | Database | 23.0% | 40.0% | 97.4% | 55.4% | 55.9% | 56.8% | 50.5% | 50.5% | 50.6% | Critical |
| efsdbsdr01 | Database | 39.5% | 43.7% | 85.4% | 59.9% | 60.4% | 61.1% | 70.2% | 70.2% | 70.6% | Critical |
| efsdbsdr02 | Database | 2.6% | 10.5% | 39.2% | 49.8% | 50.2% | 51.0% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 3.3% | 8.0% | 98.9% | 40.8% | 41.1% | 42.8% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 16.7% | 32.7% | 97.5% | 53.2% | 53.7% | 55.2% | 47.0% | 54.1% | 63.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 80.4% | 5.7% | 6.0% | 7.3% | 24.3% | 24.3% | 24.6% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 85.4% | 5.9% | 6.2% | 7.1% | 41.2% | 41.2% | 41.6% | Critical |
| ebsintslp01 | App | 4.1% | 8.1% | 72.3% | 47.0% | 47.3% | 49.1% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,443 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.55%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
