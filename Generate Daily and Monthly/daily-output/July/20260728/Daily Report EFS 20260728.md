# EFS DAILY HEALTH REPORT
**Periode:** 28 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260728.xlsx, EFS_Infrastructures_20260728.xlsx, EFS_XLA_20260728.xlsx, EFS_GL_20260728.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,527,610
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,103
- **Infrastruktur Status:** 2 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,103 records. GL Posted mencapai 228,237 (99.76% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.76% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| BNI FAH Journal Reversal | 0 | 0.00 | 253.92 | 253.92 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 133.70 | 133.70 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 86.69 | 86.69 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 39.42 | 39.42 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 36.61 | 36.61 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 31.14 | 31.14 | 100.00% | Critical |
| BNI GL Accrue Expense Generate | 0 | 0.00 | 7.84 | 7.84 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 6.04 | 6.04 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 3.71 | 3.71 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 3.71 | 3.71 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,527,610 | Volume total harian |
| Processed (P / XLA=S) | 2,521,507 | Sukses diproses (100.00%) |
| Unprocessed (U) | 6,103 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 228,790
- **FAH Success:** 228,788
- **FAH Error:** 2
- **Not Accounted:** 228,237
- **Posted GL:** 228,237 (99.76% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 227,522 | 2 | 226,995 | 226,995 | 0 |
| CROSS BORDER PAYMENT Custom Application | 976 | 0 | 976 | 976 | 0 |
| TRADE FINANCE Custom Application | 194 | 0 | 194 | 194 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 32 | 32 | 0 |
| PREPAID SYSTEM Custom Application | 23 | 0 | 15 | 15 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,393,244 | 1,392,248 | 996 | 0.07% | 206,651,817,302,164.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 495,032 | 495,032 | 0 | 0.00% | 16,505,277,182,303.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 224,742 | 224,742 | 0 | 0.00% | 38,326,600,026,097.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 175,575 | 175,575 | 0 | 0.00% | -30,092,042,712.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 91,585 | 91,585 | 0 | 0.00% | 1,824,737,690.00 | Healthy |
| LON-Q_GLCP_GEND872 | 71,105 | 71,105 | 0 | 0.00% | -120,954,455.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 44,602 | 44,602 | 0 | 0.00% | 46,954,353,956,913.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,338 | 7,338 | 0 | 0.00% | 53,217,021,012,593.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,766 | 5,766 | 0 | 0.00% | -40,323,365,924,260.00 | Healthy |
| LON-NQ_ED2P_BORV | 5,765 | 2,382 | 3,383 | 58.68% | 3,167,135,463,194.00 | Critical |

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
| ebsintslp01 | App | 4.4% | 16.4% | 47.3% | 0.0% | 0.0% | 0.0% | 18.0% | 18.1% | 18.5% | Healthy |
| ebsintslp02 | App | 4.5% | 16.7% | 55.5% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.3% | Healthy |
| efsdbsdr01 | Database | 21.5% | 28.2% | 45.1% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 67.1% | Warning |
| efsdbsdr02 | Database | 3.5% | 8.7% | 20.8% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.4% | Healthy |
| efsdbslp01 | Database | 13.9% | 48.3% | 90.0% | 0.0% | 0.0% | 0.0% | 56.7% | 60.5% | 64.4% | Critical |
| efsdbslp02 | Database | 43.5% | 61.7% | 88.8% | 0.0% | 0.0% | 0.0% | 59.2% | 59.2% | 59.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,103 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
