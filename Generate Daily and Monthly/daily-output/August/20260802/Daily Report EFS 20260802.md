# EFS DAILY HEALTH REPORT
**Periode:** 2 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260802.xlsx, EFS_Infrastructures_20260802.xlsx, EFS_XLA_20260802.xlsx, EFS_GL_20260802.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,518,987
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,251
- **Infrastruktur Status:** 3 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,251 records. GL Posted mencapai 146,597 (99.92% intake).

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
| Create Accounting | 177 | 59 | 118 | 0 | 30.16 | 49.08 | WARNING | - |
| Accounting Program | 228 | 89 | 139 | 0 | 41.35 | 48.42 | WARNING | - |
| Journal Import | 117 | 115 | 2 | 0 | 2.04 | 3.87 | WARNING | - |
| Posting: Single Ledger | 115 | 115 | 0 | 0 | 0.52 | 0.62 | HEALTHY | - |
| Transfer Journal Entries to GL | 4 | 4 | 0 | 0 | 10.52 | 11.38 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 1 | 1 | 0 | 0 | 0.98 | 0.98 | HEALTHY | - |
| BNI FAH Journal Reversal | 1 | 1 | 0 | 0 | 17.02 | 17.02 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 9 | 9 | 0 | 0 | 21.81 | 21.91 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,518,987 | Volume total harian |
| Processed (P / XLA=S) | 2,500,734 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,251 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 146,714
- **2. FAH Processing (FAH Success / Error):** 146,714 / 0
- **3. SLA Accounting (Accounted / Not Accounted):** 146,597 / 117
- **4. Transfer to GL (Transferred):** 146,597
- **5. GL Posting (Posted / Unposted):** 146,597 (99.92% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 146,537 | 0 | 115 | 146,422 | 0 |
| CROSS BORDER PAYMENT Custom Application | 133 | 0 | 0 | 133 | 0 |
| CREDIT CARD Custom Application | 25 | 0 | 0 | 25 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 0 | 2 | 0 |
| TREASURY Custom Application | 2 | 0 | 0 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,250,888 | 1,241,667 | 9,221 | 0.74% | 35,084,030,234,999.47 | Warning |
| DEP-Q_GLCP_GEND870 | 412,039 | 411,889 | 150 | 0.04% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 411,402 | 411,402 | 0 | 0.00% | 10,914,357,823,511.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 172,417 | 172,417 | 0 | 0.00% | 5,423,471,348,869.00 | Healthy |
| LON-Q_GLCP_GEND872 | 148,962 | 148,962 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,650 | 84,650 | 0 | 0.00% | 1,651,767,050.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,523 | 11,523 | 0 | 0.00% | -1,440,574,542,529.16 | Healthy |
| LON-NQ_ED2P_BORV | 10,007 | 3,028 | 6,979 | 69.74% | 233,881,745,753.00 | Critical |
| LON-Q_GLCP_GLIF | 5,392 | 5,392 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 4,342 | 4,342 | 0 | 0.00% | 95,780,724,022.84 | Healthy |

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
| efsdbslp02 | Database | 35.8% | 56.3% | 95.0% | 57.5% | 57.8% | 58.4% | 50.4% | 50.4% | 50.6% | Critical |
| efsdbsdr01 | Database | 26.9% | 31.7% | 62.3% | 51.1% | 51.6% | 52.3% | 70.2% | 70.3% | 70.5% | Warning |
| efsdbsdr02 | Database | 2.4% | 6.2% | 28.5% | 48.8% | 49.1% | 49.8% | 43.2% | 43.3% | 43.3% | Healthy |
| ebsintslp02 | App | 20.0% | 24.7% | 93.8% | 41.8% | 42.3% | 43.7% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 10.0% | 28.7% | 92.0% | 51.6% | 52.4% | 53.1% | 51.0% | 54.9% | 58.8% | Critical |
| ebsintslp01 | App | 3.7% | 7.6% | 75.4% | 49.3% | 49.7% | 50.4% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,251 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
