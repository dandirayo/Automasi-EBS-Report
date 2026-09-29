# EFS DAILY HEALTH REPORT
**Periode:** 13 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260713.xlsx, EFS_Infrastructures_20260713.xlsx, EFS_XLA_20260713.xlsx, EFS_GL_20260713.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,367,839
- **XLA Success Rate:** 98.89%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 2,523
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 2,523 records. GL Posted mencapai 199,829 (99.79% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 98.89% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.79% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 650.75 | 650.75 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 110.65 | 110.65 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 36.41 | 36.41 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 30.66 | 30.66 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 28.58 | 28.58 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 20.37 | 20.37 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 19.73 | 19.73 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 7.84 | 7.84 | 100.00% | Critical |
| BNI GL Revaluasi Harian | 0 | 0.00 | 2.60 | 2.60 | 100.00% | Healthy |
| BNI GL Bugla EFS Outbound F1 | 0 | 0.00 | 1.97 | 1.97 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,367,839 | Volume total harian |
| Processed (P / XLA=S) | 2,365,316 | Sukses diproses (98.89%) |
| Unprocessed (U) | 2,523 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 200,240
- **FAH Success:** 200,238
- **FAH Error:** 2
- **Not Accounted:** 199,829
- **Posted GL:** 199,829 (99.79% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 200,120 | 2 | 199,711 | 199,711 | 0 |
| CROSS BORDER PAYMENT Custom Application | 63 | 0 | 63 | 63 | 0 |
| CREDIT CARD Custom Application | 41 | 0 | 41 | 41 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 4 | 0 | 4 | 4 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 3 | 0 | 3 | 3 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,313,079 | 1,312,390 | 689 | 0.05% | 284,974,012,566,425.81 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 464,486 | 464,486 | 0 | 0.00% | 15,358,067,914,593.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 188,669 | 188,669 | 0 | 0.00% | 66,108,302,206,110.38 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,664 | 181,664 | 0 | 0.00% | 1,986,636,592.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,091 | 84,091 | 0 | 0.00% | 1,545,997,648.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,628 | 70,628 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,762 | 46,762 | 0 | 0.00% | 55,730,475,769,691.34 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,345 | 7,345 | 0 | 0.00% | 60,729,844,368,863.75 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,937 | 4,937 | 0 | 0.00% | 3,286,989,666,600.51 | Healthy |
| LON-NQ_ED2P_BORV | 2,284 | 1,024 | 1,260 | 55.17% | 2,470,798,113,534.71 | Critical |

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
| ebsintsdr01 | App | 1.8% | 3.2% | 12.3% | 0.0% | 0.0% | 0.0% | 21.3% | 21.4% | 22.8% | Healthy |
| ebsintsdr02 | App | 3.0% | 4.0% | 10.5% | 0.0% | 0.0% | 0.0% | 12.2% | 12.3% | 13.0% | Healthy |
| ebsintslp01 | App | 4.4% | 15.8% | 73.9% | 0.0% | 0.0% | 0.0% | 25.1% | 25.4% | 26.1% | Warning |
| ebsintslp02 | App | 4.7% | 11.0% | 24.5% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 22.6% | 28.6% | 38.4% | 0.0% | 0.0% | 0.0% | 66.8% | 67.0% | 67.2% | Warning |
| efsdbsdr02 | Database | 3.2% | 10.0% | 23.4% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 21.5% | 42.5% | 95.4% | 0.0% | 0.0% | 0.0% | 56.3% | 60.6% | 62.9% | Critical |
| efsdbslp02 | Database | 6.9% | 28.2% | 48.5% | 0.0% | 0.0% | 0.0% | 58.8% | 58.9% | 58.9% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 2,523 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
