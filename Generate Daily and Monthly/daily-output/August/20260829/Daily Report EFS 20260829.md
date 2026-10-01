# EFS DAILY HEALTH REPORT
**Periode:** 29 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260829.xlsx, EFS_Infrastructures_20260829.xlsx, EFS_XLA_20260829.xlsx, EFS_GL_20260829.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,825,662
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 27,256
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 27,256 records. GL Posted mencapai 201,840 (99.38% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.38% | WARNING |

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
| Create Accounting | 147 | 66 | 81 | 0 | 41.55 | 69.10 | WARNING | - |
| Accounting Program | 231 | 136 | 95 | 0 | 61.16 | 67.52 | WARNING | [Warning] [95x] (no completion text) |
| Journal Import | 148 | 148 | 0 | 0 | 2.65 | 3.58 | HEALTHY | - |
| Posting: Single Ledger | 148 | 148 | 0 | 0 | 0.73 | 0.91 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 11.82 | 12.60 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.67 | 1.67 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 21.42 | 21.42 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 9 | 9 | 0 | 0 | 21.25 | 21.42 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,825,662 | Volume total harian |
| Processed (P / XLA=S) | 2,798,404 | Sukses diproses (100.00%) |
| Unprocessed (U) | 27,256 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 203,098
- **2. FAH Processing (FAH Success / Error):** 202,011 / 78
- **3. SLA Accounting (Accounted / Not Accounted):** 201,937 / 74
- **4. Transfer to GL (Transferred):** 201,840
- **5. GL Posting (Posted / Unposted):** 201,840 (99.38% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 202,184 | 2 | 53 | 201,023 | 0 |
| CROSS BORDER PAYMENT Custom Application | 560 | 0 | 0 | 560 | 0 |
| TRADE FINANCE Custom Application | 190 | 0 | 2 | 188 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 17 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 0 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 0 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,395,409 | 1,387,898 | 7,511 | 0.54% | 23,200,915,461,363.79 | Warning |
| DEP-NQ_ED2P_SC_BFST | 458,008 | 458,008 | 0 | 0.00% | 13,190,768,556,604.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 422,025 | 421,871 | 154 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 227,388 | 227,388 | 0 | 0.00% | 5,678,700,311,342.90 | Healthy |
| LON-Q_GLCP_GEND872 | 151,998 | 151,992 | 6 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 111,997 | 111,997 | 0 | 0.00% | 2,235,578,965.00 | Healthy |
| LON-NQ_ED2P_BORV | 22,712 | 6,795 | 15,917 | 70.08% | 461,840,894,171.76 | Critical |
| LON-Q_GLCP_GLIF | 11,955 | 11,955 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,352 | 11,352 | 0 | 0.00% | -106,428,028,158.52 | Healthy |
| LON-Q_GLCP_BORV | 3,879 | 213 | 3,666 | 94.51% | 241,569,498,012.00 | Critical |

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
| efsdbslp02 | Database | 23.4% | 41.8% | 91.0% | 56.7% | 57.2% | 57.9% | 50.6% | 50.6% | 50.7% | Critical |
| efsdbsdr01 | Database | 39.5% | 41.4% | 79.1% | 61.2% | 61.5% | 63.3% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.7% | 6.4% | 27.8% | 49.9% | 50.1% | 50.7% | 43.5% | 43.6% | 43.6% | Healthy |
| ebsintslp02 | App | 3.7% | 8.9% | 98.6% | 42.6% | 43.0% | 45.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 16.6% | 34.6% | 99.0% | 54.2% | 54.7% | 55.9% | 45.7% | 54.5% | 62.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.1% | 5.9% | 6.2% | 7.6% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.2% | 87.0% | 6.2% | 6.5% | 7.8% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.1% | 8.5% | 72.2% | 47.3% | 47.8% | 49.8% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 27,256 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.38%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
