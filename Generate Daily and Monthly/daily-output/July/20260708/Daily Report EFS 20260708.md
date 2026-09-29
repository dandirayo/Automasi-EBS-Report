# EFS DAILY HEALTH REPORT
**Periode:** 8 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260708.xlsx, EFS_Infrastructures_20260708.xlsx, EFS_XLA_20260708.xlsx, EFS_GL_20260708.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,567,352
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,465
- **Infrastruktur Status:** 1 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,465 records. GL Posted mencapai 227,209 (99.81% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.81% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 585.02 | 585.02 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 115.06 | 115.06 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 28.11 | 28.11 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 26.36 | 26.36 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 25.70 | 25.70 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 23.25 | 23.25 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.08 | 5.08 | 100.00% | Critical |
| BNI GL Revaluasi Harian | 0 | 0.00 | 4.42 | 4.42 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 2.95 | 2.95 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.77 | 2.77 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,567,352 | Volume total harian |
| Processed (P / XLA=S) | 2,562,887 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,465 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 227,644
- **FAH Success:** 227,640
- **FAH Error:** 4
- **Not Accounted:** 227,209
- **Posted GL:** 227,209 (99.81% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 226,535 | 4 | 226,124 | 226,124 | 0 |
| CROSS BORDER PAYMENT Custom Application | 475 | 0 | 475 | 475 | 0 |
| TRADE FINANCE Custom Application | 315 | 0 | 315 | 315 | 0 |
| PSAK 71 Custom Application | 230 | 0 | 228 | 228 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 31 | 31 | 0 |
| TREASURY Custom Application | 15 | 0 | 15 | 15 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,417,114 | 1,416,415 | 699 | 0.05% | 198,756,260,419,711.12 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 513,595 | 513,595 | 0 | 0.00% | 15,063,732,279,182.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 223,856 | 223,856 | 0 | 0.00% | 35,811,981,009,113.76 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,745 | 181,745 | 0 | 0.00% | -1.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,117 | 92,117 | 0 | 0.00% | 1,583,785,976.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,067 | 67,067 | 0 | 0.00% | 707,194,900.85 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,658 | 43,658 | 0 | 0.00% | 44,647,075,825,196.23 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,187 | 7,187 | 0 | 0.00% | 50,049,800,026,918.36 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,821 | 5,821 | 0 | 0.00% | -42,082,401,234,647.68 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,733 | 4,733 | 0 | 0.00% | 2,524,022,327,413.34 | Healthy |

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
| ebsintsdr01 | App | 2.2% | 2.9% | 12.0% | 0.0% | 0.0% | 0.0% | 20.6% | 20.6% | 22.2% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.6% | 10.3% | 0.0% | 0.0% | 0.0% | 12.3% | 12.4% | 13.3% | Healthy |
| ebsintslp01 | App | 4.9% | 25.2% | 63.6% | 0.0% | 0.0% | 0.0% | 21.7% | 22.1% | 22.5% | Warning |
| ebsintslp02 | App | 4.2% | 12.2% | 46.2% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.3% | Healthy |
| efsdbsdr01 | Database | 53.6% | 60.6% | 74.1% | 0.0% | 0.0% | 0.0% | 66.2% | 66.3% | 66.4% | Warning |
| efsdbsdr02 | Database | 3.3% | 8.2% | 22.1% | 0.0% | 0.0% | 0.0% | 46.4% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 13.0% | 33.4% | 64.0% | 0.0% | 0.0% | 0.0% | 59.2% | 61.2% | 63.2% | Warning |
| efsdbslp02 | Database | 10.6% | 27.4% | 83.1% | 0.0% | 0.0% | 0.0% | 58.6% | 58.7% | 58.8% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,465 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.81%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
