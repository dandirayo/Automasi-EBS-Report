# EFS DAILY HEALTH REPORT
**Periode:** 30 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260830.xlsx, EFS_Infrastructures_20260830.xlsx, EFS_XLA_20260830.xlsx, EFS_GL_20260830.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,227,346
- **XLA Success Rate:** 94.42%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 124,651
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 124,651 records. GL Posted mencapai 192,810 (99.50% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 94.42% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.50% | PASS |

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
| Create Accounting | 146 | 66 | 78 | 0 | 40.53 | 69.10 | WARNING | - |
| Accounting Program | 225 | 131 | 94 | 0 | 61.08 | 68.10 | WARNING | [Warning] [94x] (no completion text) |
| Journal Import | 120 | 120 | 0 | 0 | 1.83 | 13.10 | HEALTHY | - |
| Posting: Single Ledger | 120 | 120 | 0 | 0 | 0.68 | 0.80 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 5.21 | 5.27 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 18.38 | 18.38 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 23 | 21 | 0 | 0 | 22.36 | 22.73 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,227,346 | Volume total harian |
| Processed (P / XLA=S) | 2,102,695 | Sukses diproses (94.42%) |
| Unprocessed (U) | 124,651 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 193,773
- **2. FAH Processing (FAH Success / Error):** 192,937 / 78
- **3. SLA Accounting (Accounted / Not Accounted):** 192,810 / 127
- **4. Transfer to GL (Transferred):** 192,810
- **5. GL Posting (Posted / Unposted):** 192,810 (99.50% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 193,521 | 2 | 125 | 192,636 | 0 |
| CROSS BORDER PAYMENT Custom Application | 129 | 0 | 0 | 129 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 27 | 0 | 0 | 27 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 3 | 0 | 0 | 3 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,201,473 | 1,076,825 | 124,648 | 10.37% | 17,260,170,002,664.05 | Warning |
| DEP-NQ_ED2P_SC_BFST | 449,707 | 449,707 | 0 | 0.00% | 9,732,265,874,698.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 206,509 | 206,509 | 0 | 0.00% | 4,479,055,100,280.60 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,845 | 196,845 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 87,017 | 87,017 | 0 | 0.00% | 1,481,577,382.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,796 | 72,796 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,673 | 5,673 | 0 | 0.00% | -36,309,725,515,362.70 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,515 | 3,515 | 0 | 0.00% | 74,107,943,554.12 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,452 | 2,452 | 0 | 0.00% | 7,472,486,024.83 | Healthy |
| BRA-NQ_ED2P_ELOG | 867 | 867 | 0 | 0.00% | 359,965,397,940.00 | Healthy |

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
| efsdbslp02 | Database | 28.9% | 41.7% | 88.2% | 57.1% | 57.5% | 58.3% | 50.6% | 50.7% | 50.7% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.0% | 77.0% | 61.7% | 62.1% | 63.1% | 70.3% | 70.3% | 70.5% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.3% | 27.2% | 50.0% | 50.2% | 51.1% | 43.5% | 43.6% | 43.6% | Healthy |
| ebsintslp02 | App | 3.6% | 8.5% | 98.5% | 42.6% | 43.0% | 44.5% | 10.7% | 10.7% | 11.0% | Critical |
| efsdbslp01 | Database | 16.5% | 32.7% | 96.4% | 54.3% | 54.9% | 56.6% | 46.3% | 50.7% | 55.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 82.5% | 6.0% | 6.3% | 7.6% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.9% | 6.4% | 6.5% | 7.5% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.0% | 8.0% | 71.5% | 47.3% | 47.6% | 49.0% | 15.8% | 15.8% | 16.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 124,651 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.50%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
