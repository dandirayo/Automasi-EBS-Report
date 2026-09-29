# EFS DAILY HEALTH REPORT
**Periode:** 23 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260723.xlsx, EFS_Infrastructures_20260723.xlsx, EFS_XLA_20260723.xlsx, EFS_GL_20260723.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,953,811
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 23,987
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 23,987 records. GL Posted mencapai 208,666 (99.78% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.78% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 121.78 | 121.78 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 53.27 | 53.27 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 32.03 | 32.03 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 25.44 | 25.44 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 25.08 | 25.08 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.66 | 5.66 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 2.22 | 2.22 | 100.00% | Healthy |
| Create Accounting - Receiving | 0 | 0.00 | 2.10 | 2.10 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 1.77 | 1.77 | 100.00% | Healthy |
| Create Accounting - Cost Management | 0 | 0.00 | 1.54 | 1.54 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,953,811 | Volume total harian |
| Processed (P / XLA=S) | 2,929,824 | Sukses diproses (100.00%) |
| Unprocessed (U) | 23,987 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 209,117
- **FAH Success:** 209,115
- **FAH Error:** 2
- **Not Accounted:** 208,666
- **Posted GL:** 208,666 (99.78% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 208,353 | 2 | 207,919 | 207,919 | 0 |
| CROSS BORDER PAYMENT Custom Application | 507 | 0 | 507 | 507 | 0 |
| TRADE FINANCE Custom Application | 176 | 0 | 176 | 176 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 7 | 0 | 7 | 7 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 7 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,440,439 | 1,433,108 | 7,331 | 0.51% | 207,188,024,395,470.00 | Warning |
| DEP-NQ_ED2P_SC_BFST | 511,996 | 511,996 | 0 | 0.00% | 14,404,054,500,593.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 431,336 | 431,190 | 146 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 224,308 | 224,305 | 3 | 0.00% | 68,866,296,192,707.00 | Healthy |
| LON-Q_GLCP_GEND872 | 147,458 | 147,448 | 10 | 0.01% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 87,260 | 87,260 | 0 | 0.00% | 1,530,620,659.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 40,339 | 40,339 | 0 | 0.00% | 62,905,658,641,105.00 | Healthy |
| LON-NQ_ED2P_BORV | 17,881 | 5,672 | 12,209 | 68.28% | 7,989,464,732,011.00 | Critical |
| LON-Q_GLCP_GLIF | 14,241 | 14,117 | 124 | 0.87% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,817 | 11,817 | 0 | 0.00% | -20,434,320,874.00 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.5% | 19.1% | 0.0% | 0.0% | 0.0% | 21.5% | 21.6% | 22.5% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.6% | 19.1% | 0.0% | 0.0% | 0.0% | 12.6% | 12.7% | 15.5% | Healthy |
| ebsintslp01 | App | 4.4% | 16.7% | 53.1% | 0.0% | 0.0% | 0.0% | 18.0% | 18.0% | 18.0% | Healthy |
| ebsintslp02 | App | 4.7% | 14.4% | 39.7% | 0.0% | 0.0% | 0.0% | 10.0% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 1.5% | 33.3% | 50.7% | 0.0% | 0.0% | 0.0% | 65.0% | 67.6% | 68.1% | Warning |
| efsdbsdr02 | Database | 1.5% | 6.0% | 24.9% | 0.0% | 0.0% | 0.0% | 45.3% | 46.7% | 47.4% | Healthy |
| efsdbslp01 | Database | 19.1% | 45.2% | 90.6% | 0.0% | 0.0% | 0.0% | 56.8% | 61.1% | 64.5% | Critical |
| efsdbslp02 | Database | 27.3% | 41.5% | 67.0% | 0.0% | 0.0% | 0.0% | 59.1% | 59.1% | 59.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 23,987 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.78%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
