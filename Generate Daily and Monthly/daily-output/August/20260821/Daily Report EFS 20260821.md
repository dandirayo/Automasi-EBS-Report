# EFS DAILY HEALTH REPORT
**Periode:** 21 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260821.xlsx, EFS_Infrastructures_20260821.xlsx, EFS_XLA_20260821.xlsx, EFS_GL_20260821.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,571,672
- **XLA Success Rate:** 94.19%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 136,432
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 136,432 records. GL Posted mencapai 229,522 (99.34% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 94.19% | WARNING |
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
| Create Accounting | 163 | 80 | 81 | 0 | 42.03 | 65.78 | WARNING | - |
| Accounting Program | 232 | 126 | 106 | 0 | 55.25 | 64.30 | WARNING | [Warning] [106x] (no completion text) |
| Journal Import | 164 | 164 | 0 | 0 | 3.77 | 11.38 | HEALTHY | - |
| Posting: Single Ledger | 164 | 164 | 0 | 0 | 0.67 | 0.78 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 4.11 | 4.17 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 3 | 3 | 0 | 0 | 1.10 | 1.11 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 19.88 | 19.88 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 22 | 22 | 0 | 0 | 28.05 | 29.94 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,571,672 | Volume total harian |
| Processed (P / XLA=S) | 2,416,148 | Sukses diproses (94.19%) |
| Unprocessed (U) | 136,432 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 231,038
- **2. FAH Processing (FAH Success / Error):** 230,038 / 198
- **3. SLA Accounting (Accounted / Not Accounted):** 229,522 / 516
- **4. Transfer to GL (Transferred):** 229,522
- **5. GL Posting (Posted / Unposted):** 229,522 (99.34% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 230,210 | 122 | 497 | 228,789 | 0 |
| CROSS BORDER PAYMENT Custom Application | 477 | 0 | 0 | 477 | 0 |
| TRADE FINANCE Custom Application | 185 | 0 | 0 | 185 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 17 | 32 | 0 |
| TREASURY Custom Application | 14 | 0 | 0 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,406,114 | 1,275,160 | 130,954 | 9.31% | 252,067,839,100,527.75 | Warning |
| DEP-NQ_ED2P_SC_BFST | 492,444 | 492,444 | 0 | 0.00% | 16,679,246,416,419.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 231,702 | 231,702 | 0 | 0.00% | 51,242,490,188,100.52 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,673 | 175,869 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 94,548 | 94,548 | 0 | 0.00% | 3,315,194,925.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,826 | 72,538 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,244 | 46,244 | 0 | 0.00% | 66,859,147,784,109.25 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,464 | 7,464 | 0 | 0.00% | 73,917,203,901,167.02 | Healthy |
| LON-NQ_ED2P_BORV | 5,892 | 2,332 | 3,560 | 60.42% | 5,569,651,534,181.09 | Critical |
| LON-Q_GLCP_LOND2140 | 5,886 | 5,886 | 0 | 0.00% | -38,486,236,599,685.40 | Healthy |

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
| efsdbslp02 | Database | 30.7% | 63.1% | 98.0% | 55.1% | 57.2% | 61.3% | 50.4% | 50.5% | 50.7% | Critical |
| efsdbsdr01 | Database | 39.5% | 46.9% | 78.2% | 58.8% | 59.4% | 61.0% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.8% | 8.7% | 40.3% | 49.8% | 50.1% | 51.6% | 43.5% | 43.5% | 43.7% | Healthy |
| efsdbslp01 | Database | 10.5% | 41.0% | 98.0% | 52.2% | 54.8% | 59.9% | 46.4% | 53.6% | 63.3% | Critical |
| ebsintslp02 | App | 3.4% | 31.6% | 99.8% | 39.4% | 42.4% | 48.0% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.6% | 5.4% | 5.8% | 7.0% | 24.3% | 24.3% | 24.8% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.0% | 5.7% | 6.0% | 6.9% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.2% | 16.8% | 95.2% | 46.9% | 49.4% | 54.8% | 15.8% | 15.8% | 15.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 136,432 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
