# EFS DAILY HEALTH REPORT
**Periode:** 13 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260813.xlsx, EFS_Infrastructures_20260813.xlsx, EFS_XLA_20260813.xlsx, EFS_GL_20260813.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,341,208
- **XLA Success Rate:** 99.20%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,784
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,784 records. GL Posted mencapai 208,165 (99.68% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.20% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.68% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,341,208 | Volume total harian |
| Processed (P / XLA=S) | 2,317,648 | Sukses diproses (99.20%) |
| Unprocessed (U) | 4,784 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 208,833
- **FAH Success:** 208,594
- **FAH Error:** 219
- **Not Accounted:** 208,169
- **Posted GL:** 208,165 (99.68% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 208,081 | 219 | 207,437 | 207,433 | 4 |
| CROSS BORDER PAYMENT Custom Application | 421 | 0 | 421 | 421 | 0 |
| TRADE FINANCE Custom Application | 171 | 0 | 171 | 171 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 33 | 33 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,290,347 | 1,289,729 | 618 | 0.05% | 187,889,450,244,109.59 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 412,593 | 412,593 | 0 | 0.00% | 14,643,812,762,048.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 206,789 | 206,789 | 0 | 0.00% | 39,308,279,949,957.42 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,626 | 176,246 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,862 | 93,862 | 0 | 0.00% | 3,528,776,289.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,704 | 72,416 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,112 | 42,112 | 0 | 0.00% | 41,074,749,624,973.55 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,723 | 6,723 | 0 | 0.00% | 62,575,633,798,460.18 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,841 | 5,841 | 0 | 0.00% | -36,642,793,162,725.51 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,630 | 4,630 | 0 | 0.00% | 1,488,314,030,247.83 | Healthy |

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
| efsdbslp02 | Database | 28.9% | 49.3% | 92.3% | 51.3% | 54.2% | 58.6% | 50.3% | 50.4% | 50.8% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.1% | 76.8% | 56.1% | 56.6% | 59.1% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.5% | 11.4% | 51.8% | 49.6% | 50.1% | 51.0% | 43.4% | 43.4% | 43.8% | Healthy |
| ebsintslp02 | App | 36.7% | 53.4% | 97.5% | 44.0% | 46.3% | 50.9% | 10.7% | 10.7% | 10.9% | Critical |
| efsdbslp01 | Database | 17.5% | 49.0% | 98.0% | 50.5% | 53.0% | 57.6% | 48.4% | 57.8% | 63.2% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 85.3% | 5.1% | 5.5% | 6.4% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.2% | 5.0% | 5.3% | 6.6% | 24.3% | 24.3% | 25.0% | Critical |
| ebsintslp01 | App | 20.6% | 42.9% | 96.3% | 50.6% | 52.9% | 58.3% | 15.9% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,784 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.68%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
