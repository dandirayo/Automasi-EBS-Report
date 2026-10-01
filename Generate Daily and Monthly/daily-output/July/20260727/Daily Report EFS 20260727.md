# EFS DAILY HEALTH REPORT
**Periode:** 27 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260727.xlsx, EFS_Infrastructures_20260727.xlsx, EFS_XLA_20260727.xlsx, EFS_GL_20260727.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,109,178
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,537
- **Infrastruktur Status:** 3 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,537 records. GL Posted mencapai 229,954 (99.74% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.74% | PASS |

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
| Create Accounting | 2,729 | 2,640 | 84 | 5 | 1.92 | 4.34 | CRITICAL | - |
| Accounting Program | 228 | 119 | 109 | 0 | 40.08 | 44.60 | WARNING | - |
| Journal Import | 2,606 | 2,606 | 0 | 0 | 0.43 | 1.23 | HEALTHY | - |
| Posting | 1 | 1 | 0 | 0 | 0.43 | 0.43 | HEALTHY | - |
| Posting: Single Ledger | 2,606 | 2,606 | 0 | 0 | 0.43 | 0.46 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 4.63 | 4.86 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 1.68 | 1.68 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 8.72 | 8.72 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 21 | 21 | 0 | 0 | 25.93 | 26.01 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,109,178 | Volume total harian |
| Processed (P / XLA=S) | 2,103,641 | Sukses diproses (100.00%) |
| Unprocessed (U) | 5,537 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 230,559
- **2. FAH Processing (FAH Success / Error):** 230,555 / 4
- **3. SLA Accounting (Accounted / Not Accounted):** 229,954 / 601
- **4. Transfer to GL (Transferred):** 229,954
- **5. GL Posting (Posted / Unposted):** 229,954 (99.74% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 230,426 | 4 | 601 | 229,821 | 0 |
| CROSS BORDER PAYMENT Custom Application | 77 | 0 | 0 | 77 | 0 |
| CREDIT CARD Custom Application | 39 | 0 | 0 | 39 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 0 | 10 | 0 |
| PREPAID SYSTEM Custom Application | 5 | 0 | 0 | 5 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,121,031 | 1,120,118 | 913 | 0.08% | 232,179,247,103,663.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 393,076 | 393,076 | 0 | 0.00% | 15,757,779,942,712.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 183,497 | 183,497 | 0 | 0.00% | 59,889,048,195,104.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 175,876 | 175,876 | 0 | 0.00% | 1,022,670.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 85,037 | 85,037 | 0 | 0.00% | 1,749,148,378.00 | Healthy |
| LON-Q_GLCP_GEND872 | 69,799 | 69,799 | 0 | 0.00% | -7,290,019,991.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 48,931 | 48,931 | 0 | 0.00% | 62,272,214,525,565.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,601 | 8,601 | 0 | 0.00% | 66,355,048,706,286.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,739 | 5,739 | 0 | 0.00% | -40,536,605,694,054.00 | Healthy |
| LON-NQ_ED2P_BORV | 5,423 | 2,293 | 3,130 | 57.72% | 6,727,943,604,528.00 | Critical |

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
| ebsintslp01 | App | 4.3% | 17.1% | 69.5% | 0.0% | 0.0% | 0.0% | 18.0% | 18.1% | 18.5% | Warning |
| ebsintslp02 | App | 4.3% | 17.0% | 54.7% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.5% | Healthy |
| efsdbsdr01 | Database | 15.3% | 27.4% | 89.6% | 0.0% | 0.0% | 0.0% | 66.8% | 66.8% | 66.9% | Critical |
| efsdbsdr02 | Database | 3.5% | 9.0% | 49.3% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.4% | Healthy |
| efsdbslp01 | Database | 13.9% | 43.1% | 84.5% | 0.0% | 0.0% | 0.0% | 59.4% | 61.5% | 65.7% | Critical |
| efsdbslp02 | Database | 42.0% | 62.6% | 87.0% | 0.0% | 0.0% | 0.0% | 59.1% | 59.1% | 59.2% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,537 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.74%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
