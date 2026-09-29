# EFS DAILY HEALTH REPORT
**Periode:** 3 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260803.xlsx, EFS_Infrastructures_20260803.xlsx, EFS_XLA_20260803.xlsx, EFS_GL_20260803.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,964,193
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 22,661
- **Infrastruktur Status:** 4 Critical, 1 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 22,661 records. GL Posted mencapai 236,253 (99.83% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.83% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,964,193 | Volume total harian |
| Processed (P / XLA=S) | 2,941,530 | Sukses diproses (100.00%) |
| Unprocessed (U) | 22,661 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 236,646
- **FAH Success:** 236,644
- **FAH Error:** 2
- **Not Accounted:** 236,253
- **Posted GL:** 236,253 (99.83% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 236,282 | 2 | 235,891 | 235,891 | 0 |
| PSAK 71 Custom Application | 228 | 0 | 228 | 228 | 0 |
| CROSS BORDER PAYMENT Custom Application | 80 | 0 | 80 | 80 | 0 |
| CREDIT CARD Custom Application | 41 | 0 | 41 | 41 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,458,079 | 1,449,360 | 8,719 | 0.60% | 245,083,927,559,453.81 | Warning |
| DEP-NQ_ED2P_SC_BFST | 504,354 | 504,354 | 0 | 0.00% | 18,753,079,203,448.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 413,636 | 413,482 | 154 | 0.04% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 221,966 | 221,962 | 4 | 0.00% | 115,115,702,406,281.38 | Healthy |
| LON-Q_GLCP_GEND872 | 149,022 | 149,022 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 93,121 | 93,121 | 0 | 0.00% | 1,823,492,924.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 55,635 | 55,635 | 0 | 0.00% | 80,423,225,470,378.86 | Healthy |
| LON-NQ_ED2P_BORV | 16,408 | 5,633 | 10,775 | 65.67% | 8,478,347,128,775.21 | Critical |
| LON-Q_GLCP_LOND2140 | 11,555 | 11,555 | 0 | 0.00% | -206,000,316,389.03 | Healthy |
| LON-Q_GLCP_GLIF | 11,410 | 11,241 | 169 | 1.48% | 0.00 | Healthy |

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
| efsdbslp02 | Database | 17.0% | 65.5% | 98.2% | 48.5% | 57.9% | 64.8% | 50.4% | 50.4% | 50.8% | Critical |
| efsdbsdr01 | Database | 27.0% | 37.3% | 69.0% | 51.7% | 52.5% | 53.4% | 70.2% | 70.3% | 70.6% | Warning |
| efsdbsdr02 | Database | 2.7% | 8.5% | 29.7% | 49.0% | 49.3% | 50.1% | 43.2% | 43.3% | 43.3% | Healthy |
| efsdbslp01 | Database | 4.0% | 47.7% | 98.3% | 49.5% | 53.7% | 58.7% | 49.4% | 58.3% | 62.2% | Critical |
| ebsintslp02 | App | 3.5% | 20.2% | 88.7% | 42.3% | 44.6% | 49.2% | 10.7% | 10.7% | 10.8% | Critical |
| ebsintslp01 | App | 3.5% | 16.1% | 83.4% | 49.6% | 51.9% | 58.3% | 15.8% | 15.8% | 15.9% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 22,661 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.83%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
