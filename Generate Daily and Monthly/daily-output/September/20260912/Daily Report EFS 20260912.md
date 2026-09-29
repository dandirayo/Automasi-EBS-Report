# EFS DAILY HEALTH REPORT
**Periode:** 12 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260912.xlsx, EFS_Infrastructures_20260912.xlsx, EFS_XLA_20260912.xlsx, EFS_GL_20260912.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,852,387
- **XLA Success Rate:** 85.51%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 590
- **Infrastruktur Status:** 4 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 590 records. GL Posted mencapai 148,257 (98.76% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 85.51% | WARNING |
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
| Total Records | 1,852,387 | Volume total harian |
| Processed (P / XLA=S) | 1,584,013 | Sukses diproses (85.51%) |
| Unprocessed (U) | 590 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 150,118
- **FAH Success:** 148,524
- **FAH Error:** 78
- **Not Accounted:** 148,257
- **Posted GL:** 148,257 (98.76% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 149,225 | 2 | 147,573 | 147,573 | 0 |
| CROSS BORDER PAYMENT Custom Application | 451 | 0 | 451 | 451 | 0 |
| TRADE FINANCE Custom Application | 212 | 0 | 195 | 195 | 0 |
| CREDIT CARD Custom Application | 114 | 0 | 0 | 0 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,055,192 | 867,298 | 565 | 0.05% | 22,289,615,393,434.61 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 243,975 | 179,583 | 0 | 0.00% | 9,943,804,525,523.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,243 | 195,243 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 155,848 | 155,848 | 0 | 0.00% | 5,782,663,277,969.95 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 115,734 | 100,270 | 0 | 0.00% | 3,042,937,297.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,698 | 73,698 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,789 | 5,789 | 0 | 0.00% | -43,188,559,755,147.40 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,765 | 2,215 | 0 | 0.00% | 70,097,226,448.55 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,752 | 2,752 | 0 | 0.00% | 14,163,539,617.91 | Healthy |
| BRA-NQ_ED2P_ELOG | 568 | 568 | 0 | 0.00% | 406,636,026,761.00 | Healthy |

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
| efsdbslp02 | Database | 9.6% | 16.6% | 82.1% | 59.5% | 59.9% | 61.0% | 51.1% | 51.1% | 51.2% | Critical |
| efsdbsdr01 | Database | 13.3% | 14.8% | 30.4% | 65.8% | 66.2% | 66.7% | 70.4% | 70.5% | 70.7% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.5% | 17.4% | 50.4% | 50.8% | 51.6% | 43.7% | 43.7% | 44.1% | Healthy |
| ebsintslp02 | App | 3.7% | 12.7% | 98.0% | 43.5% | 43.8% | 46.3% | 10.8% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 5.9% | 15.7% | 74.6% | 56.5% | 57.2% | 58.2% | 48.5% | 58.0% | 66.4% | Warning |
| ebsintsdr01 | App | 0.8% | 2.0% | 86.6% | 7.3% | 7.5% | 8.4% | 41.3% | 41.3% | 42.4% | Critical |
| ebsintsdr02 | App | 0.9% | 2.1% | 82.1% | 7.0% | 7.2% | 8.6% | 24.4% | 24.4% | 25.5% | Critical |
| ebsintslp01 | App | 3.8% | 8.1% | 72.7% | 49.7% | 50.1% | 51.9% | 15.8% | 15.9% | 16.0% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 590 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
