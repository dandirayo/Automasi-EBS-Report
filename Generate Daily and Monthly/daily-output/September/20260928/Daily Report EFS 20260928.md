# EFS DAILY HEALTH REPORT
**Periode:** 28 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260928.xlsx, EFS_Infrastructures_20260928.xlsx, EFS_XLA_20260928.xlsx, EFS_GL_20260928.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,829,570
- **XLA Success Rate:** 96.73%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 11,349
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 11,349 records. GL Posted mencapai 129,401 (99.74% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 96.73% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.74% | PASS |

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
| Create Accounting | 128 | 36 | 91 | 0 | 50.49 | 114.61 | WARNING | - |
| Accounting Program | 196 | 88 | 108 | 0 | 79.06 | 112.61 | WARNING | [Warning] [107x] (no completion text) | [1x] (no completion text) |
| Journal Import | 122 | 122 | 0 | 0 | 2.18 | 4.55 | HEALTHY | - |
| Posting | 11 | 9 | 0 | 2 | 1.04 | 1.05 | CRITICAL | [Error] [2x] Concurrent program returned no reason for failure. |
| Posting: Single Ledger | 113 | 113 | 0 | 0 | 0.93 | 1.07 | HEALTHY | - |
| Transfer Journal Entries to GL | 5 | 5 | 0 | 0 | 5.60 | 5.64 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 17.60 | 17.60 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 25 | 25 | 0 | 0 | 10.23 | 14.97 | HEALTHY | - |
| BNI FAH Laporan Konfigurasi | 1 | 1 | 0 | 0 | 0.32 | 0.32 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 4 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 2 | 3.07 | Healthy |
| BNI GL KLN Load File to Table | 2 | 0.08 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,829,570 | Volume total harian |
| Processed (P / XLA=S) | 1,758,678 | Sukses diproses (96.73%) |
| Unprocessed (U) | 11,349 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 129,735
- **2. FAH Processing (FAH Success / Error):** 129,624 / 0
- **3. SLA Accounting (Accounted / Not Accounted):** 129,512 / 112
- **4. Transfer to GL (Transferred):** 129,417
- **5. GL Posting (Posted / Unposted):** 129,401 (99.74% intake) / 16

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 129,482 | 0 | 148 | 129,264 | 16 |
| CROSS BORDER PAYMENT Custom Application | 129 | 0 | 0 | 129 | 0 |
| PSAK 71 Custom Application | 76 | 0 | -76 | 0 | 0 |
| CREDIT CARD Custom Application | 40 | 0 | 40 | 0 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 928,877 | 921,272 | 7,605 | 0.82% | 264,412,189,887,163.81 | Warning |
| DEP-NQ_ED2P_SC_BFST | 303,146 | 303,146 | 0 | 0.00% | 18,505,842,436,884.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 197,091 | 197,091 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 130,361 | 130,156 | 0 | 0.00% | 113,037,283,824,907.91 | Healthy |
| LON-Q_GLCP_GEND872 | 74,034 | 73,922 | 112 | 0.15% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 63,995 | 63,995 | 0 | 0.00% | 1,673,523,206.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 40,936 | 40,153 | 0 | 0.00% | 77,882,578,639,244.30 | Healthy |
| LON-NQ_ED2P_BORV | 32,212 | 1,841 | 2,459 | 7.63% | 7,314,679,413,410.97 | Warning |
| LON-Q_GLCP_GLIF | 25,064 | 0 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_BORV | 8,123 | 2,618 | 977 | 12.03% | 6,038,928,525,134.10 | Warning |

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
| efsdbslp02 | Database | 11.9% | 31.9% | 94.7% | 62.1% | 64.6% | 69.1% | 51.7% | 51.7% | 52.1% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.2% | 57.5% | 70.2% | 70.5% | 71.5% | 70.7% | 70.7% | 71.1% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.3% | 13.3% | 50.5% | 50.8% | 51.4% | 43.8% | 43.9% | 43.9% | Healthy |
| ebsintslp02 | App | 2.5% | 10.4% | 98.4% | 44.0% | 46.5% | 51.3% | 10.8% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 10.2% | 34.7% | 96.6% | 59.2% | 61.8% | 68.3% | 47.6% | 56.0% | 63.1% | Critical |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.1% | 7.3% | 7.4% | 8.8% | 24.4% | 24.4% | 24.9% | Warning |
| ebsintsdr01 | App | 0.5% | 1.4% | 68.7% | 7.3% | 7.6% | 8.6% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintslp01 | App | 2.8% | 10.8% | 62.0% | 49.8% | 52.4% | 58.3% | 15.9% | 15.9% | 16.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 11,349 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.74%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
