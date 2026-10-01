# EFS DAILY HEALTH REPORT
**Periode:** 14 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260714.xlsx, EFS_Infrastructures_20260714.xlsx, EFS_XLA_20260714.xlsx, EFS_GL_20260714.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,346,394
- **XLA Success Rate:** 99.89%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 3,510
- **Infrastruktur Status:** 1 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 3,510 records. GL Posted mencapai 220,666 (99.80% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.89% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.80% | PASS |

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
| Create Accounting | 1,424 | 1,063 | 327 | 1 | 41.63 | 43.02 | CRITICAL | - |
| Accounting Program | 202 | 105 | 97 | 0 | 29.76 | 31.54 | WARNING | - |
| Journal Import | 1,348 | 1,342 | 5 | 0 | 0.40 | 3.65 | WARNING | - |
| Posting | 1 | 1 | 0 | 0 | 0.03 | 0.03 | HEALTHY | - |
| Posting: Single Ledger | 1,346 | 1,344 | 0 | 0 | 0.38 | 0.50 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 4 | 0 | 0 | 6.70 | 6.78 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.15 | 1.15 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 20.95 | 20.95 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 22 | 18 | 2 | 0 | 55.33 | 58.63 | WARNING | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 36 | 0.25 | Healthy |
| BNI GL Interface Jurnal KLN | 6 | 1.33 | Healthy |
| BNI GL KLN Load File to Table | 6 | 0.18 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,346,394 | Volume total harian |
| Processed (P / XLA=S) | 2,342,884 | Sukses diproses (99.89%) |
| Unprocessed (U) | 3,510 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 221,116
- **2. FAH Processing (FAH Success / Error):** 221,114 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 220,666 / 448
- **4. Transfer to GL (Transferred):** 220,666
- **5. GL Posting (Posted / Unposted):** 220,666 (99.80% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 220,445 | 2 | 429 | 220,014 | 0 |
| CROSS BORDER PAYMENT Custom Application | 401 | 0 | 0 | 401 | 0 |
| TRADE FINANCE Custom Application | 186 | 0 | 0 | 186 | 0 |
| CREDIT CARD Custom Application | 48 | 0 | 17 | 31 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,253,118 | 1,252,518 | 600 | 0.05% | 171,219,778,230,931.50 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 486,662 | 486,662 | 0 | 0.00% | 13,091,816,609,250.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 202,631 | 202,631 | 0 | 0.00% | 42,253,198,041,169.29 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,888 | 182,888 | 0 | 0.00% | -6,733.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 87,937 | 87,937 | 0 | 0.00% | 1,500,745,090.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,862 | 67,862 | 0 | 0.00% | 4,264,105,990.35 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,930 | 41,930 | 0 | 0.00% | 44,801,897,776,673.02 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,855 | 5,855 | 0 | 0.00% | -39,963,598,875,584.04 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,704 | 5,704 | 0 | 0.00% | 21,489,744,041,030.14 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,543 | 4,543 | 0 | 0.00% | 2,976,889,901,638.85 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.2% | 13.9% | 0.0% | 0.0% | 0.0% | 21.4% | 21.4% | 22.8% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.5% | 13.1% | 0.0% | 0.0% | 0.0% | 12.3% | 12.4% | 13.7% | Healthy |
| ebsintslp01 | App | 4.2% | 19.6% | 54.7% | 0.0% | 0.0% | 0.0% | 17.6% | 24.4% | 27.1% | Healthy |
| ebsintslp02 | App | 4.9% | 14.9% | 45.9% | 0.0% | 0.0% | 0.0% | 9.7% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 22.4% | 31.8% | 47.5% | 0.0% | 0.0% | 0.0% | 66.9% | 67.0% | 67.0% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.4% | 24.9% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 21.9% | 40.7% | 85.3% | 0.0% | 0.0% | 0.0% | 56.6% | 61.5% | 63.9% | Critical |
| efsdbslp02 | Database | 17.7% | 29.6% | 54.2% | 0.0% | 0.0% | 0.0% | 58.8% | 58.9% | 58.9% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 3,510 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.80%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
