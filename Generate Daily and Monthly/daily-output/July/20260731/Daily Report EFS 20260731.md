# EFS DAILY HEALTH REPORT
**Periode:** 31 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260731.xlsx, EFS_Infrastructures_20260731.xlsx, EFS_XLA_20260731.xlsx, EFS_GL_20260731.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,544,591
- **XLA Success Rate:** 87.60%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 321,564
- **Infrastruktur Status:** 2 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 321,564 records. GL Posted mencapai 235,964 (99.76% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 87.60% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.76% | PASS |

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
| Create Accounting | 2,612 | 2,526 | 81 | 5 | 2.05 | 5.70 | CRITICAL | - |
| Accounting Program | 263 | 144 | 119 | 0 | 42.03 | 50.72 | WARNING | - |
| Journal Import | 2,507 | 2,507 | 0 | 0 | 0.47 | 1.73 | HEALTHY | - |
| Posting | 2 | 2 | 0 | 0 | 0.45 | 0.45 | HEALTHY | - |
| Posting: Single Ledger | 2,505 | 2,505 | 0 | 0 | 0.47 | 0.50 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 8.40 | 10.62 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 1 | 0 | 0 | 0.53 | 0.53 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 19.40 | 19.40 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 36 | 35 | 0 | 0 | 30.69 | 40.48 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,544,591 | Volume total harian |
| Processed (P / XLA=S) | 2,223,027 | Sukses diproses (87.60%) |
| Unprocessed (U) | 321,564 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 236,535
- **2. FAH Processing (FAH Success / Error):** 236,533 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 235,964 / 569
- **4. Transfer to GL (Transferred):** 235,964
- **5. GL Posting (Posted / Unposted):** 235,964 (99.76% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 235,773 | 2 | 550 | 235,221 | 0 |
| CROSS BORDER PAYMENT Custom Application | 495 | 0 | 0 | 495 | 0 |
| TRADE FINANCE Custom Application | 178 | 0 | 0 | 178 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 17 | 33 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 0 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,477,676 | 1,161,669 | 316,007 | 21.39% | 356,327,133,573,420.00 | Critical |
| DEP-NQ_ED2P_SC_BFST | 416,984 | 416,984 | 0 | 0.00% | 16,345,889,448,506.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 237,697 | 237,697 | 0 | 0.00% | 62,487,049,395,827.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 178,100 | 178,100 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 78,241 | 78,241 | 0 | 0.00% | 1,611,546,059.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,257 | 70,257 | 0 | 0.00% | -756,041,441.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 51,086 | 51,086 | 0 | 0.00% | 53,993,009,675,593.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,561 | 8,561 | 0 | 0.00% | 85,295,551,257,441.00 | Healthy |
| LON-NQ_ED2P_BORV | 6,077 | 2,445 | 3,632 | 59.77% | 4,882,828,620,544.00 | Critical |
| LON-Q_GLCP_BORV | 5,948 | 4,201 | 1,747 | 29.37% | 6,174,673,204,517.00 | Critical |

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
| ebsintslp01 | App | 20.8% | 32.2% | 57.0% | 0.0% | 0.0% | 0.0% | 18.1% | 18.1% | 18.2% | Healthy |
| ebsintslp02 | App | 4.5% | 23.3% | 58.5% | 0.0% | 0.0% | 0.0% | 10.1% | 10.2% | 10.3% | Healthy |
| efsdbsdr01 | Database | 27.9% | 34.4% | 53.7% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 67.1% | Warning |
| efsdbsdr02 | Database | 3.7% | 8.4% | 20.9% | 0.0% | 0.0% | 0.0% | 47.4% | 47.5% | 47.5% | Healthy |
| efsdbslp01 | Database | 0.0% | 57.3% | 94.4% | 0.0% | 0.0% | 0.0% | 0.0% | 61.2% | 65.8% | Critical |
| efsdbslp02 | Database | 0.0% | 62.9% | 93.7% | 0.0% | 0.0% | 0.0% | 0.0% | 59.1% | 59.4% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 321,564 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.76%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
