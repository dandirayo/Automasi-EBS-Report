# EFS DAILY HEALTH REPORT
**Periode:** 31 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260731.xlsx, EFS_Infrastructures_20260731.xlsx, EFS_XLA_20260731.xlsx, EFS_GL_20260731.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,544,591
- **XLA Success Rate:** 87.60%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 321,564
- **Infrastruktur Status:** 2 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 321,564 records. GL Posted mencapai 235,964 (99.76% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 87.60% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.76% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 180.58 | 180.58 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 151.36 | 151.36 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 81.37 | 81.37 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 42.03 | 42.03 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 40.05 | 40.05 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 30.69 | 30.69 | 100.00% | Critical |
| Depreciation Run | 0 | 0.00 | 22.41 | 22.41 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 19.40 | 19.40 | 100.00% | Healthy |
| BNI GL Accrue Expense Generate | 0 | 0.00 | 12.83 | 12.83 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 8.40 | 8.40 | 100.00% | Critical |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,544,591 | Volume total harian |
| Processed (P / XLA=S) | 2,223,027 | Sukses diproses (87.60%) |
| Unprocessed (U) | 321,564 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 236,535
- **FAH Success:** 236,533
- **FAH Error:** 2
- **Not Accounted:** 235,964
- **Posted GL:** 235,964 (99.76% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 235,773 | 2 | 235,221 | 235,221 | 0 |
| CROSS BORDER PAYMENT Custom Application | 495 | 0 | 495 | 495 | 0 |
| TRADE FINANCE Custom Application | 178 | 0 | 178 | 178 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 33 | 33 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,477,676 | 1,161,669 | 316,007 | 21.39% | 356,327,133,573,420.00 | Critical |
| DEP-NQ_ED2P_SC_BFST | 416,984 | 416,984 | 0 | 0.00% | 16,345,889,448,506.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 237,697 | 237,697 | 0 | 0.00% | 62,487,049,395,827.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 178,100 | 178,100 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 78,241 | 78,241 | 0 | 0.00% | 1,611,546,059.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,257 | 70,257 | 0 | 0.00% | -756,041,441.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 51,086 | 51,086 | 0 | 0.00% | 53,993,009,675,593.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 8,561 | 8,561 | 0 | 0.00% | 85,295,551,257,441.00 | Healthy |
| LON-NQ_ED2P_BORV | 6,077 | 2,445 | 3,632 | 59.77% | 4,882,828,620,544.00 | Critical |
| LON-Q_GLCP_BORV | 5,948 | 4,201 | 1,747 | 29.37% | 6,174,673,204,517.00 | Critical |

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
| ebsintslp01 | App | 20.8% | 32.2% | 57.0% | 0.0% | 0.0% | 0.0% | 18.1% | 18.1% | 18.2% | Healthy |
| ebsintslp02 | App | 4.5% | 23.3% | 58.5% | 0.0% | 0.0% | 0.0% | 10.1% | 10.2% | 10.3% | Healthy |
| efsdbsdr01 | Database | 27.9% | 34.4% | 53.7% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 67.1% | Warning |
| efsdbsdr02 | Database | 3.7% | 8.4% | 20.9% | 0.0% | 0.0% | 0.0% | 47.4% | 47.5% | 47.5% | Healthy |
| efsdbslp01 | Database | 0.0% | 57.3% | 94.4% | 0.0% | 0.0% | 0.0% | 0.0% | 61.2% | 65.8% | Critical |
| efsdbslp02 | Database | 0.0% | 62.9% | 93.7% | 0.0% | 0.0% | 0.0% | 0.0% | 59.1% | 59.4% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 321,564 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.76%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
