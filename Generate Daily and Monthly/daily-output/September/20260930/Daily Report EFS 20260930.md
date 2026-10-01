# EFS DAILY HEALTH REPORT
**Periode:** 30 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260930.xlsx, EFS_Infrastructures_20260930.xlsx, EFS_XLA_20260930.xlsx, EFS_GL_20260930.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,426,587
- **XLA Success Rate:** 98.60%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,610
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,610 records. GL Posted mencapai 117,500 (99.08% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 98.60% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.08% | WARNING |

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
| Create Accounting | 141 | 41 | 88 | 11 | 62.01 | 116.66 | CRITICAL | - |
| Accounting Program | 216 | 95 | 110 | 11 | 80.68 | 122.19 | CRITICAL | [Error] [109x] (no completion text) | [11x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program XLA_00200_AAD_C_011130_PKG.EventClass_352.  ORA-01403: no data found. |
| Journal Import | 139 | 139 | 0 | 0 | 2.09 | 35.78 | HEALTHY | - |
| Posting | 5 | 5 | 0 | 0 | 0.83 | 0.83 | HEALTHY | - |
| Posting: Single Ledger | 138 | 138 | 0 | 0 | 0.92 | 0.98 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 6.55 | 7.10 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 2.73 | 2.73 | HEALTHY | - |
| BNI FAH Journal Reversal | 3 | 3 | 0 | 0 | 27.31 | 27.72 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 25 | 25 | 0 | 0 | 5.20 | 6.88 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 2 | 0.00 | Healthy |
| BNI GL Interface Jurnal KLN | 1 | 3.83 | Healthy |
| BNI GL KLN Load File to Table | 1 | 0.08 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,426,587 | Volume total harian |
| Processed (P / XLA=S) | 1,399,947 | Sukses diproses (98.60%) |
| Unprocessed (U) | 6,610 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 118,593
- **2. FAH Processing (FAH Success / Error):** 117,930 / 254
- **3. SLA Accounting (Accounted / Not Accounted):** 117,500 / 430
- **4. Transfer to GL (Transferred):** 117,500
- **5. GL Posting (Posted / Unposted):** 117,500 (99.08% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 116,840 | 86 | 361 | 116,198 | 0 |
| CROSS BORDER PAYMENT Custom Application | 1,146 | 0 | 0 | 1,146 | 0 |
| PSAK 71 Custom Application | 293 | 168 | 0 | 125 | 0 |
| TRADE FINANCE Custom Application | 214 | 0 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 69 | 0 | 69 | 0 | 0 |
| JOINT FINANCE Custom Application | 14 | 0 | 0 | 14 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 0 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 754,485 | 753,970 | 515 | 0.07% | 408,437,956,088,147.62 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 238,114 | 238,114 | 0 | 0.00% | 18,276,701,920,548.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 197,074 | 177,950 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 96,809 | 96,809 | 0 | 0.00% | 75,316,272,496,513.98 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 56,199 | 56,199 | 0 | 0.00% | 1,856,113,476.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 39,062 | 39,062 | 0 | 0.00% | 76,001,252,932,946.64 | Healthy |
| LON-NQ_ED2P_BORV | 7,233 | 2,842 | 4,391 | 60.71% | 11,127,246,193,632.52 | Critical |
| LON-Q_GLCP_BORV | 6,162 | 4,693 | 1,469 | 23.84% | 27,639,255,741,551.67 | Critical |
| BRA-NQ_ED2P_T_GLDV | 6,114 | 6,114 | 0 | 0.00% | 79,843,166,958,817.05 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,666 | 5,666 | 0 | 0.00% | 27,553,644,200,536.51 | Healthy |

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
| efsdbslp02 | Database | 12.1% | 41.4% | 92.6% | 63.0% | 65.4% | 69.9% | 51.8% | 51.8% | 52.0% | Critical |
| efsdbsdr01 | Database | 13.4% | 15.1% | 56.2% | 70.2% | 70.7% | 72.2% | 70.7% | 70.7% | 71.5% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.7% | 13.3% | 50.1% | 50.5% | 52.2% | 43.9% | 43.9% | 43.9% | Healthy |
| ebsintslp02 | App | 13.6% | 23.0% | 99.5% | 39.8% | 45.2% | 52.8% | 10.8% | 10.8% | 11.3% | Critical |
| efsdbslp01 | Database | 12.8% | 41.4% | 96.8% | 59.4% | 62.2% | 66.8% | 49.0% | 57.8% | 67.3% | Critical |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.2% | 7.3% | 7.5% | 8.9% | 24.4% | 24.4% | 24.8% | Warning |
| ebsintsdr01 | App | 0.6% | 1.6% | 66.5% | 7.4% | 7.6% | 9.0% | 41.3% | 41.3% | 42.1% | Warning |
| ebsintslp01 | App | 3.0% | 11.3% | 71.2% | 50.4% | 53.4% | 59.6% | 15.9% | 15.9% | 16.4% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,610 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.08%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
