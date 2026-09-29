# EFS DAILY HEALTH REPORT
**Periode:** 24 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260724.xlsx, EFS_Infrastructures_20260724.xlsx, EFS_XLA_20260724.xlsx, EFS_GL_20260724.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,607,850
- **XLA Success Rate:** 99.99%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,164
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,164 records. GL Posted mencapai 225,320 (99.78% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.99% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.78% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 147.31 | 147.31 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 44.19 | 44.19 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 34.95 | 34.95 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 32.71 | 32.71 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 23.82 | 23.82 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 4.93 | 4.93 | 100.00% | Healthy |
| Gather Schema Statistics | 0 | 0.00 | 3.09 | 3.09 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 3.04 | 3.04 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 2.29 | 2.29 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 1.83 | 1.83 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,607,850 | Volume total harian |
| Processed (P / XLA=S) | 2,601,686 | Sukses diproses (99.99%) |
| Unprocessed (U) | 6,164 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 225,820
- **FAH Success:** 225,818
- **FAH Error:** 2
- **Not Accounted:** 225,320
- **Posted GL:** 225,320 (99.78% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 224,873 | 2 | 224,390 | 224,390 | 0 |
| CROSS BORDER PAYMENT Custom Application | 663 | 0 | 663 | 663 | 0 |
| TRADE FINANCE Custom Application | 198 | 0 | 198 | 198 | 0 |
| CREDIT CARD Custom Application | 54 | 0 | 37 | 37 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| PREPAID SYSTEM Custom Application | 7 | 0 | 7 | 7 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,452,938 | 1,452,238 | 700 | 0.05% | 270,932,796,765,698.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 508,361 | 508,361 | 0 | 0.00% | 18,748,429,882,759.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 227,101 | 227,101 | 0 | 0.00% | 56,082,472,395,545.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,094 | 182,094 | 0 | 0.00% | 20,942,546.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,467 | 93,467 | 0 | 0.00% | 1,876,640,174.00 | Healthy |
| LON-Q_GLCP_GEND872 | 69,226 | 69,226 | 0 | 0.00% | 163,848,123.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 47,491 | 47,491 | 0 | 0.00% | 61,086,250,910,431.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,392 | 7,392 | 0 | 0.00% | 67,958,892,351,279.00 | Healthy |
| LON-NQ_ED2P_BORV | 5,778 | 2,279 | 3,499 | 60.56% | 4,441,368,662,689.00 | Critical |
| DEP-NQ_ED2P_CC_INVV | 5,735 | 5,735 | 0 | 0.00% | 3,179,082,963,761.00 | Healthy |

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
| ebsintslp01 | App | 4.7% | 18.4% | 56.1% | 0.0% | 0.0% | 0.0% | 18.0% | 18.0% | 18.1% | Healthy |
| ebsintslp02 | App | 4.5% | 17.4% | 46.4% | 0.0% | 0.0% | 0.0% | 10.0% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 1.6% | 4.6% | 22.9% | 0.0% | 0.0% | 0.0% | 66.4% | 66.6% | 66.9% | Warning |
| efsdbsdr02 | Database | 3.5% | 7.2% | 28.8% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.6% | Healthy |
| efsdbslp01 | Database | 19.0% | 50.1% | 90.5% | 0.0% | 0.0% | 0.0% | 57.2% | 60.9% | 66.0% | Critical |
| efsdbslp02 | Database | 35.5% | 49.7% | 77.0% | 0.0% | 0.0% | 0.0% | 59.0% | 59.1% | 59.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,164 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.78%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
