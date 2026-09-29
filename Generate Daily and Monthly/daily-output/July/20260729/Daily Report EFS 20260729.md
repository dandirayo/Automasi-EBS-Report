# EFS DAILY HEALTH REPORT
**Periode:** 29 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260729.xlsx, EFS_Infrastructures_20260729.xlsx, EFS_XLA_20260729.xlsx, EFS_GL_20260729.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,469,139
- **XLA Success Rate:** 99.96%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,648
- **Infrastruktur Status:** 2 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,648 records. GL Posted mencapai 221,499 (99.75% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.96% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.75% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 134.30 | 134.30 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 73.10 | 73.10 | 100.00% | Healthy |
| Validate Application Accounting Definitions | 0 | 0.00 | 53.38 | 53.38 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 39.55 | 39.55 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 33.40 | 33.40 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 28.67 | 28.67 | 100.00% | Healthy |
| BNI GL Accrue Expense Generate | 0 | 0.00 | 21.84 | 21.84 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 20.33 | 20.33 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.10 | 5.10 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 2.83 | 2.83 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,469,139 | Volume total harian |
| Processed (P / XLA=S) | 2,462,491 | Sukses diproses (99.96%) |
| Unprocessed (U) | 6,648 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 222,044
- **FAH Success:** 222,042
- **FAH Error:** 2
- **Not Accounted:** 221,499
- **Posted GL:** 221,499 (99.75% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 221,261 | 2 | 220,736 | 220,736 | 0 |
| CROSS BORDER PAYMENT Custom Application | 510 | 0 | 510 | 510 | 0 |
| TRADE FINANCE Custom Application | 185 | 0 | 185 | 185 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 33 | 33 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,358,790 | 1,358,141 | 649 | 0.05% | 236,999,825,909,208.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 484,495 | 484,495 | 0 | 0.00% | 15,665,869,637,756.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 212,758 | 212,758 | 0 | 0.00% | 41,160,022,180,217.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 177,625 | 177,625 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 90,969 | 90,969 | 0 | 0.00% | 1,728,894,106.00 | Healthy |
| LON-Q_GLCP_GEND872 | 71,165 | 71,165 | 0 | 0.00% | -227,577,026.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 41,606 | 41,606 | 0 | 0.00% | 51,355,266,428,944.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,900 | 6,900 | 0 | 0.00% | 54,592,680,179,763.00 | Healthy |
| LON-NQ_ED2P_BORV | 5,909 | 2,330 | 3,579 | 60.57% | 3,828,398,679,736.00 | Critical |
| LON-Q_GLCP_LOND2140 | 5,778 | 5,778 | 0 | 0.00% | -40,620,317,247,870.00 | Healthy |

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
| ebsintslp01 | App | 4.4% | 24.7% | 71.3% | 0.0% | 0.0% | 0.0% | 18.1% | 18.1% | 19.0% | Warning |
| ebsintslp02 | App | 4.5% | 17.4% | 56.4% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 11.0% | Healthy |
| efsdbsdr01 | Database | 27.8% | 31.6% | 46.3% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 66.9% | Warning |
| efsdbsdr02 | Database | 3.5% | 10.8% | 19.5% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.5% | Healthy |
| efsdbslp01 | Database | 19.6% | 46.6% | 93.4% | 0.0% | 0.0% | 0.0% | 57.7% | 60.1% | 64.3% | Critical |
| efsdbslp02 | Database | 43.3% | 59.3% | 91.9% | 0.0% | 0.0% | 0.0% | 59.2% | 59.2% | 59.4% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,648 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.75%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
