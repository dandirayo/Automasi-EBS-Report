# EFS DAILY HEALTH REPORT
**Periode:** 1 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260801.xlsx, EFS_Infrastructures_20260801.xlsx, EFS_XLA_20260801.xlsx, EFS_GL_20260801.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,467,934
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,179
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,179 records. GL Posted mencapai 153,888 (99.41% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.41% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,467,934 | Volume total harian |
| Processed (P / XLA=S) | 2,449,755 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,179 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 154,795
- **FAH Success:** 154,793
- **FAH Error:** 2
- **Not Accounted:** 153,888
- **Posted GL:** 153,888 (99.41% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 153,978 | 2 | 153,091 | 153,091 | 0 |
| CROSS BORDER PAYMENT Custom Application | 502 | 0 | 502 | 502 | 0 |
| TRADE FINANCE Custom Application | 220 | 0 | 220 | 220 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 33 | 33 | 0 |
| JOINT FINANCE Custom Application | 14 | 0 | 14 | 14 | 0 |
| TREASURY Custom Application | 14 | 0 | 14 | 14 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 5 | 0 | 5 | 5 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,267,263 | 1,258,624 | 8,639 | 0.68% | 51,572,964,948,507.47 | Warning |
| DEP-NQ_ED2P_SC_BFST | 433,894 | 433,894 | 0 | 0.00% | 16,990,135,864,549.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 308,054 | 307,932 | 122 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 174,152 | 174,152 | 0 | 0.00% | 6,770,192,352,897.12 | Healthy |
| LON-Q_GLCP_GEND872 | 141,494 | 141,492 | 2 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 92,656 | 92,656 | 0 | 0.00% | 2,155,061,124.00 | Healthy |
| LON-Q_GLCP_GLIF | 14,475 | 14,475 | 0 | 0.00% | 0.00 | Healthy |
| LON-NQ_ED2P_BORV | 11,690 | 3,901 | 7,789 | 66.63% | 8,440,446,174,551.65 | Critical |
| LON-Q_GLCP_LOND2140 | 11,496 | 11,496 | 0 | 0.00% | 7,866,178,402,218.20 | Healthy |
| DEP-NQ_ED2P_T_INVV | 5,864 | 5,864 | 0 | 0.00% | 99,418,030,839.06 | Healthy |

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
| efsdbslp02 | Database | 36.3% | 51.4% | 87.8% | 56.6% | 57.1% | 58.6% | 50.4% | 50.5% | 50.5% | Critical |
| efsdbsdr01 | Database | 26.9% | 31.6% | 68.8% | 50.6% | 51.0% | 51.8% | 70.2% | 70.3% | 70.7% | Warning |
| efsdbsdr02 | Database | 2.5% | 10.4% | 36.4% | 48.8% | 49.3% | 50.1% | 43.2% | 43.3% | 43.5% | Healthy |
| ebsintslp02 | App | 20.3% | 25.4% | 100.0% | 41.7% | 42.1% | 54.6% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 11.0% | 41.5% | 99.6% | 51.7% | 52.2% | 53.2% | 53.6% | 56.7% | 64.8% | Critical |
| ebsintslp01 | App | 4.3% | 12.9% | 99.7% | 49.2% | 49.7% | 58.7% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,179 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.41%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
