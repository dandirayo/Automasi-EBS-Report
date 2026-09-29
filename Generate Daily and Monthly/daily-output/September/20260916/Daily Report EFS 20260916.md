# EFS DAILY HEALTH REPORT
**Periode:** 16 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260916.xlsx, EFS_Infrastructures_20260916.xlsx, EFS_XLA_20260916.xlsx, EFS_GL_20260916.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,780,772
- **XLA Success Rate:** 82.10%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 214,411
- **Infrastruktur Status:** 2 Critical, 5 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 214,411 records. GL Posted mencapai 156,207 (97.30% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 82.10% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 97.30% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,780,772 | Volume total harian |
| Processed (P / XLA=S) | 1,458,158 | Sukses diproses (82.10%) |
| Unprocessed (U) | 214,411 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 160,538
- **FAH Success:** 156,530
- **FAH Error:** 329
- **Not Accounted:** 156,207
- **Posted GL:** 156,207 (97.30% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 159,410 | 176 | 155,310 | 155,310 | 0 |
| CROSS BORDER PAYMENT Custom Application | 458 | 0 | 458 | 458 | 0 |
| PSAK 71 Custom Application | 371 | 152 | 217 | 217 | 0 |
| TRADE FINANCE Custom Application | 194 | 1 | 187 | 187 | 0 |
| CREDIT CARD Custom Application | 68 | 0 | 0 | 0 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 10 | 0 | 8 | 8 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 935,216 | 724,070 | 211,146 | 22.58% | 186,641,225,830,456.69 | Critical |
| DEP-NQ_ED2P_SC_BFST | 318,712 | 249,839 | 0 | 0.00% | 13,647,481,436,056.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 183,810 | 165,042 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 145,035 | 145,035 | 0 | 0.00% | 34,008,521,418,094.27 | Healthy |
| LON-Q_GLCP_GEND872 | 73,652 | 73,368 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 62,475 | 45,168 | 0 | 0.00% | 1,399,324,614.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 34,693 | 33,485 | 0 | 0.00% | 48,109,968,618,285.29 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,803 | 5,803 | 0 | 0.00% | -42,748,948,434,421.76 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,588 | 5,588 | 0 | 0.00% | 65,686,431,928,510.33 | Healthy |
| LON-NQ_ED2P_BORV | 4,762 | 1,264 | 1,753 | 36.81% | 5,471,066,480,307.24 | Critical |

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
| efsdbslp02 | Database | 9.3% | 21.8% | 69.8% | 60.5% | 62.5% | 66.6% | 51.2% | 51.3% | 51.4% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.0% | 29.0% | 66.9% | 67.2% | 68.1% | 70.5% | 70.5% | 70.6% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.2% | 16.3% | 50.3% | 50.7% | 51.5% | 43.7% | 43.7% | 44.1% | Healthy |
| ebsintslp02 | App | 2.3% | 10.2% | 99.2% | 43.9% | 46.1% | 51.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 6.6% | 26.0% | 89.2% | 56.8% | 59.3% | 64.0% | 52.7% | 57.6% | 64.4% | Critical |
| ebsintsdr01 | App | 0.6% | 1.5% | 65.4% | 7.3% | 7.5% | 8.8% | 41.3% | 41.3% | 41.7% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.5% | 7.3% | 7.4% | 8.9% | 24.4% | 24.4% | 25.5% | Warning |
| ebsintslp01 | App | 2.6% | 9.6% | 62.5% | 49.9% | 52.0% | 57.3% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 214,411 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 97.30%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
