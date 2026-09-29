# EFS DAILY HEALTH REPORT
**Periode:** 15 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260815.xlsx, EFS_Infrastructures_20260815.xlsx, EFS_XLA_20260815.xlsx, EFS_GL_20260815.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,280,599
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 788
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 788 records. GL Posted mencapai 198,030 (99.91% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.91% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,280,599 | Volume total harian |
| Processed (P / XLA=S) | 2,279,791 | Sukses diproses (100.00%) |
| Unprocessed (U) | 788 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 198,215
- **FAH Success:** 198,193
- **FAH Error:** 22
- **Not Accounted:** 198,030
- **Posted GL:** 198,030 (99.91% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 197,309 | 22 | 197,144 | 197,144 | 0 |
| CROSS BORDER PAYMENT Custom Application | 558 | 0 | 558 | 558 | 0 |
| TRADE FINANCE Custom Application | 186 | 0 | 186 | 186 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,300,638 | 1,299,855 | 783 | 0.06% | 22,637,840,958,156.76 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 366,349 | 366,349 | 0 | 0.00% | 11,330,630,806,116.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 211,256 | 211,256 | 0 | 0.00% | 5,819,917,506,452.45 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,310 | 195,310 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 120,352 | 120,352 | 0 | 0.00% | 2,977,488,467.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,788 | 72,788 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,886 | 5,886 | 0 | 0.00% | -36,425,263,407,790.40 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,520 | 3,520 | 0 | 0.00% | 59,252,967,342.62 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 3,008 | 3,008 | 0 | 0.00% | 21,589,179,641.30 | Healthy |
| BRA-NQ_ED2P_ELOG | 804 | 804 | 0 | 0.00% | 368,680,938,124.00 | Healthy |

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
| efsdbslp02 | Database | 16.2% | 32.4% | 93.6% | 51.7% | 52.1% | 52.9% | 50.4% | 50.4% | 50.5% | Critical |
| efsdbsdr01 | Database | 33.4% | 40.5% | 76.4% | 56.7% | 57.2% | 58.1% | 70.2% | 70.2% | 70.9% | Warning |
| efsdbsdr02 | Database | 2.5% | 8.2% | 29.7% | 49.7% | 50.0% | 50.8% | 43.4% | 43.4% | 43.5% | Healthy |
| ebsintslp02 | App | 3.2% | 16.4% | 92.9% | 43.3% | 43.9% | 45.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 9.6% | 23.5% | 88.2% | 50.5% | 50.9% | 51.9% | 44.7% | 52.4% | 61.4% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.5% | 5.2% | 5.4% | 6.6% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 86.2% | 5.4% | 5.6% | 6.5% | 41.2% | 41.2% | 41.7% | Critical |
| ebsintslp01 | App | 21.0% | 28.6% | 89.9% | 50.7% | 50.9% | 52.6% | 15.9% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 788 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.91%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
