# EFS DAILY HEALTH REPORT
**Periode:** 17 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260817.xlsx, EFS_Infrastructures_20260817.xlsx, EFS_XLA_20260817.xlsx, EFS_GL_20260817.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,165,105
- **XLA Success Rate:** 99.13%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 544
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 544 records. GL Posted mencapai 186,640 (99.87% intake).

---

## 02. Glosari dan Service Level Objective (SLO)
### Service Level Objective (SLO)
| Sinyal / Domain | Metrik | Target | Realisasi | Verdict |
|---|---|---|---|---|
| Errors (Kualitas) | XLA Code Success Rate | >= 99.5% | 99.13% | WARNING |
| Latency (Kecepatan) | Batch Program P99 Latency | Dalam baseline harian | Evaluasi P99 | CHECK |
| Saturation (Beban) | CPU Server Max | < 80% | Infrastructure Overview | CRITICAL |
| GL Funnel (Integritas) | GL Posted / Total Intake | >= 99.5% | 99.87% | PASS |

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
| Create Accounting | 165 | 92 | 71 | 0 | 34.93 | 54.57 | WARNING | - |
| Accounting Program | 201 | 109 | 92 | 0 | 50.36 | 54.17 | WARNING | [Warning] [92x] (no completion text) |
| Journal Import | 140 | 140 | 0 | 0 | 1.82 | 12.72 | HEALTHY | - |
| Posting: Single Ledger | 140 | 140 | 0 | 0 | 0.67 | 0.76 | HEALTHY | - |
| Transfer Journal Entries to GL | 7 | 7 | 0 | 0 | 4.77 | 4.95 | HEALTHY | - |
| BNI GL Interface Kurs Harian | 2 | 2 | 0 | 0 | 1.30 | 1.35 | HEALTHY | - |
| BNI FAH Journal Reversal | 2 | 2 | 0 | 0 | 16.52 | 16.52 | HEALTHY | - |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 16 | 16 | 0 | 0 | 15.82 | 19.90 | HEALTHY | - |

### Monitoring Program KLN (Kliring)
| Program Name | Total Hit | P99 (min) | Status |
|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,165,105 | Volume total harian |
| Processed (P / XLA=S) | 2,145,699 | Sukses diproses (99.13%) |
| Unprocessed (U) | 544 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. Monitoring Alur Akuntansi End-to-End (FAH Intake s/d GL Posting)
- **1. FAH Interface / Intake (Masuk FAH):** 186,881
- **2. FAH Processing (FAH Success / Error):** 186,759 / 122
- **3. SLA Accounting (Accounted / Not Accounted):** 186,640 / 119
- **4. Transfer to GL (Transferred):** 186,640
- **5. GL Posting (Posted / Unposted):** 186,640 (99.87% intake) / 0

### Detail Per Application:
| Application | 1. Masuk FAH (Intake) | 2. FAH Error (Pre-process) | 3. Not Accounted (SLA) | 4. Posted (GL) | 5. Unposted (GL) |
|---|---|---|---|---|---|
| ICONS Custom Application | 186,650 | 122 | 117 | 186,411 | 0 |
| CROSS BORDER PAYMENT Custom Application | 88 | 0 | 0 | 88 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 0 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 0 | 52 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 2 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 0 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,176,540 | 1,175,997 | 543 | 0.05% | 16,691,950,324,397.31 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 428,799 | 428,799 | 0 | 0.00% | 8,861,879,084,091.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 197,829 | 197,829 | 0 | 0.00% | 4,067,842,178,210.18 | Healthy |
| DEP-Q_GLCP_GEND870 | 193,680 | 175,106 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 81,181 | 81,181 | 0 | 0.00% | 1,398,183,017.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,764 | 72,476 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,890 | 5,890 | 0 | 0.00% | -36,407,351,553,750.40 | Healthy |
| DEP-NQ_ED2P_T_INVV | 4,407 | 4,407 | 0 | 0.00% | 73,099,403,017.49 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,707 | 2,707 | 0 | 0.00% | 29,977,329,481.11 | Healthy |
| BRA-NQ_ED2P_ELOG | 853 | 853 | 0 | 0.00% | 335,032,960,937.00 | Healthy |

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
| efsdbslp02 | Database | 22.8% | 40.4% | 95.7% | 53.0% | 53.4% | 53.9% | 50.3% | 50.4% | 50.9% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.0% | 78.4% | 57.2% | 57.7% | 58.5% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.6% | 6.3% | 28.8% | 49.7% | 49.8% | 50.5% | 43.4% | 43.4% | 43.5% | Healthy |
| ebsintslp02 | App | 3.2% | 7.8% | 89.1% | 43.5% | 43.9% | 45.3% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 10.1% | 24.7% | 91.8% | 51.4% | 51.7% | 52.6% | 48.7% | 55.5% | 62.7% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 87.6% | 5.5% | 5.7% | 6.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.3% | 5.3% | 5.5% | 6.8% | 24.3% | 24.3% | 24.8% | Critical |
| ebsintslp01 | App | 4.0% | 7.8% | 70.6% | 50.7% | 50.9% | 51.6% | 15.9% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 544 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.87%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
