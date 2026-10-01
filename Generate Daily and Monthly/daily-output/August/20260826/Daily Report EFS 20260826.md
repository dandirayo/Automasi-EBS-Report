# EFS DAILY HEALTH REPORT
**Periode:** 26 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260826.xlsx, EFS_Infrastructures_20260826.xlsx, EFS_XLA_20260826.xlsx, EFS_GL_20260826.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,859,700
- **XLA Success Rate:** 98.94%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,678
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,678 records. GL Posted mencapai 170,446 (99.47% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 98.94% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.47% | WARNING |

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
| Create Accounting | 158 | 32 | 123 | 1 | 38.53 | 72.05 | CRITICAL | - |
| Accounting Program | 239 | 86 | 152 | 1 | 58.51 | 71.82 | CRITICAL | [Error] [152x] (no completion text) | [1x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program xla_ap_acct_hooks_pkg.main.  Technical problem : Error encountered in product API for extrac |
| Journal Import | 115 | 115 | 0 | 0 | 3.66 | 7.70 | HEALTHY | - |
| Posting | 1 | 1 | 0 | 0 | 0.03 | 0.03 | HEALTHY | - |
| Posting: Single Ledger | 115 | 115 | 0 | 0 | 0.70 | 0.82 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 12.84 | 13.70 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 2 | 0 | 0 | 3.35 | 3.47 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 17.60 | 17.60 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 45 | 40 | 0 | 0 | 32.04 | 32.54 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,859,700 | Volume total harian |
| Processed (P / XLA=S) | 1,834,394 | Sukses diproses (98.94%) |
| Unprocessed (U) | 5,678 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 171,361
- **2. FAH Processing (FAH Success / Error):** 170,895 / 361
- **3. SLA Accounting (Accounted / Not Accounted):** 170,451 / 444
- **4. Transfer to GL (Transferred):** 170,446
- **5. GL Posting (Posted / Unposted):** 170,446 (99.47% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 170,762 | 285 | 442 | 169,925 | 0 |
| CROSS BORDER PAYMENT Custom Application | 453 | 0 | 0 | 453 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 36 | 0 | 0 | 36 | 0 |
| JOINT FINANCE Custom Application | 16 | 0 | 0 | 16 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| TREASURY Custom Application | 9 | 0 | 0 | 9 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 979,587 | 978,211 | 1,376 | 0.14% | 235,672,977,314,929.91 | Warning |
| DEP-NQ_ED2P_SC_BFST | 332,506 | 332,506 | 0 | 0.00% | 17,677,251,540,989.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,034 | 177,138 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 170,135 | 170,135 | 0 | 0.00% | 57,105,277,779,379.83 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 71,327 | 71,327 | 0 | 0.00% | 2,010,585,139.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,782 | 41,782 | 0 | 0.00% | 57,799,939,191,774.79 | Healthy |
| LON-Q_GLCP_GEND872 | 38,018 | 37,944 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,406 | 7,406 | 0 | 0.00% | 63,480,307,379,858.09 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,631 | 5,631 | 0 | 0.00% | -36,750,470,186,964.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,535 | 5,535 | 0 | 0.00% | 2,725,939,584,405.06 | Healthy |

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
| efsdbslp02 | Database | 34.3% | 53.2% | 94.4% | 56.0% | 57.9% | 62.4% | 50.5% | 50.6% | 50.9% | Critical |
| efsdbsdr01 | Database | 39.5% | 42.3% | 79.0% | 60.5% | 61.2% | 63.0% | 70.1% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.7% | 7.2% | 30.0% | 49.9% | 50.1% | 51.1% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 3.6% | 15.8% | 98.7% | 41.1% | 43.5% | 49.2% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 20.9% | 53.9% | 98.8% | 53.9% | 55.7% | 60.1% | 49.6% | 57.6% | 73.3% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.8% | 6.0% | 6.3% | 7.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.2% | 5.7% | 6.1% | 7.4% | 24.3% | 24.3% | 25.0% | Critical |
| ebsintslp01 | App | 3.9% | 14.8% | 81.2% | 47.0% | 49.4% | 55.5% | 15.8% | 15.8% | 15.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,678 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.47%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
