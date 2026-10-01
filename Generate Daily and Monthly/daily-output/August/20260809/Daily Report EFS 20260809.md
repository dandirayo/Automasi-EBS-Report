# EFS DAILY HEALTH REPORT
**Periode:** 9 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260809.xlsx, EFS_Infrastructures_20260809.xlsx, EFS_XLA_20260809.xlsx, EFS_GL_20260809.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,676,477
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,352
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,352 records. GL Posted mencapai 190,605 (99.93% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.93% | PASS |

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
| Create Accounting | 156 | 100 | 54 | 0 | 33.42 | 50.26 | WARNING | - |
| Accounting Program | 196 | 133 | 63 | 0 | 45.90 | 48.94 | WARNING | [Warning] [63x] (no completion text) |
| Journal Import | 133 | 133 | 0 | 0 | 2.46 | 3.57 | HEALTHY | - |
| Posting: Single Ledger | 133 | 133 | 0 | 0 | 0.57 | 0.72 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 3.66 | 3.67 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 17.65 | 17.65 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 16 | 16 | 0 | 0 | 14.42 | 16.39 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,676,477 | Volume total harian |
| Processed (P / XLA=S) | 2,658,123 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,352 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 190,730
- **2. FAH Processing (FAH Success / Error):** 190,728 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 190,605 / 123
- **4. Transfer to GL (Transferred):** 190,605
- **5. GL Posting (Posted / Unposted):** 190,605 (99.93% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 190,517 | 2 | 121 | 190,394 | 0 |
| CROSS BORDER PAYMENT Custom Application | 106 | 0 | 0 | 106 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 16 | 0 | 0 | 16 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,299,287 | 1,290,797 | 8,490 | 0.65% | 16,367,941,499,300.44 | Warning |
| DEP-NQ_ED2P_SC_BFST | 468,558 | 468,558 | 0 | 0.00% | 9,860,364,034,370.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 419,188 | 419,038 | 150 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 213,851 | 213,851 | 0 | 0.00% | 4,758,969,630,671.95 | Healthy |
| LON-Q_GLCP_GEND872 | 149,424 | 149,424 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 89,209 | 89,209 | 0 | 0.00% | 1,476,383,328.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,693 | 11,693 | 0 | 0.00% | -473,496,949.00 | Healthy |
| LON-NQ_ED2P_BORV | 10,496 | 3,045 | 7,451 | 70.99% | 148,155,003,833.98 | Critical |
| LON-Q_GLCP_GLIF | 4,010 | 4,010 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,202 | 3,202 | 0 | 0.00% | 68,565,977,866.77 | Healthy |

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
| efsdbslp02 | Database | 15.9% | 32.7% | 83.1% | 50.7% | 51.0% | 51.6% | 50.3% | 50.4% | 50.4% | Critical |
| efsdbsdr01 | Database | 33.2% | 40.4% | 76.1% | 54.6% | 55.1% | 55.7% | 70.2% | 70.3% | 70.3% | Warning |
| efsdbsdr02 | Database | 2.5% | 8.2% | 54.9% | 49.3% | 49.7% | 51.0% | 43.4% | 43.4% | 43.7% | Healthy |
| ebsintslp02 | App | 3.2% | 7.6% | 87.5% | 43.2% | 43.4% | 44.8% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 15.7% | 28.9% | 92.8% | 51.0% | 51.5% | 52.1% | 49.6% | 56.9% | 61.5% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 81.5% | 4.8% | 5.1% | 6.3% | 24.3% | 24.4% | 25.4% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 88.6% | 5.0% | 5.2% | 5.7% | 41.2% | 41.2% | 41.8% | Critical |
| ebsintslp01 | App | 3.8% | 7.7% | 73.3% | 50.2% | 50.4% | 51.1% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,352 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.93%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
