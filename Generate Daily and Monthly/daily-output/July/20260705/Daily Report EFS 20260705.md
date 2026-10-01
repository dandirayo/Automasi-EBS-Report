# EFS DAILY HEALTH REPORT
**Periode:** 5 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260705.xlsx, EFS_Infrastructures_20260705.xlsx, EFS_XLA_20260705.xlsx, EFS_GL_20260705.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,350,709
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,472
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,472 records. GL Posted mencapai 183,161 (99.95% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.95% | PASS |

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
| Create Accounting | 217 | 140 | 77 | 0 | 23.54 | 25.26 | WARNING | - |
| Accounting Program | 311 | 207 | 104 | 0 | 22.95 | 24.40 | WARNING | - |
| Journal Import | 170 | 170 | 0 | 0 | 1.79 | 4.09 | HEALTHY | - |
| Posting: Single Ledger | 170 | 170 | 0 | 0 | 0.42 | 0.46 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 6.14 | 6.39 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.00 | 0.00 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 28.08 | 28.08 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 3 | 3 | 0 | 0 | 24.34 | 24.63 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,350,709 | Volume total harian |
| Processed (P / XLA=S) | 2,349,237 | Sukses diproses (100.00%) |
| Unprocessed (U) | 1,472 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 183,244
- **2. FAH Processing (FAH Success / Error):** 183,240 / 4
- **3. SLA Accounting (Accounted / Not Accounted):** 183,161 / 79
- **4. Transfer to GL (Transferred):** 183,161
- **5. GL Posting (Posted / Unposted):** 183,161 (99.95% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 183,119 | 4 | 77 | 183,038 | 0 |
| CROSS BORDER PAYMENT Custom Application | 93 | 0 | 0 | 93 | 0 |
| CREDIT CARD Custom Application | 18 | 0 | 0 | 18 | 0 |
| PREPAID SYSTEM Custom Application | 8 | 0 | 2 | 6 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,317,550 | 1,316,081 | 1,469 | 0.11% | 19,328,010,691,666.05 | Warning |
| DEP-NQ_ED2P_SC_BFST | 462,806 | 462,806 | 0 | 0.00% | 9,335,343,122,647.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 203,868 | 203,868 | 0 | 0.00% | 4,966,772,204,292.50 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,622 | 196,622 | 0 | 0.00% | -89,394.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 90,206 | 90,206 | 0 | 0.00% | 1,456,723,492.00 | Healthy |
| LON-Q_GLCP_GEND872 | 69,208 | 69,208 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 6,773 | 6,773 | 0 | 0.00% | 97,924,994,554.29 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,382 | 2,382 | 0 | 0.00% | 9,914,623,373.08 | Healthy |
| BRA-NQ_ED2P_ELOG | 871 | 871 | 0 | 0.00% | 376,116,148,982.00 | Healthy |
| BRA-NQ_ED2P_CC_GLDV | 112 | 112 | 0 | 0.00% | 311,399,466.00 | Healthy |

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
| ebsintsdr01 | App | 2.1% | 4.1% | 11.9% | 0.0% | 0.0% | 0.0% | 20.4% | 20.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 2.0% | 3.1% | 13.1% | 0.0% | 0.0% | 0.0% | 12.3% | 12.3% | 13.8% | Healthy |
| ebsintslp01 | App | 3.9% | 11.2% | 26.4% | 0.0% | 0.0% | 0.0% | 25.9% | 25.9% | 25.9% | Healthy |
| ebsintslp02 | App | 21.0% | 23.4% | 32.9% | 0.0% | 0.0% | 0.0% | 10.0% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 53.7% | 59.5% | 72.9% | 0.0% | 0.0% | 0.0% | 65.8% | 65.9% | 65.9% | Warning |
| efsdbsdr02 | Database | 3.1% | 7.9% | 16.7% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 31.4% | 40.1% | 55.7% | 0.0% | 0.0% | 0.0% | 59.7% | 61.0% | 62.4% | Warning |
| efsdbslp02 | Database | 30.6% | 44.5% | 88.1% | 0.0% | 0.0% | 0.0% | 58.2% | 58.3% | 58.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,472 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.95%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
