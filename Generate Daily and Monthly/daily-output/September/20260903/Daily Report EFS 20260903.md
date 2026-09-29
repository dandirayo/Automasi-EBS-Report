# EFS DAILY HEALTH REPORT
**Periode:** 3 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260903.xlsx, EFS_Infrastructures_20260903.xlsx, EFS_XLA_20260903.xlsx, EFS_GL_20260903.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,576,947
- **XLA Success Rate:** 94.31%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 134,279
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 134,279 records. GL Posted mencapai 222,824 (99.37% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 94.31% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.37% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,576,947 | Volume total harian |
| Processed (P / XLA=S) | 2,425,290 | Sukses diproses (94.31%) |
| Unprocessed (U) | 134,279 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 224,234
- **FAH Success:** 223,261
- **FAH Error:** 196
- **Not Accounted:** 222,824
- **Posted GL:** 222,824 (99.37% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 223,301 | 119 | 221,987 | 221,987 | 0 |
| CROSS BORDER PAYMENT Custom Application | 573 | 0 | 573 | 573 | 0 |
| TRADE FINANCE Custom Application | 182 | 0 | 182 | 182 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 57 | 0 | 40 | 40 | 0 |
| TREASURY Custom Application | 15 | 1 | 14 | 14 | 0 |
| JOINT FINANCE Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,416,086 | 1,285,944 | 130,142 | 9.19% | 191,318,161,391,649.09 | Warning |
| DEP-NQ_ED2P_SC_BFST | 506,970 | 506,970 | 0 | 0.00% | 16,657,312,310,346.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 226,326 | 226,326 | 0 | 0.00% | 45,122,892,585,245.44 | Healthy |
| DEP-Q_GLCP_GEND870 | 190,763 | 173,669 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 90,447 | 90,447 | 0 | 0.00% | 1,676,085,326.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,552 | 73,268 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,865 | 42,865 | 0 | 0.00% | 41,814,456,269,581.24 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,337 | 7,337 | 0 | 0.00% | 47,231,892,573,346.19 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,745 | 5,745 | 0 | 0.00% | -41,611,473,734,106.03 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,259 | 5,259 | 0 | 0.00% | 2,941,561,702,725.21 | Healthy |

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
| efsdbslp02 | Database | 14.6% | 33.1% | 78.1% | 58.2% | 60.2% | 64.4% | 50.9% | 51.0% | 51.0% | Warning |
| efsdbsdr01 | Database | 19.9% | 22.1% | 45.2% | 63.3% | 63.7% | 64.5% | 70.3% | 70.4% | 70.4% | Warning |
| efsdbsdr02 | Database | 1.2% | 5.7% | 52.9% | 50.1% | 50.5% | 51.4% | 43.6% | 43.6% | 44.0% | Healthy |
| ebsintslp02 | App | 3.4% | 13.4% | 98.7% | 44.8% | 46.8% | 50.9% | 10.7% | 10.7% | 11.0% | Critical |
| efsdbslp01 | Database | 8.7% | 36.1% | 93.4% | 55.1% | 57.5% | 62.0% | 50.4% | 58.9% | 63.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.0% | 85.3% | 6.5% | 6.8% | 7.8% | 41.2% | 41.2% | 41.8% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 82.2% | 6.4% | 6.6% | 7.9% | 24.3% | 24.4% | 24.8% | Critical |
| ebsintslp01 | App | 20.7% | 30.7% | 94.7% | 50.2% | 52.4% | 57.5% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 134,279 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.37%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
