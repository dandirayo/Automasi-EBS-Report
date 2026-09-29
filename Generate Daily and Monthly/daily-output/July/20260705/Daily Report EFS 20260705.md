# EFS DAILY HEALTH REPORT
**Periode:** 5 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260705.xlsx, EFS_Infrastructures_20260705.xlsx, EFS_XLA_20260705.xlsx, EFS_GL_20260705.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,350,709
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,472
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,472 records. GL Posted mencapai 183,161 (99.95% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.95% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 572.28 | 572.28 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 92.76 | 92.76 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 28.08 | 28.08 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 24.34 | 24.34 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 23.95 | 23.95 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 23.54 | 23.54 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 22.95 | 22.95 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 6.14 | 6.14 | 100.00% | Critical |
| Journal Import | 0 | 0.00 | 1.79 | 1.79 | 100.00% | Healthy |
| Create Accounting - Cost Management | 0 | 0.00 | 0.62 | 0.62 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,350,709 | Volume total harian |
| Processed (P / XLA=S) | 2,349,237 | Sukses diproses (100.00%) |
| Unprocessed (U) | 1,472 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 183,244
- **FAH Success:** 183,240
- **FAH Error:** 4
- **Not Accounted:** 183,161
- **Posted GL:** 183,161 (99.95% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 183,119 | 4 | 183,038 | 183,038 | 0 |
| CROSS BORDER PAYMENT Custom Application | 93 | 0 | 93 | 93 | 0 |
| CREDIT CARD Custom Application | 18 | 0 | 18 | 18 | 0 |
| PREPAID SYSTEM Custom Application | 8 | 0 | 6 | 6 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,317,550 | 1,316,081 | 1,469 | 0.11% | 19,328,010,691,666.05 | Warning |
| DEP-NQ_ED2P_SC_BFST | 462,806 | 462,806 | 0 | 0.00% | 9,335,343,122,647.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 203,868 | 203,868 | 0 | 0.00% | 4,966,772,204,292.50 | Healthy |
| DEP-Q_GLCP_GEND870 | 196,622 | 196,622 | 0 | 0.00% | -89,394.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 90,206 | 90,206 | 0 | 0.00% | 1,456,723,492.00 | Healthy |
| LON-Q_GLCP_GEND872 | 69,208 | 69,208 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 6,773 | 6,773 | 0 | 0.00% | 97,924,994,554.29 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,382 | 2,382 | 0 | 0.00% | 9,914,623,373.08 | Healthy |
| BRA-NQ_ED2P_ELOG | 871 | 871 | 0 | 0.00% | 376,116,148,982.00 | Healthy |
| BRA-NQ_ED2P_CC_GLDV | 112 | 112 | 0 | 0.00% | 311,399,466.00 | Healthy |

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
| ebsintsdr01 | App | 2.1% | 4.1% | 11.9% | 0.0% | 0.0% | 0.0% | 20.4% | 20.5% | 22.0% | Healthy |
| ebsintsdr02 | App | 2.0% | 3.1% | 13.1% | 0.0% | 0.0% | 0.0% | 12.3% | 12.3% | 13.8% | Healthy |
| ebsintslp01 | App | 3.9% | 11.2% | 26.4% | 0.0% | 0.0% | 0.0% | 25.9% | 25.9% | 25.9% | Healthy |
| ebsintslp02 | App | 21.0% | 23.4% | 32.9% | 0.0% | 0.0% | 0.0% | 10.0% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 53.7% | 59.5% | 72.9% | 0.0% | 0.0% | 0.0% | 65.8% | 65.9% | 65.9% | Warning |
| efsdbsdr02 | Database | 3.1% | 7.9% | 16.7% | 0.0% | 0.0% | 0.0% | 46.3% | 46.4% | 46.4% | Healthy |
| efsdbslp01 | Database | 31.4% | 40.1% | 55.7% | 0.0% | 0.0% | 0.0% | 59.7% | 61.0% | 62.4% | Warning |
| efsdbslp02 | Database | 30.6% | 44.5% | 88.1% | 0.0% | 0.0% | 0.0% | 58.2% | 58.3% | 58.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,472 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.95%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
