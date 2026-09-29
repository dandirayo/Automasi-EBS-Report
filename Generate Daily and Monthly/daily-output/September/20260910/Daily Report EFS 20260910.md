# EFS DAILY HEALTH REPORT
**Periode:** 10 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260910.xlsx, EFS_Infrastructures_20260910.xlsx, EFS_XLA_20260910.xlsx, EFS_GL_20260910.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,351,818
- **XLA Success Rate:** 89.01%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,410
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,410 records. GL Posted mencapai 213,305 (98.41% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 89.01% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.41% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,351,818 | Volume total harian |
| Processed (P / XLA=S) | 2,088,017 | Sukses diproses (89.01%) |
| Unprocessed (U) | 5,410 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 216,746
- **FAH Success:** 213,748
- **FAH Error:** 1,315
- **Not Accounted:** 213,305
- **Posted GL:** 213,305 (98.41% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 216,371 | 1,239 | 213,040 | 213,040 | 0 |
| TRADE FINANCE Custom Application | 205 | 0 | 191 | 191 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 31 | 31 | 0 |
| PREPAID SYSTEM Custom Application | 17 | 0 | 15 | 15 | 0 |
| TREASURY Custom Application | 11 | 0 | 11 | 11 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 7 | 0 | 7 | 7 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,323,383 | 1,161,906 | 928 | 0.07% | 259,523,890,842,766.69 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 457,491 | 401,875 | 0 | 0.00% | 15,677,090,829,439.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 215,688 | 215,686 | 0 | 0.00% | 45,319,090,070,680.81 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,345 | 175,955 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 85,446 | 73,042 | 0 | 0.00% | 1,840,318,432.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 45,058 | 36,668 | 0 | 0.00% | 66,247,131,479,923.78 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,889 | 6,889 | 0 | 0.00% | 68,683,792,631,292.40 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,780 | 5,780 | 0 | 0.00% | -42,989,063,402,552.97 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,403 | 2,769 | 0 | 0.00% | 2,432,566,292,746.83 | Healthy |
| LON-NQ_ED2P_BORV | 5,136 | 1,922 | 2,869 | 55.86% | 4,647,950,173,490.05 | Critical |

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
| efsdbslp02 | Database | 13.7% | 37.5% | 88.1% | 59.1% | 61.5% | 66.0% | 51.1% | 51.1% | 51.3% | Critical |
| efsdbsdr01 | Database | 13.4% | 20.7% | 41.7% | 65.2% | 65.8% | 67.6% | 70.4% | 70.4% | 70.8% | Warning |
| efsdbsdr02 | Database | 1.2% | 3.3% | 19.0% | 50.3% | 50.5% | 51.2% | 43.6% | 43.7% | 44.0% | Healthy |
| ebsintslp02 | App | 3.5% | 24.0% | 99.1% | 36.4% | 41.3% | 47.6% | 10.7% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 6.3% | 35.2% | 93.6% | 56.5% | 59.2% | 64.0% | 53.4% | 58.3% | 64.9% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.7% | 6.9% | 7.1% | 8.4% | 24.4% | 24.4% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.0% | 84.9% | 7.2% | 7.4% | 8.3% | 41.3% | 41.3% | 41.7% | Critical |
| ebsintslp01 | App | 3.8% | 14.4% | 87.5% | 42.2% | 48.0% | 56.4% | 15.8% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,410 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.41%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
