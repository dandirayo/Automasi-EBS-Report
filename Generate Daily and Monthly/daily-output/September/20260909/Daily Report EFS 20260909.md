# EFS DAILY HEALTH REPORT
**Periode:** 9 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260909.xlsx, EFS_Infrastructures_20260909.xlsx, EFS_XLA_20260909.xlsx, EFS_GL_20260909.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,297,070
- **XLA Success Rate:** 92.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,007
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,007 records. GL Posted mencapai 206,235 (98.62% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 92.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.62% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,297,070 | Volume total harian |
| Processed (P / XLA=S) | 2,108,317 | Sukses diproses (92.00%) |
| Unprocessed (U) | 5,007 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 209,117
- **FAH Success:** 206,597
- **FAH Error:** 78
- **Not Accounted:** 206,240
- **Posted GL:** 206,235 (98.62% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 207,780 | 2 | 205,009 | 205,004 | 0 |
| CROSS BORDER PAYMENT Custom Application | 1,018 | 0 | 1,018 | 1,018 | 0 |
| TRADE FINANCE Custom Application | 151 | 0 | 145 | 145 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 53 | 0 | 31 | 31 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| PREPAID SYSTEM Custom Application | 10 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,310,580 | 1,309,891 | 689 | 0.05% | 173,708,792,982,981.66 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 440,395 | 440,395 | 0 | 0.00% | 13,422,922,397,154.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 201,965 | 201,965 | 0 | 0.00% | 32,790,281,552,132.90 | Healthy |
| DEP-Q_GLCP_GEND870 | 110,106 | 0 | 0 | 0.00% | -311,564,138.73 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,602 | 92,602 | 0 | 0.00% | 2,056,855,546.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,632 | 0 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 38,583 | 38,583 | 0 | 0.00% | 49,589,839,772,034.13 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 6,390 | 6,390 | 0 | 0.00% | 52,809,266,540,646.56 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,765 | 5,765 | 0 | 0.00% | -43,021,831,631,211.99 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,445 | 5,445 | 0 | 0.00% | 2,642,940,052,785.15 | Healthy |

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
| efsdbslp02 | Database | 17.5% | 35.1% | 80.9% | 58.8% | 60.9% | 65.0% | 51.0% | 51.1% | 51.6% | Critical |
| efsdbsdr01 | Database | 19.9% | 22.1% | 45.6% | 65.1% | 65.5% | 67.2% | 70.4% | 70.4% | 70.8% | Warning |
| efsdbsdr02 | Database | 1.1% | 5.3% | 18.4% | 50.2% | 50.7% | 51.5% | 43.6% | 43.7% | 44.0% | Healthy |
| ebsintslp02 | App | 3.4% | 14.9% | 98.5% | 26.0% | 46.0% | 53.1% | 10.7% | 10.8% | 10.9% | Critical |
| efsdbslp01 | Database | 8.6% | 36.0% | 94.4% | 56.5% | 59.1% | 63.9% | 47.9% | 57.5% | 66.9% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 84.9% | 7.0% | 7.3% | 8.2% | 41.3% | 41.3% | 41.6% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 81.3% | 6.8% | 7.0% | 8.3% | 24.4% | 24.4% | 24.6% | Critical |
| ebsintslp01 | App | 3.9% | 14.2% | 84.4% | 32.4% | 51.3% | 57.1% | 15.8% | 15.9% | 16.1% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,007 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.62%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
