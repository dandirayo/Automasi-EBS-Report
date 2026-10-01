# EFS DAILY HEALTH REPORT
**Periode:** 11 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260811.xlsx, EFS_Infrastructures_20260811.xlsx, EFS_XLA_20260811.xlsx, EFS_GL_20260811.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,034,400
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 23,602
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 23,602 records. GL Posted mencapai 229,568 (99.73% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.73% | PASS |

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
| Create Accounting | 2,268 | 2,176 | 86 | 4 | 1.95 | 5.72 | CRITICAL | - |
| Accounting Program | 237 | 121 | 116 | 0 | 47.38 | 54.91 | WARNING | [Warning] [116x] (no completion text) |
| Journal Import | 2,203 | 2,203 | 0 | 0 | 0.53 | 1.61 | HEALTHY | - |
| Posting | 1 | 1 | 0 | 0 | 0.50 | 0.50 | HEALTHY | - |
| Posting: Single Ledger | 2,202 | 2,202 | 0 | 0 | 0.52 | 0.53 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 6.50 | 6.97 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 19.70 | 19.70 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 23 | 23 | 0 | 0 | 34.28 | 36.30 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,034,400 | Volume total harian |
| Processed (P / XLA=S) | 3,010,796 | Sukses diproses (100.00%) |
| Unprocessed (U) | 23,602 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 230,187
- **2. FAH Processing (FAH Success / Error):** 230,066 / 121
- **3. SLA Accounting (Accounted / Not Accounted):** 229,568 / 498
- **4. Transfer to GL (Transferred):** 229,568
- **5. GL Posting (Posted / Unposted):** 229,568 (99.73% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,333 | 121 | 477 | 228,735 | 0 |
| CROSS BORDER PAYMENT Custom Application | 519 | 0 | 0 | 519 | 0 |
| TRADE FINANCE Custom Application | 167 | 0 | 1 | 166 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 18 | 34 | 0 |
| TREASURY Custom Application | 14 | 0 | 0 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 0 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,492,704 | 1,484,755 | 7,949 | 0.53% | 186,787,919,490,521.19 | Warning |
| DEP-NQ_ED2P_SC_BFST | 522,410 | 522,410 | 0 | 0.00% | 16,224,554,083,290.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 417,108 | 416,978 | 130 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 241,702 | 241,699 | 3 | 0.00% | 76,229,614,298,105.81 | Healthy |
| LON-Q_GLCP_GEND872 | 147,758 | 147,758 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 98,962 | 98,962 | 0 | 0.00% | 1,986,381,423.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 45,618 | 45,618 | 0 | 0.00% | 56,407,813,389,410.19 | Healthy |
| LON-NQ_ED2P_BORV | 17,255 | 5,657 | 11,598 | 67.22% | 12,277,625,292,894.62 | Critical |
| LON-Q_GLCP_GLIF | 11,887 | 11,727 | 160 | 1.35% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,694 | 11,694 | 0 | 0.00% | -1,659,131,937,643.20 | Healthy |

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
| efsdbslp02 | Database | 21.4% | 40.9% | 91.7% | 51.0% | 52.9% | 58.4% | 50.2% | 50.3% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.3% | 71.3% | 55.4% | 55.9% | 57.2% | 70.2% | 70.2% | 70.3% | Warning |
| efsdbsdr02 | Database | 2.5% | 6.8% | 54.9% | 49.4% | 49.7% | 50.4% | 43.3% | 43.4% | 43.8% | Healthy |
| ebsintslp02 | App | 3.3% | 14.4% | 85.0% | 43.6% | 45.8% | 50.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 28.8% | 61.1% | 98.9% | 50.0% | 54.5% | 60.9% | 44.1% | 56.0% | 65.5% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.8% | 5.0% | 5.2% | 6.4% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.0% | 5.2% | 5.3% | 6.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.8% | 14.8% | 79.4% | 50.4% | 52.6% | 57.4% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 23,602 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.73%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
