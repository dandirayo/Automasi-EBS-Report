# EFS DAILY HEALTH REPORT
**Periode:** 1 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260801.xlsx, EFS_Infrastructures_20260801.xlsx, EFS_XLA_20260801.xlsx, EFS_GL_20260801.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,467,934
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,179
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,179 records. GL Posted mencapai 153,888 (99.41% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 100.00% | PASS |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.41% | WARNING |

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
| Create Accounting | 157 | 86 | 71 | 0 | 40.27 | 49.14 | WARNING | - |
| Accounting Program | 215 | 126 | 89 | 0 | 43.57 | 49.87 | WARNING | - |
| Journal Import | 138 | 135 | 3 | 0 | 6.69 | 12.98 | WARNING | - |
| Posting | 1 | 1 | 0 | 0 | 0.43 | 0.43 | HEALTHY | - |
| Posting: Single Ledger | 135 | 135 | 0 | 0 | 0.73 | 1.06 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 12.99 | 14.06 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.62 | 0.62 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 24.90 | 24.90 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 27 | 27 | 0 | 0 | 24.81 | 345.04 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,467,934 | Volume total harian |
| Processed (P / XLA=S) | 2,449,755 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,179 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 154,795
- **2. FAH Processing (FAH Success / Error):** 154,793 / 2
- **3. SLA Accounting (Accounted / Not Accounted):** 153,888 / 905
- **4. Transfer to GL (Transferred):** 153,888
- **5. GL Posting (Posted / Unposted):** 153,888 (99.41% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 153,978 | 2 | 885 | 153,091 | 0 |
| CROSS BORDER PAYMENT Custom Application | 502 | 0 | 0 | 502 | 0 |
| TRADE FINANCE Custom Application | 220 | 0 | 0 | 220 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 18 | 33 | 0 |
| JOINT FINANCE Custom Application | 14 | 0 | 0 | 14 | 0 |
| TREASURY Custom Application | 14 | 0 | 0 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 2 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 0 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,267,263 | 1,258,624 | 8,639 | 0.68% | 51,572,964,948,507.47 | Warning |
| DEP-NQ_ED2P_SC_BFST | 433,894 | 433,894 | 0 | 0.00% | 16,990,135,864,549.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 308,054 | 307,932 | 122 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 174,152 | 174,152 | 0 | 0.00% | 6,770,192,352,897.12 | Healthy |
| LON-Q_GLCP_GEND872 | 141,494 | 141,492 | 2 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,656 | 92,656 | 0 | 0.00% | 2,155,061,124.00 | Healthy |
| LON-Q_GLCP_GLIF | 14,475 | 14,475 | 0 | 0.00% | 0.00 | Healthy |
| LON-NQ_ED2P_BORV | 11,690 | 3,901 | 7,789 | 66.63% | 8,440,446,174,551.65 | Critical |
| LON-Q_GLCP_LOND2140 | 11,496 | 11,496 | 0 | 0.00% | 7,866,178,402,218.20 | Healthy |
| DEP-NQ_ED2P_T_INVV | 5,864 | 5,864 | 0 | 0.00% | 99,418,030,839.06 | Healthy |

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
| efsdbslp02 | Database | 36.3% | 51.4% | 87.8% | 56.6% | 57.1% | 58.6% | 50.4% | 50.5% | 50.5% | Critical |
| efsdbsdr01 | Database | 26.9% | 31.6% | 68.8% | 50.6% | 51.0% | 51.8% | 70.2% | 70.3% | 70.7% | Warning |
| efsdbsdr02 | Database | 2.5% | 10.4% | 36.4% | 48.8% | 49.3% | 50.1% | 43.2% | 43.3% | 43.5% | Healthy |
| ebsintslp02 | App | 20.3% | 25.4% | 100.0% | 41.7% | 42.1% | 54.6% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 11.0% | 41.5% | 99.6% | 51.7% | 52.2% | 53.2% | 53.6% | 56.7% | 64.8% | Critical |
| ebsintslp01 | App | 4.3% | 12.9% | 99.7% | 49.2% | 49.7% | 58.7% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,179 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.41%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
