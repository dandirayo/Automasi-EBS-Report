# EFS DAILY HEALTH REPORT
**Periode:** 8 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260908.xlsx, EFS_Infrastructures_20260908.xlsx, EFS_XLA_20260908.xlsx, EFS_GL_20260908.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,531,808
- **XLA Success Rate:** 99.26%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,058
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,058 records. GL Posted mencapai 222,688 (99.30% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.26% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.30% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,531,808 | Volume total harian |
| Processed (P / XLA=S) | 2,508,173 | Sukses diproses (99.26%) |
| Unprocessed (U) | 5,058 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 224,260
- **FAH Success:** 223,072
- **FAH Error:** 256
- **Not Accounted:** 222,696
- **Posted GL:** 222,688 (99.30% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 223,967 | 180 | 222,507 | 222,499 | 0 |
| TRADE FINANCE Custom Application | 131 | 0 | 124 | 124 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 53 | 0 | 34 | 34 | 0 |
| PREPAID SYSTEM Custom Application | 10 | 0 | 8 | 8 | 0 |
| TREASURY Custom Application | 9 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,387,061 | 1,386,366 | 695 | 0.05% | 162,010,941,539,219.41 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 489,374 | 489,374 | 0 | 0.00% | 16,181,146,058,096.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 225,351 | 225,351 | 0 | 0.00% | 42,637,819,583,868.64 | Healthy |
| DEP-Q_GLCP_GEND870 | 193,770 | 175,514 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 88,995 | 88,995 | 0 | 0.00% | 1,723,299,544.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,674 | 73,390 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,366 | 43,366 | 0 | 0.00% | 65,570,832,905,848.12 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,176 | 7,149 | 0 | 0.00% | 72,258,317,966,278.25 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,761 | 5,761 | 0 | 0.00% | -42,147,482,786,794.26 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,441 | 5,441 | 0 | 0.00% | 2,785,124,264,130.59 | Healthy |

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
| efsdbslp02 | Database | 17.2% | 33.5% | 81.1% | 58.5% | 60.6% | 67.0% | 51.0% | 51.0% | 51.1% | Critical |
| efsdbsdr01 | Database | 19.9% | 22.6% | 79.9% | 64.8% | 65.5% | 68.8% | 70.4% | 70.4% | 70.8% | Warning |
| efsdbsdr02 | Database | 1.1% | 4.2% | 14.5% | 50.0% | 50.6% | 51.4% | 43.6% | 43.6% | 43.7% | Healthy |
| ebsintslp02 | App | 3.4% | 14.2% | 98.6% | 45.0% | 46.9% | 51.7% | 10.7% | 10.8% | 11.0% | Critical |
| efsdbslp01 | Database | 8.7% | 35.6% | 97.5% | 56.1% | 58.9% | 63.5% | 50.4% | 57.0% | 65.5% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 84.4% | 7.0% | 7.2% | 8.1% | 41.3% | 41.3% | 42.1% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 81.0% | 6.8% | 6.9% | 8.2% | 24.4% | 24.4% | 25.2% | Critical |
| ebsintslp01 | App | 4.0% | 14.8% | 84.8% | 50.2% | 52.6% | 58.1% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,058 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.30%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
