# EFS DAILY HEALTH REPORT
**Periode:** 14 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260914.xlsx, EFS_Infrastructures_20260914.xlsx, EFS_XLA_20260914.xlsx, EFS_GL_20260914.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,045,888
- **XLA Success Rate:** 92.56%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 156,893
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 156,893 records. GL Posted mencapai 209,102 (99.37% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 92.56% | WARNING |
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
| Total Records | 2,045,888 | Volume total harian |
| Processed (P / XLA=S) | 1,888,995 | Sukses diproses (92.56%) |
| Unprocessed (U) | 156,893 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 210,421
- **FAH Success:** 209,478
- **FAH Error:** 76
- **Not Accounted:** 209,102
- **Posted GL:** 209,102 (99.37% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 210,197 | 0 | 209,010 | 209,010 | 0 |
| CROSS BORDER PAYMENT Custom Application | 78 | 0 | 78 | 78 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 54 | 0 | 0 | 0 | 0 |
| PREPAID SYSTEM Custom Application | 8 | 0 | 6 | 6 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,233,864 | 1,081,071 | 152,793 | 12.38% | 439,492,152,220,547.50 | Warning |
| DEP-NQ_ED2P_SC_BFST | 442,494 | 442,494 | 0 | 0.00% | 14,848,848,114,173.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 213,397 | 213,397 | 0 | 0.00% | 57,732,285,236,884.05 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 79,681 | 79,681 | 0 | 0.00% | 1,402,080,456.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,507 | 46,507 | 0 | 0.00% | 65,162,449,331,393.25 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,067 | 8,067 | 0 | 0.00% | 68,812,117,514,413.30 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,788 | 5,788 | 0 | 0.00% | -42,979,375,807,081.40 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,904 | 4,904 | 0 | 0.00% | 4,334,054,082,331.05 | Healthy |
| LON-NQ_ED2P_BORV | 4,659 | 1,919 | 2,740 | 58.81% | 6,215,250,854,958.48 | Critical |
| LON-Q_GLCP_BORV | 4,175 | 2,948 | 1,227 | 29.39% | 2,831,500,323,031.16 | Critical |

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
| efsdbslp02 | Database | 11.3% | 22.8% | 63.0% | 59.9% | 62.0% | 66.7% | 51.1% | 51.2% | 51.3% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.9% | 30.2% | 66.4% | 67.0% | 68.4% | 70.5% | 70.5% | 70.9% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.9% | 46.7% | 50.2% | 50.8% | 52.1% | 43.7% | 43.7% | 44.1% | Healthy |
| ebsintslp02 | App | 3.4% | 14.1% | 98.2% | 43.6% | 45.5% | 50.1% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 6.0% | 23.8% | 88.8% | 56.6% | 59.2% | 64.4% | 53.5% | 60.7% | 67.2% | Critical |
| ebsintsdr01 | App | 0.9% | 2.2% | 86.5% | 7.2% | 7.5% | 8.4% | 41.3% | 41.3% | 41.5% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 82.7% | 7.1% | 7.4% | 8.7% | 24.3% | 24.4% | 24.9% | Critical |
| ebsintslp01 | App | 3.9% | 14.1% | 84.1% | 49.7% | 52.2% | 59.6% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 156,893 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
