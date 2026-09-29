# EFS DAILY HEALTH REPORT
**Periode:** 26 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260926.xlsx, EFS_Infrastructures_20260926.xlsx, EFS_XLA_20260926.xlsx, EFS_GL_20260926.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,221,618
- **XLA Success Rate:** 73.29%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 198,207
- **Infrastruktur Status:** 2 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 198,207 records. GL Posted mencapai 88,333 (99.46% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 73.29% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.46% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,221,618 | Volume total harian |
| Processed (P / XLA=S) | 921,963 | Sukses diproses (73.29%) |
| Unprocessed (U) | 198,207 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 88,812
- **FAH Success:** 88,736
- **FAH Error:** 76
- **Not Accounted:** 88,333
- **Posted GL:** 88,333 (99.46% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 87,830 | 0 | 87,503 | 87,503 | 0 |
| CROSS BORDER PAYMENT Custom Application | 581 | 0 | 581 | 581 | 0 |
| TRADE FINANCE Custom Application | 227 | 0 | 223 | 223 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 72 | 0 | 0 | 0 | 0 |
| JOINT FINANCE Custom Application | 12 | 0 | 12 | 12 | 0 |
| TREASURY Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 633,385 | 435,216 | 198,169 | 31.29% | 17,714,538,656,482.83 | Critical |
| DEP-NQ_ED2P_SC_BFST | 217,075 | 137,653 | 0 | 0.00% | 10,288,621,306,523.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,930 | 196,930 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 80,406 | 80,406 | 0 | 0.00% | 4,618,067,200,031.35 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 48,763 | 27,732 | 0 | 0.00% | 1,292,887,404.00 | Healthy |
| LON-Q_GLCP_GEND872 | 38,706 | 38,706 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,156 | 2,306 | 0 | 0.00% | 59,267,179,437.13 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,240 | 2,239 | 1 | 0.04% | 19,820,759,550.46 | Healthy |
| BRA-NQ_ED2P_ELOG | 335 | 335 | 0 | 0.00% | 400,145,477,244.00 | Healthy |
| LON-Q_GLCP_BORV | 164 | 88 | 4 | 2.44% | 109,103,251,009.00 | Healthy |

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
| efsdbslp02 | Database | 9.5% | 16.9% | 64.0% | 61.5% | 62.1% | 62.9% | 51.6% | 51.7% | 51.7% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.9% | 28.6% | 69.9% | 70.1% | 71.1% | 70.7% | 70.7% | 71.0% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.8% | 9.8% | 50.4% | 50.9% | 51.8% | 43.8% | 43.9% | 43.9% | Healthy |
| ebsintslp02 | App | 2.6% | 6.0% | 99.2% | 44.0% | 44.3% | 45.9% | 10.8% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 11.3% | 21.0% | 85.2% | 58.4% | 59.1% | 60.4% | 45.9% | 55.0% | 65.8% | Critical |
| ebsintsdr01 | App | 0.5% | 1.5% | 65.7% | 7.3% | 7.6% | 9.1% | 41.3% | 41.3% | 41.7% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.9% | 7.2% | 7.4% | 8.9% | 24.4% | 24.4% | 24.8% | Warning |
| ebsintslp01 | App | 2.9% | 6.1% | 55.7% | 49.8% | 50.2% | 52.1% | 15.9% | 15.9% | 16.0% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 198,207 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.46%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
