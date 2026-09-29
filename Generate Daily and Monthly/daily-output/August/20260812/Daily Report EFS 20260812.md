# EFS DAILY HEALTH REPORT
**Periode:** 12 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260812.xlsx, EFS_Infrastructures_20260812.xlsx, EFS_XLA_20260812.xlsx, EFS_GL_20260812.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,993,911
- **XLA Success Rate:** 99.90%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 24,436
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 24,436 records. GL Posted mencapai 222,307 (99.72% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 99.90% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.72% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,993,911 | Volume total harian |
| Processed (P / XLA=S) | 2,966,453 | Sukses diproses (99.90%) |
| Unprocessed (U) | 24,436 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 222,929
- **FAH Success:** 222,785
- **FAH Error:** 134
- **Not Accounted:** 222,307
- **Posted GL:** 222,307 (99.72% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 222,050 | 134 | 221,448 | 221,448 | 0 |
| CROSS BORDER PAYMENT Custom Application | 551 | 0 | 551 | 551 | 0 |
| TRADE FINANCE Custom Application | 164 | 0 | 164 | 164 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 34 | 34 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,480,022 | 1,469,003 | 7,999 | 0.54% | 170,251,528,419,029.84 | Warning |
| DEP-NQ_ED2P_SC_BFST | 493,791 | 493,791 | 0 | 0.00% | 15,119,591,149,222.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 418,606 | 418,458 | 148 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 233,023 | 233,018 | 5 | 0.00% | 69,012,094,923,484.22 | Healthy |
| LON-Q_GLCP_GEND872 | 150,114 | 150,112 | 2 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 107,255 | 107,255 | 0 | 0.00% | 3,385,899,416.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,257 | 43,257 | 0 | 0.00% | 42,983,315,127,068.92 | Healthy |
| LON-NQ_ED2P_BORV | 17,737 | 5,718 | 12,019 | 67.76% | 5,209,662,270,342.91 | Critical |
| LON-Q_GLCP_LOND2140 | 11,684 | 11,684 | 0 | 0.00% | 378,915,353,677.09 | Healthy |
| LON-Q_GLCP_GLIF | 11,623 | 11,477 | 146 | 1.26% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 22.5% | 42.5% | 94.5% | 51.1% | 53.1% | 57.7% | 50.3% | 50.4% | 51.0% | Critical |
| efsdbsdr01 | Database | 33.3% | 40.8% | 77.6% | 55.7% | 56.4% | 57.2% | 70.2% | 70.2% | 70.7% | Warning |
| efsdbsdr02 | Database | 2.9% | 8.9% | 27.5% | 49.6% | 49.9% | 50.7% | 43.4% | 43.4% | 43.6% | Healthy |
| efsdbslp01 | Database | 20.1% | 45.1% | 94.8% | 50.1% | 52.4% | 56.2% | 49.8% | 56.1% | 66.1% | Critical |
| ebsintslp02 | App | 3.1% | 32.4% | 94.6% | 43.8% | 46.0% | 50.4% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 80.8% | 4.9% | 5.2% | 6.6% | 24.3% | 24.4% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 85.3% | 5.2% | 5.4% | 6.4% | 41.2% | 41.2% | 41.5% | Critical |
| ebsintslp01 | App | 4.0% | 23.8% | 89.1% | 50.6% | 52.7% | 56.8% | 15.8% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 24,436 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.72%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
