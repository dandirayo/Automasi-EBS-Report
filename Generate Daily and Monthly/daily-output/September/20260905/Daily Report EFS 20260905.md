# EFS DAILY HEALTH REPORT
**Periode:** 5 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260905.xlsx, EFS_Infrastructures_20260905.xlsx, EFS_XLA_20260905.xlsx, EFS_GL_20260905.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 272,222
- **XLA Success Rate:** 93.32%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 0
- **Infrastruktur Status:** 4 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 0 records. GL Posted mencapai 17,960 (94.20% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 93.32% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 94.20% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 272,222 | Volume total harian |
| Processed (P / XLA=S) | 254,024 | Sukses diproses (93.32%) |
| Unprocessed (U) | 0 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 19,065
- **FAH Success:** 18,020
- **FAH Error:** 221
- **Not Accounted:** 17,960
- **Posted GL:** 17,960 (94.20% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 18,475 | 145 | 17,482 | 17,482 | 0 |
| TRADE FINANCE Custom Application | 376 | 0 | 376 | 376 | 0 |
| CREDIT CARD Custom Application | 87 | 0 | 53 | 53 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| TREASURY Custom Application | 28 | 0 | 28 | 28 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-Q_GLCP_GEND870 | 192,470 | 174,588 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,638 | 73,354 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,764 | 5,743 | 0 | 0.00% | -42,048,809,481,341.27 | Healthy |
| BRA-NQ_ED2P_ELOG | 301 | 290 | 0 | 0.00% | 389,584,535,086.00 | Healthy |
| BRA-NQ_ED2P_BFST | 35 | 35 | 0 | 0.00% | 11,246,655,575,698.00 | Healthy |
| ACCRUAL JF | 4 | 4 | 0 | 0.00% | 0.00 | Healthy |
| SETTLEMENT | 3 | 3 | 0 | 0.00% | 75,000.00 | Healthy |
| MERCHANT BNI_J | 2 | 2 | 0 | 0.00% | 3,278,354.00 | Healthy |
| MERCHANT BNI_M | 2 | 2 | 0 | 0.00% | 117,418,090.00 | Healthy |
| MERCHANT BNI_V | 2 | 2 | 0 | 0.00% | 187,481,287.00 | Healthy |

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
| efsdbslp02 | Database | 11.8% | 21.6% | 78.0% | 57.7% | 58.4% | 59.5% | 51.0% | 51.0% | 51.0% | Warning |
| efsdbsdr01 | Database | 19.9% | 22.2% | 42.3% | 63.9% | 64.2% | 65.2% | 70.4% | 70.4% | 70.8% | Warning |
| efsdbsdr02 | Database | 1.1% | 4.0% | 15.3% | 50.1% | 50.5% | 51.6% | 43.6% | 43.6% | 43.7% | Healthy |
| ebsintslp02 | App | 3.5% | 8.1% | 97.3% | 44.7% | 45.0% | 46.5% | 10.7% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 8.7% | 21.8% | 88.2% | 55.8% | 56.5% | 58.1% | 51.6% | 55.7% | 59.2% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 81.0% | 6.4% | 6.8% | 8.1% | 24.4% | 24.4% | 24.8% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 85.7% | 6.7% | 7.0% | 8.0% | 41.2% | 41.3% | 41.6% | Critical |
| ebsintslp01 | App | 4.2% | 11.8% | 76.5% | 50.4% | 50.7% | 52.2% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 0 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 94.20%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
