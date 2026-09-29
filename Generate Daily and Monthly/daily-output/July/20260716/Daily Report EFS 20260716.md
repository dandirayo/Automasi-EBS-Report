# EFS DAILY HEALTH REPORT
**Periode:** 16 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260716.xlsx, EFS_Infrastructures_20260716.xlsx, EFS_XLA_20260716.xlsx, EFS_GL_20260716.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,529,491
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,324
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,324 records. GL Posted mencapai 220,219 (99.79% intake).

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
| Gather Schema Statistics | 0 | 0.00 | 615.12 | 615.12 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 116.35 | 116.35 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 41.74 | 41.74 | 100.00% | Critical |
| Create Accounting - Cost Management | 0 | 0.00 | 39.90 | 39.90 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 36.15 | 36.15 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 34.26 | 34.26 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 30.54 | 30.54 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 22.42 | 22.42 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 4.27 | 4.27 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 3.11 | 3.11 | 100.00% | Critical |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,529,491 | Volume total harian |
| Processed (P / XLA=S) | 2,525,167 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,324 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 220,679
- **FAH Success:** 220,677
- **FAH Error:** 2
- **Not Accounted:** 220,219
- **Posted GL:** 220,219 (99.79% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 219,979 | 2 | 219,537 | 219,537 | 0 |
| CROSS BORDER PAYMENT Custom Application | 432 | 0 | 432 | 432 | 0 |
| TRADE FINANCE Custom Application | 185 | 0 | 185 | 185 | 0 |
| CREDIT CARD Custom Application | 46 | 0 | 30 | 30 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,402,260 | 1,401,534 | 726 | 0.05% | 162,281,718,008,463.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 505,460 | 505,460 | 0 | 0.00% | 14,614,238,290,558.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 222,485 | 222,485 | 0 | 0.00% | 36,273,432,407,840.17 | Healthy |
| DEP-Q_GLCP_GEND870 | 170,756 | 170,756 | 0 | 0.00% | 12,434,679.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 88,571 | 88,571 | 0 | 0.00% | 1,539,171,938.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,676 | 70,676 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,405 | 41,405 | 0 | 0.00% | 59,178,086,280,597.03 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,922 | 6,922 | 0 | 0.00% | 65,374,136,517,755.25 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,870 | 5,870 | 0 | 0.00% | -39,484,249,484,642.30 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,025 | 5,025 | 0 | 0.00% | 2,771,651,199,824.31 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.3% | 9.5% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 9.7% | 0.0% | 0.0% | 0.0% | 12.5% | 12.5% | 14.3% | Healthy |
| ebsintslp01 | App | 4.5% | 21.7% | 47.8% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.0% | Healthy |
| ebsintslp02 | App | 4.5% | 13.7% | 32.1% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.4% | Healthy |
| efsdbsdr01 | Database | 34.9% | 44.5% | 57.1% | 0.0% | 0.0% | 0.0% | 67.1% | 67.2% | 67.3% | Warning |
| efsdbsdr02 | Database | 3.2% | 10.1% | 17.6% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 24.2% | 44.4% | 90.5% | 0.0% | 0.0% | 0.0% | 57.7% | 60.2% | 63.5% | Critical |
| efsdbslp02 | Database | 23.8% | 35.3% | 71.2% | 0.0% | 0.0% | 0.0% | 58.9% | 59.0% | 59.0% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,324 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
