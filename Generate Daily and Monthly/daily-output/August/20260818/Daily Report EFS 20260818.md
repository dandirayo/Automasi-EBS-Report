# EFS DAILY HEALTH REPORT
**Periode:** 18 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260818.xlsx, EFS_Infrastructures_20260818.xlsx, EFS_XLA_20260818.xlsx, EFS_GL_20260818.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,507,796
- **XLA Success Rate:** 48.51%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,055
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,055 records. GL Posted mencapai 215,022 (94.43% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 48.51% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 94.43% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,507,796 | Volume total harian |
| Processed (P / XLA=S) | 1,215,732 | Sukses diproses (48.51%) |
| Unprocessed (U) | 1,055 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 227,713
- **FAH Success:** 215,140
- **FAH Error:** 505
- **Not Accounted:** 215,022
- **Posted GL:** 215,022 (94.43% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 227,350 | 505 | 214,673 | 214,673 | 0 |
| CROSS BORDER PAYMENT Custom Application | 218 | 0 | 218 | 218 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 42 | 0 | 30 | 30 | 0 |
| TREASURY Custom Application | 10 | 0 | 10 | 10 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,361,327 | 438,676 | 255 | 0.02% | 255,212,561,155,523.56 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 483,146 | 218,754 | 0 | 0.00% | 16,116,548,444,867.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 229,239 | 229,239 | 0 | 0.00% | 69,071,926,114,800.13 | Healthy |
| DEP-Q_GLCP_GEND870 | 193,696 | 175,078 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 89,169 | 36,475 | 0 | 0.00% | 1,689,339,878.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,772 | 72,484 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 48,107 | 25,955 | 0 | 0.00% | 63,630,410,262,027.71 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,743 | 8,743 | 0 | 0.00% | 72,803,110,846,561.98 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,887 | 5,887 | 0 | 0.00% | -36,378,551,385,159.40 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,262 | 1,386 | 0 | 0.00% | 4,335,257,613,376.91 | Healthy |

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
| efsdbslp02 | Database | 29.3% | 46.5% | 92.2% | 53.4% | 55.4% | 58.9% | 50.3% | 50.4% | 50.7% | Critical |
| efsdbsdr01 | Database | 33.3% | 40.9% | 76.2% | 57.7% | 58.2% | 59.0% | 70.2% | 70.2% | 70.9% | Warning |
| efsdbsdr02 | Database | 2.6% | 8.5% | 29.9% | 49.7% | 50.0% | 50.8% | 43.4% | 43.5% | 43.5% | Healthy |
| efsdbslp01 | Database | 10.1% | 37.4% | 92.5% | 51.5% | 53.9% | 58.8% | 53.3% | 57.2% | 64.4% | Critical |
| ebsintslp02 | App | 3.2% | 13.3% | 98.7% | 43.7% | 46.8% | 53.9% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 82.0% | 5.4% | 5.5% | 6.9% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 87.7% | 5.6% | 5.7% | 6.6% | 41.2% | 41.2% | 42.0% | Critical |
| ebsintslp01 | App | 4.0% | 16.2% | 99.2% | 50.7% | 54.1% | 61.0% | 15.8% | 15.9% | 16.0% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,055 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 94.43%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
