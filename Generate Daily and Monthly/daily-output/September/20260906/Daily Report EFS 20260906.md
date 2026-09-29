# EFS DAILY HEALTH REPORT
**Periode:** 6 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260906.xlsx, EFS_Infrastructures_20260906.xlsx, EFS_XLA_20260906.xlsx, EFS_GL_20260906.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,761,312
- **XLA Success Rate:** 98.91%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 462
- **Infrastruktur Status:** 3 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 462 records. GL Posted mencapai 171,592 (99.49% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 98.91% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.49% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,761,312 | Volume total harian |
| Processed (P / XLA=S) | 1,741,683 | Sukses diproses (98.91%) |
| Unprocessed (U) | 462 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 172,480
- **FAH Success:** 171,689
- **FAH Error:** 769
- **Not Accounted:** 171,594
- **Posted GL:** 171,592 (99.49% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 171,800 | 693 | 170,992 | 170,990 | 0 |
| CROSS BORDER PAYMENT Custom Application | 570 | 0 | 570 | 570 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 17 | 17 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 924,547 | 923,444 | 450 | 0.05% | 17,440,767,306,324.53 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 329,635 | 329,635 | 0 | 0.00% | 8,690,350,354,358.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 192,940 | 174,906 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 149,598 | 149,570 | 0 | 0.00% | 4,729,483,843,419.95 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 78,460 | 78,421 | 0 | 0.00% | 1,620,625,895.00 | Healthy |
| LON-Q_GLCP_GEND872 | 73,564 | 73,280 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,744 | 5,744 | 0 | 0.00% | -41,993,677,159,395.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,602 | 3,508 | 0 | 0.00% | 96,602,637,690.64 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,278 | 2,278 | 0 | 0.00% | 7,602,851,736.83 | Healthy |
| BRA-NQ_ED2P_ELOG | 570 | 545 | 0 | 0.00% | 388,587,083,045.00 | Healthy |

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
| efsdbslp02 | Database | 12.0% | 20.4% | 57.9% | 57.9% | 58.4% | 59.0% | 50.9% | 51.0% | 51.1% | Healthy |
| efsdbsdr01 | Database | 19.9% | 22.0% | 44.6% | 63.9% | 64.4% | 64.9% | 70.4% | 70.4% | 70.9% | Warning |
| efsdbsdr02 | Database | 1.2% | 5.1% | 18.9% | 50.1% | 50.6% | 51.4% | 43.6% | 43.6% | 43.8% | Healthy |
| ebsintslp02 | App | 3.6% | 8.1% | 97.7% | 44.8% | 45.0% | 46.4% | 10.8% | 10.8% | 11.2% | Critical |
| efsdbslp01 | Database | 8.9% | 18.3% | 76.0% | 56.1% | 56.7% | 57.7% | 47.9% | 55.8% | 63.7% | Warning |
| ebsintsdr02 | App | 0.9% | 2.1% | 80.9% | 6.6% | 6.8% | 8.1% | 24.4% | 24.4% | 24.8% | Critical |
| ebsintsdr01 | App | 0.7% | 2.0% | 85.2% | 6.8% | 7.1% | 8.0% | 41.2% | 41.3% | 41.6% | Critical |
| ebsintslp01 | App | 4.1% | 7.8% | 67.4% | 50.3% | 50.6% | 52.0% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 462 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.49%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
