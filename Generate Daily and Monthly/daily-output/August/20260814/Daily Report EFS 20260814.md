# EFS DAILY HEALTH REPORT
**Periode:** 14 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260814.xlsx, EFS_Infrastructures_20260814.xlsx, EFS_XLA_20260814.xlsx, EFS_GL_20260814.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,594,883
- **XLA Success Rate:** 99.25%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,969
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,969 records. GL Posted mencapai 230,558 (99.71% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.25% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.71% | PASS |

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
| Create Accounting | 2,599 | 2,517 | 77 | 3 | 1.98 | 5.47 | CRITICAL | - |
| Accounting Program | 219 | 113 | 106 | 0 | 49.37 | 56.62 | WARNING | [Warning] [106x] (no completion text) |
| Journal Import | 2,491 | 2,487 | 4 | 0 | 0.55 | 1.34 | WARNING | [Warning] [4x] Not all of your data was imported successfully or it was imported with warnings.  Please review output file. |
| Posting | 8 | 8 | 0 | 0 | 0.67 | 0.68 | HEALTHY | - |
| Posting: Single Ledger | 2,488 | 2,488 | 0 | 0 | 0.53 | 0.58 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 8.77 | 9.02 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 3 | 3 | 0 | 0 | 1.20 | 1.20 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 16.38 | 16.38 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 30 | 30 | 0 | 0 | 30.64 | 34.32 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 20 | 0.03 | Healthy |
| BNI GL Interface Jurnal KLN | 4 | 1.90 | Healthy |
| BNI GL KLN Load File to Table | 4 | 0.32 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,594,883 | Volume total harian |
| Processed (P / XLA=S) | 2,570,106 | Sukses diproses (99.25%) |
| Unprocessed (U) | 5,969 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 231,228
- **2. FAH Processing (FAH Success / Error):** 231,025 / 126
- **3. SLA Accounting (Accounted / Not Accounted):** 230,588 / 437
- **4. Transfer to GL (Transferred):** 230,558
- **5. GL Posting (Posted / Unposted):** 230,558 (99.71% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 230,456 | 126 | 417 | 229,806 | 0 |
| CROSS BORDER PAYMENT Custom Application | 468 | 0 | 0 | 468 | 0 |
| TRADE FINANCE Custom Application | 139 | 0 | 0 | 139 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 18 | 33 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,420,655 | 1,419,950 | 705 | 0.05% | 262,676,033,587,870.91 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 492,239 | 492,239 | 0 | 0.00% | 16,670,443,532,150.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 232,441 | 232,441 | 0 | 0.00% | 48,671,020,190,748.24 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,009 | 176,503 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 99,484 | 99,484 | 0 | 0.00% | 2,789,997,817.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,738 | 72,450 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 48,857 | 48,857 | 0 | 0.00% | 62,148,606,842,099.30 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,772 | 7,772 | 0 | 0.00% | 71,664,176,188,663.05 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,874 | 5,874 | 0 | 0.00% | 3,084,748,972,455.74 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,867 | 5,867 | 0 | 0.00% | -37,239,412,078,904.86 | Healthy |

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
| efsdbslp02 | Database | 22.5% | 45.1% | 94.4% | 51.6% | 53.3% | 58.6% | 50.4% | 50.4% | 51.1% | Critical |
| efsdbsdr01 | Database | 33.3% | 38.4% | 72.2% | 56.2% | 56.9% | 57.6% | 70.1% | 70.2% | 70.2% | Warning |
| efsdbsdr02 | Database | 2.6% | 7.0% | 32.7% | 49.4% | 49.9% | 50.6% | 43.4% | 43.4% | 43.8% | Healthy |
| efsdbslp01 | Database | 9.9% | 52.2% | 98.2% | 50.3% | 53.4% | 58.8% | 51.0% | 58.1% | 65.2% | Critical |
| ebsintslp02 | App | 37.0% | 52.2% | 96.7% | 43.9% | 46.1% | 50.5% | 10.6% | 10.7% | 11.2% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.0% | 5.2% | 5.5% | 6.4% | 41.2% | 41.2% | 41.5% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 81.5% | 5.1% | 5.3% | 6.7% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintslp01 | App | 37.3% | 53.2% | 95.9% | 50.6% | 53.2% | 59.8% | 15.8% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,969 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.71%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
