# EFS DAILY HEALTH REPORT
**Periode:** 28 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260828.xlsx, EFS_Infrastructures_20260828.xlsx, EFS_XLA_20260828.xlsx, EFS_GL_20260828.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,663,916
- **XLA Success Rate:** 94.27%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 141,426
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 141,426 records. GL Posted mencapai 233,541 (99.34% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 94.27% | WARNING |
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
| Create Accounting | 136 | 48 | 86 | 0 | 41.11 | 72.95 | WARNING | - |
| Accounting Program | 207 | 98 | 109 | 0 | 58.59 | 70.09 | WARNING | [Warning] [109x] (no completion text) |
| Journal Import | 160 | 156 | 4 | 0 | 2.12 | 17.75 | WARNING | [Warning] [4x] Not all of your data was imported successfully or it was imported with warnings.  Please review output file. |
| Posting | 6 | 6 | 0 | 0 | 0.96 | 1.02 | HEALTHY | - |
| Posting: Single Ledger | 156 | 156 | 0 | 0 | 0.80 | 1.03 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 10.83 | 11.43 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 3 | 3 | 0 | 0 | 1.10 | 1.10 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 18.15 | 18.15 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 34 | 34 | 0 | 0 | 20.83 | 28.21 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 24 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 5 | 1.53 | Healthy |
| BNI GL KLN Load File to Table | 4 | 0.17 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,663,916 | Volume total harian |
| Processed (P / XLA=S) | 2,503,208 | Sukses diproses (94.27%) |
| Unprocessed (U) | 141,426 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 235,100
- **2. FAH Processing (FAH Success / Error):** 234,092 / 196
- **3. SLA Accounting (Accounted / Not Accounted):** 233,541 / 551
- **4. Transfer to GL (Transferred):** 233,541
- **5. GL Posting (Posted / Unposted):** 233,541 (99.34% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 234,302 | 120 | 532 | 232,838 | 0 |
| CROSS BORDER PAYMENT Custom Application | 498 | 0 | 0 | 498 | 0 |
| TRADE FINANCE Custom Application | 145 | 0 | 0 | 145 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 47 | 0 | 17 | 30 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| TREASURY Custom Application | 11 | 0 | 0 | 11 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 0 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,452,288 | 1,317,960 | 134,328 | 9.25% | 243,818,602,852,641.53 | Warning |
| DEP-NQ_ED2P_SC_BFST | 522,091 | 522,091 | 0 | 0.00% | 19,324,671,295,757.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 236,440 | 236,440 | 0 | 0.00% | 47,521,398,714,458.71 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,520 | 177,520 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 96,183 | 96,183 | 0 | 0.00% | 2,062,811,655.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,618 | 72,336 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 50,151 | 50,151 | 0 | 0.00% | 60,481,011,257,702.91 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,228 | 8,228 | 0 | 0.00% | 65,677,145,666,019.21 | Healthy |
| LON-NQ_ED2P_BORV | 7,782 | 3,039 | 4,743 | 60.95% | 5,871,576,469,012.85 | Critical |
| LON-Q_GLCP_BORV | 7,378 | 5,177 | 2,201 | 29.83% | 8,057,811,280,301.35 | Critical |

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
| efsdbslp02 | Database | 28.8% | 50.2% | 96.4% | 56.4% | 58.5% | 64.3% | 50.6% | 50.6% | 51.4% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.1% | 82.7% | 61.3% | 61.9% | 63.4% | 70.2% | 70.3% | 70.6% | Critical |
| efsdbsdr02 | Database | 2.8% | 11.4% | 38.3% | 49.7% | 50.3% | 51.2% | 43.5% | 43.6% | 43.8% | Healthy |
| ebsintslp02 | App | 3.7% | 16.6% | 98.9% | 41.9% | 44.8% | 51.0% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 16.7% | 50.3% | 98.7% | 53.8% | 56.7% | 62.6% | 51.5% | 60.2% | 79.8% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 81.6% | 5.9% | 6.2% | 7.5% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.6% | 6.2% | 6.4% | 7.0% | 41.2% | 41.2% | 41.9% | Critical |
| ebsintslp01 | App | 4.0% | 15.9% | 87.2% | 46.8% | 49.4% | 54.4% | 15.8% | 15.8% | 15.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 141,426 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
