# EFS DAILY HEALTH REPORT
**Periode:** 27 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260827.xlsx, EFS_Infrastructures_20260827.xlsx, EFS_XLA_20260827.xlsx, EFS_GL_20260827.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,523,075
- **XLA Success Rate:** 99.21%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,582
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,582 records. GL Posted mencapai 224,349 (99.63% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.21% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.63% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,523,075 | Volume total harian |
| Processed (P / XLA=S) | 2,497,258 | Sukses diproses (99.21%) |
| Unprocessed (U) | 6,582 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 225,177
- **FAH Success:** 224,877
- **FAH Error:** 210
- **Not Accounted:** 224,373
- **Posted GL:** 224,349 (99.63% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 224,199 | 134 | 223,493 | 223,469 | 0 |
| CROSS BORDER PAYMENT Custom Application | 612 | 0 | 612 | 612 | 0 |
| TRADE FINANCE Custom Application | 204 | 0 | 202 | 202 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 31 | 31 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| TREASURY Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,371,157 | 1,370,287 | 870 | 0.06% | 229,479,098,865,670.84 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 491,487 | 491,487 | 0 | 0.00% | 17,162,202,417,036.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 224,952 | 224,952 | 0 | 0.00% | 45,033,224,342,623.35 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,250 | 177,320 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 89,216 | 89,216 | 0 | 0.00% | 1,842,260,382.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,178 | 72,896 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,920 | 43,920 | 0 | 0.00% | 52,652,657,926,206.08 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,458 | 7,458 | 0 | 0.00% | 54,481,946,216,590.82 | Healthy |
| LON-NQ_ED2P_BORV | 6,145 | 2,488 | 3,657 | 59.51% | 4,981,489,513,576.87 | Critical |
| LON-Q_GLCP_BORV | 5,774 | 3,859 | 1,915 | 33.17% | 6,907,677,341,825.13 | Critical |

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
| efsdbslp02 | Database | 29.1% | 56.4% | 96.1% | 56.3% | 58.6% | 62.6% | 50.5% | 50.6% | 50.8% | Critical |
| efsdbsdr01 | Database | 39.5% | 44.3% | 79.5% | 61.0% | 61.5% | 62.3% | 70.2% | 70.2% | 70.8% | Warning |
| efsdbsdr02 | Database | 2.8% | 9.3% | 38.8% | 49.9% | 50.2% | 51.2% | 43.5% | 43.5% | 43.6% | Healthy |
| ebsintslp02 | App | 3.8% | 16.5% | 98.9% | 41.5% | 44.0% | 49.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 20.4% | 55.5% | 99.1% | 53.7% | 56.2% | 60.6% | 52.1% | 57.9% | 78.4% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.4% | 6.0% | 6.1% | 7.4% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.1% | 6.2% | 6.4% | 7.4% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.0% | 16.1% | 85.2% | 46.9% | 49.6% | 55.2% | 15.8% | 15.8% | 15.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,582 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.63%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
