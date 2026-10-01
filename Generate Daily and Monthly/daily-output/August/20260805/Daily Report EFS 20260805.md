# EFS DAILY HEALTH REPORT
**Periode:** 5 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260805.xlsx, EFS_Infrastructures_20260805.xlsx, EFS_XLA_20260805.xlsx, EFS_GL_20260805.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,151,255
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 26,173
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 26,173 records. GL Posted mencapai 229,939 (99.81% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.81% | PASS |

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
| Create Accounting | 2,158 | 2,068 | 89 | 1 | 1.94 | 7.41 | CRITICAL | - |
| Accounting Program | 253 | 137 | 116 | 0 | 43.50 | 51.35 | WARNING | - |
| Journal Import | 2,099 | 2,099 | 0 | 0 | 0.48 | 1.39 | HEALTHY | - |
| Posting | 10 | 10 | 0 | 0 | 0.89 | 1.06 | HEALTHY | - |
| Posting: Single Ledger | 2,093 | 2,093 | 0 | 0 | 0.48 | 0.53 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 7.03 | 7.11 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.58 | 0.58 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 23.33 | 23.33 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 29 | 29 | 0 | 0 | 28.33 | 48.14 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 4 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 1 | 0.50 | Healthy |
| BNI GL KLN Load File to Table | 1 | 0.13 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,151,255 | Volume total harian |
| Processed (P / XLA=S) | 3,125,080 | Sukses diproses (100.00%) |
| Unprocessed (U) | 26,173 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 230,368
- **2. FAH Processing (FAH Success / Error):** 230,366 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 229,939 / 427
- **4. Transfer to GL (Transferred):** 229,939
- **5. GL Posting (Posted / Unposted):** 229,939 (99.81% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,534 | 2 | 409 | 229,123 | 0 |
| CROSS BORDER PAYMENT Custom Application | 489 | 0 | 0 | 489 | 0 |
| TRADE FINANCE Custom Application | 179 | 0 | 0 | 179 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 48 | 0 | 16 | 32 | 0 |
| TREASURY Custom Application | 15 | 0 | 0 | 15 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,590,463 | 1,580,756 | 9,707 | 0.61% | 212,156,236,340,663.12 | Warning |
| DEP-NQ_ED2P_SC_BFST | 523,442 | 523,442 | 0 | 0.00% | 17,398,576,199,099.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 417,008 | 416,886 | 122 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 243,773 | 243,770 | 3 | 0.00% | 93,313,643,715,607.45 | Healthy |
| LON-Q_GLCP_GEND872 | 150,326 | 150,320 | 6 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 107,988 | 107,988 | 0 | 0.00% | 2,151,442,632.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 49,362 | 49,362 | 0 | 0.00% | 49,650,621,981,251.92 | Healthy |
| LON-NQ_ED2P_BORV | 17,808 | 5,784 | 12,024 | 67.52% | 3,440,086,512,508.74 | Critical |
| LON-Q_GLCP_GLIF | 11,949 | 11,747 | 202 | 1.69% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,639 | 11,639 | 0 | 0.00% | 252,792,890,288.22 | Healthy |

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
| efsdbslp02 | Database | 8.6% | 30.1% | 92.5% | 48.5% | 49.8% | 52.4% | 50.2% | 50.4% | 50.7% | Critical |
| efsdbsdr01 | Database | 33.3% | 40.0% | 81.2% | 52.6% | 53.3% | 54.1% | 70.2% | 70.2% | 70.6% | Critical |
| efsdbsdr02 | Database | 2.6% | 7.0% | 28.9% | 48.9% | 49.2% | 49.9% | 43.3% | 43.3% | 43.4% | Healthy |
| efsdbslp01 | Database | 3.8% | 34.2% | 92.6% | 49.8% | 52.1% | 56.5% | 50.4% | 56.4% | 66.0% | Critical |
| ebsintslp02 | App | 3.2% | 13.7% | 90.9% | 42.8% | 45.0% | 50.0% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 80.5% | 4.6% | 4.8% | 5.3% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.5% | 4.8% | 4.9% | 5.4% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.7% | 14.0% | 84.0% | 49.9% | 52.0% | 55.8% | 15.8% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 26,173 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.81%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
