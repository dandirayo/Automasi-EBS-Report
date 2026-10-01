# EFS DAILY HEALTH REPORT
**Periode:** 6 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260806.xlsx, EFS_Infrastructures_20260806.xlsx, EFS_XLA_20260806.xlsx, EFS_GL_20260806.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,083,634
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,925
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,925 records. GL Posted mencapai 227,156 (99.80% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.80% | PASS |

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
| Create Accounting | 2,295 | 2,214 | 79 | 2 | 1.96 | 5.02 | CRITICAL | - |
| Accounting Program | 226 | 122 | 104 | 0 | 41.58 | 51.68 | WARNING | - |
| Journal Import | 2,212 | 2,212 | 0 | 0 | 0.48 | 1.35 | HEALTHY | - |
| Posting | 2 | 2 | 0 | 0 | 0.05 | 0.05 | HEALTHY | - |
| Posting: Single Ledger | 2,211 | 2,210 | 0 | 1 | 0.48 | 0.52 | CRITICAL | [Error] [1x] Concurrent program returned no reason for failure. |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 6.78 | 7.25 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 3.07 | 3.07 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 24.07 | 24.07 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 11 | 11 | 0 | 0 | 27.74 | 29.37 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,083,634 | Volume total harian |
| Processed (P / XLA=S) | 3,060,707 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,925 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 227,614
- **2. FAH Processing (FAH Success / Error):** 227,612 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 227,156 / 456
- **4. Transfer to GL (Transferred):** 227,156
- **5. GL Posting (Posted / Unposted):** 227,156 (99.80% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 226,793 | 2 | 437 | 226,354 | 0 |
| CROSS BORDER PAYMENT Custom Application | 503 | 0 | 0 | 503 | 0 |
| TRADE FINANCE Custom Application | 151 | 0 | 0 | 151 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 17 | 35 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,535,770 | 1,527,213 | 8,557 | 0.56% | 246,094,759,258,274.72 | Warning |
| DEP-NQ_ED2P_SC_BFST | 515,565 | 515,565 | 0 | 0.00% | 15,989,687,909,918.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 415,494 | 415,374 | 120 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 239,760 | 239,756 | 4 | 0.00% | 108,365,143,475,049.72 | Healthy |
| LON-Q_GLCP_GEND872 | 149,266 | 149,266 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 118,354 | 118,354 | 0 | 0.00% | 2,404,534,370.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 44,667 | 44,667 | 0 | 0.00% | 62,668,804,976,243.58 | Healthy |
| LON-NQ_ED2P_BORV | 15,795 | 5,165 | 10,630 | 67.30% | 2,833,540,778,197.02 | Critical |
| LON-Q_GLCP_LOND2140 | 11,658 | 11,658 | 0 | 0.00% | -191,308,631,301.42 | Healthy |
| LON-Q_GLCP_GLIF | 10,932 | 10,766 | 166 | 1.52% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 17.7% | 40.7% | 93.1% | 48.8% | 51.0% | 55.1% | 50.2% | 50.3% | 50.5% | Critical |
| efsdbsdr01 | Database | 33.3% | 40.8% | 72.4% | 53.2% | 54.0% | 55.3% | 70.2% | 70.3% | 70.7% | Warning |
| efsdbsdr02 | Database | 2.9% | 9.0% | 29.0% | 48.9% | 49.4% | 50.2% | 43.3% | 43.3% | 43.5% | Healthy |
| efsdbslp01 | Database | 3.4% | 32.0% | 91.2% | 49.9% | 52.0% | 58.2% | 49.9% | 56.7% | 61.5% | Critical |
| ebsintslp02 | App | 3.3% | 13.7% | 86.5% | 43.0% | 45.0% | 49.7% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 80.6% | 4.5% | 4.9% | 6.2% | 24.3% | 24.3% | 25.0% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.4% | 4.8% | 5.0% | 6.0% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.7% | 14.4% | 78.3% | 49.9% | 52.1% | 57.1% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,925 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.80%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
