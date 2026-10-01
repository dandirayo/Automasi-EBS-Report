# EFS DAILY HEALTH REPORT
**Periode:** 17 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260717.xlsx, EFS_Infrastructures_20260717.xlsx, EFS_XLA_20260717.xlsx, EFS_GL_20260717.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,282,000
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 3,974
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 3,974 records. GL Posted mencapai 214,271 (99.77% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | PASS |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | PASS |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.77% | PASS |

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
| Create Accounting | 2,292 | 2,186 | 102 | 4 | 1.81 | 10.10 | CRITICAL | - |
| Accounting Program | 266 | 119 | 146 | 1 | 30.97 | 37.43 | CRITICAL | [Error] [1x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program xla_accounting_pkg.ValidateAAD.  ORA-0000: normal, successful completion. |
| Journal Import | 2,212 | 2,212 | 0 | 0 | 0.40 | 1.47 | HEALTHY | - |
| Posting | 2 | 2 | 0 | 0 | 1.14 | 1.17 | HEALTHY | - |
| Posting: Single Ledger | 2,211 | 2,211 | 0 | 0 | 0.38 | 0.42 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 6 | 0 | 0 | 4.83 | 5.05 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 0 | 0 | 1 | 0.00 | 0.00 | CRITICAL | [Error] [1x] Concurrent Manager encountered an error while attempting to start your immediate concurrent program XXCUST_GL_DAILY_RATES. Routine &ROUTINE received a return code of failure.  Contact your support representative. |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 21.97 | 21.97 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 33 | 31 | 0 | 0 | 31.52 | 41.39 | WARNING | [Warning] [1x] An error occurred while attempting to terminate this request. |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,282,000 | Volume total harian |
| Processed (P / XLA=S) | 2,278,026 | Sukses diproses (100.00%) |
| Unprocessed (U) | 3,974 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 214,771
- **2. FAH Processing (FAH Success / Error):** 214,769 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 214,271 / 498
- **4. Transfer to GL (Transferred):** 214,271
- **5. GL Posting (Posted / Unposted):** 214,271 (99.77% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 213,921 | 2 | 479 | 213,440 | 0 |
| CROSS BORDER PAYMENT Custom Application | 582 | 0 | 0 | 582 | 0 |
| TRADE FINANCE Custom Application | 181 | 0 | 0 | 181 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 17 | 34 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,251,346 | 1,250,704 | 642 | 0.05% | 243,315,992,458,371.53 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 440,897 | 440,897 | 0 | 0.00% | 13,965,264,586,912.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 193,846 | 193,846 | 0 | 0.00% | 43,400,608,225,050.25 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,018 | 182,018 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,970 | 84,970 | 0 | 0.00% | 1,556,174,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,676 | 67,676 | 0 | 0.00% | 1,287,776,572.80 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,839 | 42,839 | 0 | 0.00% | 52,572,101,170,321.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 4,824 | 4,824 | 0 | 0.00% | 58,290,445,099,229.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,271 | 4,271 | 0 | 0.00% | 3,445,250,124,501.54 | Healthy |
| LON-Q_GLCP_BORV | 3,731 | 2,604 | 1,127 | 30.21% | 3,771,205,945,250.00 | Critical |

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
| ebsintsdr01 | App | 1.8% | 2.4% | 10.4% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.8% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 14.6% | 0.0% | 0.0% | 0.0% | 12.5% | 12.5% | 13.9% | Healthy |
| ebsintslp01 | App | 4.4% | 18.9% | 56.5% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.6% | Healthy |
| ebsintslp02 | App | 4.4% | 15.8% | 45.0% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.1% | Healthy |
| efsdbsdr01 | Database | 35.0% | 40.3% | 54.3% | 0.0% | 0.0% | 0.0% | 67.3% | 67.4% | 67.4% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.1% | 17.4% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.6% | Healthy |
| efsdbslp01 | Database | 16.2% | 37.0% | 79.6% | 0.0% | 0.0% | 0.0% | 57.3% | 60.4% | 63.3% | Warning |
| efsdbslp02 | Database | 10.6% | 30.8% | 62.0% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 3,974 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.77%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
