# EFS DAILY HEALTH REPORT
**Periode:** 19 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260719.xlsx, EFS_Infrastructures_20260719.xlsx, EFS_XLA_20260719.xlsx, EFS_GL_20260719.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,234,000
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 536
- **Infrastruktur Status:** 0 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 536 records. GL Posted mencapai 184,663 (99.93% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | PASS |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | PASS |
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
| Create Accounting | 276 | 95 | 181 | 0 | 22.90 | 33.60 | WARNING | - |
| Accounting Program | 387 | 139 | 248 | 0 | 29.10 | 33.06 | WARNING | - |
| Journal Import | 201 | 201 | 0 | 0 | 1.82 | 5.16 | HEALTHY | - |
| Posting: Single Ledger | 201 | 201 | 0 | 0 | 0.48 | 0.61 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 5.51 | 5.68 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 0 | 0 | 1 | 0.38 | 0.38 | CRITICAL | [Error] [1x] Concurrent Manager encountered an error while attempting to start your immediate concurrent program XXCUST_GL_DAILY_RATES. Routine &ROUTINE received a return code of failure.  Contact your support representative. |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 18.67 | 18.67 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 8 | 8 | 0 | 0 | 21.70 | 23.26 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,234,000 | Volume total harian |
| Processed (P / XLA=S) | 2,233,463 | Sukses diproses (100.00%) |
| Unprocessed (U) | 536 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 184,794
- **2. FAH Processing (FAH Success / Error):** 184,792 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 184,663 / 129
- **4. Transfer to GL (Transferred):** 184,663
- **5. GL Posting (Posted / Unposted):** 184,663 (99.93% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 184,670 | 2 | 127 | 184,541 | 0 |
| CROSS BORDER PAYMENT Custom Application | 90 | 0 | 0 | 90 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 0 | 17 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,249,029 | 1,248,500 | 529 | 0.04% | 16,058,654,507,868.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 453,973 | 453,973 | 0 | 0.00% | 8,678,312,776,725.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 188,687 | 188,687 | 0 | 0.00% | 3,985,600,386,126.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,191 | 181,191 | 0 | 0.00% | -34,829,771,499.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,180 | 84,180 | 0 | 0.00% | 1,346,018,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,651 | 70,651 | 0 | 0.00% | -2,231,915,984.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,690 | 2,690 | 0 | 0.00% | 56,677,420,703.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,607 | 2,607 | 0 | 0.00% | 6,803,238,944.00 | Healthy |
| BRA-NQ_ED2P_ELOG | 628 | 628 | 0 | 0.00% | 278,313,763,917.00 | Healthy |
| LON-Q_GLCP_BORV | 98 | 95 | 2 | 2.04% | 36,335,342,310.00 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.3% | 13.1% | 0.0% | 0.0% | 0.0% | 21.4% | 21.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.4% | 14.9% | 0.0% | 0.0% | 0.0% | 12.5% | 12.6% | 14.2% | Healthy |
| ebsintslp01 | App | 4.3% | 7.0% | 17.9% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.6% | Healthy |
| ebsintslp02 | App | 4.6% | 7.1% | 19.8% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.0% | Healthy |
| efsdbsdr01 | Database | 35.1% | 43.3% | 60.2% | 0.0% | 0.0% | 0.0% | 67.5% | 67.6% | 67.7% | Warning |
| efsdbsdr02 | Database | 3.4% | 10.2% | 33.1% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.6% | Healthy |
| efsdbslp01 | Database | 13.2% | 25.3% | 49.5% | 0.0% | 0.0% | 0.0% | 56.3% | 58.2% | 60.1% | Warning |
| efsdbslp02 | Database | 12.6% | 23.5% | 38.2% | 0.0% | 0.0% | 0.0% | 58.9% | 59.0% | 59.0% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 536 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
