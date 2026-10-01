# EFS DAILY HEALTH REPORT
**Periode:** 6 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260706.xlsx, EFS_Infrastructures_20260706.xlsx, EFS_XLA_20260706.xlsx, EFS_GL_20260706.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,628,000
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,538
- **Infrastruktur Status:** 4 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,538 records. GL Posted mencapai 222,903 (99.82% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.82% | PASS |

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
| Create Accounting | 879 | 747 | 131 | 1 | 3.77 | 24.46 | CRITICAL | - |
| Accounting Program | 393 | 203 | 190 | 0 | 23.70 | 26.29 | WARNING | - |
| Journal Import | 875 | 872 | 3 | 0 | 0.97 | 2.19 | WARNING | - |
| Posting | 7 | 7 | 0 | 0 | 1.72 | 1.76 | HEALTHY | - |
| Posting: Single Ledger | 873 | 873 | 0 | 0 | 0.38 | 0.65 | HEALTHY | - |
| Transfer Journal Entries to GL | 5 | 5 | 0 | 0 | 8.63 | 9.53 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 2 | 0 | 0 | 0.30 | 0.30 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 21.43 | 21.43 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 39 | 32 | 0 | 1 | 26.78 | 27.75 | CRITICAL | [Error] [1x] Concurrent program returned no reason for failure. |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 6 | 0.02 | Healthy |
| BNI GL Interface Jurnal KLN | 2 | 0.73 | Healthy |
| BNI GL KLN Load File to Table | 2 | 0.20 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,628,000 | Volume total harian |
| Processed (P / XLA=S) | 2,623,457 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,538 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 223,303
- **2. FAH Processing (FAH Success / Error):** 223,283 / 20
- **3. SLA Accounting (Accounted / Not Accounted):** 222,903 / 380
- **4. Transfer to GL (Transferred):** 222,903
- **5. GL Posting (Posted / Unposted):** 222,903 (99.82% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 223,195 | 20 | 378 | 222,797 | 0 |
| CROSS BORDER PAYMENT Custom Application | 54 | 0 | 0 | 54 | 0 |
| CREDIT CARD Custom Application | 39 | 0 | 0 | 39 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,481,412 | 1,480,234 | 1,178 | 0.08% | 243,553,686,418,100.38 | Warning |
| DEP-NQ_ED2P_SC_BFST | 517,176 | 517,176 | 0 | 0.00% | 16,605,684,948,634.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 212,252 | 212,252 | 0 | 0.00% | 59,581,705,132,786.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,014 | 181,014 | 0 | 0.00% | 2,639,856.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,966 | 92,966 | 0 | 0.00% | 1,720,348,000.00 | Healthy |
| LON-Q_GLCP_GEND872 | 66,485 | 66,485 | 0 | 0.00% | -207,837,008.13 | Healthy |
| DEP-NQ_ED2P_T_INVV | 49,479 | 49,479 | 0 | 0.00% | 45,282,574,111,679.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,748 | 7,748 | 0 | 0.00% | 46,719,972,828,377.25 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,637 | 5,637 | 0 | 0.00% | -39,722,339,456,459.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,739 | 4,739 | 0 | 0.00% | 2,851,086,205,774.80 | Healthy |

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
| ebsintsdr01 | App | 2.2% | 2.8% | 10.6% | 0.0% | 0.0% | 0.0% | 20.5% | 20.5% | 22.3% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.5% | 12.0% | 0.0% | 0.0% | 0.0% | 12.3% | 12.3% | 13.2% | Healthy |
| ebsintslp01 | App | 3.8% | 19.3% | 44.9% | 0.0% | 0.0% | 0.0% | 20.8% | 23.9% | 25.9% | Healthy |
| ebsintslp02 | App | 4.5% | 14.8% | 97.9% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 15.0% | Critical |
| efsdbsdr01 | Database | 54.3% | 62.2% | 82.1% | 0.0% | 0.0% | 0.0% | 65.9% | 66.0% | 66.0% | Critical |
| efsdbsdr02 | Database | 3.2% | 6.3% | 16.7% | 0.0% | 0.0% | 0.0% | 46.4% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 6.9% | 39.1% | 92.3% | 0.0% | 0.0% | 0.0% | 53.9% | 59.3% | 62.2% | Critical |
| efsdbslp02 | Database | 14.2% | 39.1% | 81.8% | 0.0% | 0.0% | 0.0% | 58.2% | 58.4% | 58.6% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,538 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.82%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
