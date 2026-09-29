# EFS DAILY HEALTH REPORT
**Periode:** 4 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260804.xlsx, EFS_Infrastructures_20260804.xlsx, EFS_XLA_20260804.xlsx, EFS_GL_20260804.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,057,404
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,846
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,846 records. GL Posted mencapai 229,939 (99.79% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.79% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,057,404 | Volume total harian |
| Processed (P / XLA=S) | 3,034,556 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,846 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 230,413
- **FAH Success:** 230,411
- **FAH Error:** 2
- **Not Accounted:** 229,939
- **Posted GL:** 229,939 (99.79% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,354 | 2 | 228,902 | 228,902 | 0 |
| CROSS BORDER PAYMENT Custom Application | 547 | 0 | 547 | 547 | 0 |
| PSAK 71 Custom Application | 225 | 0 | 222 | 222 | 0 |
| TRADE FINANCE Custom Application | 198 | 0 | 198 | 198 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,505,238 | 1,496,498 | 8,740 | 0.58% | 194,100,628,912,357.38 | Warning |
| DEP-NQ_ED2P_SC_BFST | 535,714 | 535,714 | 0 | 0.00% | 16,849,352,725,907.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 415,178 | 415,046 | 132 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 242,455 | 242,452 | 3 | 0.00% | 73,018,253,775,145.42 | Healthy |
| LON-Q_GLCP_GEND872 | 148,934 | 148,934 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 96,638 | 96,638 | 0 | 0.00% | 1,742,726,841.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,899 | 46,899 | 0 | 0.00% | 58,442,465,952,506.28 | Healthy |
| LON-NQ_ED2P_BORV | 16,043 | 5,403 | 10,640 | 66.32% | 4,678,960,822,359.41 | Critical |
| LON-Q_GLCP_GLIF | 11,823 | 11,577 | 246 | 2.08% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,611 | 11,611 | 0 | 0.00% | 1,148,016,022,538.16 | Healthy |

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
| efsdbslp02 | Database | 11.2% | 31.8% | 86.3% | 48.5% | 50.5% | 56.3% | 50.4% | 50.5% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.0% | 74.9% | 52.4% | 52.8% | 53.5% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.6% | 10.6% | 34.5% | 49.0% | 49.4% | 50.2% | 43.3% | 43.3% | 43.3% | Healthy |
| efsdbslp01 | Database | 3.6% | 36.9% | 92.7% | 49.6% | 51.8% | 56.3% | 49.3% | 56.2% | 63.3% | Critical |
| ebsintslp02 | App | 3.4% | 15.2% | 89.0% | 42.8% | 45.2% | 50.0% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintslp01 | App | 3.8% | 14.4% | 80.7% | 50.0% | 52.0% | 57.1% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,846 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.79%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
