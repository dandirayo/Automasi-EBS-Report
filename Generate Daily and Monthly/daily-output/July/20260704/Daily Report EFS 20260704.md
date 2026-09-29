# EFS DAILY HEALTH REPORT
**Periode:** 4 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260704.xlsx, EFS_Infrastructures_20260704.xlsx, EFS_XLA_20260704.xlsx, EFS_GL_20260704.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,433,231
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 572
- **Infrastruktur Status:** 1 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 572 records. GL Posted mencapai 194,536 (99.92% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.92% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 101.80 | 101.80 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 26.63 | 26.63 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 24.03 | 24.03 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 23.86 | 23.86 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 23.72 | 23.72 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 22.92 | 22.92 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 8.19 | 8.19 | 100.00% | Critical |
| Journal Import | 0 | 0.00 | 2.52 | 2.52 | 100.00% | Critical |
| Create Accounting - Receiving | 0 | 0.00 | 2.12 | 2.12 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.03 | 2.03 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,433,231 | Volume total harian |
| Processed (P / XLA=S) | 2,432,659 | Sukses diproses (100.00%) |
| Unprocessed (U) | 572 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 194,699
- **FAH Success:** 194,695
- **FAH Error:** 4
- **Not Accounted:** 194,536
- **Posted GL:** 194,536 (99.92% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 193,969 | 4 | 193,824 | 193,824 | 0 |
| CROSS BORDER PAYMENT Custom Application | 408 | 0 | 408 | 408 | 0 |
| TRADE FINANCE Custom Application | 237 | 0 | 237 | 237 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 34 | 34 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,360,750 | 1,360,184 | 566 | 0.04% | 21,312,055,097,295.72 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 483,241 | 483,241 | 0 | 0.00% | 12,333,817,521,526.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 211,218 | 211,218 | 0 | 0.00% | 5,805,589,053,282.65 | Healthy |
| DEP-Q_GLCP_GEND870 | 197,145 | 197,145 | 0 | 0.00% | -3,507,450.81 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 100,194 | 100,194 | 0 | 0.00% | 1,763,868,411.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,533 | 67,533 | 0 | 0.00% | 2,254,233,674.83 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,802 | 5,802 | 0 | 0.00% | -40,008,043,138,337.67 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,277 | 3,277 | 0 | 0.00% | 73,196,870,307.54 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,468 | 2,468 | 0 | 0.00% | 21,402,358,536.31 | Healthy |
| BRA-NQ_ED2P_ELOG | 824 | 824 | 0 | 0.00% | 412,129,889,912.00 | Healthy |

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
| ebsintsdr01 | App | 2.2% | 3.6% | 13.2% | 0.0% | 0.0% | 0.0% | 20.4% | 20.4% | 20.5% | Healthy |
| ebsintsdr02 | App | 2.1% | 4.1% | 11.2% | 0.0% | 0.0% | 0.0% | 12.2% | 12.3% | 13.0% | Healthy |
| ebsintslp01 | App | 3.8% | 11.7% | 27.3% | 0.0% | 0.0% | 0.0% | 25.5% | 25.7% | 26.4% | Healthy |
| ebsintslp02 | App | 20.7% | 23.7% | 33.7% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 53.7% | 61.9% | 99.3% | 0.0% | 0.0% | 0.0% | 65.7% | 65.8% | 65.9% | Critical |
| efsdbsdr02 | Database | 3.1% | 10.4% | 20.9% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 18.3% | 33.6% | 74.4% | 0.0% | 0.0% | 0.0% | 58.8% | 60.7% | 62.4% | Warning |
| efsdbslp02 | Database | 23.6% | 32.9% | 54.3% | 0.0% | 0.0% | 0.0% | 58.2% | 58.2% | 58.2% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 572 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.92%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
