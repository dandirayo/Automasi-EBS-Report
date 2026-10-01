# EFS DAILY HEALTH REPORT
**Periode:** 4 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260804.xlsx, EFS_Infrastructures_20260804.xlsx, EFS_XLA_20260804.xlsx, EFS_GL_20260804.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,057,404
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,846
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,846 records. GL Posted mencapai 229,939 (99.79% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.79% | PASS |

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
| Create Accounting | 2,305 | 2,224 | 80 | 1 | 1.93 | 5.25 | CRITICAL | - |
| Accounting Program | 233 | 128 | 105 | 0 | 44.50 | 49.99 | WARNING | - |
| Journal Import | 2,211 | 2,211 | 0 | 0 | 0.48 | 1.90 | HEALTHY | - |
| Posting | 8 | 8 | 0 | 0 | 0.79 | 0.80 | HEALTHY | - |
| Posting: Single Ledger | 2,209 | 2,209 | 0 | 0 | 0.47 | 0.50 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 11.58 | 12.10 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.63 | 0.63 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 19.77 | 19.77 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 17 | 17 | 0 | 0 | 52.71 | 61.64 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,057,404 | Volume total harian |
| Processed (P / XLA=S) | 3,034,556 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,846 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 230,413
- **2. FAH Processing (FAH Success / Error):** 230,411 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 229,939 / 472
- **4. Transfer to GL (Transferred):** 229,939
- **5. GL Posting (Posted / Unposted):** 229,939 (99.79% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,354 | 2 | 450 | 228,902 | 0 |
| CROSS BORDER PAYMENT Custom Application | 547 | 0 | 0 | 547 | 0 |
| PSAK 71 Custom Application | 225 | 0 | 3 | 222 | 0 |
| TRADE FINANCE Custom Application | 198 | 0 | 0 | 198 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 17 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,505,238 | 1,496,498 | 8,740 | 0.58% | 194,100,628,912,357.38 | Warning |
| DEP-NQ_ED2P_SC_BFST | 535,714 | 535,714 | 0 | 0.00% | 16,849,352,725,907.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 415,178 | 415,046 | 132 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 242,455 | 242,452 | 3 | 0.00% | 73,018,253,775,145.42 | Healthy |
| LON-Q_GLCP_GEND872 | 148,934 | 148,934 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 96,638 | 96,638 | 0 | 0.00% | 1,742,726,841.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,899 | 46,899 | 0 | 0.00% | 58,442,465,952,506.28 | Healthy |
| LON-NQ_ED2P_BORV | 16,043 | 5,403 | 10,640 | 66.32% | 4,678,960,822,359.41 | Critical |
| LON-Q_GLCP_GLIF | 11,823 | 11,577 | 246 | 2.08% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,611 | 11,611 | 0 | 0.00% | 1,148,016,022,538.16 | Healthy |

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
| efsdbslp02 | Database | 11.2% | 31.8% | 86.3% | 48.5% | 50.5% | 56.3% | 50.4% | 50.5% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.0% | 74.9% | 52.4% | 52.8% | 53.5% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.6% | 10.6% | 34.5% | 49.0% | 49.4% | 50.2% | 43.3% | 43.3% | 43.3% | Healthy |
| efsdbslp01 | Database | 3.6% | 36.9% | 92.7% | 49.6% | 51.8% | 56.3% | 49.3% | 56.2% | 63.3% | Critical |
| ebsintslp02 | App | 3.4% | 15.2% | 89.0% | 42.8% | 45.2% | 50.0% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintslp01 | App | 3.8% | 14.4% | 80.7% | 50.0% | 52.0% | 57.1% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,846 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.79%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
