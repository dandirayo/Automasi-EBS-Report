# EFS DAILY HEALTH REPORT
**Periode:** 3 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260703.xlsx, EFS_Infrastructures_20260703.xlsx, EFS_XLA_20260703.xlsx, EFS_GL_20260703.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,877,471
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,650
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,650 records. GL Posted mencapai 174,817 (99.77% intake).

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
| Report Set | 0 | 0.00 | 109.97 | 109.97 | 100.00% | Critical |
| Validate Application Accounting Definitions | 0 | 0.00 | 42.67 | 42.67 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 25.12 | 25.12 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 24.89 | 24.89 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 24.05 | 24.05 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 23.77 | 23.77 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.68 | 5.68 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 3.54 | 3.54 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 2.83 | 2.83 | 100.00% | Healthy |
| BNI GL Interface Kurs Harian | 0 | 0.00 | 0.65 | 0.65 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,877,471 | Volume total harian |
| Processed (P / XLA=S) | 1,872,821 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,650 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 175,220
- **FAH Success:** 175,214
- **FAH Error:** 6
- **Not Accounted:** 174,817
- **Posted GL:** 174,817 (99.77% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 174,429 | 6 | 174,045 | 174,045 | 0 |
| CROSS BORDER PAYMENT Custom Application | 549 | 0 | 549 | 549 | 0 |
| TRADE FINANCE Custom Application | 145 | 0 | 145 | 145 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 26 | 0 | 26 | 26 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,019,233 | 1,018,350 | 883 | 0.09% | 215,909,508,515,233.44 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 330,527 | 330,527 | 0 | 0.00% | 13,492,288,012,038.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 179,880 | 179,880 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 142,471 | 142,471 | 0 | 0.00% | 50,410,972,353,217.37 | Healthy |
| LON-Q_GLCP_GEND872 | 68,442 | 68,442 | 0 | 0.00% | -999,015,973.94 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 65,736 | 65,736 | 0 | 0.00% | 1,352,237,958.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,558 | 43,558 | 0 | 0.00% | 38,467,080,104,021.07 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,347 | 7,347 | 0 | 0.00% | 44,323,016,076,011.66 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,772 | 5,772 | 0 | 0.00% | -39,449,231,239,633.96 | Healthy |
| LON-NQ_ED2P_BORV | 4,580 | 1,925 | 2,655 | 57.97% | 5,250,991,894,898.61 | Critical |

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
| ebsintsdr01 | App | 2.0% | 2.6% | 12.0% | 0.0% | 0.0% | 0.0% | 20.3% | 20.3% | 20.4% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.7% | 15.4% | 0.0% | 0.0% | 0.0% | 12.2% | 12.2% | 12.3% | Healthy |
| ebsintslp01 | App | 3.8% | 16.1% | 48.4% | 0.0% | 0.0% | 0.0% | 24.7% | 25.1% | 25.5% | Healthy |
| ebsintslp02 | App | 4.4% | 18.4% | 53.3% | 0.0% | 0.0% | 0.0% | 9.9% | 10.0% | 10.2% | Healthy |
| efsdbsdr01 | Database | 47.4% | 57.6% | 79.1% | 0.0% | 0.0% | 0.0% | 65.4% | 65.6% | 65.7% | Warning |
| efsdbsdr02 | Database | 3.2% | 6.0% | 18.5% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 13.0% | 38.9% | 95.2% | 0.0% | 0.0% | 0.0% | 53.7% | 59.6% | 62.9% | Critical |
| efsdbslp02 | Database | 17.0% | 34.5% | 64.0% | 0.0% | 0.0% | 0.0% | 58.2% | 58.2% | 58.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,650 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
