# EFS DAILY HEALTH REPORT
**Periode:** 8 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260808.xlsx, EFS_Infrastructures_20260808.xlsx, EFS_XLA_20260808.xlsx, EFS_GL_20260808.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,853,043
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,143
- **Infrastruktur Status:** 5 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,143 records. GL Posted mencapai 204,596 (99.81% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.81% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,853,043 | Volume total harian |
| Processed (P / XLA=S) | 2,834,898 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,143 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 204,977
- **FAH Success:** 204,975
- **FAH Error:** 2
- **Not Accounted:** 204,804
- **Posted GL:** 204,596 (99.81% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 204,135 | 2 | 203,982 | 203,774 | 207 |
| CROSS BORDER PAYMENT Custom Application | 489 | 0 | 489 | 489 | 0 |
| TRADE FINANCE Custom Application | 189 | 0 | 189 | 189 | 0 |
| PSAK 71 Custom Application | 76 | 0 | 76 | 76 | 0 |
| CREDIT CARD Custom Application | 53 | 0 | 35 | 35 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,414,265 | 1,406,361 | 7,904 | 0.56% | 23,401,647,206,796.93 | Warning |
| DEP-NQ_ED2P_SC_BFST | 507,021 | 507,021 | 0 | 0.00% | 13,031,355,355,438.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 416,515 | 416,409 | 106 | 0.03% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 229,860 | 229,860 | 0 | 0.00% | 5,648,976,018,871.61 | Healthy |
| LON-Q_GLCP_GEND872 | 149,500 | 149,498 | 2 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 97,230 | 97,230 | 0 | 0.00% | 1,747,164,150.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,694 | 11,694 | 0 | 0.00% | -3,267,123,669.18 | Healthy |
| LON-NQ_ED2P_BORV | 11,024 | 3,250 | 7,774 | 70.52% | 243,176,002,645.35 | Critical |
| LON-Q_GLCP_GLIF | 4,583 | 4,583 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,138 | 3,138 | 0 | 0.00% | 65,880,983,047.22 | Healthy |

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
| efsdbslp02 | Database | 16.2% | 32.7% | 90.9% | 49.7% | 50.4% | 51.4% | 50.4% | 50.4% | 50.4% | Critical |
| efsdbsdr01 | Database | 33.2% | 38.2% | 64.4% | 54.2% | 54.6% | 55.2% | 70.2% | 70.3% | 70.8% | Warning |
| efsdbsdr02 | Database | 2.5% | 6.5% | 29.1% | 49.2% | 49.4% | 50.3% | 43.3% | 43.4% | 43.8% | Healthy |
| ebsintslp02 | App | 3.3% | 7.8% | 87.2% | 43.1% | 43.4% | 44.8% | 10.6% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 9.9% | 27.0% | 93.6% | 50.4% | 50.8% | 52.0% | 52.0% | 56.2% | 60.3% | Critical |
| ebsintsdr01 | App | 0.7% | 2.1% | 86.1% | 4.8% | 5.1% | 6.1% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 81.2% | 4.8% | 5.0% | 6.3% | 24.3% | 24.3% | 24.7% | Critical |
| ebsintslp01 | App | 3.9% | 7.8% | 70.9% | 50.2% | 50.5% | 51.3% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,143 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.81%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
