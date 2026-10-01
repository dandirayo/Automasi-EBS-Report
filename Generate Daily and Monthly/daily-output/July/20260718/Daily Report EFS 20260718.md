# EFS DAILY HEALTH REPORT
**Periode:** 18 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260718.xlsx, EFS_Infrastructures_20260718.xlsx, EFS_XLA_20260718.xlsx, EFS_GL_20260718.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,198,294
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 605
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 605 records. GL Posted mencapai 185,972 (99.90% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | PASS |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | PASS |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.90% | PASS |

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
| Create Accounting | 240 | 83 | 157 | 0 | 24.75 | 33.32 | WARNING | - |
| Accounting Program | 334 | 119 | 215 | 0 | 28.55 | 33.10 | WARNING | - |
| Journal Import | 197 | 197 | 0 | 0 | 1.83 | 4.63 | HEALTHY | - |
| Posting: Single Ledger | 197 | 197 | 0 | 0 | 0.42 | 0.54 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 4.89 | 5.06 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 0 | 0 | 1 | 0.00 | 0.00 | CRITICAL | [Error] [1x] Concurrent Manager encountered an error while attempting to start your immediate concurrent program XXCUST_GL_DAILY_RATES. Routine &ROUTINE received a return code of failure.  Contact your support representative. |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 22.70 | 22.70 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 10 | 9 | 0 | 0 | 23.78 | 24.72 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,198,294 | Volume total harian |
| Processed (P / XLA=S) | 2,197,689 | Sukses diproses (100.00%) |
| Unprocessed (U) | 605 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 186,152
- **2. FAH Processing (FAH Success / Error):** 186,150 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 185,972 / 178
- **4. Transfer to GL (Transferred):** 185,972
- **5. GL Posting (Posted / Unposted):** 185,972 (99.90% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 185,417 | 2 | 159 | 185,256 | 0 |
| CROSS BORDER PAYMENT Custom Application | 460 | 0 | 0 | 460 | 0 |
| TRADE FINANCE Custom Application | 188 | 0 | 0 | 188 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 17 | 33 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,343,248 | 1,342,652 | 596 | 0.04% | 21,834,660,375,817.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 253,880 | 253,880 | 0 | 0.00% | 6,422,297,590,908.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 191,629 | 191,629 | 0 | 0.00% | 5,880,922,289,854.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 179,267 | 179,267 | 0 | 0.00% | -53,150,917,214.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 153,758 | 153,758 | 0 | 0.00% | 4,052,679,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,829 | 70,829 | 0 | 0.00% | 70,614,552.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,491 | 2,491 | 0 | 0.00% | 16,829,946,082.59 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,116 | 2,116 | 0 | 0.00% | 46,627,959,023.00 | Healthy |
| BRA-NQ_ED2P_ELOG | 564 | 564 | 0 | 0.00% | 293,217,009,359.00 | Healthy |
| LON-Q_GLCP_BORV | 143 | 143 | 0 | 0.00% | 119,263,744,566.00 | Healthy |

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
| ebsintsdr01 | App | 1.8% | 2.7% | 15.6% | 0.0% | 0.0% | 0.0% | 21.5% | 21.6% | 22.9% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.2% | 9.4% | 0.0% | 0.0% | 0.0% | 12.5% | 12.6% | 13.9% | Healthy |
| ebsintslp01 | App | 4.6% | 11.1% | 27.2% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.0% | Healthy |
| ebsintslp02 | App | 4.5% | 7.3% | 23.3% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.4% | Healthy |
| efsdbsdr01 | Database | 34.9% | 40.8% | 63.2% | 0.0% | 0.0% | 0.0% | 67.4% | 67.5% | 67.6% | Warning |
| efsdbsdr02 | Database | 3.4% | 5.7% | 21.0% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.6% | Healthy |
| efsdbslp01 | Database | 12.6% | 24.1% | 38.7% | 0.0% | 0.0% | 0.0% | 56.2% | 61.1% | 62.6% | Warning |
| efsdbslp02 | Database | 6.4% | 24.6% | 73.1% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 605 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.90%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
