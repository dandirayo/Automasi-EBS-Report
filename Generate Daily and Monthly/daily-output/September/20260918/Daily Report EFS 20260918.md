# EFS DAILY HEALTH REPORT
**Periode:** 18 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260918.xlsx, EFS_Infrastructures_20260918.xlsx, EFS_XLA_20260918.xlsx, EFS_GL_20260918.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,185,298
- **XLA Success Rate:** 98.38%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,917
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,917 records. GL Posted mencapai 103,805 (97.88% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 98.38% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 97.88% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,185,298 | Volume total harian |
| Processed (P / XLA=S) | 1,161,224 | Sukses diproses (98.38%) |
| Unprocessed (U) | 4,917 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 106,056
- **FAH Success:** 104,644
- **FAH Error:** 195
- **Not Accounted:** 103,805
- **Posted GL:** 103,805 (97.88% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 105,194 | 119 | 103,099 | 103,099 | 0 |
| CROSS BORDER PAYMENT Custom Application | 520 | 0 | 520 | 520 | 0 |
| TRADE FINANCE Custom Application | 156 | 0 | 149 | 149 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 69 | 0 | 0 | 0 | 0 |
| PREPAID SYSTEM Custom Application | 16 | 0 | 12 | 12 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| TREASURY Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 552,404 | 551,796 | 608 | 0.11% | 209,649,860,824,130.38 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,558 | 175,686 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 180,773 | 180,773 | 0 | 0.00% | 12,746,211,156,004.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 77,941 | 77,940 | 0 | 0.00% | 41,452,069,204,585.89 | Healthy |
| LON-Q_GLCP_GEND872 | 73,832 | 73,548 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 42,574 | 42,574 | 0 | 0.00% | 1,257,414,296.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 36,458 | 36,458 | 0 | 0.00% | 65,674,984,255,319.72 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,813 | 5,813 | 0 | 0.00% | -42,607,149,401,724.78 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,588 | 5,588 | 0 | 0.00% | 71,721,647,191,814.73 | Healthy |
| LON-NQ_ED2P_BORV | 4,738 | 1,839 | 2,899 | 61.19% | 3,918,976,866,542.91 | Critical |

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
| efsdbslp02 | Database | 10.6% | 30.9% | 91.7% | 60.2% | 62.8% | 68.1% | 51.4% | 51.4% | 51.9% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.8% | 31.2% | 67.5% | 67.9% | 68.4% | 70.5% | 70.6% | 70.8% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.8% | 43.4% | 50.5% | 50.9% | 51.7% | 43.8% | 43.8% | 44.1% | Healthy |
| ebsintslp02 | App | 2.4% | 9.9% | 98.9% | 44.1% | 46.2% | 54.0% | 10.7% | 10.7% | 11.0% | Critical |
| efsdbslp01 | Database | 8.3% | 35.0% | 95.1% | 56.8% | 59.3% | 64.4% | 48.2% | 57.0% | 65.0% | Critical |
| ebsintsdr01 | App | 0.6% | 1.6% | 66.4% | 7.4% | 7.5% | 8.6% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.7% | 7.2% | 7.3% | 8.8% | 24.4% | 24.4% | 24.8% | Warning |
| ebsintslp01 | App | 2.7% | 10.3% | 60.1% | 50.2% | 52.7% | 58.0% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,917 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 97.88%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
