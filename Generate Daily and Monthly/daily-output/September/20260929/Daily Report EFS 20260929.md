# EFS DAILY HEALTH REPORT
**Periode:** 29 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260929.xlsx, EFS_Infrastructures_20260929.xlsx, EFS_XLA_20260929.xlsx, EFS_GL_20260929.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,867,600
- **XLA Success Rate:** 80.95%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 38,864
- **Infrastruktur Status:** 4 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 38,864 records. GL Posted mencapai 125,583 (99.46% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 80.95% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.46% | WARNING |

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
| Create Accounting | 112 | 40 | 71 | 0 | 53.38 | 127.02 | WARNING | - |
| Accounting Program | 181 | 91 | 90 | 0 | 75.38 | 124.88 | WARNING | [Warning] [89x] (no completion text) | [1x] (no completion text) |
| Journal Import | 113 | 113 | 0 | 0 | 3.01 | 7.15 | HEALTHY | - |
| Posting | 4 | 4 | 0 | 0 | 1.24 | 1.26 | HEALTHY | - |
| Posting: Single Ledger | 110 | 110 | 0 | 0 | 0.87 | 0.91 | HEALTHY | - |
| Transfer Journal Entries to GL | 5 | 5 | 0 | 0 | 5.96 | 6.08 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 23.53 | 23.53 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 21 | 21 | 0 | 0 | 9.30 | 10.65 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 2 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 1 | 0.27 | Healthy |
| BNI GL KLN Load File to Table | 1 | 0.12 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,867,600 | Volume total harian |
| Processed (P / XLA=S) | 1,477,164 | Sukses diproses (80.95%) |
| Unprocessed (U) | 38,864 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 126,262
- **2. FAH Processing (FAH Success / Error):** 125,981 / 76
- **3. SLA Accounting (Accounted / Not Accounted):** 125,583 / 398
- **4. Transfer to GL (Transferred):** 125,583
- **5. GL Posting (Posted / Unposted):** 125,583 (99.46% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 125,166 | 0 | 325 | 124,841 | 0 |
| CROSS BORDER PAYMENT Custom Application | 717 | 0 | 0 | 717 | 0 |
| TRADE FINANCE Custom Application | 205 | 0 | 0 | 0 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 73 | 0 | 73 | 0 | 0 |
| TREASURY Custom Application | 11 | 0 | 0 | 11 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 912,496 | 902,154 | 10,342 | 1.13% | 345,586,933,111,839.38 | Warning |
| DEP-NQ_ED2P_SC_BFST | 311,439 | 311,439 | 0 | 0.00% | 17,399,785,147,371.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 237,567 | 0 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 133,202 | 132,751 | 0 | 0.00% | 51,518,407,565,894.93 | Healthy |
| LON-Q_GLCP_GEND872 | 74,148 | 0 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 63,929 | 63,929 | 0 | 0.00% | 1,623,163,159.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 36,062 | 36,062 | 0 | 0.00% | 62,913,928,265,066.14 | Healthy |
| LON-Q_GLCP_GLIF | 35,370 | 0 | 0 | 0.00% | 0.00 | Healthy |
| LON-NQ_ED2P_BORV | 33,959 | 10,813 | 23,146 | 68.16% | 4,880,992,482,578.69 | Critical |
| LON-Q_GLCP_BORV | 9,146 | 4,006 | 5,140 | 56.20% | 10,913,584,838,070.23 | Critical |

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
| efsdbslp02 | Database | 12.0% | 54.3% | 94.2% | 62.4% | 65.5% | 70.0% | 51.7% | 51.8% | 52.0% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.9% | 28.8% | 70.1% | 70.3% | 70.9% | 70.7% | 70.7% | 71.3% | Warning |
| efsdbsdr02 | Database | 0.9% | 3.0% | 47.1% | 50.0% | 50.3% | 51.7% | 43.8% | 43.9% | 44.2% | Healthy |
| ebsintslp02 | App | 2.5% | 17.2% | 95.6% | 44.4% | 47.7% | 53.5% | 10.7% | 10.8% | 10.9% | Critical |
| efsdbslp01 | Database | 11.0% | 58.5% | 96.9% | 59.2% | 62.5% | 66.9% | 51.6% | 57.1% | 65.2% | Critical |
| ebsintsdr02 | App | 0.6% | 1.4% | 63.4% | 7.3% | 7.4% | 8.9% | 24.4% | 24.4% | 24.6% | Warning |
| ebsintsdr01 | App | 0.5% | 1.5% | 64.8% | 7.5% | 7.6% | 9.0% | 41.3% | 41.3% | 42.1% | Warning |
| ebsintslp01 | App | 3.0% | 11.1% | 93.7% | 50.0% | 53.0% | 57.9% | 15.9% | 15.9% | 16.0% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 38,864 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.46%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
