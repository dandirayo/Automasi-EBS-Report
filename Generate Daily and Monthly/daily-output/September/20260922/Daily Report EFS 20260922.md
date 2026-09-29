# EFS DAILY HEALTH REPORT
**Periode:** 22 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260922.xlsx, EFS_Infrastructures_20260922.xlsx, EFS_XLA_20260922.xlsx, EFS_GL_20260922.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,784,725
- **XLA Success Rate:** 82.30%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 207,175
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 207,175 records. GL Posted mencapai 153,431 (99.59% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 82.30% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.59% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,784,725 | Volume total harian |
| Processed (P / XLA=S) | 1,465,600 | Sukses diproses (82.30%) |
| Unprocessed (U) | 207,175 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 154,067
- **FAH Success:** 153,808
- **FAH Error:** 247
- **Not Accounted:** 153,431
- **Posted GL:** 153,431 (99.59% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 152,991 | 171 | 152,501 | 152,501 | 0 |
| CROSS BORDER PAYMENT Custom Application | 707 | 0 | 707 | 707 | 0 |
| TRADE FINANCE Custom Application | 197 | 0 | 197 | 197 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 70 | 0 | 0 | 0 | 0 |
| TREASURY Custom Application | 11 | 0 | 11 | 11 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 924,369 | 719,884 | 204,485 | 22.12% | 221,945,150,481,274.28 | Critical |
| DEP-NQ_ED2P_SC_BFST | 320,473 | 252,114 | 0 | 0.00% | 13,290,403,911,263.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,450 | 176,448 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 147,336 | 147,336 | 0 | 0.00% | 59,281,702,949,176.59 | Healthy |
| LON-Q_GLCP_GEND872 | 73,876 | 73,586 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 61,270 | 44,559 | 0 | 0.00% | 1,314,138,505.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 34,524 | 30,502 | 0 | 0.00% | 58,335,224,160,934.06 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,849 | 5,849 | 0 | 0.00% | -41,992,416,722,574.35 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,705 | 5,705 | 0 | 0.00% | 61,213,425,359,466.66 | Healthy |
| LON-NQ_ED2P_BORV | 4,725 | 1,259 | 1,711 | 36.21% | 6,505,665,281,756.50 | Critical |

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
| efsdbslp02 | Database | 11.1% | 35.0% | 91.4% | 61.2% | 63.4% | 67.6% | 51.5% | 51.5% | 52.0% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.1% | 29.5% | 68.5% | 68.9% | 69.3% | 70.6% | 70.6% | 70.8% | Warning |
| efsdbsdr02 | Database | 0.9% | 2.3% | 44.3% | 50.3% | 50.7% | 51.5% | 43.8% | 43.8% | 44.1% | Healthy |
| ebsintslp02 | App | 2.5% | 11.0% | 98.3% | 43.9% | 47.0% | 53.8% | 10.7% | 10.8% | 11.3% | Critical |
| efsdbslp01 | Database | 9.9% | 46.3% | 97.6% | 57.9% | 61.0% | 67.4% | 47.3% | 55.6% | 66.5% | Critical |
| ebsintsdr01 | App | 0.5% | 1.5% | 65.5% | 7.3% | 7.6% | 8.7% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.8% | 7.2% | 7.3% | 8.8% | 24.4% | 24.4% | 25.5% | Warning |
| ebsintslp01 | App | 2.7% | 11.0% | 74.1% | 50.9% | 53.5% | 60.6% | 15.8% | 15.9% | 16.5% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 207,175 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.59%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
