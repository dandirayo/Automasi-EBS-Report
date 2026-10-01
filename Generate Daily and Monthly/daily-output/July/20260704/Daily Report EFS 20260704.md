# EFS DAILY HEALTH REPORT
**Periode:** 4 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260704.xlsx, EFS_Infrastructures_20260704.xlsx, EFS_XLA_20260704.xlsx, EFS_GL_20260704.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,433,231
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 572
- **Infrastruktur Status:** 1 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 572 records. GL Posted mencapai 194,536 (99.92% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.92% | PASS |

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
| Create Accounting | 211 | 135 | 76 | 0 | 23.72 | 26.01 | WARNING | - |
| Accounting Program | 307 | 206 | 101 | 0 | 22.92 | 25.91 | WARNING | - |
| Journal Import | 187 | 187 | 0 | 0 | 2.52 | 9.50 | HEALTHY | - |
| Posting: Single Ledger | 187 | 186 | 0 | 1 | 0.43 | 0.53 | CRITICAL | [Error] [1x] Concurrent program returned no reason for failure. |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 8.19 | 8.54 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.77 | 0.77 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 26.63 | 26.63 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 3 | 3 | 0 | 0 | 23.86 | 24.08 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,433,231 | Volume total harian |
| Processed (P / XLA=S) | 2,432,659 | Sukses diproses (100.00%) |
| Unprocessed (U) | 572 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 194,699
- **2. FAH Processing (FAH Success / Error):** 194,695 / 4
- **3. SLA Accounting (Accounted / Not Accounted):** 194,536 / 159
- **4. Transfer to GL (Transferred):** 194,536
- **5. GL Posting (Posted / Unposted):** 194,536 (99.92% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 193,969 | 4 | 141 | 193,824 | 0 |
| CROSS BORDER PAYMENT Custom Application | 408 | 0 | 0 | 408 | 0 |
| TRADE FINANCE Custom Application | 237 | 0 | 0 | 237 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 16 | 34 | 0 |
| TREASURY Custom Application | 12 | 0 | 0 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,360,750 | 1,360,184 | 566 | 0.04% | 21,312,055,097,295.72 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 483,241 | 483,241 | 0 | 0.00% | 12,333,817,521,526.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 211,218 | 211,218 | 0 | 0.00% | 5,805,589,053,282.65 | Healthy |
| DEP-Q_GLCP_GEND870 | 197,145 | 197,145 | 0 | 0.00% | -3,507,450.81 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 100,194 | 100,194 | 0 | 0.00% | 1,763,868,411.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,533 | 67,533 | 0 | 0.00% | 2,254,233,674.83 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,802 | 5,802 | 0 | 0.00% | -40,008,043,138,337.67 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,277 | 3,277 | 0 | 0.00% | 73,196,870,307.54 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,468 | 2,468 | 0 | 0.00% | 21,402,358,536.31 | Healthy |
| BRA-NQ_ED2P_ELOG | 824 | 824 | 0 | 0.00% | 412,129,889,912.00 | Healthy |

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
| ebsintsdr01 | App | 2.2% | 3.6% | 13.2% | 0.0% | 0.0% | 0.0% | 20.4% | 20.4% | 20.5% | Healthy |
| ebsintsdr02 | App | 2.1% | 4.1% | 11.2% | 0.0% | 0.0% | 0.0% | 12.2% | 12.3% | 13.0% | Healthy |
| ebsintslp01 | App | 3.8% | 11.7% | 27.3% | 0.0% | 0.0% | 0.0% | 25.5% | 25.7% | 26.4% | Healthy |
| ebsintslp02 | App | 20.7% | 23.7% | 33.7% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 53.7% | 61.9% | 99.3% | 0.0% | 0.0% | 0.0% | 65.7% | 65.8% | 65.9% | Critical |
| efsdbsdr02 | Database | 3.1% | 10.4% | 20.9% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 18.3% | 33.6% | 74.4% | 0.0% | 0.0% | 0.0% | 58.8% | 60.7% | 62.4% | Warning |
| efsdbslp02 | Database | 23.6% | 32.9% | 54.3% | 0.0% | 0.0% | 0.0% | 58.2% | 58.2% | 58.2% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 572 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.92%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
