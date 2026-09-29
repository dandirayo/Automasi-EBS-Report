# EFS DAILY HEALTH REPORT
**Periode:** 30 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260730.xlsx, EFS_Infrastructures_20260730.xlsx, EFS_XLA_20260730.xlsx, EFS_GL_20260730.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,487,649
- **XLA Success Rate:** 99.99%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,516
- **Infrastruktur Status:** 3 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,516 records. GL Posted mencapai 231,066 (99.76% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.99% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.76% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 142.87 | 142.87 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 128.33 | 128.33 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 41.43 | 41.43 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 35.27 | 35.27 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 27.19 | 27.19 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 22.96 | 22.96 | 100.00% | Healthy |
| BNI GL Accrue Expense Generate | 0 | 0.00 | 12.32 | 12.32 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 8.77 | 8.77 | 100.00% | Critical |
| BNI GL Revaluasi Harian | 0 | 0.00 | 4.02 | 4.02 | 100.00% | Healthy |
| BNI GL Interface Kurs Harian | 0 | 0.00 | 2.98 | 2.98 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,487,649 | Volume total harian |
| Processed (P / XLA=S) | 2,481,133 | Sukses diproses (99.99%) |
| Unprocessed (U) | 6,516 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 231,614
- **FAH Success:** 231,614
- **FAH Error:** 0
- **Not Accounted:** 231,066
- **Posted GL:** 231,066 (99.76% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 230,854 | 0 | 230,326 | 230,326 | 0 |
| CROSS BORDER PAYMENT Custom Application | 471 | 0 | 471 | 471 | 0 |
| TRADE FINANCE Custom Application | 199 | 0 | 199 | 199 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| JOINT FINANCE Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,357,956 | 1,357,388 | 568 | 0.04% | 263,618,669,063,790.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 488,208 | 488,208 | 0 | 0.00% | 16,335,032,171,868.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 228,138 | 228,138 | 0 | 0.00% | 43,318,793,388,278.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 176,626 | 176,626 | 0 | 0.00% | 172,679,664.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 88,845 | 88,845 | 0 | 0.00% | 1,673,074,792.00 | Healthy |
| LON-Q_GLCP_GEND872 | 71,568 | 71,568 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,093 | 43,093 | 0 | 0.00% | 52,918,321,497,034.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,258 | 7,258 | 0 | 0.00% | 58,166,720,682,917.00 | Healthy |
| LON-NQ_ED2P_BORV | 6,412 | 2,535 | 3,877 | 60.46% | 4,028,609,360,458.00 | Critical |
| LON-Q_GLCP_BORV | 5,969 | 4,065 | 1,904 | 31.90% | 4,021,361,500,154.00 | Critical |

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
| ebsintslp01 | App | 21.0% | 33.7% | 98.9% | 0.0% | 0.0% | 0.0% | 18.1% | 18.1% | 19.0% | Critical |
| ebsintslp02 | App | 4.2% | 16.6% | 56.1% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 27.9% | 32.4% | 47.2% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 67.0% | Warning |
| efsdbsdr02 | Database | 3.5% | 6.7% | 20.2% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.5% | Healthy |
| efsdbslp01 | Database | 15.2% | 50.4% | 90.5% | 0.0% | 0.0% | 0.0% | 59.4% | 61.5% | 65.0% | Critical |
| efsdbslp02 | Database | 43.8% | 65.4% | 94.6% | 0.0% | 0.0% | 0.0% | 59.2% | 59.3% | 59.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,516 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.76%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
