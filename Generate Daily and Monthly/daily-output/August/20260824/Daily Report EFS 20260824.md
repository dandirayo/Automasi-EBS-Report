# EFS DAILY HEALTH REPORT
**Periode:** 24 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260824.xlsx, EFS_Infrastructures_20260824.xlsx, EFS_XLA_20260824.xlsx, EFS_GL_20260824.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,644,409
- **XLA Success Rate:** 99.27%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,550
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,550 records. GL Posted mencapai 232,429 (99.68% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.27% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.68% | PASS |

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
| Create Accounting | 156 | 53 | 101 | 0 | 40.93 | 63.37 | WARNING | - |
| Accounting Program | 248 | 122 | 126 | 0 | 51.83 | 62.09 | WARNING | [Warning] [126x] (no completion text) |
| Journal Import | 180 | 176 | 4 | 0 | 2.62 | 4.04 | WARNING | [Warning] [4x] Not all of your data was imported successfully or it was imported with warnings.  Please review output file. |
| Posting | 5 | 5 | 0 | 0 | 0.70 | 0.75 | HEALTHY | - |
| Posting: Single Ledger | 177 | 177 | 0 | 0 | 0.73 | 0.87 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 9.72 | 9.98 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 12.72 | 12.72 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 28 | 28 | 0 | 0 | 30.25 | 31.06 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 30 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 5 | 1.99 | Healthy |
| BNI GL KLN Load File to Table | 5 | 0.20 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,644,409 | Volume total harian |
| Processed (P / XLA=S) | 2,619,651 | Sukses diproses (99.27%) |
| Unprocessed (U) | 5,550 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 233,172
- **2. FAH Processing (FAH Success / Error):** 232,913 / 236
- **3. SLA Accounting (Accounted / Not Accounted):** 232,439 / 474
- **4. Transfer to GL (Transferred):** 232,429
- **5. GL Posting (Posted / Unposted):** 232,429 (99.68% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 232,967 | 160 | 472 | 232,302 | 0 |
| CROSS BORDER PAYMENT Custom Application | 80 | 0 | 0 | 80 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 38 | 0 | 0 | 38 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,451,306 | 1,450,633 | 673 | 0.05% | 259,090,949,868,399.69 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 507,747 | 507,747 | 0 | 0.00% | 20,077,140,957,139.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 234,765 | 234,765 | 0 | 0.00% | 66,616,031,832,758.99 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,253 | 176,363 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 97,342 | 97,342 | 0 | 0.00% | 2,670,557,307.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,864 | 72,584 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 51,073 | 51,073 | 0 | 0.00% | 64,510,704,596,223.37 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,821 | 8,821 | 0 | 0.00% | 71,929,478,042,690.41 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 6,063 | 6,062 | 1 | 0.02% | 1,836,238,634,764.90 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,889 | 5,889 | 0 | 0.00% | -37,660,201,006,091.43 | Healthy |

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
| efsdbslp02 | Database | 30.5% | 51.7% | 93.0% | 55.6% | 57.4% | 61.0% | 50.4% | 50.5% | 50.7% | Critical |
| efsdbsdr01 | Database | 33.4% | 40.7% | 78.2% | 59.6% | 60.1% | 61.2% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.4% | 28.7% | 49.9% | 50.1% | 51.0% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 3.4% | 22.9% | 99.1% | 40.7% | 42.5% | 46.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 16.4% | 44.6% | 97.8% | 53.0% | 55.2% | 59.6% | 50.6% | 57.2% | 66.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.1% | 5.8% | 6.0% | 7.3% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 86.3% | 6.0% | 6.2% | 6.6% | 41.2% | 41.2% | 41.7% | Critical |
| ebsintslp01 | App | 4.1% | 16.5% | 89.5% | 47.1% | 49.4% | 55.2% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,550 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.68%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
