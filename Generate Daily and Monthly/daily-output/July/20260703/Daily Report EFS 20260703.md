# EFS DAILY HEALTH REPORT
**Periode:** 3 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260703.xlsx, EFS_Infrastructures_20260703.xlsx, EFS_XLA_20260703.xlsx, EFS_GL_20260703.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,877,471
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,650
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,650 records. GL Posted mencapai 174,817 (99.77% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.77% | PASS |

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
| Create Accounting | 1,814 | 1,698 | 114 | 1 | 2.83 | 18.18 | CRITICAL | - |
| Accounting Program | 325 | 173 | 152 | 0 | 24.05 | 30.60 | WARNING | - |
| Journal Import | 1,728 | 1,726 | 0 | 2 | 0.37 | 1.78 | CRITICAL | [Error] [2x] Program exited with status 1 |
| Posting: Single Ledger | 1,726 | 1,726 | 0 | 0 | 0.33 | 0.44 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 5 | 0 | 0 | 5.68 | 6.35 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 3 | 2 | 0 | 0 | 0.65 | 0.67 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 23.77 | 23.77 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 27 | 27 | 0 | 0 | 25.12 | 26.65 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,877,471 | Volume total harian |
| Processed (P / XLA=S) | 1,872,821 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,650 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 175,220
- **2. FAH Processing (FAH Success / Error):** 175,214 / 6
- **3. SLA Accounting (Accounted / Not Accounted):** 174,817 / 397
- **4. Transfer to GL (Transferred):** 174,817
- **5. GL Posting (Posted / Unposted):** 174,817 (99.77% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 174,429 | 6 | 378 | 174,045 | 0 |
| CROSS BORDER PAYMENT Custom Application | 549 | 0 | 0 | 549 | 0 |
| TRADE FINANCE Custom Application | 145 | 0 | 0 | 145 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 17 | 32 | 0 |
| TREASURY Custom Application | 26 | 0 | 0 | 26 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 0 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,019,233 | 1,018,350 | 883 | 0.09% | 215,909,508,515,233.44 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 330,527 | 330,527 | 0 | 0.00% | 13,492,288,012,038.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 179,880 | 179,880 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 142,471 | 142,471 | 0 | 0.00% | 50,410,972,353,217.37 | Healthy |
| LON-Q_GLCP_GEND872 | 68,442 | 68,442 | 0 | 0.00% | -999,015,973.94 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 65,736 | 65,736 | 0 | 0.00% | 1,352,237,958.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,558 | 43,558 | 0 | 0.00% | 38,467,080,104,021.07 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,347 | 7,347 | 0 | 0.00% | 44,323,016,076,011.66 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,772 | 5,772 | 0 | 0.00% | -39,449,231,239,633.96 | Healthy |
| LON-NQ_ED2P_BORV | 4,580 | 1,925 | 2,655 | 57.97% | 5,250,991,894,898.61 | Critical |

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
| ebsintsdr01 | App | 2.0% | 2.6% | 12.0% | 0.0% | 0.0% | 0.0% | 20.3% | 20.3% | 20.4% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.7% | 15.4% | 0.0% | 0.0% | 0.0% | 12.2% | 12.2% | 12.3% | Healthy |
| ebsintslp01 | App | 3.8% | 16.1% | 48.4% | 0.0% | 0.0% | 0.0% | 24.7% | 25.1% | 25.5% | Healthy |
| ebsintslp02 | App | 4.4% | 18.4% | 53.3% | 0.0% | 0.0% | 0.0% | 9.9% | 10.0% | 10.2% | Healthy |
| efsdbsdr01 | Database | 47.4% | 57.6% | 79.1% | 0.0% | 0.0% | 0.0% | 65.4% | 65.6% | 65.7% | Warning |
| efsdbsdr02 | Database | 3.2% | 6.0% | 18.5% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 13.0% | 38.9% | 95.2% | 0.0% | 0.0% | 0.0% | 53.7% | 59.6% | 62.9% | Critical |
| efsdbslp02 | Database | 17.0% | 34.5% | 64.0% | 0.0% | 0.0% | 0.0% | 58.2% | 58.2% | 58.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,650 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.77%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
