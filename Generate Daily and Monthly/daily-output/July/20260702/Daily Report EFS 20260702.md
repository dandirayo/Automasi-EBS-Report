# EFS DAILY HEALTH REPORT
**Periode:** 2 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260702.xlsx, EFS_Infrastructures_20260702.xlsx, EFS_XLA_20260702.xlsx, EFS_GL_20260702.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 1,610,121
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,532
- **Infrastruktur Status:** 0 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,532 records. GL Posted mencapai 185,210 (99.77% intake).

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
| Create Accounting | 1,552 | 1,458 | 83 | 11 | 2.97 | 12.94 | CRITICAL | - |
| Accounting Program | 262 | 152 | 104 | 6 | 23.31 | 25.73 | CRITICAL | [Error] [6x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program XLA_00200_AAD_C_011130_PKG.EventClass_349.  ORA-01403: no data found. |
| Journal Import | 1,416 | 1,415 | 0 | 1 | 0.40 | 1.77 | CRITICAL | [Error] [1x] Program exited with status 1 |
| Posting: Single Ledger | 1,415 | 1,415 | 0 | 0 | 0.32 | 0.42 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 3 | 0 | 1 | 6.06 | 6.07 | CRITICAL | [Error] [1x] ORA-06502: PL/SQL: numeric or value error: character string buffer too small ORA-06512: at line 17 |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.10 | 1.10 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 18.50 | 18.50 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 26 | 26 | 0 | 0 | 40.51 | 48.22 | HEALTHY | - |
| BNI FAH Laporan Konfigurasi | 1 | 1 | 0 | 0 | 0.72 | 0.72 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,610,121 | Volume total harian |
| Processed (P / XLA=S) | 1,605,589 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,532 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 185,642
- **2. FAH Processing (FAH Success / Error):** 185,636 / 6
- **3. SLA Accounting (Accounted / Not Accounted):** 185,210 / 426
- **4. Transfer to GL (Transferred):** 185,210
- **5. GL Posting (Posted / Unposted):** 185,210 (99.77% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 184,811 | 6 | 406 | 184,399 | 0 |
| CROSS BORDER PAYMENT Custom Application | 468 | 0 | 0 | 468 | 0 |
| TRADE FINANCE Custom Application | 203 | 0 | 0 | 203 | 0 |
| CREDIT CARD Custom Application | 137 | 0 | 18 | 119 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 0 | 4 | 0 |
| TREASURY Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 841,705 | 840,398 | 1,307 | 0.16% | 192,151,229,102,961.03 | Warning |
| DEP-NQ_ED2P_SC_BFST | 276,541 | 276,541 | 0 | 0.00% | 13,630,244,000,874.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,775 | 181,775 | 0 | 0.00% | 5,298.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 115,010 | 115,010 | 0 | 0.00% | 37,121,967,725,051.44 | Healthy |
| LON-Q_GLCP_GEND872 | 69,121 | 69,121 | 0 | 0.00% | -98,430,438.52 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 62,542 | 62,542 | 0 | 0.00% | 1,465,441,627.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 38,384 | 38,384 | 0 | 0.00% | 35,900,043,895,202.70 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,458 | 6,458 | 0 | 0.00% | 41,691,005,213,802.17 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,745 | 5,745 | 0 | 0.00% | -41,283,481,890,359.81 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,633 | 4,633 | 0 | 0.00% | 2,294,954,976,033.04 | Healthy |

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
| ebsintsdr01 | App | 1.9% | 2.6% | 10.8% | 0.0% | 0.0% | 0.0% | 18.2% | 19.1% | 20.3% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.7% | 14.9% | 0.0% | 0.0% | 0.0% | 8.6% | 10.1% | 12.2% | Healthy |
| ebsintslp01 | App | 4.5% | 17.3% | 37.5% | 0.0% | 0.0% | 0.0% | 23.6% | 24.2% | 24.9% | Healthy |
| ebsintslp02 | App | 4.4% | 15.8% | 43.6% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.0% | Healthy |
| efsdbsdr01 | Database | 16.2% | 22.4% | 49.3% | 0.0% | 0.0% | 0.0% | 65.3% | 65.4% | 65.5% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.0% | 16.8% | 0.0% | 0.0% | 0.0% | 46.3% | 46.3% | 46.3% | Healthy |
| efsdbslp01 | Database | 5.7% | 33.2% | 75.8% | 0.0% | 0.0% | 0.0% | 56.2% | 59.6% | 64.2% | Warning |
| efsdbslp02 | Database | 17.3% | 31.3% | 59.4% | 0.0% | 0.0% | 0.0% | 58.1% | 58.2% | 58.2% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,532 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
