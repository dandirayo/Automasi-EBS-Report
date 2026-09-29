# EFS DAILY HEALTH REPORT
**Periode:** 29 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260829.xlsx, EFS_Infrastructures_20260829.xlsx, EFS_XLA_20260829.xlsx, EFS_GL_20260829.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,825,662
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 27,256
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 27,256 records. GL Posted mencapai 201,840 (99.38% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.38% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,825,662 | Volume total harian |
| Processed (P / XLA=S) | 2,798,404 | Sukses diproses (100.00%) |
| Unprocessed (U) | 27,256 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 203,098
- **FAH Success:** 202,011
- **FAH Error:** 78
- **Not Accounted:** 201,937
- **Posted GL:** 201,840 (99.38% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 202,184 | 2 | 201,120 | 201,023 | 0 |
| CROSS BORDER PAYMENT Custom Application | 560 | 0 | 560 | 560 | 0 |
| TRADE FINANCE Custom Application | 190 | 0 | 188 | 188 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 32 | 32 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,395,409 | 1,387,898 | 7,511 | 0.54% | 23,200,915,461,363.79 | Warning |
| DEP-NQ_ED2P_SC_BFST | 458,008 | 458,008 | 0 | 0.00% | 13,190,768,556,604.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 422,025 | 421,871 | 154 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 227,388 | 227,388 | 0 | 0.00% | 5,678,700,311,342.90 | Healthy |
| LON-Q_GLCP_GEND872 | 151,998 | 151,992 | 6 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 111,997 | 111,997 | 0 | 0.00% | 2,235,578,965.00 | Healthy |
| LON-NQ_ED2P_BORV | 22,712 | 6,795 | 15,917 | 70.08% | 461,840,894,171.76 | Critical |
| LON-Q_GLCP_GLIF | 11,955 | 11,955 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,352 | 11,352 | 0 | 0.00% | -106,428,028,158.52 | Healthy |
| LON-Q_GLCP_BORV | 3,879 | 213 | 3,666 | 94.51% | 241,569,498,012.00 | Critical |

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
| efsdbslp02 | Database | 23.4% | 41.8% | 91.0% | 56.7% | 57.2% | 57.9% | 50.6% | 50.6% | 50.7% | Critical |
| efsdbsdr01 | Database | 39.5% | 41.4% | 79.1% | 61.2% | 61.5% | 63.3% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.7% | 6.4% | 27.8% | 49.9% | 50.1% | 50.7% | 43.5% | 43.6% | 43.6% | Healthy |
| ebsintslp02 | App | 3.7% | 8.9% | 98.6% | 42.6% | 43.0% | 45.6% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 16.6% | 34.6% | 99.0% | 54.2% | 54.7% | 55.9% | 45.7% | 54.5% | 62.7% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.1% | 5.9% | 6.2% | 7.6% | 24.3% | 24.3% | 24.9% | Critical |
| ebsintsdr01 | App | 0.8% | 2.2% | 87.0% | 6.2% | 6.5% | 7.8% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintslp01 | App | 4.1% | 8.5% | 72.2% | 47.3% | 47.8% | 49.8% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 27,256 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.38%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
