# EFS DAILY HEALTH REPORT
**Periode:** 21 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260921.xlsx, EFS_Infrastructures_20260921.xlsx, EFS_XLA_20260921.xlsx, EFS_GL_20260921.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,906,102
- **XLA Success Rate:** 84.94%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,346
- **Infrastruktur Status:** 3 Critical, 4 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,346 records. GL Posted mencapai 158,638 (99.67% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 84.94% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.67% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,906,102 | Volume total harian |
| Processed (P / XLA=S) | 1,614,690 | Sukses diproses (84.94%) |
| Unprocessed (U) | 4,346 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 159,170
- **FAH Success:** 158,974
- **FAH Error:** 196
- **Not Accounted:** 158,638
- **Posted GL:** 158,638 (99.67% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 159,040 | 120 | 158,625 | 158,625 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 40 | 0 | 0 | 0 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 8 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,002,252 | 815,086 | 677 | 0.07% | 247,944,480,554,144.47 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 344,903 | 280,418 | 0 | 0.00% | 15,502,191,953,362.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 195,203 | 176,213 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 153,401 | 153,400 | 0 | 0.00% | 53,457,867,690,168.50 | Healthy |
| LON-Q_GLCP_GEND872 | 73,856 | 73,570 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 67,489 | 52,958 | 0 | 0.00% | 1,477,997,752.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 40,355 | 39,540 | 0 | 0.00% | 55,696,748,168,499.74 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,017 | 7,017 | 0 | 0.00% | 60,562,005,276,882.51 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,824 | 5,824 | 0 | 0.00% | -42,399,945,288,751.61 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 5,057 | 4,416 | 0 | 0.00% | 2,417,875,366,249.75 | Healthy |

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
| efsdbslp02 | Database | 10.9% | 30.2% | 89.4% | 61.1% | 63.0% | 68.3% | 51.4% | 51.5% | 51.6% | Critical |
| efsdbsdr01 | Database | 13.4% | 14.9% | 30.8% | 68.4% | 68.8% | 69.4% | 70.6% | 70.6% | 71.0% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.6% | 12.4% | 50.3% | 50.9% | 51.8% | 43.8% | 43.8% | 43.8% | Healthy |
| ebsintslp02 | App | 2.5% | 10.2% | 99.3% | 44.2% | 46.6% | 53.0% | 10.7% | 10.8% | 10.8% | Critical |
| efsdbslp01 | Database | 10.3% | 38.3% | 94.6% | 57.3% | 60.3% | 64.8% | 46.2% | 56.2% | 64.9% | Critical |
| ebsintsdr01 | App | 0.6% | 1.6% | 66.8% | 7.2% | 7.6% | 8.7% | 41.3% | 41.3% | 41.7% | Warning |
| ebsintsdr02 | App | 0.6% | 1.4% | 62.7% | 7.2% | 7.3% | 8.7% | 24.4% | 24.4% | 25.5% | Warning |
| ebsintslp01 | App | 2.7% | 9.9% | 66.3% | 50.2% | 52.8% | 58.1% | 15.8% | 15.9% | 16.0% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,346 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.67%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
