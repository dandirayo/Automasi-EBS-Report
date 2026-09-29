# EFS DAILY HEALTH REPORT
**Periode:** 15 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260915.xlsx, EFS_Infrastructures_20260915.xlsx, EFS_XLA_20260915.xlsx, EFS_GL_20260915.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,715,459
- **XLA Success Rate:** 81.75%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 221,967
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 221,967 records. GL Posted mencapai 172,167 (98.55% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 81.75% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.55% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,715,459 | Volume total harian |
| Processed (P / XLA=S) | 1,399,053 | Sukses diproses (81.75%) |
| Unprocessed (U) | 221,967 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 174,695
- **FAH Success:** 172,496
- **FAH Error:** 116
- **Not Accounted:** 172,167
- **Posted GL:** 172,167 (98.55% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 173,839 | 40 | 171,468 | 171,468 | 0 |
| CROSS BORDER PAYMENT Custom Application | 464 | 0 | 464 | 464 | 0 |
| TRADE FINANCE Custom Application | 210 | 0 | 202 | 202 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 71 | 0 | 0 | 0 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| TREASURY Custom Application | 11 | 0 | 11 | 11 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,054,874 | 835,632 | 219,242 | 20.78% | 273,830,842,496,365.97 | Critical |
| DEP-NQ_ED2P_SC_BFST | 358,834 | 287,842 | 0 | 0.00% | 14,751,949,460,268.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 163,662 | 163,662 | 0 | 0.00% | 46,039,533,124,072.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 69,095 | 50,442 | 0 | 0.00% | 1,460,583,727.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 40,503 | 39,092 | 0 | 0.00% | 46,945,887,511,938.02 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,266 | 6,266 | 0 | 0.00% | 63,756,672,778,098.26 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,799 | 5,799 | 0 | 0.00% | -43,371,557,507,090.79 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,981 | 4,981 | 0 | 0.00% | 3,008,946,266,587.88 | Healthy |
| LON-NQ_ED2P_BORV | 4,802 | 1,337 | 1,736 | 36.15% | 3,189,854,597,247.79 | Critical |
| LON-Q_GLCP_BORV | 4,442 | 1,973 | 833 | 18.75% | 3,418,519,689,495.70 | Warning |

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
| efsdbslp02 | Database | 10.0% | 21.4% | 67.7% | 60.2% | 62.2% | 66.6% | 51.2% | 51.2% | 51.4% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.9% | 55.2% | 66.5% | 67.1% | 67.7% | 70.5% | 70.5% | 70.9% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.6% | 12.8% | 50.4% | 50.8% | 51.5% | 43.7% | 43.7% | 43.8% | Healthy |
| ebsintslp02 | App | 2.3% | 14.6% | 98.5% | 43.7% | 45.9% | 50.7% | 10.7% | 10.7% | 11.1% | Critical |
| efsdbslp01 | Database | 5.9% | 24.5% | 89.5% | 56.5% | 58.9% | 64.1% | 48.1% | 54.8% | 63.5% | Critical |
| ebsintsdr02 | App | 0.6% | 2.0% | 82.5% | 7.2% | 7.4% | 8.7% | 24.3% | 24.4% | 24.6% | Critical |
| ebsintsdr01 | App | 0.6% | 2.0% | 86.5% | 7.1% | 7.4% | 8.4% | 41.3% | 41.3% | 41.7% | Critical |
| ebsintslp01 | App | 2.6% | 13.3% | 86.4% | 49.9% | 51.8% | 56.3% | 15.8% | 15.8% | 15.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 221,967 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.55%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
