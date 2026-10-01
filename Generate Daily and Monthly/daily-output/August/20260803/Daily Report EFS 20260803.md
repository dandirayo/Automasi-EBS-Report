# EFS DAILY HEALTH REPORT
**Periode:** 3 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260803.xlsx, EFS_Infrastructures_20260803.xlsx, EFS_XLA_20260803.xlsx, EFS_GL_20260803.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,964,193
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,661
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,661 records. GL Posted mencapai 236,253 (99.83% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.83% | PASS |

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
| Create Accounting | 1,770 | 1,668 | 97 | 5 | 2.20 | 8.23 | CRITICAL | - |
| Accounting Program | 253 | 122 | 130 | 1 | 46.35 | 51.16 | CRITICAL | [Error] [1x] An internal error occurred.  Please inform your system administrator or support representative that:  An internal error has occurred in the program xla_ap_acct_hooks_pkg.main.  Technical problem : Error encountered in product API for extrac |
| Journal Import | 1,686 | 1,682 | 4 | 0 | 0.50 | 1.78 | WARNING | - |
| Posting | 4 | 4 | 0 | 0 | 0.52 | 0.54 | HEALTHY | - |
| Posting: Single Ledger | 1,680 | 1,680 | 0 | 0 | 0.48 | 0.59 | HEALTHY | - |
| Transfer Journal Entries to GL | 5 | 5 | 0 | 0 | 11.00 | 11.96 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.67 | 0.67 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 51.74 | 53.16 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 34 | 34 | 0 | 0 | 40.94 | 44.74 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 12 | 0.03 | Healthy |
| BNI GL Interface Jurnal KLN | 2 | 0.52 | Healthy |
| BNI GL KLN Load File to Table | 2 | 0.20 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,964,193 | Volume total harian |
| Processed (P / XLA=S) | 2,941,530 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,661 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 236,646
- **2. FAH Processing (FAH Success / Error):** 236,644 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 236,253 / 391
- **4. Transfer to GL (Transferred):** 236,253
- **5. GL Posting (Posted / Unposted):** 236,253 (99.83% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 236,282 | 2 | 389 | 235,891 | 0 |
| PSAK 71 Custom Application | 228 | 0 | 0 | 228 | 0 |
| CROSS BORDER PAYMENT Custom Application | 80 | 0 | 0 | 80 | 0 |
| CREDIT CARD Custom Application | 41 | 0 | 0 | 41 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,458,079 | 1,449,360 | 8,719 | 0.60% | 245,083,927,559,453.81 | Warning |
| DEP-NQ_ED2P_SC_BFST | 504,354 | 504,354 | 0 | 0.00% | 18,753,079,203,448.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 413,636 | 413,482 | 154 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 221,966 | 221,962 | 4 | 0.00% | 115,115,702,406,281.38 | Healthy |
| LON-Q_GLCP_GEND872 | 149,022 | 149,022 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,121 | 93,121 | 0 | 0.00% | 1,823,492,924.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 55,635 | 55,635 | 0 | 0.00% | 80,423,225,470,378.86 | Healthy |
| LON-NQ_ED2P_BORV | 16,408 | 5,633 | 10,775 | 65.67% | 8,478,347,128,775.21 | Critical |
| LON-Q_GLCP_LOND2140 | 11,555 | 11,555 | 0 | 0.00% | -206,000,316,389.03 | Healthy |
| LON-Q_GLCP_GLIF | 11,410 | 11,241 | 169 | 1.48% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 17.0% | 65.5% | 98.2% | 48.5% | 57.9% | 64.8% | 50.4% | 50.4% | 50.8% | Critical |
| efsdbsdr01 | Database | 27.0% | 37.3% | 69.0% | 51.7% | 52.5% | 53.4% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.5% | 29.7% | 49.0% | 49.3% | 50.1% | 43.2% | 43.3% | 43.3% | Healthy |
| efsdbslp01 | Database | 4.0% | 47.7% | 98.3% | 49.5% | 53.7% | 58.7% | 49.4% | 58.3% | 62.2% | Critical |
| ebsintslp02 | App | 3.5% | 20.2% | 88.7% | 42.3% | 44.6% | 49.2% | 10.7% | 10.7% | 10.8% | Critical |
| ebsintslp01 | App | 3.5% | 16.1% | 83.4% | 49.6% | 51.9% | 58.3% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,661 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.83%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
