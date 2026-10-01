# EFS DAILY HEALTH REPORT
**Periode:** 9 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260709.xlsx, EFS_Infrastructures_20260709.xlsx, EFS_XLA_20260709.xlsx, EFS_GL_20260709.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,484,959
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,282
- **Infrastruktur Status:** 2 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,282 records. GL Posted mencapai 224,453 (99.79% intake).

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
| Create Accounting | 1,783 | 1,652 | 130 | 1 | 3.27 | 21.99 | CRITICAL | - |
| Accounting Program | 373 | 184 | 189 | 0 | 24.75 | 28.62 | WARNING | - |
| Journal Import | 1,765 | 1,765 | 0 | 0 | 0.55 | 2.57 | HEALTHY | - |
| Posting | 15 | 15 | 0 | 0 | 1.85 | 2.19 | HEALTHY | - |
| Posting: Single Ledger | 1,765 | 1,764 | 0 | 1 | 0.37 | 0.85 | CRITICAL | [Error] [1x] Program exited with status 1 |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 5.70 | 5.80 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 2 | 0 | 0 | 0.91 | 0.93 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 23.26 | 23.32 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 20 | 20 | 0 | 0 | 36.36 | 38.33 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,484,959 | Volume total harian |
| Processed (P / XLA=S) | 2,480,677 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,282 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 224,917
- **2. FAH Processing (FAH Success / Error):** 224,898 / 19
- **3. SLA Accounting (Accounted / Not Accounted):** 224,453 / 445
- **4. Transfer to GL (Transferred):** 224,453
- **5. GL Posting (Posted / Unposted):** 224,453 (99.79% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 224,142 | 19 | 424 | 223,699 | 0 |
| CROSS BORDER PAYMENT Custom Application | 484 | 0 | 0 | 484 | 0 |
| TRADE FINANCE Custom Application | 208 | 0 | 0 | 208 | 0 |
| CREDIT CARD Custom Application | 45 | 0 | 19 | 26 | 0 |
| TREASURY Custom Application | 15 | 0 | 0 | 15 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,376,295 | 1,375,623 | 672 | 0.05% | 246,139,552,056,221.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 503,629 | 503,629 | 0 | 0.00% | 14,959,153,685,609.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 205,278 | 205,278 | 0 | 0.00% | 53,675,952,114,804.38 | Healthy |
| DEP-Q_GLCP_GEND870 | 180,094 | 180,094 | 0 | 0.00% | -23,216,832,079.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 91,395 | 91,395 | 0 | 0.00% | 1,526,718,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,932 | 68,932 | 0 | 0.00% | -8,305,096.72 | Healthy |
| DEP-NQ_ED2P_T_INVV | 37,709 | 37,709 | 0 | 0.00% | 52,880,194,209,187.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 4,959 | 4,959 | 0 | 0.00% | -35,580,609,191,862.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,893 | 4,893 | 0 | 0.00% | 3,318,485,164,985.64 | Healthy |
| LON-NQ_ED2P_BORV | 3,893 | 1,579 | 2,314 | 59.44% | 3,586,066,753,714.88 | Critical |

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
| ebsintsdr01 | App | 2.3% | 2.9% | 10.7% | 0.0% | 0.0% | 0.0% | 20.6% | 20.6% | 22.2% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.5% | 14.8% | 0.0% | 0.0% | 0.0% | 12.3% | 12.4% | 13.3% | Healthy |
| ebsintslp01 | App | 3.6% | 17.0% | 34.9% | 0.0% | 0.0% | 0.0% | 22.4% | 22.8% | 23.1% | Healthy |
| ebsintslp02 | App | 4.4% | 13.8% | 100.0% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.8% | Critical |
| efsdbsdr01 | Database | 54.0% | 62.2% | 78.2% | 0.0% | 0.0% | 0.0% | 66.3% | 66.4% | 66.5% | Warning |
| efsdbsdr02 | Database | 3.2% | 6.1% | 16.8% | 0.0% | 0.0% | 0.0% | 46.4% | 46.4% | 46.5% | Healthy |
| efsdbslp01 | Database | 17.8% | 41.2% | 95.4% | 0.0% | 0.0% | 0.0% | 57.9% | 62.3% | 65.4% | Critical |
| efsdbslp02 | Database | 19.5% | 39.0% | 65.3% | 0.0% | 0.0% | 0.0% | 58.7% | 58.7% | 58.8% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,282 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
