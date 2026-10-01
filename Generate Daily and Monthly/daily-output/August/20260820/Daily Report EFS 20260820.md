# EFS DAILY HEALTH REPORT
**Periode:** 20 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260820.xlsx, EFS_Infrastructures_20260820.xlsx, EFS_XLA_20260820.xlsx, EFS_GL_20260820.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,541,285
- **XLA Success Rate:** 94.10%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 135,987
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 135,987 records. GL Posted mencapai 225,799 (99.34% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 94.10% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.34% | WARNING |

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
| Create Accounting | 776 | 691 | 82 | 1 | 5.82 | 50.47 | CRITICAL | - |
| Accounting Program | 233 | 123 | 109 | 1 | 54.97 | 73.60 | CRITICAL | [Error] [109x] (no completion text) | [1x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program xla_ap_acct_hooks_pkg.main.  Technical problem : Error encountered in product API for extrac |
| Journal Import | 178 | 175 | 3 | 0 | 6.83 | 28.82 | WARNING | [Warning] [3x] Not all of your data was imported successfully or it was imported with warnings.  Please review output file. |
| Posting | 5 | 5 | 0 | 0 | 2.25 | 2.49 | HEALTHY | - |
| Posting: Single Ledger | 179 | 177 | 0 | 2 | 0.77 | 0.99 | CRITICAL | [Error] [2x] Concurrent program returned no reason for failure. |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 7.49 | 8.03 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.43 | 0.43 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 21.78 | 21.78 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 21 | 21 | 0 | 0 | 27.56 | 30.86 | HEALTHY | - |
| BNI FAH Laporan Konfigurasi | 1 | 1 | 0 | 0 | 5.38 | 5.38 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 18 | 0.03 | Healthy |
| BNI GL Interface Jurnal KLN | 3 | 1.45 | Healthy |
| BNI GL KLN Load File to Table | 3 | 0.20 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,541,285 | Volume total harian |
| Processed (P / XLA=S) | 2,386,301 | Sukses diproses (94.10%) |
| Unprocessed (U) | 135,987 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 227,302
- **2. FAH Processing (FAH Success / Error):** 226,252 / 239
- **3. SLA Accounting (Accounted / Not Accounted):** 225,799 / 453
- **4. Transfer to GL (Transferred):** 225,799
- **5. GL Posting (Posted / Unposted):** 225,799 (99.34% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 226,551 | 163 | 434 | 225,143 | 0 |
| CROSS BORDER PAYMENT Custom Application | 405 | 0 | 0 | 405 | 0 |
| TRADE FINANCE Custom Application | 184 | 0 | 0 | 184 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 17 | 33 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 0 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,394,253 | 1,262,585 | 131,668 | 9.44% | 229,938,508,784,216.47 | Warning |
| DEP-NQ_ED2P_SC_BFST | 486,520 | 486,520 | 0 | 0.00% | 15,517,992,242,065.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 228,679 | 228,679 | 0 | 0.00% | 44,176,457,864,680.78 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,185 | 175,517 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 91,712 | 91,712 | 0 | 0.00% | 2,407,266,673.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,804 | 72,516 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,177 | 43,177 | 0 | 0.00% | 61,949,094,269,666.56 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,950 | 6,950 | 0 | 0.00% | 65,533,801,486,629.14 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,896 | 5,896 | 0 | 0.00% | -38,556,042,649,052.15 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,348 | 5,348 | 0 | 0.00% | 2,387,965,462,715.17 | Healthy |

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
| efsdbslp02 | Database | 35.9% | 59.2% | 96.8% | 54.7% | 57.0% | 61.1% | 50.4% | 50.4% | 50.5% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.8% | 82.8% | 58.4% | 59.0% | 61.1% | 70.2% | 70.2% | 70.2% | Critical |
| efsdbsdr02 | Database | 2.6% | 7.2% | 54.2% | 49.7% | 49.9% | 50.7% | 43.5% | 43.5% | 43.9% | Healthy |
| efsdbslp01 | Database | 11.0% | 45.9% | 98.0% | 52.1% | 54.8% | 59.8% | 46.8% | 55.5% | 63.1% | Critical |
| ebsintslp02 | App | 3.3% | 15.7% | 98.2% | 36.8% | 40.8% | 47.1% | 10.7% | 10.7% | 10.8% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 85.9% | 5.7% | 5.9% | 6.8% | 41.2% | 41.2% | 41.9% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 81.9% | 5.4% | 5.7% | 7.0% | 24.3% | 24.3% | 25.1% | Critical |
| ebsintslp01 | App | 3.8% | 16.8% | 90.9% | 43.5% | 48.6% | 54.5% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 135,987 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.34%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
