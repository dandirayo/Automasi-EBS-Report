# EFS DAILY HEALTH REPORT
**Periode:** 25 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260725.xlsx, EFS_Infrastructures_20260725.xlsx, EFS_XLA_20260725.xlsx, EFS_GL_20260725.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,455,832
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,451
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,451 records. GL Posted mencapai 207,567 (99.92% intake).

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
| Report Set | 0 | 0.00 | 113.60 | 113.60 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 54.44 | 54.44 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 33.81 | 33.81 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 32.04 | 32.04 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 30.90 | 30.90 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 26.48 | 26.48 | 100.00% | Healthy |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 19.87 | 19.87 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 3.78 | 3.78 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.49 | 2.49 | 100.00% | Healthy |
| Journal Import | 0 | 0.00 | 1.90 | 1.90 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,455,832 | Volume total harian |
| Processed (P / XLA=S) | 2,454,381 | Sukses diproses (100.00%) |
| Unprocessed (U) | 1,451 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 207,741
- **FAH Success:** 207,739
- **FAH Error:** 2
- **Not Accounted:** 207,567
- **Posted GL:** 207,567 (99.92% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 206,715 | 2 | 206,558 | 206,558 | 0 |
| CROSS BORDER PAYMENT Custom Application | 764 | 0 | 764 | 764 | 0 |
| TRADE FINANCE Custom Application | 175 | 0 | 175 | 175 | 0 |
| CREDIT CARD Custom Application | 53 | 0 | 36 | 36 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| PREPAID SYSTEM Custom Application | 7 | 0 | 7 | 7 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,361,996 | 1,360,670 | 1,326 | 0.10% | 28,201,169,924,920.00 | Warning |
| DEP-NQ_ED2P_SC_BFST | 492,075 | 492,075 | 0 | 0.00% | 13,707,890,511,970.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 223,092 | 223,092 | 0 | 0.00% | 6,323,122,612,578.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,335 | 195,335 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 95,847 | 95,847 | 0 | 0.00% | 1,739,494,412.00 | Healthy |
| LON-Q_GLCP_GEND872 | 71,300 | 71,300 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,943 | 5,943 | 0 | 0.00% | -40,755,536,431,156.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 5,346 | 5,346 | 0 | 0.00% | 63,087,363,417.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 3,073 | 3,073 | 0 | 0.00% | 15,613,540,581.00 | Healthy |
| BRA-NQ_ED2P_ELOG | 854 | 854 | 0 | 0.00% | 403,996,719,258.00 | Healthy |

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
| ebsintslp01 | App | 4.0% | 7.7% | 20.3% | 0.0% | 0.0% | 0.0% | 18.0% | 18.0% | 18.9% | Healthy |
| ebsintslp02 | App | 4.5% | 7.8% | 20.2% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.1% | Healthy |
| efsdbsdr01 | Database | 2.9% | 8.8% | 17.4% | 0.0% | 0.0% | 0.0% | 66.9% | 66.9% | 66.9% | Warning |
| efsdbsdr02 | Database | 3.5% | 8.6% | 55.9% | 0.0% | 0.0% | 0.0% | 47.4% | 47.5% | 47.9% | Healthy |
| efsdbslp01 | Database | 13.1% | 30.4% | 55.2% | 0.0% | 0.0% | 0.0% | 58.0% | 60.6% | 72.6% | Warning |
| efsdbslp02 | Database | 30.2% | 43.8% | 92.0% | 0.0% | 0.0% | 0.0% | 59.1% | 59.2% | 59.2% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,451 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
