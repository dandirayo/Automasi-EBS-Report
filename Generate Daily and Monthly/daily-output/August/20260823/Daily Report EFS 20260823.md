# EFS DAILY HEALTH REPORT
**Periode:** 23 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260823.xlsx, EFS_Infrastructures_20260823.xlsx, EFS_XLA_20260823.xlsx, EFS_GL_20260823.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,646,232
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 19,365
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 19,365 records. GL Posted mencapai 89,312 (99.77% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
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
| Create Accounting | 123 | 37 | 85 | 0 | 60.10 | 62.82 | WARNING | - |
| Accounting Program | 183 | 80 | 103 | 0 | 59.80 | 61.87 | WARNING | [Warning] [103x] (no completion text) |
| Journal Import | 77 | 77 | 0 | 0 | 1.85 | 16.19 | HEALTHY | - |
| Posting: Single Ledger | 77 | 77 | 0 | 0 | 0.60 | 0.78 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 6 | 0 | 0 | 7.19 | 7.65 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.20 | 0.20 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 18.47 | 18.47 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 8 | 8 | 0 | 0 | 12.76 | 17.12 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,646,232 | Volume total harian |
| Processed (P / XLA=S) | 1,626,865 | Sukses diproses (100.00%) |
| Unprocessed (U) | 19,365 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 89,519
- **2. FAH Processing (FAH Success / Error):** 89,426 / 78
- **3. SLA Accounting (Accounted / Not Accounted):** 89,317 / 109
- **4. Transfer to GL (Transferred):** 89,312
- **5. GL Posting (Posted / Unposted):** 89,312 (99.77% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 89,292 | 2 | 107 | 89,163 | 0 |
| CROSS BORDER PAYMENT Custom Application | 117 | 0 | 0 | 117 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 0 | 17 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 659,768 | 652,493 | 7,275 | 1.10% | 18,264,404,834,844.55 | Warning |
| DEP-Q_GLCP_GEND870 | 418,276 | 418,130 | 146 | 0.03% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 234,474 | 234,474 | 0 | 0.00% | 9,047,634,356,070.00 | Healthy |
| LON-Q_GLCP_GEND872 | 150,884 | 150,876 | 8 | 0.01% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 90,088 | 90,088 | 0 | 0.00% | 4,490,040,787,041.95 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 53,464 | 53,464 | 0 | 0.00% | 2,457,760,514.00 | Healthy |
| LON-NQ_ED2P_BORV | 12,841 | 3,717 | 9,124 | 71.05% | 1,444,431,577,235.38 | Critical |
| LON-Q_GLCP_LOND2140 | 11,784 | 11,784 | 0 | 0.00% | -48,621,469,107.00 | Healthy |
| LON-Q_GLCP_GLIF | 5,344 | 5,344 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_BORV | 2,906 | 95 | 2,811 | 96.73% | 283,027,308,140.89 | Critical |

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
| efsdbslp02 | Database | 24.2% | 42.6% | 93.3% | 55.5% | 56.0% | 57.0% | 50.4% | 50.5% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.1% | 79.2% | 59.3% | 59.7% | 60.7% | 70.2% | 70.2% | 70.8% | Warning |
| efsdbsdr02 | Database | 2.5% | 6.3% | 38.8% | 49.9% | 50.0% | 50.6% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 36.8% | 40.8% | 99.4% | 40.7% | 41.0% | 42.3% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 16.6% | 30.6% | 96.0% | 52.8% | 53.1% | 53.7% | 45.2% | 53.0% | 62.6% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 86.2% | 6.0% | 6.1% | 7.0% | 41.2% | 41.2% | 41.6% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.7% | 5.7% | 5.9% | 7.2% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintslp01 | App | 4.1% | 8.1% | 77.8% | 47.1% | 47.4% | 49.0% | 15.8% | 15.8% | 16.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 19,365 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
