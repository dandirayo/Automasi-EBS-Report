# EFS DAILY HEALTH REPORT
**Periode:** 22 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260822.xlsx, EFS_Infrastructures_20260822.xlsx, EFS_XLA_20260822.xlsx, EFS_GL_20260822.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,320,568
- **XLA Success Rate:** 94.70%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 123,599
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 123,599 records. GL Posted mencapai 203,511 (99.49% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 94.70% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.49% | WARNING |

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
| Create Accounting | 147 | 67 | 78 | 0 | 40.00 | 64.11 | WARNING | - |
| Accounting Program | 226 | 138 | 88 | 0 | 51.67 | 62.22 | WARNING | [Warning] [88x] (no completion text) |
| Journal Import | 146 | 146 | 0 | 0 | 3.33 | 12.40 | HEALTHY | - |
| Posting: Single Ledger | 146 | 146 | 0 | 0 | 0.69 | 0.98 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 7.09 | 7.27 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.63 | 1.63 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 19.60 | 19.60 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 16 | 16 | 0 | 0 | 15.68 | 19.71 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,320,568 | Volume total harian |
| Processed (P / XLA=S) | 2,196,969 | Sukses diproses (94.70%) |
| Unprocessed (U) | 123,599 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 204,550
- **2. FAH Processing (FAH Success / Error):** 203,687 / 78
- **3. SLA Accounting (Accounted / Not Accounted):** 203,601 / 86
- **4. Transfer to GL (Transferred):** 203,511
- **5. GL Posting (Posted / Unposted):** 203,511 (99.49% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 203,692 | 2 | 66 | 202,749 | 0 |
| CROSS BORDER PAYMENT Custom Application | 507 | 0 | 0 | 507 | 0 |
| TRADE FINANCE Custom Application | 180 | 0 | 0 | 180 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 54 | 0 | 18 | 36 | 0 |
| TREASURY Custom Application | 14 | 0 | 0 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,263,148 | 1,139,554 | 123,594 | 9.78% | 22,438,748,813,436.65 | Warning |
| DEP-NQ_ED2P_SC_BFST | 465,152 | 465,152 | 0 | 0.00% | 11,900,370,132,197.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 217,140 | 217,140 | 0 | 0.00% | 5,425,037,114,220.45 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,003 | 195,003 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 94,032 | 94,032 | 0 | 0.00% | 3,571,538,299.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,860 | 72,860 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,900 | 5,900 | 0 | 0.00% | -37,753,678,492,524.43 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,887 | 2,887 | 0 | 0.00% | 18,752,741,914.70 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,630 | 2,630 | 0 | 0.00% | 47,701,997,237.51 | Healthy |
| BRA-NQ_ED2P_ELOG | 872 | 872 | 0 | 0.00% | 355,426,244,691.00 | Healthy |

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
| efsdbslp02 | Database | 24.3% | 39.9% | 97.2% | 55.1% | 55.5% | 56.5% | 50.4% | 50.5% | 50.5% | Critical |
| efsdbsdr01 | Database | 33.2% | 37.8% | 77.2% | 59.0% | 59.3% | 60.7% | 70.2% | 70.2% | 71.0% | Warning |
| efsdbsdr02 | Database | 2.6% | 10.5% | 36.6% | 49.8% | 50.2% | 51.0% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 36.8% | 40.9% | 99.5% | 40.7% | 41.0% | 43.7% | 10.7% | 10.7% | 11.0% | Critical |
| efsdbslp01 | Database | 16.6% | 33.7% | 97.3% | 52.5% | 53.2% | 54.4% | 50.0% | 55.0% | 59.2% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.3% | 5.7% | 5.8% | 7.1% | 24.3% | 24.3% | 25.3% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 87.1% | 5.9% | 6.0% | 7.0% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.1% | 8.4% | 77.9% | 47.0% | 47.4% | 49.2% | 15.8% | 15.8% | 16.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 123,599 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.49%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
