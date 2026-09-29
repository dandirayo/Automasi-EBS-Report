# EFS DAILY HEALTH REPORT
**Periode:** 11 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260911.xlsx, EFS_Infrastructures_20260911.xlsx, EFS_XLA_20260911.xlsx, EFS_GL_20260911.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,349,901
- **XLA Success Rate:** 85.22%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 6,286
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 6,286 records. GL Posted mencapai 230,987 (98.76% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 85.22% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.76% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,349,901 | Volume total harian |
| Processed (P / XLA=S) | 1,996,296 | Sukses diproses (85.22%) |
| Unprocessed (U) | 6,286 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 233,882
- **FAH Success:** 231,474
- **FAH Error:** 146
- **Not Accounted:** 230,987
- **Posted GL:** 230,987 (98.76% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 232,528 | 70 | 229,792 | 229,792 | 0 |
| CROSS BORDER PAYMENT Custom Application | 974 | 0 | 974 | 974 | 0 |
| TRADE FINANCE Custom Application | 170 | 0 | 155 | 155 | 0 |
| CREDIT CARD Custom Application | 99 | 0 | 33 | 33 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,387,216 | 1,095,865 | 868 | 0.06% | 200,811,199,051,885.19 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 491,063 | 443,455 | 0 | 0.00% | 16,829,366,659,874.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 227,226 | 227,226 | 0 | 0.00% | 36,471,942,188,863.60 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,337 | 84,699 | 0 | 0.00% | 1,834,142,594.00 | Healthy |
| LON-Q_GLCP_GEND872 | 71,616 | 71,616 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 46,754 | 46,350 | 0 | 0.00% | 52,601,805,784,412.71 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,259 | 7,259 | 0 | 0.00% | 68,635,012,444,813.45 | Healthy |
| LON-NQ_ED2P_BORV | 6,033 | 2,387 | 3,547 | 58.79% | 5,871,738,575,164.41 | Critical |
| LON-Q_GLCP_BORV | 5,794 | 3,979 | 1,731 | 29.88% | 4,792,302,555,208.06 | Critical |
| LON-Q_GLCP_LOND2140 | 5,781 | 5,781 | 0 | 0.00% | -42,593,095,015,818.39 | Healthy |

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
| efsdbslp02 | Database | 13.0% | 26.5% | 69.4% | 59.7% | 61.5% | 65.6% | 51.1% | 51.1% | 51.6% | Warning |
| efsdbsdr01 | Database | 13.3% | 15.2% | 28.4% | 65.7% | 66.2% | 67.3% | 70.4% | 70.5% | 70.5% | Warning |
| efsdbsdr02 | Database | 0.9% | 3.1% | 17.0% | 50.3% | 50.7% | 51.9% | 43.7% | 43.7% | 44.1% | Healthy |
| ebsintslp02 | App | 20.1% | 30.9% | 99.3% | 41.5% | 44.3% | 50.1% | 10.7% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 6.0% | 27.4% | 88.5% | 56.4% | 59.3% | 64.1% | 46.1% | 56.3% | 64.1% | Critical |
| ebsintsdr02 | App | 0.9% | 2.3% | 80.7% | 6.9% | 7.2% | 8.5% | 24.4% | 24.4% | 25.5% | Critical |
| ebsintsdr01 | App | 0.8% | 2.2% | 85.6% | 7.2% | 7.5% | 8.4% | 41.3% | 41.3% | 41.8% | Critical |
| ebsintslp01 | App | 3.7% | 14.7% | 86.7% | 49.4% | 51.7% | 56.1% | 15.8% | 15.9% | 16.0% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 6,286 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.76%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
