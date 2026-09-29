# EFS DAILY HEALTH REPORT
**Periode:** 10 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260810.xlsx, EFS_Infrastructures_20260810.xlsx, EFS_XLA_20260810.xlsx, EFS_GL_20260810.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 3,169,786
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 43,337
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 43,337 records. GL Posted mencapai 231,382 (99.77% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.77% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 3,169,786 | Volume total harian |
| Processed (P / XLA=S) | 3,126,447 | Sukses diproses (100.00%) |
| Unprocessed (U) | 43,337 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 231,911
- **FAH Success:** 231,791
- **FAH Error:** 120
- **Not Accounted:** 231,382
- **Posted GL:** 231,382 (99.77% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 231,715 | 120 | 231,188 | 231,188 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CROSS BORDER PAYMENT Custom Application | 66 | 0 | 66 | 66 | 0 |
| CREDIT CARD Custom Application | 38 | 0 | 38 | 38 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 1 | 0 | 1 | 1 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,555,516 | 1,547,157 | 8,359 | 0.54% | 299,768,445,766,894.31 | Warning |
| DEP-NQ_ED2P_SC_BFST | 537,979 | 537,979 | 0 | 0.00% | 18,411,256,086,876.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 416,992 | 416,864 | 128 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 245,141 | 245,138 | 3 | 0.00% | 115,732,282,319,280.48 | Healthy |
| LON-Q_GLCP_GEND872 | 159,318 | 157,709 | 1,609 | 1.01% | 0.00 | Warning |
| DEP-NQ_ED2P_SC_ELOG | 102,102 | 102,102 | 0 | 0.00% | 2,142,570,632.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 54,473 | 54,473 | 0 | 0.00% | 78,642,828,782,836.78 | Healthy |
| LON-NQ_ED2P_BORV | 30,860 | 8,949 | 21,911 | 71.00% | 3,669,177,285,279.15 | Critical |
| LON-Q_GLCP_GLIF | 17,693 | 17,511 | 182 | 1.03% | 0.00 | Healthy |
| LON-Q_GLCP_BORV | 14,662 | 3,698 | 10,964 | 74.78% | 4,786,918,752,679.34 | Critical |

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
| efsdbslp02 | Database | 22.7% | 45.1% | 88.4% | 50.9% | 52.8% | 56.3% | 50.2% | 50.3% | 50.6% | Critical |
| efsdbsdr01 | Database | 33.2% | 37.7% | 78.2% | 55.0% | 55.5% | 56.4% | 70.2% | 70.2% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.5% | 10.9% | 36.8% | 49.4% | 49.9% | 50.8% | 43.4% | 43.4% | 43.6% | Healthy |
| ebsintslp02 | App | 3.2% | 14.4% | 86.3% | 43.2% | 45.4% | 50.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 22.3% | 51.0% | 96.3% | 51.7% | 54.0% | 58.5% | 52.6% | 57.7% | 65.5% | Critical |
| ebsintsdr02 | App | 0.9% | 2.0% | 81.6% | 4.8% | 5.1% | 6.4% | 24.3% | 24.3% | 24.6% | Critical |
| ebsintsdr01 | App | 0.8% | 2.1% | 86.0% | 5.1% | 5.2% | 6.2% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 3.8% | 15.0% | 79.4% | 50.2% | 52.3% | 57.1% | 15.8% | 15.9% | 16.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 43,337 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.77%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
