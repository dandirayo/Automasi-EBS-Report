# EFS DAILY HEALTH REPORT
**Periode:** 4 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260904.xlsx, EFS_Infrastructures_20260904.xlsx, EFS_XLA_20260904.xlsx, EFS_GL_20260904.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,403,145
- **XLA Success Rate:** 91.47%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,793
- **Infrastruktur Status:** 6 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,793 records. GL Posted mencapai 217,743 (98.50% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 91.47% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.50% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,403,145 | Volume total harian |
| Processed (P / XLA=S) | 2,192,612 | Sukses diproses (91.47%) |
| Unprocessed (U) | 5,793 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 221,054
- **FAH Success:** 218,200
- **FAH Error:** 1,127
- **Not Accounted:** 217,743
- **Posted GL:** 217,743 (98.50% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 220,439 | 1,050 | 217,207 | 217,207 | 0 |
| CROSS BORDER PAYMENT Custom Application | 489 | 1 | 488 | 488 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 26 | 0 | 26 | 26 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,496,531 | 1,353,624 | 664 | 0.04% | 190,357,258,360,539.53 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 487,417 | 436,546 | 0 | 0.00% | 14,328,029,527,574.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 233,472 | 233,472 | 0 | 0.00% | 47,135,540,693,159.73 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 110,775 | 101,327 | 0 | 0.00% | 2,410,007,670.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 48,394 | 46,702 | 0 | 0.00% | 55,651,190,564,905.95 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,696 | 7,447 | 249 | 3.24% | 60,094,440,915,245.27 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,735 | 5,393 | 0 | 0.00% | 2,263,775,616,026.01 | Healthy |
| LON-NQ_ED2P_BORV | 5,490 | 2,236 | 3,253 | 59.25% | 3,837,128,026,092.57 | Critical |
| LON-Q_GLCP_BORV | 5,098 | 3,608 | 1,480 | 29.03% | 4,821,551,437,490.40 | Critical |
| BRA-NQ_ED2P_ELOG | 861 | 861 | 0 | 0.00% | 401,176,241,355.00 | Healthy |

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
| efsdbslp02 | Database | 14.7% | 34.5% | 84.1% | 58.1% | 60.3% | 64.9% | 51.0% | 51.0% | 51.6% | Critical |
| efsdbsdr01 | Database | 19.9% | 20.9% | 42.0% | 63.6% | 64.0% | 64.8% | 70.3% | 70.4% | 70.4% | Warning |
| efsdbsdr02 | Database | 1.2% | 3.4% | 62.0% | 50.1% | 50.4% | 51.2% | 43.6% | 43.6% | 44.0% | Warning |
| ebsintslp02 | App | 3.2% | 12.7% | 97.2% | 44.8% | 46.4% | 50.7% | 10.7% | 10.8% | 11.3% | Critical |
| efsdbslp01 | Database | 9.6% | 32.0% | 90.2% | 55.5% | 57.7% | 62.3% | 50.6% | 58.5% | 64.0% | Critical |
| ebsintsdr01 | App | 0.8% | 2.0% | 86.8% | 6.7% | 6.9% | 7.9% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 82.3% | 6.5% | 6.7% | 8.0% | 24.4% | 24.4% | 24.8% | Critical |
| ebsintslp01 | App | 20.7% | 31.0% | 93.3% | 50.3% | 52.9% | 59.0% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,793 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.50%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
