# EFS DAILY HEALTH REPORT
**Periode:** 15 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260715.xlsx, EFS_Infrastructures_20260715.xlsx, EFS_XLA_20260715.xlsx, EFS_GL_20260715.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,884,394
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 2,823
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 2,823 records. GL Posted mencapai 219,293 (99.79% intake).

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
| Gather Schema Statistics | 0 | 0.00 | 576.55 | 576.55 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 160.57 | 160.57 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 60.73 | 60.73 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 42.59 | 42.59 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 42.22 | 42.22 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 41.32 | 41.32 | 100.00% | Critical |
| Create Accounting - Receiving | 0 | 0.00 | 37.80 | 37.80 | 100.00% | Healthy |
| Create Accounting - Cost Management | 0 | 0.00 | 36.42 | 36.42 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 33.57 | 33.57 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 30.95 | 30.95 | 100.00% | Critical |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,884,394 | Volume total harian |
| Processed (P / XLA=S) | 1,881,571 | Sukses diproses (100.00%) |
| Unprocessed (U) | 2,823 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 219,758
- **FAH Success:** 219,756
- **FAH Error:** 2
- **Not Accounted:** 219,293
- **Posted GL:** 219,293 (99.79% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 219,002 | 2 | 218,556 | 218,556 | 0 |
| CROSS BORDER PAYMENT Custom Application | 449 | 0 | 449 | 449 | 0 |
| TRADE FINANCE Custom Application | 224 | 0 | 224 | 224 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 32 | 32 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| TREASURY Custom Application | 11 | 0 | 11 | 11 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 974,359 | 973,704 | 655 | 0.07% | 265,475,084,916,917.09 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 325,480 | 325,480 | 0 | 0.00% | 10,270,136,523,650.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 212,973 | 212,973 | 0 | 0.00% | 60,555,298,225,761.97 | Healthy |
| DEP-Q_GLCP_GEND870 | 183,400 | 183,400 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_GEND872 | 69,547 | 69,547 | 0 | 0.00% | -49,853,780.15 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 54,052 | 54,052 | 0 | 0.00% | 941,298,792.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,354 | 41,354 | 0 | 0.00% | 29,361,095,476,557.66 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,612 | 6,612 | 0 | 0.00% | 45,900,355,345,250.22 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,863 | 5,863 | 0 | 0.00% | -40,399,519,431,276.98 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 3,938 | 3,937 | 1 | 0.03% | 2,392,970,949,242.83 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.2% | 10.0% | 0.0% | 0.0% | 0.0% | 21.4% | 21.5% | 22.8% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 13.6% | 0.0% | 0.0% | 0.0% | 12.4% | 12.5% | 14.1% | Healthy |
| ebsintslp01 | App | 21.5% | 28.8% | 47.3% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 17.9% | Healthy |
| ebsintslp02 | App | 4.4% | 15.8% | 41.3% | 0.0% | 0.0% | 0.0% | 9.8% | 9.9% | 9.9% | Healthy |
| efsdbsdr01 | Database | 34.8% | 40.9% | 58.8% | 0.0% | 0.0% | 0.0% | 67.0% | 67.1% | 67.2% | Warning |
| efsdbsdr02 | Database | 3.3% | 5.6% | 21.2% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 18.7% | 35.9% | 72.7% | 0.0% | 0.0% | 0.0% | 56.7% | 58.9% | 63.0% | Warning |
| efsdbslp02 | Database | 16.6% | 38.0% | 84.0% | 0.0% | 0.0% | 0.0% | 58.9% | 59.0% | 59.0% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 2,823 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
