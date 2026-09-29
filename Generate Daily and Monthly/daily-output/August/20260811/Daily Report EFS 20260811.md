# EFS DAILY HEALTH REPORT
**Periode:** 11 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260811.xlsx, EFS_Infrastructures_20260811.xlsx, EFS_XLA_20260811.xlsx, EFS_GL_20260811.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,034,400
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 23,602
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 23,602 records. GL Posted mencapai 229,568 (99.73% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.73% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,034,400 | Volume total harian |
| Processed (P / XLA=S) | 3,010,796 | Sukses diproses (100.00%) |
| Unprocessed (U) | 23,602 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 230,187
- **FAH Success:** 230,066
- **FAH Error:** 121
- **Not Accounted:** 229,568
- **Posted GL:** 229,568 (99.73% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,333 | 121 | 228,735 | 228,735 | 0 |
| CROSS BORDER PAYMENT Custom Application | 519 | 0 | 519 | 519 | 0 |
| TRADE FINANCE Custom Application | 167 | 0 | 166 | 166 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 34 | 34 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,492,704 | 1,484,755 | 7,949 | 0.53% | 186,787,919,490,521.19 | Warning |
| DEP-NQ_ED2P_SC_BFST | 522,410 | 522,410 | 0 | 0.00% | 16,224,554,083,290.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 417,108 | 416,978 | 130 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 241,702 | 241,699 | 3 | 0.00% | 76,229,614,298,105.81 | Healthy |
| LON-Q_GLCP_GEND872 | 147,758 | 147,758 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 98,962 | 98,962 | 0 | 0.00% | 1,986,381,423.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 45,618 | 45,618 | 0 | 0.00% | 56,407,813,389,410.19 | Healthy |
| LON-NQ_ED2P_BORV | 17,255 | 5,657 | 11,598 | 67.22% | 12,277,625,292,894.62 | Critical |
| LON-Q_GLCP_GLIF | 11,887 | 11,727 | 160 | 1.35% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,694 | 11,694 | 0 | 0.00% | -1,659,131,937,643.20 | Healthy |

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
| efsdbslp02 | Database | 21.4% | 40.9% | 91.7% | 51.0% | 52.9% | 58.4% | 50.2% | 50.3% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.3% | 71.3% | 55.4% | 55.9% | 57.2% | 70.2% | 70.2% | 70.3% | Warning |
| efsdbsdr02 | Database | 2.5% | 6.8% | 54.9% | 49.4% | 49.7% | 50.4% | 43.3% | 43.4% | 43.8% | Healthy |
| ebsintslp02 | App | 3.3% | 14.4% | 85.0% | 43.6% | 45.8% | 50.7% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 28.8% | 61.1% | 98.9% | 50.0% | 54.5% | 60.9% | 44.1% | 56.0% | 65.5% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.8% | 5.0% | 5.2% | 6.4% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.0% | 5.2% | 5.3% | 6.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.8% | 14.8% | 79.4% | 50.4% | 52.6% | 57.4% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 23,602 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.73%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
