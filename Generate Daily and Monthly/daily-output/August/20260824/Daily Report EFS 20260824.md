# EFS DAILY HEALTH REPORT
**Periode:** 24 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260824.xlsx, EFS_Infrastructures_20260824.xlsx, EFS_XLA_20260824.xlsx, EFS_GL_20260824.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,644,409
- **XLA Success Rate:** 99.27%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,550
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,550 records. GL Posted mencapai 232,429 (99.68% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.27% | WARNING |
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
| Total Records | 2,644,409 | Volume total harian |
| Processed (P / XLA=S) | 2,619,651 | Sukses diproses (99.27%) |
| Unprocessed (U) | 5,550 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 233,172
- **FAH Success:** 232,913
- **FAH Error:** 236
- **Not Accounted:** 232,439
- **Posted GL:** 232,429 (99.68% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 232,967 | 160 | 232,312 | 232,302 | 0 |
| CROSS BORDER PAYMENT Custom Application | 80 | 0 | 80 | 80 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 38 | 0 | 38 | 38 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,451,306 | 1,450,633 | 673 | 0.05% | 259,090,949,868,399.69 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 507,747 | 507,747 | 0 | 0.00% | 20,077,140,957,139.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 234,765 | 234,765 | 0 | 0.00% | 66,616,031,832,758.99 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,253 | 176,363 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 97,342 | 97,342 | 0 | 0.00% | 2,670,557,307.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,864 | 72,584 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 51,073 | 51,073 | 0 | 0.00% | 64,510,704,596,223.37 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,821 | 8,821 | 0 | 0.00% | 71,929,478,042,690.41 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 6,063 | 6,062 | 1 | 0.02% | 1,836,238,634,764.90 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,889 | 5,889 | 0 | 0.00% | -37,660,201,006,091.43 | Healthy |

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
| efsdbslp02 | Database | 30.5% | 51.7% | 93.0% | 55.6% | 57.4% | 61.0% | 50.4% | 50.5% | 50.7% | Critical |
| efsdbsdr01 | Database | 33.4% | 40.7% | 78.2% | 59.6% | 60.1% | 61.2% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.4% | 28.7% | 49.9% | 50.1% | 51.0% | 43.5% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 3.4% | 22.9% | 99.1% | 40.7% | 42.5% | 46.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 16.4% | 44.6% | 97.8% | 53.0% | 55.2% | 59.6% | 50.6% | 57.2% | 66.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.1% | 5.8% | 6.0% | 7.3% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 86.3% | 6.0% | 6.2% | 6.6% | 41.2% | 41.2% | 41.7% | Critical |
| ebsintslp01 | App | 4.1% | 16.5% | 89.5% | 47.1% | 49.4% | 55.2% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,550 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
