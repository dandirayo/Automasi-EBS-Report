# EFS DAILY HEALTH REPORT
**Periode:** 23 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260923.xlsx, EFS_Infrastructures_20260923.xlsx, EFS_XLA_20260923.xlsx, EFS_GL_20260923.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,787,834
- **XLA Success Rate:** 84.33%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 186,728
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 186,728 records. GL Posted mencapai 154,305 (99.60% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 84.33% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.60% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,787,834 | Volume total harian |
| Processed (P / XLA=S) | 1,503,069 | Sukses diproses (84.33%) |
| Unprocessed (U) | 186,728 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 154,924
- **FAH Success:** 154,728
- **FAH Error:** 196
- **Not Accounted:** 154,305
- **Posted GL:** 154,305 (99.60% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 154,558 | 120 | 154,087 | 154,087 | 0 |
| TRADE FINANCE Custom Application | 199 | 0 | 198 | 198 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 71 | 0 | 0 | 0 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |
| JOINT FINANCE Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 930,215 | 747,592 | 182,623 | 19.63% | 156,862,571,344,499.59 | Warning |
| DEP-NQ_ED2P_SC_BFST | 320,771 | 257,632 | 0 | 0.00% | 13,791,905,465,741.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,800 | 176,744 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 140,092 | 140,092 | 0 | 0.00% | 36,367,244,697,024.43 | Healthy |
| LON-Q_GLCP_GEND872 | 73,944 | 73,654 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 64,348 | 50,334 | 0 | 0.00% | 1,388,607,101.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 34,893 | 34,230 | 0 | 0.00% | 55,275,858,941,149.06 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,853 | 5,853 | 0 | 0.00% | -43,033,894,838,202.29 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,782 | 5,782 | 0 | 0.00% | 58,922,671,585,262.62 | Healthy |
| LON-NQ_ED2P_BORV | 4,829 | 1,765 | 2,615 | 54.15% | 14,504,102,376,630.16 | Critical |

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
| efsdbslp02 | Database | 10.6% | 39.3% | 90.1% | 61.0% | 63.5% | 67.3% | 51.5% | 51.6% | 51.6% | Critical |
| efsdbsdr01 | Database | 13.4% | 15.0% | 28.6% | 68.9% | 69.4% | 70.7% | 70.6% | 70.6% | 71.0% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.9% | 48.2% | 50.4% | 50.8% | 52.3% | 43.8% | 43.8% | 44.2% | Healthy |
| ebsintslp02 | App | 2.5% | 11.0% | 97.9% | 26.8% | 46.5% | 52.5% | 10.7% | 10.8% | 10.9% | Critical |
| efsdbslp01 | Database | 11.4% | 43.8% | 94.9% | 58.3% | 60.6% | 65.0% | 48.8% | 57.6% | 63.9% | Critical |
| ebsintsdr01 | App | 0.6% | 1.4% | 65.8% | 7.4% | 7.6% | 9.0% | 41.3% | 41.3% | 41.7% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 63.2% | 7.2% | 7.4% | 8.8% | 24.4% | 24.4% | 24.6% | Warning |
| ebsintslp01 | App | 2.7% | 10.8% | 70.3% | 32.8% | 52.5% | 58.0% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 186,728 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.60%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
