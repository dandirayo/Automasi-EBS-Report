# EFS DAILY HEALTH REPORT
**Periode:** 20 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260720.xlsx, EFS_Infrastructures_20260720.xlsx, EFS_XLA_20260720.xlsx, EFS_GL_20260720.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,629,258
- **XLA Success Rate:** 99.97%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,105
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,105 records. GL Posted mencapai 241,421 (99.82% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.97% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.82% | PASS |

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
| Create Accounting | 2,418 | 2,291 | 125 | 2 | 1.92 | 5.49 | CRITICAL | - |
| Accounting Program | 302 | 137 | 165 | 0 | 31.69 | 34.82 | WARNING | - |
| Journal Import | 2,348 | 2,346 | 2 | 0 | 0.40 | 1.37 | WARNING | - |
| Posting | 8 | 8 | 0 | 0 | 0.68 | 0.70 | HEALTHY | - |
| Posting: Single Ledger | 2,345 | 2,345 | 0 | 0 | 0.40 | 0.45 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 4.85 | 5.37 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 4 | 4 | 0 | 0 | 1.05 | 1.07 | HEALTHY | - |
| BNI FAH Journal Reversal | 4 | 4 | 0 | 0 | 24.08 | 24.18 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 25 | 25 | 0 | 0 | 28.43 | 30.99 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 18 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 3 | 2.01 | Healthy |
| BNI GL KLN Load File to Table | 3 | 0.25 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,629,258 | Volume total harian |
| Processed (P / XLA=S) | 2,624,153 | Sukses diproses (99.97%) |
| Unprocessed (U) | 5,105 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 241,850
- **2. FAH Processing (FAH Success / Error):** 241,848 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 241,421 / 427
- **4. Transfer to GL (Transferred):** 241,421
- **5. GL Posting (Posted / Unposted):** 241,421 (99.82% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 241,721 | 2 | 425 | 241,294 | 0 |
| CROSS BORDER PAYMENT Custom Application | 74 | 0 | 0 | 74 | 0 |
| CREDIT CARD Custom Application | 38 | 0 | 0 | 38 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,462,671 | 1,461,889 | 782 | 0.05% | 216,506,065,427,514.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 517,230 | 517,230 | 0 | 0.00% | 16,054,445,212,797.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 227,217 | 227,217 | 0 | 0.00% | 57,689,930,741,730.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,376 | 181,376 | 0 | 0.00% | 708,346.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,160 | 92,160 | 0 | 0.00% | 1,628,260,632.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,890 | 70,890 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 48,344 | 47,561 | 783 | 1.62% | 58,758,644,726,018.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,426 | 8,426 | 0 | 0.00% | 64,169,734,185,023.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,870 | 5,870 | 0 | 0.00% | -40,026,063,941,000.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,743 | 4,743 | 0 | 0.00% | 2,095,424,098,821.00 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.2% | 10.4% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.4% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 10.0% | 0.0% | 0.0% | 0.0% | 12.6% | 12.6% | 13.5% | Healthy |
| ebsintslp01 | App | 4.5% | 14.6% | 39.0% | 0.0% | 0.0% | 0.0% | 17.9% | 18.0% | 18.1% | Healthy |
| ebsintslp02 | App | 4.5% | 14.4% | 42.8% | 0.0% | 0.0% | 0.0% | 9.9% | 10.0% | 10.0% | Healthy |
| efsdbsdr01 | Database | 34.9% | 39.6% | 55.8% | 0.0% | 0.0% | 0.0% | 67.6% | 67.7% | 67.8% | Warning |
| efsdbsdr02 | Database | 3.4% | 8.4% | 18.9% | 0.0% | 0.0% | 0.0% | 46.5% | 46.6% | 46.6% | Healthy |
| efsdbslp01 | Database | 14.2% | 36.3% | 83.5% | 0.0% | 0.0% | 0.0% | 56.9% | 60.8% | 65.0% | Critical |
| efsdbslp02 | Database | 18.8% | 32.1% | 62.4% | 0.0% | 0.0% | 0.0% | 58.9% | 59.0% | 59.0% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,105 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.82%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
