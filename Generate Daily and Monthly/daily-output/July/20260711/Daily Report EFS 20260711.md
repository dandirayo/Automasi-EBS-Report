# EFS DAILY HEALTH REPORT
**Periode:** 11 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260711.xlsx, EFS_Infrastructures_20260711.xlsx, EFS_XLA_20260711.xlsx, EFS_GL_20260711.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,427,056
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 790
- **Infrastruktur Status:** 2 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 790 records. GL Posted mencapai 196,178 (99.90% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.90% | PASS |

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
| Create Accounting | 239 | 158 | 81 | 0 | 26.96 | 29.57 | WARNING | - |
| Accounting Program | 306 | 200 | 106 | 0 | 27.02 | 28.96 | WARNING | - |
| Journal Import | 227 | 227 | 0 | 0 | 2.01 | 5.06 | HEALTHY | - |
| Posting: Single Ledger | 227 | 226 | 0 | 1 | 0.46 | 1.18 | CRITICAL | [Error] [1x] Concurrent program returned no reason for failure. |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 4.17 | 4.18 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.50 | 0.50 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 23.63 | 23.63 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 3 | 3 | 0 | 0 | 23.12 | 23.17 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,427,056 | Volume total harian |
| Processed (P / XLA=S) | 2,426,266 | Sukses diproses (100.00%) |
| Unprocessed (U) | 790 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 196,368
- **2. FAH Processing (FAH Success / Error):** 196,366 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 196,178 / 188
- **4. Transfer to GL (Transferred):** 196,178
- **5. GL Posting (Posted / Unposted):** 196,178 (99.90% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 195,674 | 2 | 167 | 195,505 | 0 |
| CROSS BORDER PAYMENT Custom Application | 444 | 0 | 0 | 444 | 0 |
| TRADE FINANCE Custom Application | 166 | 0 | 0 | 166 | 0 |
| CREDIT CARD Custom Application | 53 | 0 | 19 | 34 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |
| JOINT FINANCE Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,341,168 | 1,340,387 | 781 | 0.06% | 20,175,367,268,279.99 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 495,143 | 495,143 | 0 | 0.00% | 12,012,968,744,787.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 210,862 | 210,862 | 0 | 0.00% | 5,346,836,549,064.10 | Healthy |
| DEP-Q_GLCP_GEND870 | 201,116 | 201,116 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 96,070 | 96,070 | 0 | 0.00% | 1,718,728,967.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,970 | 68,970 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,849 | 5,849 | 0 | 0.00% | -40,818,423,287,901.28 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,653 | 3,653 | 0 | 0.00% | 141,375,953,490.05 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,629 | 2,629 | 0 | 0.00% | 20,640,571,261.08 | Healthy |
| BRA-NQ_ED2P_ELOG | 891 | 891 | 0 | 0.00% | 405,710,013,667.00 | Healthy |

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
| ebsintsdr01 | App | 2.1% | 5.7% | 29.4% | 0.0% | 0.0% | 0.0% | 20.4% | 21.0% | 23.3% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.9% | 40.4% | 0.0% | 0.0% | 0.0% | 12.4% | 12.4% | 13.9% | Healthy |
| ebsintslp01 | App | 4.8% | 11.3% | 22.2% | 0.0% | 0.0% | 0.0% | 23.8% | 24.1% | 24.5% | Healthy |
| ebsintslp02 | App | 4.5% | 29.0% | 99.4% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.2% | Critical |
| efsdbsdr01 | Database | 22.2% | 44.2% | 71.8% | 0.0% | 0.0% | 0.0% | 66.5% | 66.7% | 66.7% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.0% | 20.0% | 0.0% | 0.0% | 0.0% | 46.4% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 17.9% | 37.4% | 59.9% | 0.0% | 0.0% | 0.0% | 58.5% | 61.7% | 64.6% | Warning |
| efsdbslp02 | Database | 13.5% | 29.7% | 84.7% | 0.0% | 0.0% | 0.0% | 58.8% | 58.9% | 58.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 790 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.90%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
