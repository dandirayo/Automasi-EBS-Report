# EFS DAILY HEALTH REPORT
**Periode:** 7 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260707.xlsx, EFS_Infrastructures_20260707.xlsx, EFS_XLA_20260707.xlsx, EFS_GL_20260707.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,639,670
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,519
- **Infrastruktur Status:** 2 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,519 records. GL Posted mencapai 220,370 (99.80% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.80% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 690.58 | 690.58 | 100.00% | Critical |
| BNI GL Accrue Expense Generate | 0 | 0.00 | 341.08 | 341.08 | 100.00% | Healthy |
| Report Set | 0 | 0.00 | 120.13 | 120.13 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 39.34 | 39.34 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 25.66 | 25.66 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 25.29 | 25.29 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 22.58 | 22.58 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 7.70 | 7.70 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 2.78 | 2.78 | 100.00% | Healthy |
| Create Accounting - Cost Management | 0 | 0.00 | 2.42 | 2.42 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,639,670 | Volume total harian |
| Processed (P / XLA=S) | 2,635,151 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,519 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 220,812
- **FAH Success:** 220,808
- **FAH Error:** 4
- **Not Accounted:** 220,370
- **Posted GL:** 220,370 (99.80% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 220,234 | 4 | 219,812 | 219,812 | 0 |
| CROSS BORDER PAYMENT Custom Application | 415 | 0 | 415 | 415 | 0 |
| TRADE FINANCE Custom Application | 80 | 0 | 80 | 80 | 0 |
| CREDIT CARD Custom Application | 44 | 0 | 26 | 26 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,483,549 | 1,482,769 | 780 | 0.05% | 172,910,933,453,611.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 517,458 | 517,458 | 0 | 0.00% | 15,963,468,047,677.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 228,706 | 228,706 | 0 | 0.00% | 41,853,280,574,681.25 | Healthy |
| DEP-Q_GLCP_GEND870 | 178,274 | 178,274 | 0 | 0.00% | 1,956,522,084.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 94,201 | 94,201 | 0 | 0.00% | 1,646,312,186.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,938 | 67,938 | 0 | 0.00% | -3,090,413,465.22 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,412 | 46,412 | 0 | 0.00% | 43,930,325,884,014.21 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,574 | 7,574 | 0 | 0.00% | 50,602,977,928,381.78 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,935 | 4,935 | 0 | 0.00% | 2,419,327,874,919.63 | Healthy |
| LON-NQ_ED2P_BORV | 4,485 | 1,872 | 2,613 | 58.26% | 4,599,725,035,372.93 | Critical |

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
| ebsintsdr01 | App | 2.2% | 2.8% | 15.9% | 0.0% | 0.0% | 0.0% | 20.5% | 20.6% | 21.9% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.4% | 9.9% | 0.0% | 0.0% | 0.0% | 12.3% | 12.3% | 13.7% | Healthy |
| ebsintslp01 | App | 20.9% | 33.5% | 60.6% | 0.0% | 0.0% | 0.0% | 21.1% | 21.4% | 21.9% | Warning |
| ebsintslp02 | App | 4.2% | 12.3% | 33.9% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.1% | Healthy |
| efsdbsdr01 | Database | 53.9% | 60.5% | 81.2% | 0.0% | 0.0% | 0.0% | 66.0% | 66.2% | 66.2% | Critical |
| efsdbsdr02 | Database | 3.2% | 10.2% | 27.4% | 0.0% | 0.0% | 0.0% | 46.4% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 11.1% | 40.5% | 93.3% | 0.0% | 0.0% | 0.0% | 57.3% | 59.6% | 65.2% | Critical |
| efsdbslp02 | Database | 10.3% | 28.5% | 57.5% | 0.0% | 0.0% | 0.0% | 58.5% | 58.6% | 58.7% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,519 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.80%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
