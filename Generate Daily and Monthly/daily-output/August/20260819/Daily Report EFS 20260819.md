# EFS DAILY HEALTH REPORT
**Periode:** 19 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260819.xlsx, EFS_Infrastructures_20260819.xlsx, EFS_XLA_20260819.xlsx, EFS_GL_20260819.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,486,091
- **XLA Success Rate:** 16.46%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 94
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 94 records. GL Posted mencapai 17,149 (7.66% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 16.46% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 7.66% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,486,091 | Volume total harian |
| Processed (P / XLA=S) | 409,018 | Sukses diproses (16.46%) |
| Unprocessed (U) | 94 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 223,895
- **FAH Success:** 17,274
- **FAH Error:** 145
- **Not Accounted:** 17,149
- **Posted GL:** 17,149 (7.66% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 222,989 | 69 | 16,340 | 16,340 | 0 |
| CROSS BORDER PAYMENT Custom Application | 547 | 0 | 547 | 547 | 0 |
| TRADE FINANCE Custom Application | 194 | 0 | 194 | 194 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,354,344 | 79,217 | 85 | 0.01% | 156,916,151,967,790.88 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 480,064 | 49,036 | 0 | 0.00% | 15,116,207,424,731.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 224,559 | 0 | 0 | 0.00% | 40,389,654,644,961.24 | Healthy |
| DEP-Q_GLCP_GEND870 | 193,860 | 193,860 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 88,077 | 6,283 | 0 | 0.00% | 1,754,177,061.00 | Healthy |
| LON-Q_GLCP_GEND872 | 72,798 | 72,798 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 43,188 | 215 | 0 | 0.00% | 48,512,455,870,027.55 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,119 | 0 | 0 | 0.00% | 52,940,620,406,886.16 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,891 | 5,891 | 0 | 0.00% | -38,739,308,566,957.02 | Healthy |
| LON-NQ_ED2P_BORV | 4,678 | 76 | 1 | 0.02% | 3,586,525,212,682.88 | Healthy |

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
| efsdbslp02 | Database | 27.2% | 53.0% | 92.6% | 54.0% | 56.6% | 61.8% | 50.4% | 50.4% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.2% | 76.7% | 57.9% | 58.6% | 59.6% | 70.2% | 70.2% | 70.4% | Warning |
| efsdbsdr02 | Database | 2.6% | 10.7% | 36.3% | 49.8% | 50.1% | 50.9% | 43.4% | 43.5% | 43.5% | Healthy |
| ebsintslp02 | App | 3.4% | 15.9% | 96.9% | 43.7% | 46.7% | 53.4% | 10.7% | 10.7% | 10.9% | Critical |
| efsdbslp01 | Database | 10.5% | 39.1% | 94.4% | 51.8% | 54.4% | 59.5% | 55.2% | 59.5% | 67.0% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.7% | 5.5% | 5.6% | 6.9% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.2% | 87.2% | 5.7% | 5.8% | 6.8% | 41.2% | 41.2% | 42.0% | Critical |
| ebsintslp01 | App | 4.1% | 16.4% | 91.6% | 50.3% | 53.2% | 58.9% | 15.9% | 15.9% | 16.3% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 94 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 7.66%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
