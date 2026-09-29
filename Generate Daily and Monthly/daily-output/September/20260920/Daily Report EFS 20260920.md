# EFS DAILY HEALTH REPORT
**Periode:** 20 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260920.xlsx, EFS_Infrastructures_20260920.xlsx, EFS_XLA_20260920.xlsx, EFS_GL_20260920.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,548,686
- **XLA Success Rate:** 83.17%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 184,165
- **Infrastruktur Status:** 1 Critical, 5 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 184,165 records. GL Posted mencapai 126,012 (99.84% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 83.17% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.84% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,548,686 | Volume total harian |
| Processed (P / XLA=S) | 1,287,457 | Sukses diproses (83.17%) |
| Unprocessed (U) | 184,165 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 126,214
- **FAH Success:** 126,138
- **FAH Error:** 76
- **Not Accounted:** 126,012
- **Posted GL:** 126,012 (99.84% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 126,119 | 0 | 126,005 | 126,005 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 12 | 0 | 0 | 0 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 1 | 0 | 1 | 1 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 801,177 | 617,023 | 184,154 | 22.99% | 17,825,703,753,757.33 | Critical |
| DEP-NQ_ED2P_SC_BFST | 282,147 | 220,174 | 0 | 0.00% | 9,192,037,113,147.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 194,940 | 194,940 | 0 | 0.00% | 0.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 122,514 | 122,514 | 0 | 0.00% | 4,097,778,043,594.22 | Healthy |
| LON-Q_GLCP_GEND872 | 73,850 | 73,850 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 62,150 | 47,648 | 0 | 0.00% | 1,272,751,479.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,831 | 5,831 | 0 | 0.00% | -42,422,085,585,736.61 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,771 | 2,231 | 0 | 0.00% | 64,725,141,642.20 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,548 | 2,548 | 0 | 0.00% | 11,142,463,386.38 | Healthy |
| BRA-NQ_ED2P_ELOG | 409 | 409 | 0 | 0.00% | 375,691,228,930.00 | Healthy |

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
| efsdbslp02 | Database | 10.8% | 16.3% | 60.1% | 60.7% | 61.2% | 62.2% | 51.4% | 51.5% | 51.5% | Warning |
| efsdbsdr01 | Database | 13.4% | 15.0% | 59.0% | 68.0% | 68.5% | 69.3% | 70.6% | 70.6% | 71.0% | Warning |
| efsdbsdr02 | Database | 0.8% | 2.7% | 11.3% | 50.5% | 50.8% | 51.6% | 43.8% | 43.8% | 43.8% | Healthy |
| ebsintslp02 | App | 2.3% | 5.7% | 98.8% | 44.1% | 44.3% | 45.9% | 10.7% | 10.7% | 10.8% | Critical |
| efsdbslp01 | Database | 8.6% | 15.9% | 73.5% | 57.1% | 57.8% | 58.8% | 45.8% | 54.1% | 63.0% | Warning |
| ebsintsdr01 | App | 0.6% | 1.6% | 65.7% | 7.3% | 7.5% | 8.6% | 41.3% | 41.3% | 42.4% | Warning |
| ebsintsdr02 | App | 0.6% | 1.5% | 62.0% | 7.0% | 7.3% | 8.8% | 24.3% | 24.4% | 25.5% | Warning |
| ebsintslp01 | App | 2.6% | 5.5% | 53.6% | 50.2% | 50.5% | 52.3% | 15.8% | 15.9% | 15.9% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 184,165 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.84%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
