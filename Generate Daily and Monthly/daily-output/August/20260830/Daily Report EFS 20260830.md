# EFS DAILY HEALTH REPORT
**Periode:** 30 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260830.xlsx, EFS_Infrastructures_20260830.xlsx, EFS_XLA_20260830.xlsx, EFS_GL_20260830.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,227,346
- **XLA Success Rate:** 94.42%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 124,651
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 124,651 records. GL Posted mencapai 192,810 (99.50% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 94.42% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.50% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,227,346 | Volume total harian |
| Processed (P / XLA=S) | 2,102,695 | Sukses diproses (94.42%) |
| Unprocessed (U) | 124,651 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 193,773
- **FAH Success:** 192,937
- **FAH Error:** 78
- **Not Accounted:** 192,810
- **Posted GL:** 192,810 (99.50% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 193,521 | 2 | 192,636 | 192,636 | 0 |
| CROSS BORDER PAYMENT Custom Application | 129 | 0 | 129 | 129 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 27 | 0 | 27 | 27 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 3 | 0 | 3 | 3 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,201,473 | 1,076,825 | 124,648 | 10.37% | 17,260,170,002,664.05 | Warning |
| DEP-NQ_ED2P_SC_BFST | 449,707 | 449,707 | 0 | 0.00% | 9,732,265,874,698.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 206,509 | 206,509 | 0 | 0.00% | 4,479,055,100,280.60 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,845 | 196,845 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 87,017 | 87,017 | 0 | 0.00% | 1,481,577,382.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,796 | 72,796 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,673 | 5,673 | 0 | 0.00% | -36,309,725,515,362.70 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,515 | 3,515 | 0 | 0.00% | 74,107,943,554.12 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,452 | 2,452 | 0 | 0.00% | 7,472,486,024.83 | Healthy |
| BRA-NQ_ED2P_ELOG | 867 | 867 | 0 | 0.00% | 359,965,397,940.00 | Healthy |

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
| efsdbslp02 | Database | 28.9% | 41.7% | 88.2% | 57.1% | 57.5% | 58.3% | 50.6% | 50.7% | 50.7% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.0% | 77.0% | 61.7% | 62.1% | 63.1% | 70.3% | 70.3% | 70.5% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.3% | 27.2% | 50.0% | 50.2% | 51.1% | 43.5% | 43.6% | 43.6% | Healthy |
| ebsintslp02 | App | 3.6% | 8.5% | 98.5% | 42.6% | 43.0% | 44.5% | 10.7% | 10.7% | 11.0% | Critical |
| efsdbslp01 | Database | 16.5% | 32.7% | 96.4% | 54.3% | 54.9% | 56.6% | 46.3% | 50.7% | 55.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 82.5% | 6.0% | 6.3% | 7.6% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.9% | 6.4% | 6.5% | 7.5% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.0% | 8.0% | 71.5% | 47.3% | 47.6% | 49.0% | 15.8% | 15.8% | 16.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 124,651 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.50%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
