# EFS DAILY HEALTH REPORT
**Periode:** 2 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260702.xlsx, EFS_Infrastructures_20260702.xlsx, EFS_XLA_20260702.xlsx, EFS_GL_20260702.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 1,610,121
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,532
- **Infrastruktur Status:** 0 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,532 records. GL Posted mencapai 185,210 (99.77% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.77% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Depreciation Run | 0 | 0.00 | 612.28 | 612.28 | 100.00% | Healthy |
| Report Set | 0 | 0.00 | 127.82 | 127.82 | 100.00% | Critical |
| Validate Application Accounting Definitions | 0 | 0.00 | 57.17 | 57.17 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 40.51 | 40.51 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 23.31 | 23.31 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 22.89 | 22.89 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 18.50 | 18.50 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 8.96 | 8.96 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 6.06 | 6.06 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 2.97 | 2.97 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,610,121 | Volume total harian |
| Processed (P / XLA=S) | 1,605,589 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,532 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 185,642
- **FAH Success:** 185,636
- **FAH Error:** 6
- **Not Accounted:** 185,210
- **Posted GL:** 185,210 (99.77% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 184,811 | 6 | 184,399 | 184,399 | 0 |
| CROSS BORDER PAYMENT Custom Application | 468 | 0 | 468 | 468 | 0 |
| TRADE FINANCE Custom Application | 203 | 0 | 203 | 203 | 0 |
| CREDIT CARD Custom Application | 137 | 0 | 119 | 119 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |
| TREASURY Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 841,705 | 840,398 | 1,307 | 0.16% | 192,151,229,102,961.03 | Warning |
| DEP-NQ_ED2P_SC_BFST | 276,541 | 276,541 | 0 | 0.00% | 13,630,244,000,874.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,775 | 181,775 | 0 | 0.00% | 5,298.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 115,010 | 115,010 | 0 | 0.00% | 37,121,967,725,051.44 | Healthy |
| LON-Q_GLCP_GEND872 | 69,121 | 69,121 | 0 | 0.00% | -98,430,438.52 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 62,542 | 62,542 | 0 | 0.00% | 1,465,441,627.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 38,384 | 38,384 | 0 | 0.00% | 35,900,043,895,202.70 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,458 | 6,458 | 0 | 0.00% | 41,691,005,213,802.17 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,745 | 5,745 | 0 | 0.00% | -41,283,481,890,359.81 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,633 | 4,633 | 0 | 0.00% | 2,294,954,976,033.04 | Healthy |

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
| ebsintsdr01 | App | 1.9% | 2.6% | 10.8% | 0.0% | 0.0% | 0.0% | 18.2% | 19.1% | 20.3% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.7% | 14.9% | 0.0% | 0.0% | 0.0% | 8.6% | 10.1% | 12.2% | Healthy |
| ebsintslp01 | App | 4.5% | 17.3% | 37.5% | 0.0% | 0.0% | 0.0% | 23.6% | 24.2% | 24.9% | Healthy |
| ebsintslp02 | App | 4.4% | 15.8% | 43.6% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.0% | Healthy |
| efsdbsdr01 | Database | 16.2% | 22.4% | 49.3% | 0.0% | 0.0% | 0.0% | 65.3% | 65.4% | 65.5% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.0% | 16.8% | 0.0% | 0.0% | 0.0% | 46.3% | 46.3% | 46.3% | Healthy |
| efsdbslp01 | Database | 5.7% | 33.2% | 75.8% | 0.0% | 0.0% | 0.0% | 56.2% | 59.6% | 64.2% | Warning |
| efsdbslp02 | Database | 17.3% | 31.3% | 59.4% | 0.0% | 0.0% | 0.0% | 58.1% | 58.2% | 58.2% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,532 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.77%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
