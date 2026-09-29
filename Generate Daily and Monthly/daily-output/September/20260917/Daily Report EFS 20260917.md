# EFS DAILY HEALTH REPORT
**Periode:** 17 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260917.xlsx, EFS_Infrastructures_20260917.xlsx, EFS_XLA_20260917.xlsx, EFS_GL_20260917.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,549,822
- **XLA Success Rate:** 98.59%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,599
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,599 records. GL Posted mencapai 139,057 (99.53% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 98.59% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.53% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,549,822 | Volume total harian |
| Processed (P / XLA=S) | 1,525,117 | Sukses diproses (98.59%) |
| Unprocessed (U) | 5,599 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 139,718
- **FAH Success:** 139,436
- **FAH Error:** 194
- **Not Accounted:** 139,091
- **Posted GL:** 139,057 (99.53% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 138,779 | 118 | 138,307 | 138,273 | 0 |
| CROSS BORDER PAYMENT Custom Application | 579 | 0 | 579 | 579 | 0 |
| TRADE FINANCE Custom Application | 174 | 0 | 166 | 166 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 69 | 0 | 0 | 0 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 7 | 0 | 7 | 7 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 778,292 | 777,783 | 509 | 0.07% | 179,415,624,288,362.47 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 269,020 | 269,020 | 0 | 0.00% | 11,755,015,748,434.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,358 | 175,536 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 120,396 | 120,396 | 0 | 0.00% | 39,516,821,238,942.26 | Healthy |
| LON-Q_GLCP_GEND872 | 73,768 | 73,484 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 52,171 | 52,171 | 0 | 0.00% | 1,166,004,475.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 35,723 | 35,723 | 0 | 0.00% | 58,688,591,884,384.28 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 5,813 | 5,813 | 0 | 0.00% | 62,277,215,854,939.51 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,809 | 5,809 | 0 | 0.00% | -42,936,008,987,893.03 | Healthy |
| LON-NQ_ED2P_BORV | 4,345 | 1,717 | 2,628 | 60.48% | 3,094,832,794,864.15 | Critical |

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
| efsdbslp02 | Database | 10.2% | 31.6% | 82.5% | 60.4% | 62.6% | 66.8% | 51.3% | 51.4% | 51.8% | Critical |
| efsdbsdr01 | Database | 13.4% | 15.1% | 32.9% | 67.2% | 67.6% | 68.5% | 70.5% | 70.6% | 70.6% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.9% | 25.9% | 50.3% | 50.8% | 52.1% | 43.7% | 43.8% | 44.1% | Healthy |
| ebsintslp02 | App | 2.4% | 9.9% | 97.8% | 44.0% | 46.4% | 51.3% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 6.6% | 39.0% | 95.9% | 56.8% | 59.8% | 64.5% | 46.8% | 59.2% | 66.9% | Critical |
| ebsintsdr01 | App | 0.5% | 1.5% | 69.4% | 7.2% | 7.5% | 8.5% | 41.3% | 41.3% | 42.1% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 61.9% | 7.2% | 7.4% | 8.9% | 24.4% | 24.4% | 25.5% | Warning |
| ebsintslp01 | App | 2.6% | 10.0% | 66.2% | 50.0% | 52.6% | 57.8% | 15.8% | 15.8% | 15.8% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,599 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.53%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
