# EFS DAILY HEALTH REPORT
**Periode:** 6 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260806.xlsx, EFS_Infrastructures_20260806.xlsx, EFS_XLA_20260806.xlsx, EFS_GL_20260806.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,083,634
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,925
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,925 records. GL Posted mencapai 227,156 (99.80% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.80% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,083,634 | Volume total harian |
| Processed (P / XLA=S) | 3,060,707 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,925 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 227,614
- **FAH Success:** 227,612
- **FAH Error:** 2
- **Not Accounted:** 227,156
- **Posted GL:** 227,156 (99.80% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 226,793 | 2 | 226,354 | 226,354 | 0 |
| CROSS BORDER PAYMENT Custom Application | 503 | 0 | 503 | 503 | 0 |
| TRADE FINANCE Custom Application | 151 | 0 | 151 | 151 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 52 | 0 | 35 | 35 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,535,770 | 1,527,213 | 8,557 | 0.56% | 246,094,759,258,274.72 | Warning |
| DEP-NQ_ED2P_SC_BFST | 515,565 | 515,565 | 0 | 0.00% | 15,989,687,909,918.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 415,494 | 415,374 | 120 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 239,760 | 239,756 | 4 | 0.00% | 108,365,143,475,049.72 | Healthy |
| LON-Q_GLCP_GEND872 | 149,266 | 149,266 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 118,354 | 118,354 | 0 | 0.00% | 2,404,534,370.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 44,667 | 44,667 | 0 | 0.00% | 62,668,804,976,243.58 | Healthy |
| LON-NQ_ED2P_BORV | 15,795 | 5,165 | 10,630 | 67.30% | 2,833,540,778,197.02 | Critical |
| LON-Q_GLCP_LOND2140 | 11,658 | 11,658 | 0 | 0.00% | -191,308,631,301.42 | Healthy |
| LON-Q_GLCP_GLIF | 10,932 | 10,766 | 166 | 1.52% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 17.7% | 40.7% | 93.1% | 48.8% | 51.0% | 55.1% | 50.2% | 50.3% | 50.5% | Critical |
| efsdbsdr01 | Database | 33.3% | 40.8% | 72.4% | 53.2% | 54.0% | 55.3% | 70.2% | 70.3% | 70.7% | Warning |
| efsdbsdr02 | Database | 2.9% | 9.0% | 29.0% | 48.9% | 49.4% | 50.2% | 43.3% | 43.3% | 43.5% | Healthy |
| efsdbslp01 | Database | 3.4% | 32.0% | 91.2% | 49.9% | 52.0% | 58.2% | 49.9% | 56.7% | 61.5% | Critical |
| ebsintslp02 | App | 3.3% | 13.7% | 86.5% | 43.0% | 45.0% | 49.7% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 80.6% | 4.5% | 4.9% | 6.2% | 24.3% | 24.3% | 25.0% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.4% | 4.8% | 5.0% | 6.0% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.7% | 14.4% | 78.3% | 49.9% | 52.1% | 57.1% | 15.8% | 15.9% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,925 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.80%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
