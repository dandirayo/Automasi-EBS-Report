# EFS DAILY HEALTH REPORT
**Periode:** 16 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260816.xlsx, EFS_Infrastructures_20260816.xlsx, EFS_XLA_20260816.xlsx, EFS_GL_20260816.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,206,604
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 644
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 644 records. GL Posted mencapai 192,637 (99.91% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.91% | PASS |

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
| Create Accounting | 163 | 108 | 53 | 0 | 35.27 | 55.11 | WARNING | - |
| Accounting Program | 201 | 135 | 66 | 0 | 49.10 | 54.94 | WARNING | [Warning] [66x] (no completion text) |
| Journal Import | 138 | 138 | 0 | 0 | 3.36 | 13.56 | HEALTHY | - |
| Posting: Single Ledger | 138 | 138 | 0 | 0 | 0.69 | 0.85 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 6.83 | 7.10 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.03 | 0.03 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 16.22 | 16.22 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 16 | 16 | 0 | 0 | 12.88 | 17.12 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,206,604 | Volume total harian |
| Processed (P / XLA=S) | 2,205,960 | Sukses diproses (100.00%) |
| Unprocessed (U) | 644 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 192,803
- **2. FAH Processing (FAH Success / Error):** 192,801 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 192,637 / 164
- **4. Transfer to GL (Transferred):** 192,637
- **5. GL Posting (Posted / Unposted):** 192,637 (99.91% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 192,494 | 2 | 162 | 192,330 | 0 |
| CROSS BORDER PAYMENT Custom Application | 199 | 0 | 0 | 199 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 0 | 17 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,206,106 | 1,205,464 | 642 | 0.05% | 16,809,567,746,758.30 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 439,921 | 439,921 | 0 | 0.00% | 9,171,572,563,370.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 205,615 | 205,615 | 0 | 0.00% | 4,586,704,582,974.95 | Healthy |
| DEP-Q_GLCP_GEND870 | 183,313 | 183,313 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 86,109 | 86,109 | 0 | 0.00% | 1,575,373,317.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,662 | 72,662 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,885 | 5,885 | 0 | 0.00% | -36,408,051,500,749.40 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,127 | 3,127 | 0 | 0.00% | 64,851,896,692.19 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,539 | 2,539 | 0 | 0.00% | 5,906,629,662.70 | Healthy |
| BRA-NQ_ED2P_ELOG | 848 | 848 | 0 | 0.00% | 354,994,615,038.00 | Healthy |

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
| efsdbslp02 | Database | 22.0% | 38.8% | 78.5% | 52.4% | 52.7% | 53.9% | 50.4% | 50.4% | 50.4% | Warning |
| efsdbsdr01 | Database | 33.2% | 37.7% | 78.4% | 57.0% | 57.4% | 58.1% | 70.2% | 70.2% | 70.5% | Warning |
| efsdbsdr02 | Database | 2.5% | 10.3% | 35.2% | 49.7% | 50.1% | 50.9% | 43.4% | 43.4% | 43.5% | Healthy |
| ebsintslp02 | App | 3.1% | 7.8% | 89.1% | 43.7% | 43.9% | 45.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 10.1% | 23.4% | 85.4% | 51.3% | 51.5% | 52.1% | 49.5% | 54.4% | 59.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 83.0% | 5.3% | 5.4% | 6.7% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 86.1% | 5.3% | 5.6% | 6.5% | 41.2% | 41.2% | 42.0% | Critical |
| ebsintslp01 | App | 4.0% | 11.9% | 82.6% | 50.7% | 50.9% | 51.7% | 15.9% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 644 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.91%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
