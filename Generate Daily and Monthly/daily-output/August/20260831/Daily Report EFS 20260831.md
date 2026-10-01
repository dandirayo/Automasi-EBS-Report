# EFS DAILY HEALTH REPORT
**Periode:** 31 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260831.xlsx, EFS_Infrastructures_20260831.xlsx, EFS_XLA_20260831.xlsx, EFS_GL_20260831.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,739,194
- **XLA Success Rate:** 99.24%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 10,265
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 10,265 records. GL Posted mencapai 240,849 (99.67% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.24% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.67% | PASS |

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
| Create Accounting | 138 | 50 | 86 | 0 | 49.06 | 73.28 | WARNING | - |
| Accounting Program | 224 | 114 | 110 | 0 | 65.26 | 70.28 | WARNING | [Warning] [110x] (no completion text) |
| Journal Import | 169 | 167 | 2 | 0 | 2.62 | 26.01 | WARNING | [Warning] [2x] Not all of your data was imported successfully or it was imported with warnings.  Please review output file. |
| Posting | 9 | 9 | 0 | 0 | 0.62 | 0.63 | HEALTHY | - |
| Posting: Single Ledger | 164 | 164 | 0 | 0 | 0.82 | 1.13 | HEALTHY | - |
| Transfer Journal Entries to GL | 6 | 6 | 0 | 0 | 11.03 | 11.62 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.25 | 0.25 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 18.17 | 18.17 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 35 | 35 | 0 | 0 | 45.12 | 54.94 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|
| BNI GL KLN Move File to Server | 20 | 0.03 | Healthy |
| BNI GL Interface Jurnal KLN | 4 | 1.94 | Healthy |
| BNI GL KLN Load File to Table | 4 | 0.32 | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,739,194 | Volume total harian |
| Processed (P / XLA=S) | 2,709,556 | Sukses diproses (99.24%) |
| Unprocessed (U) | 10,265 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 241,648
- **2. FAH Processing (FAH Success / Error):** 241,350 / 197
- **3. SLA Accounting (Accounted / Not Accounted):** 240,902 / 448
- **4. Transfer to GL (Transferred):** 240,849
- **5. GL Posting (Posted / Unposted):** 240,849 (99.67% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 241,428 | 121 | 435 | 240,718 | 0 |
| CROSS BORDER PAYMENT Custom Application | 85 | 0 | 0 | 85 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 44 | 0 | 11 | 33 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,489,001 | 1,488,376 | 625 | 0.04% | 461,593,954,143,960.81 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 530,138 | 530,138 | 0 | 0.00% | 21,291,139,020,695.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 244,428 | 244,427 | 0 | 0.00% | 97,583,538,297,490.59 | Healthy |
| DEP-Q_GLCP_GEND870 | 197,104 | 178,014 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 107,351 | 107,351 | 0 | 0.00% | 2,299,960,891.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,818 | 72,536 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 54,029 | 54,029 | 0 | 0.00% | 76,795,078,350,743.73 | Healthy |
| LON-NQ_ED2P_BORV | 10,594 | 4,063 | 6,531 | 61.65% | 6,587,114,138,019.36 | Critical |
| LON-Q_GLCP_BORV | 9,674 | 6,703 | 2,971 | 30.71% | 13,116,100,205,374.36 | Critical |
| BRA-NQ_ED2P_T_GLDV | 9,618 | 9,618 | 0 | 0.00% | 85,364,078,422,554.42 | Healthy |

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
| efsdbslp02 | Database | 25.3% | 55.1% | 95.1% | 57.1% | 59.6% | 65.1% | 50.7% | 50.7% | 51.3% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.0% | 82.3% | 62.1% | 62.6% | 63.5% | 70.3% | 70.3% | 70.7% | Critical |
| efsdbsdr02 | Database | 2.6% | 11.1% | 50.3% | 50.0% | 50.4% | 51.2% | 43.5% | 43.6% | 44.0% | Healthy |
| ebsintslp02 | App | 3.4% | 16.5% | 98.6% | 42.6% | 45.5% | 51.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 16.5% | 54.0% | 99.2% | 54.8% | 57.2% | 62.2% | 46.1% | 56.0% | 65.0% | Critical |
| ebsintsdr01 | App | 0.8% | 2.0% | 85.5% | 6.5% | 6.6% | 7.5% | 41.2% | 41.2% | 42.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.4% | 6.0% | 6.4% | 7.7% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintslp01 | App | 4.0% | 15.5% | 92.5% | 47.3% | 50.1% | 55.1% | 15.8% | 15.8% | 16.4% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 10,265 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.67%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
