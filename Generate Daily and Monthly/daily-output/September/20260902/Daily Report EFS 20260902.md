# EFS DAILY HEALTH REPORT
**Periode:** 2 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260902.xlsx, EFS_Infrastructures_20260902.xlsx, EFS_XLA_20260902.xlsx, EFS_GL_20260902.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,483,224
- **XLA Success Rate:** 98.38%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,154
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,154 records. GL Posted mencapai 211,750 (99.34% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 98.38% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.34% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,483,224 | Volume total harian |
| Processed (P / XLA=S) | 2,437,877 | Sukses diproses (98.38%) |
| Unprocessed (U) | 5,154 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 213,148
- **FAH Success:** 212,159
- **FAH Error:** 204
- **Not Accounted:** 211,750
- **Posted GL:** 211,750 (99.34% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 212,261 | 115 | 210,972 | 210,972 | 0 |
| CROSS BORDER PAYMENT Custom Application | 527 | 0 | 527 | 527 | 0 |
| TRADE FINANCE Custom Application | 187 | 0 | 187 | 187 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 58 | 9 | 32 | 32 | 0 |
| TREASURY Custom Application | 16 | 3 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 1 | 8 | 8 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 3 | 3 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,357,975 | 1,356,692 | 1,283 | 0.09% | 234,993,766,236,375.62 | Warning |
| DEP-NQ_ED2P_SC_BFST | 473,114 | 473,114 | 0 | 0.00% | 17,829,116,144,387.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 219,168 | 219,168 | 0 | 0.00% | 55,141,589,665,378.93 | Healthy |
| DEP-Q_GLCP_GEND870 | 188,949 | 172,745 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 95,491 | 73,273 | 0 | 0.00% | 1,887,451,560.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,602 | 73,316 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 45,116 | 44,136 | 0 | 0.00% | 57,157,584,425,824.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,512 | 7,512 | 0 | 0.00% | 101,502,535,011,851.16 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,714 | 5,714 | 0 | 0.00% | -36,880,748,884,741.38 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,257 | 5,257 | 0 | 0.00% | 2,139,810,461,952.77 | Healthy |

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
| efsdbslp02 | Database | 16.4% | 57.1% | 97.9% | 57.6% | 59.6% | 63.2% | 50.8% | 50.9% | 51.1% | Critical |
| efsdbsdr01 | Database | 19.9% | 43.6% | 82.8% | 62.9% | 63.4% | 65.5% | 70.3% | 70.4% | 70.7% | Critical |
| efsdbsdr02 | Database | 1.4% | 8.6% | 48.7% | 50.1% | 50.5% | 51.7% | 43.5% | 43.6% | 43.8% | Healthy |
| ebsintslp02 | App | 3.4% | 13.5% | 97.8% | 44.8% | 47.0% | 52.0% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 8.8% | 54.2% | 98.7% | 55.2% | 57.9% | 62.7% | 46.2% | 57.7% | 63.2% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 82.5% | 6.2% | 6.5% | 7.8% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintsdr01 | App | 0.8% | 2.0% | 85.5% | 6.5% | 6.8% | 7.7% | 41.2% | 41.2% | 41.5% | Critical |
| ebsintslp01 | App | 4.2% | 20.6% | 88.5% | 48.7% | 51.7% | 58.0% | 15.8% | 15.8% | 16.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,154 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.34%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
