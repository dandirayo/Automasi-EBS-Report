# EFS DAILY HEALTH REPORT
**Periode:** 22 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260722.xlsx, EFS_Infrastructures_20260722.xlsx, EFS_XLA_20260722.xlsx, EFS_GL_20260722.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,427,419
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 757
- **Infrastruktur Status:** 1 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 757 records. GL Posted mencapai 209,254 (99.88% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.88% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Validate Application Accounting Definitions | 0 | 0.00 | 161.70 | 161.70 | 100.00% | Healthy |
| Report Set | 0 | 0.00 | 123.74 | 123.74 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 121.51 | 121.51 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 32.73 | 32.73 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 30.90 | 30.90 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 25.22 | 25.22 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 21.80 | 21.80 | 100.00% | Healthy |
| Subledger Period Close Exceptions Report | 0 | 0.00 | 14.75 | 14.75 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 5.93 | 5.93 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 4.84 | 4.84 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,427,419 | Volume total harian |
| Processed (P / XLA=S) | 2,426,662 | Sukses diproses (100.00%) |
| Unprocessed (U) | 757 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 209,495
- **FAH Success:** 209,493
- **FAH Error:** 2
- **Not Accounted:** 209,254
- **Posted GL:** 209,254 (99.88% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 208,797 | 2 | 208,574 | 208,574 | 0 |
| CROSS BORDER PAYMENT Custom Application | 419 | 0 | 419 | 419 | 0 |
| TRADE FINANCE Custom Application | 195 | 0 | 195 | 195 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| PREPAID SYSTEM Custom Application | 7 | 0 | 7 | 7 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,365,536 | 1,364,904 | 632 | 0.05% | 203,087,576,318,345.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 488,380 | 488,380 | 0 | 0.00% | 14,223,112,618,477.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 216,376 | 216,376 | 0 | 0.00% | 38,750,158,938,481.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,085 | 182,085 | 0 | 0.00% | -1,512,601.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,785 | 68,785 | 0 | 0.00% | 687,103,456.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 54,705 | 54,705 | 0 | 0.00% | 970,324,804.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 38,402 | 38,402 | 0 | 0.00% | 26,540,286,122,098.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,874 | 6,874 | 0 | 0.00% | 61,643,554,758,313.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,505 | 4,505 | 0 | 0.00% | 2,159,537,020,159.00 | Healthy |
| BRA-NQ_ED2P_ELOG | 783 | 783 | 0 | 0.00% | 293,611,196,525.00 | Healthy |

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
| ebsintsdr01 | App | 1.2% | 2.2% | 9.5% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.4% | 15.0% | 0.0% | 0.0% | 0.0% | 0.0% | 12.6% | 13.6% | Healthy |
| ebsintslp01 | App | 4.4% | 15.1% | 35.0% | 0.0% | 0.0% | 0.0% | 18.0% | 18.0% | 18.0% | Healthy |
| ebsintslp02 | App | 4.5% | 14.8% | 64.2% | 0.0% | 0.0% | 0.0% | 0.0% | 10.0% | 10.2% | Warning |
| efsdbsdr01 | Database | 35.1% | 47.3% | 60.7% | 0.0% | 0.0% | 0.0% | 67.8% | 67.9% | 68.0% | Warning |
| efsdbsdr02 | Database | 3.4% | 10.3% | 32.1% | 0.0% | 0.0% | 0.0% | 46.5% | 46.6% | 46.7% | Healthy |
| efsdbslp01 | Database | 16.5% | 40.8% | 84.0% | 0.0% | 0.0% | 0.0% | 58.6% | 62.3% | 64.9% | Critical |
| efsdbslp02 | Database | 18.8% | 39.1% | 78.3% | 0.0% | 0.0% | 0.0% | 59.0% | 59.1% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 757 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.88%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
