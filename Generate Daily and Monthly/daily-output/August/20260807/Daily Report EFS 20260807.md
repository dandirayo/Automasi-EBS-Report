# EFS DAILY HEALTH REPORT
**Periode:** 7 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260807.xlsx, EFS_Infrastructures_20260807.xlsx, EFS_XLA_20260807.xlsx, EFS_GL_20260807.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,102,871
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 23,228
- **Infrastruktur Status:** 6 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 23,228 records. GL Posted mencapai 229,727 (99.72% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
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
| Total Records | 3,102,871 | Volume total harian |
| Processed (P / XLA=S) | 3,079,641 | Sukses diproses (100.00%) |
| Unprocessed (U) | 23,228 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 230,362
- **FAH Success:** 230,209
- **FAH Error:** 138
- **Not Accounted:** 229,732
- **Posted GL:** 229,727 (99.72% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 229,614 | 138 | 229,003 | 228,998 | 0 |
| CROSS BORDER PAYMENT Custom Application | 416 | 0 | 416 | 416 | 0 |
| TRADE FINANCE Custom Application | 169 | 0 | 169 | 169 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 34 | 34 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,541,741 | 1,533,293 | 8,448 | 0.55% | 210,005,345,628,432.97 | Warning |
| DEP-NQ_ED2P_SC_BFST | 534,251 | 534,251 | 0 | 0.00% | 17,641,196,419,806.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 417,030 | 416,888 | 142 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 243,704 | 243,699 | 5 | 0.00% | 87,148,882,771,246.83 | Healthy |
| LON-Q_GLCP_GEND872 | 149,098 | 149,098 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 99,586 | 99,586 | 0 | 0.00% | 1,997,542,733.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 49,956 | 49,956 | 0 | 0.00% | 72,163,799,908,502.30 | Healthy |
| LON-NQ_ED2P_BORV | 16,152 | 5,359 | 10,793 | 66.82% | 4,781,056,832,332.27 | Critical |
| LON-Q_GLCP_LOND2140 | 11,680 | 11,680 | 0 | 0.00% | 18,071,371,758.76 | Healthy |
| LON-Q_GLCP_GLIF | 11,045 | 10,851 | 194 | 1.76% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 15.3% | 39.8% | 94.1% | 49.7% | 51.3% | 55.2% | 50.3% | 50.3% | 50.4% | Critical |
| efsdbsdr01 | Database | 33.2% | 42.0% | 73.5% | 53.8% | 54.4% | 55.8% | 70.2% | 70.3% | 71.0% | Warning |
| efsdbsdr02 | Database | 2.8% | 11.9% | 47.3% | 49.1% | 49.6% | 51.4% | 43.3% | 43.4% | 43.5% | Healthy |
| efsdbslp01 | Database | 3.4% | 35.1% | 92.8% | 49.8% | 52.0% | 56.1% | 49.6% | 57.2% | 62.2% | Critical |
| ebsintslp02 | App | 3.5% | 14.1% | 86.5% | 43.0% | 45.0% | 49.8% | 10.7% | 10.7% | 10.7% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.4% | 4.8% | 5.0% | 6.1% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.1% | 81.5% | 4.7% | 4.9% | 6.2% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintslp01 | App | 3.7% | 14.2% | 84.1% | 50.0% | 52.2% | 57.4% | 15.8% | 15.9% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 23,228 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
