# EFS DAILY HEALTH REPORT
**Periode:** 9 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260709.xlsx, EFS_Infrastructures_20260709.xlsx, EFS_XLA_20260709.xlsx, EFS_GL_20260709.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,484,959
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,282
- **Infrastruktur Status:** 2 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,282 records. GL Posted mencapai 224,453 (99.79% intake).

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
| Gather Schema Statistics | 0 | 0.00 | 708.47 | 708.47 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 104.16 | 104.16 | 100.00% | Critical |
| Validate Application Accounting Definitions | 0 | 0.00 | 56.22 | 56.22 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 36.36 | 36.36 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 24.81 | 24.81 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 24.75 | 24.75 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 23.26 | 23.26 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 8.44 | 8.44 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.70 | 5.70 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 3.27 | 3.27 | 100.00% | Critical |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,484,959 | Volume total harian |
| Processed (P / XLA=S) | 2,480,677 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,282 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 224,917
- **FAH Success:** 224,898
- **FAH Error:** 19
- **Not Accounted:** 224,453
- **Posted GL:** 224,453 (99.79% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 224,142 | 19 | 223,699 | 223,699 | 0 |
| CROSS BORDER PAYMENT Custom Application | 484 | 0 | 484 | 484 | 0 |
| TRADE FINANCE Custom Application | 208 | 0 | 208 | 208 | 0 |
| CREDIT CARD Custom Application | 45 | 0 | 26 | 26 | 0 |
| TREASURY Custom Application | 15 | 0 | 15 | 15 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,376,295 | 1,375,623 | 672 | 0.05% | 246,139,552,056,221.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 503,629 | 503,629 | 0 | 0.00% | 14,959,153,685,609.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 205,278 | 205,278 | 0 | 0.00% | 53,675,952,114,804.38 | Healthy |
| DEP-Q_GLCP_GEND870 | 180,094 | 180,094 | 0 | 0.00% | -23,216,832,079.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 91,395 | 91,395 | 0 | 0.00% | 1,526,718,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,932 | 68,932 | 0 | 0.00% | -8,305,096.72 | Healthy |
| DEP-NQ_ED2P_T_INVV | 37,709 | 37,709 | 0 | 0.00% | 52,880,194,209,187.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 4,959 | 4,959 | 0 | 0.00% | -35,580,609,191,862.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,893 | 4,893 | 0 | 0.00% | 3,318,485,164,985.64 | Healthy |
| LON-NQ_ED2P_BORV | 3,893 | 1,579 | 2,314 | 59.44% | 3,586,066,753,714.88 | Critical |

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
| ebsintsdr01 | App | 2.3% | 2.9% | 10.7% | 0.0% | 0.0% | 0.0% | 20.6% | 20.6% | 22.2% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.5% | 14.8% | 0.0% | 0.0% | 0.0% | 12.3% | 12.4% | 13.3% | Healthy |
| ebsintslp01 | App | 3.6% | 17.0% | 34.9% | 0.0% | 0.0% | 0.0% | 22.4% | 22.8% | 23.1% | Healthy |
| ebsintslp02 | App | 4.4% | 13.8% | 100.0% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.8% | Critical |
| efsdbsdr01 | Database | 54.0% | 62.2% | 78.2% | 0.0% | 0.0% | 0.0% | 66.3% | 66.4% | 66.5% | Warning |
| efsdbsdr02 | Database | 3.2% | 6.1% | 16.8% | 0.0% | 0.0% | 0.0% | 46.4% | 46.4% | 46.5% | Healthy |
| efsdbslp01 | Database | 17.8% | 41.2% | 95.4% | 0.0% | 0.0% | 0.0% | 57.9% | 62.3% | 65.4% | Critical |
| efsdbslp02 | Database | 19.5% | 39.0% | 65.3% | 0.0% | 0.0% | 0.0% | 58.7% | 58.7% | 58.8% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,282 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
