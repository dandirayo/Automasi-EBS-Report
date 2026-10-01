# EFS DAILY HEALTH REPORT
**Periode:** 16 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260716.xlsx, EFS_Infrastructures_20260716.xlsx, EFS_XLA_20260716.xlsx, EFS_GL_20260716.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,529,491
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,324
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,324 records. GL Posted mencapai 220,219 (99.79% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.79% | PASS |

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
| Create Accounting | 2,271 | 2,116 | 152 | 3 | 3.11 | 41.36 | CRITICAL | - |
| Accounting Program | 298 | 165 | 133 | 0 | 30.54 | 32.64 | WARNING | - |
| Journal Import | 2,239 | 2,239 | 0 | 0 | 0.40 | 1.75 | HEALTHY | - |
| Posting | 6 | 6 | 0 | 0 | 1.02 | 1.07 | HEALTHY | - |
| Posting: Single Ledger | 2,239 | 2,238 | 0 | 1 | 0.38 | 0.47 | CRITICAL | [Error] [1x] Program exited with status 1 |
| Transfer Journal Entries to GL | 4 | 3 | 1 | 0 | 41.74 | 46.72 | WARNING | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.43 | 1.43 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 22.42 | 22.46 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 40 | 39 | 1 | 0 | 36.15 | 51.99 | WARNING | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,529,491 | Volume total harian |
| Processed (P / XLA=S) | 2,525,167 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,324 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 220,679
- **2. FAH Processing (FAH Success / Error):** 220,677 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 220,219 / 458
- **4. Transfer to GL (Transferred):** 220,219
- **5. GL Posting (Posted / Unposted):** 220,219 (99.79% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 219,979 | 2 | 440 | 219,537 | 0 |
| CROSS BORDER PAYMENT Custom Application | 432 | 0 | 0 | 432 | 0 |
| TRADE FINANCE Custom Application | 185 | 0 | 0 | 185 | 0 |
| CREDIT CARD Custom Application | 46 | 0 | 16 | 30 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 0 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,402,260 | 1,401,534 | 726 | 0.05% | 162,281,718,008,463.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 505,460 | 505,460 | 0 | 0.00% | 14,614,238,290,558.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 222,485 | 222,485 | 0 | 0.00% | 36,273,432,407,840.17 | Healthy |
| DEP-Q_GLCP_GEND870 | 170,756 | 170,756 | 0 | 0.00% | 12,434,679.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 88,571 | 88,571 | 0 | 0.00% | 1,539,171,938.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,676 | 70,676 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,405 | 41,405 | 0 | 0.00% | 59,178,086,280,597.03 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,922 | 6,922 | 0 | 0.00% | 65,374,136,517,755.25 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,870 | 5,870 | 0 | 0.00% | -39,484,249,484,642.30 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,025 | 5,025 | 0 | 0.00% | 2,771,651,199,824.31 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.3% | 9.5% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 9.7% | 0.0% | 0.0% | 0.0% | 12.5% | 12.5% | 14.3% | Healthy |
| ebsintslp01 | App | 4.5% | 21.7% | 47.8% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.0% | Healthy |
| ebsintslp02 | App | 4.5% | 13.7% | 32.1% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.4% | Healthy |
| efsdbsdr01 | Database | 34.9% | 44.5% | 57.1% | 0.0% | 0.0% | 0.0% | 67.1% | 67.2% | 67.3% | Warning |
| efsdbsdr02 | Database | 3.2% | 10.1% | 17.6% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 24.2% | 44.4% | 90.5% | 0.0% | 0.0% | 0.0% | 57.7% | 60.2% | 63.5% | Critical |
| efsdbslp02 | Database | 23.8% | 35.3% | 71.2% | 0.0% | 0.0% | 0.0% | 58.9% | 59.0% | 59.0% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,324 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.79%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
