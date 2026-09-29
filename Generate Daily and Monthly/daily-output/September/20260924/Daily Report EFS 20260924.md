# EFS DAILY HEALTH REPORT
**Periode:** 24 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260924.xlsx, EFS_Infrastructures_20260924.xlsx, EFS_XLA_20260924.xlsx, EFS_GL_20260924.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,765,117
- **XLA Success Rate:** 80.03%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 3,370
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 3,370 records. GL Posted mencapai 118,086 (83.62% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 80.03% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 83.62% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,765,117 | Volume total harian |
| Processed (P / XLA=S) | 1,441,776 | Sukses diproses (80.03%) |
| Unprocessed (U) | 3,370 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 141,222
- **FAH Success:** 116,997
- **FAH Error:** 1,055
- **Not Accounted:** 139,378
- **Posted GL:** 118,086 (83.62% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 140,354 | 979 | 138,655 | 117,363 | 0 |
| CROSS BORDER PAYMENT Custom Application | 512 | 0 | 512 | 512 | 0 |
| TRADE FINANCE Custom Application | 176 | 0 | 176 | 176 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 69 | 0 | 0 | 0 | 0 |
| JOINT FINANCE Custom Application | 18 | 0 | 18 | 18 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 913,535 | 706,975 | 502 | 0.05% | 213,679,988,610,895.28 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 318,648 | 250,040 | 0 | 0.00% | 13,394,708,994,302.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,926 | 176,842 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 146,665 | 146,665 | 0 | 0.00% | 30,854,155,306,374.84 | Healthy |
| LON-Q_GLCP_GEND872 | 73,950 | 73,670 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 59,945 | 43,271 | 0 | 0.00% | 1,283,329,853.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 34,073 | 32,885 | 0 | 0.00% | 68,370,972,326,344.81 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,521 | 5,059 | 0 | 0.00% | 71,175,156,936,421.06 | Healthy |
| LON-NQ_ED2P_BORV | 5,082 | 1,278 | 1,826 | 35.93% | 4,469,703,218,479.90 | Critical |
| LON-Q_GLCP_BORV | 4,958 | 1,933 | 947 | 19.10% | 5,543,905,948,372.72 | Warning |

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
| efsdbslp02 | Database | 10.7% | 37.5% | 87.3% | 61.3% | 63.4% | 68.4% | 51.6% | 51.6% | 51.7% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.9% | 30.6% | 69.2% | 69.6% | 71.4% | 70.6% | 70.6% | 70.7% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.7% | 42.7% | 50.5% | 50.9% | 51.8% | 43.8% | 43.8% | 44.2% | Healthy |
| ebsintslp02 | App | 2.4% | 10.6% | 98.6% | 27.2% | 41.5% | 50.2% | 10.7% | 10.8% | 10.9% | Critical |
| efsdbslp01 | Database | 9.3% | 43.4% | 95.4% | 58.1% | 61.0% | 66.2% | 52.0% | 59.5% | 64.8% | Critical |
| ebsintsdr01 | App | 0.6% | 1.4% | 65.6% | 7.5% | 7.6% | 9.0% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.6% | 7.1% | 7.4% | 8.8% | 24.4% | 24.4% | 24.9% | Warning |
| ebsintslp01 | App | 2.8% | 10.5% | 68.0% | 32.8% | 47.8% | 57.6% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 3,370 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 83.62%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
