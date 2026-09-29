# EFS DAILY HEALTH REPORT
**Periode:** 20 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260820.xlsx, EFS_Infrastructures_20260820.xlsx, EFS_XLA_20260820.xlsx, EFS_GL_20260820.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,541,285
- **XLA Success Rate:** 94.10%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 135,987
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 135,987 records. GL Posted mencapai 225,799 (99.34% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 94.10% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.34% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,541,285 | Volume total harian |
| Processed (P / XLA=S) | 2,386,301 | Sukses diproses (94.10%) |
| Unprocessed (U) | 135,987 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 227,302
- **FAH Success:** 226,252
- **FAH Error:** 239
- **Not Accounted:** 225,799
- **Posted GL:** 225,799 (99.34% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 226,551 | 163 | 225,143 | 225,143 | 0 |
| CROSS BORDER PAYMENT Custom Application | 405 | 0 | 405 | 405 | 0 |
| TRADE FINANCE Custom Application | 184 | 0 | 184 | 184 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 33 | 33 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,394,253 | 1,262,585 | 131,668 | 9.44% | 229,938,508,784,216.47 | Warning |
| DEP-NQ_ED2P_SC_BFST | 486,520 | 486,520 | 0 | 0.00% | 15,517,992,242,065.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 228,679 | 228,679 | 0 | 0.00% | 44,176,457,864,680.78 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,185 | 175,517 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 91,712 | 91,712 | 0 | 0.00% | 2,407,266,673.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,804 | 72,516 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,177 | 43,177 | 0 | 0.00% | 61,949,094,269,666.56 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,950 | 6,950 | 0 | 0.00% | 65,533,801,486,629.14 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,896 | 5,896 | 0 | 0.00% | -38,556,042,649,052.15 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,348 | 5,348 | 0 | 0.00% | 2,387,965,462,715.17 | Healthy |

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
| efsdbslp02 | Database | 35.9% | 59.2% | 96.8% | 54.7% | 57.0% | 61.1% | 50.4% | 50.4% | 50.5% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.8% | 82.8% | 58.4% | 59.0% | 61.1% | 70.2% | 70.2% | 70.2% | Critical |
| efsdbsdr02 | Database | 2.6% | 7.2% | 54.2% | 49.7% | 49.9% | 50.7% | 43.5% | 43.5% | 43.9% | Healthy |
| efsdbslp01 | Database | 11.0% | 45.9% | 98.0% | 52.1% | 54.8% | 59.8% | 46.8% | 55.5% | 63.1% | Critical |
| ebsintslp02 | App | 3.3% | 15.7% | 98.2% | 36.8% | 40.8% | 47.1% | 10.7% | 10.7% | 10.8% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 85.9% | 5.7% | 5.9% | 6.8% | 41.2% | 41.2% | 41.9% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 81.9% | 5.4% | 5.7% | 7.0% | 24.3% | 24.3% | 25.1% | Critical |
| ebsintslp01 | App | 3.8% | 16.8% | 90.9% | 43.5% | 48.6% | 54.5% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 135,987 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.34%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
