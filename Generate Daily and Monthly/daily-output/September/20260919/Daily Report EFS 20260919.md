# EFS DAILY HEALTH REPORT
**Periode:** 19 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260919.xlsx, EFS_Infrastructures_20260919.xlsx, EFS_XLA_20260919.xlsx, EFS_GL_20260919.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,226,174
- **XLA Success Rate:** 99.99%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 502
- **Infrastruktur Status:** 2 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 502 records. GL Posted mencapai 106,873 (99.71% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.99% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.71% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,226,174 | Volume total harian |
| Processed (P / XLA=S) | 1,225,672 | Sukses diproses (99.99%) |
| Unprocessed (U) | 502 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 107,179
- **FAH Success:** 107,101
- **FAH Error:** 76
- **Not Accounted:** 106,874
- **Posted GL:** 106,873 (99.71% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 106,318 | 0 | 106,164 | 106,163 | 0 |
| CROSS BORDER PAYMENT Custom Application | 489 | 0 | 489 | 489 | 0 |
| TRADE FINANCE Custom Application | 203 | 0 | 197 | 197 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 69 | 0 | 0 | 0 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| TREASURY Custom Application | 9 | 0 | 9 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 602,874 | 602,385 | 489 | 0.08% | 17,230,949,928,513.23 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 213,406 | 213,406 | 0 | 0.00% | 9,267,884,439,517.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,830 | 194,830 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 84,300 | 84,300 | 0 | 0.00% | 3,907,416,476,116.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,858 | 73,858 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 46,182 | 46,182 | 0 | 0.00% | 1,131,566,378.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,833 | 5,833 | 0 | 0.00% | -42,428,304,261,273.61 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,110 | 2,110 | 0 | 0.00% | 12,511,865,497.54 | Healthy |
| DEP-NQ_ED2P_T_INVV | 1,720 | 1,720 | 0 | 0.00% | 41,577,437,502.26 | Healthy |
| BRA-NQ_ED2P_ELOG | 330 | 330 | 0 | 0.00% | 344,062,929,051.00 | Healthy |

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
| efsdbslp02 | Database | 8.5% | 16.3% | 66.7% | 60.4% | 61.1% | 62.4% | 51.4% | 51.4% | 51.5% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.0% | 28.9% | 67.5% | 67.9% | 68.2% | 70.5% | 70.6% | 71.0% | Warning |
| efsdbsdr02 | Database | 0.9% | 2.3% | 45.6% | 50.4% | 50.6% | 51.3% | 43.8% | 43.8% | 44.2% | Healthy |
| ebsintslp02 | App | 2.3% | 5.7% | 99.3% | 44.1% | 44.5% | 46.1% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 11.2% | 20.7% | 84.5% | 57.1% | 57.8% | 58.9% | 51.8% | 56.3% | 60.3% | Critical |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.3% | 7.2% | 7.3% | 8.8% | 24.4% | 24.4% | 25.4% | Warning |
| ebsintsdr01 | App | 0.6% | 1.6% | 65.4% | 7.2% | 7.5% | 8.8% | 41.2% | 41.3% | 42.4% | Warning |
| ebsintslp01 | App | 2.7% | 5.7% | 54.4% | 50.1% | 50.6% | 52.3% | 15.8% | 15.8% | 16.0% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 502 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.71%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
