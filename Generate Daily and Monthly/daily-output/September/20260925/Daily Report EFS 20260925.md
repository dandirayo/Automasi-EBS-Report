# EFS DAILY HEALTH REPORT
**Periode:** 25 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260925.xlsx, EFS_Infrastructures_20260925.xlsx, EFS_XLA_20260925.xlsx, EFS_GL_20260925.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,806,125
- **XLA Success Rate:** 75.26%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 3,363
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 3,363 records. GL Posted mencapai 148,820 (99.59% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 75.26% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.59% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,806,125 | Volume total harian |
| Processed (P / XLA=S) | 1,355,849 | Sukses diproses (75.26%) |
| Unprocessed (U) | 3,363 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 149,427
- **FAH Success:** 149,228
- **FAH Error:** 196
- **Not Accounted:** 148,820
- **Posted GL:** 148,820 (99.59% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 147,901 | 120 | 147,439 | 147,439 | 0 |
| CROSS BORDER PAYMENT Custom Application | 1,151 | 0 | 1,151 | 1,151 | 0 |
| TRADE FINANCE Custom Application | 204 | 0 | 202 | 202 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 67 | 0 | 0 | 0 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 962,748 | 671,056 | 1,264 | 0.13% | 297,423,511,291,514.56 | Warning |
| DEP-NQ_ED2P_SC_BFST | 305,309 | 213,848 | 0 | 0.00% | 19,582,013,517,550.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,148 | 177,058 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 125,360 | 125,360 | 0 | 0.00% | 37,322,491,789,173.28 | Healthy |
| LON-Q_GLCP_GEND872 | 74,072 | 73,780 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 65,781 | 39,821 | 0 | 0.00% | 1,957,036,708.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 44,550 | 34,717 | 0 | 0.00% | 46,912,416,826,737.60 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,444 | 6,444 | 0 | 0.00% | 53,432,431,776,363.20 | Healthy |
| LON-NQ_ED2P_BORV | 6,219 | 1,072 | 1,341 | 21.56% | 46,106,888,695,228.25 | Critical |
| LON-Q_GLCP_LOND2140 | 5,907 | 5,907 | 0 | 0.00% | -42,236,030,581,391.77 | Healthy |

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
| efsdbslp02 | Database | 11.1% | 28.2% | 82.7% | 61.7% | 63.5% | 67.6% | 51.5% | 51.6% | 51.7% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.2% | 55.8% | 69.5% | 69.9% | 70.7% | 70.6% | 70.7% | 71.4% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.3% | 9.5% | 50.6% | 50.7% | 51.5% | 43.8% | 43.8% | 43.9% | Healthy |
| ebsintslp02 | App | 2.4% | 10.7% | 99.6% | 36.7% | 42.7% | 51.5% | 10.7% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 10.8% | 34.7% | 95.5% | 58.6% | 61.3% | 66.0% | 47.0% | 57.8% | 64.1% | Critical |
| ebsintsdr02 | App | 0.6% | 1.4% | 63.3% | 7.3% | 7.4% | 8.8% | 24.4% | 24.4% | 25.5% | Warning |
| ebsintsdr01 | App | 0.5% | 1.4% | 65.1% | 7.4% | 7.7% | 9.1% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintslp01 | App | 2.8% | 10.6% | 65.0% | 42.3% | 49.0% | 56.9% | 15.9% | 15.9% | 16.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 3,363 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.59%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
