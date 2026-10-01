# EFS DAILY HEALTH REPORT
**Periode:** 10 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260810.xlsx, EFS_Infrastructures_20260810.xlsx, EFS_XLA_20260810.xlsx, EFS_GL_20260810.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,169,786
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 43,337
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 43,337 records. GL Posted mencapai 231,382 (99.77% intake).

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
| Create Accounting | 2,313 | 2,232 | 77 | 2 | 1.86 | 4.88 | CRITICAL | - |
| Accounting Program | 221 | 117 | 104 | 0 | 46.73 | 52.65 | WARNING | [Warning] [104x] (no completion text) |
| Journal Import | 2,239 | 2,239 | 0 | 0 | 0.52 | 1.51 | HEALTHY | - |
| Posting | 1 | 1 | 0 | 0 | 0.52 | 0.52 | HEALTHY | - |
| Posting: Single Ledger | 2,239 | 2,239 | 0 | 0 | 0.50 | 0.53 | HEALTHY | - |
| Transfer Journal Entries to GL | 8 | 8 | 0 | 0 | 6.42 | 7.36 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 2.65 | 2.65 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 17.07 | 17.07 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 19 | 19 | 0 | 0 | 30.43 | 32.42 | HEALTHY | - |
| BNI FAH Laporan Konfigurasi | 1 | 1 | 0 | 0 | 5.82 | 5.82 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,169,786 | Volume total harian |
| Processed (P / XLA=S) | 3,126,447 | Sukses diproses (100.00%) |
| Unprocessed (U) | 43,337 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 231,911
- **2. FAH Processing (FAH Success / Error):** 231,791 / 120
- **3. SLA Accounting (Accounted / Not Accounted):** 231,382 / 409
- **4. Transfer to GL (Transferred):** 231,382
- **5. GL Posting (Posted / Unposted):** 231,382 (99.77% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 231,715 | 120 | 407 | 231,188 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CROSS BORDER PAYMENT Custom Application | 66 | 0 | 0 | 66 | 0 |
| CREDIT CARD Custom Application | 38 | 0 | 0 | 38 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 1 | 0 | 0 | 1 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,555,516 | 1,547,157 | 8,359 | 0.54% | 299,768,445,766,894.31 | Warning |
| DEP-NQ_ED2P_SC_BFST | 537,979 | 537,979 | 0 | 0.00% | 18,411,256,086,876.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 416,992 | 416,864 | 128 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 245,141 | 245,138 | 3 | 0.00% | 115,732,282,319,280.48 | Healthy |
| LON-Q_GLCP_GEND872 | 159,318 | 157,709 | 1,609 | 1.01% | 0.00 | Warning |
| DEP-NQ_ED2P_SC_ELOG | 102,102 | 102,102 | 0 | 0.00% | 2,142,570,632.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 54,473 | 54,473 | 0 | 0.00% | 78,642,828,782,836.78 | Healthy |
| LON-NQ_ED2P_BORV | 30,860 | 8,949 | 21,911 | 71.00% | 3,669,177,285,279.15 | Critical |
| LON-Q_GLCP_GLIF | 17,693 | 17,511 | 182 | 1.03% | 0.00 | Healthy |
| LON-Q_GLCP_BORV | 14,662 | 3,698 | 10,964 | 74.78% | 4,786,918,752,679.34 | Critical |

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
| efsdbslp02 | Database | 22.7% | 45.1% | 88.4% | 50.9% | 52.8% | 56.3% | 50.2% | 50.3% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 37.7% | 78.2% | 55.0% | 55.5% | 56.4% | 70.2% | 70.2% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.5% | 10.9% | 36.8% | 49.4% | 49.9% | 50.8% | 43.4% | 43.4% | 43.6% | Healthy |
| ebsintslp02 | App | 3.2% | 14.4% | 86.3% | 43.2% | 45.4% | 50.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 22.3% | 51.0% | 96.3% | 51.7% | 54.0% | 58.5% | 52.6% | 57.7% | 65.5% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 81.6% | 4.8% | 5.1% | 6.4% | 24.3% | 24.3% | 24.6% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 86.0% | 5.1% | 5.2% | 6.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.8% | 15.0% | 79.4% | 50.2% | 52.3% | 57.1% | 15.8% | 15.9% | 16.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 43,337 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
