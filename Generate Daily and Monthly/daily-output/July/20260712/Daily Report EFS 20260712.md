# EFS DAILY HEALTH REPORT
**Periode:** 12 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260712.xlsx, EFS_Infrastructures_20260712.xlsx, EFS_XLA_20260712.xlsx, EFS_GL_20260712.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,332,116
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 592
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 592 records. GL Posted mencapai 190,922 (99.93% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.93% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 574.63 | 574.63 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 99.00 | 99.00 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 28.64 | 28.64 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 26.98 | 26.98 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 26.71 | 26.71 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 22.02 | 22.02 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 21.48 | 21.48 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 7.87 | 7.87 | 100.00% | Critical |
| Journal Import | 0 | 0.00 | 4.38 | 4.38 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 1.68 | 1.68 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,332,116 | Volume total harian |
| Processed (P / XLA=S) | 2,331,524 | Sukses diproses (100.00%) |
| Unprocessed (U) | 592 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 191,053
- **FAH Success:** 191,051
- **FAH Error:** 2
- **Not Accounted:** 190,922
- **Posted GL:** 190,922 (99.93% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 190,925 | 2 | 190,796 | 190,796 | 0 |
| CROSS BORDER PAYMENT Custom Application | 91 | 0 | 91 | 91 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 17 | 17 | 0 |
| JOINT FINANCE Custom Application | 10 | 0 | 10 | 10 | 0 |
| PREPAID SYSTEM Custom Application | 8 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,285,478 | 1,284,889 | 589 | 0.05% | 17,046,084,497,872.12 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 457,086 | 457,086 | 0 | 0.00% | 9,086,903,090,494.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 206,224 | 206,224 | 0 | 0.00% | 4,588,455,250,727.85 | Healthy |
| DEP-Q_GLCP_GEND870 | 201,256 | 201,256 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 98,048 | 98,048 | 0 | 0.00% | 1,658,292,917.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,904 | 70,904 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,857 | 5,857 | 0 | 0.00% | -40,854,178,175,184.28 | Healthy |
| DEP-NQ_ED2P_T_INVV | 3,573 | 3,573 | 0 | 0.00% | 95,902,367,737.19 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,416 | 2,416 | 0 | 0.00% | 8,827,832,204.11 | Healthy |
| BRA-NQ_ED2P_ELOG | 895 | 895 | 0 | 0.00% | 377,759,125,905.00 | Healthy |

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
| ebsintsdr01 | App | 2.9% | 3.7% | 14.5% | 0.0% | 0.0% | 0.0% | 21.3% | 21.4% | 21.5% | Healthy |
| ebsintsdr02 | App | 1.8% | 3.2% | 15.1% | 0.0% | 0.0% | 0.0% | 12.2% | 12.3% | 13.2% | Healthy |
| ebsintslp01 | App | 4.4% | 10.4% | 31.4% | 0.0% | 0.0% | 0.0% | 24.5% | 24.8% | 25.4% | Healthy |
| ebsintslp02 | App | 4.7% | 6.9% | 17.1% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.8% | Healthy |
| efsdbsdr01 | Database | 22.2% | 30.7% | 43.8% | 0.0% | 0.0% | 0.0% | 66.7% | 66.8% | 66.9% | Warning |
| efsdbsdr02 | Database | 3.1% | 5.6% | 19.6% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 19.6% | 30.3% | 44.8% | 0.0% | 0.0% | 0.0% | 58.7% | 60.2% | 61.6% | Warning |
| efsdbslp02 | Database | 11.4% | 27.6% | 71.8% | 0.0% | 0.0% | 0.0% | 58.8% | 58.9% | 58.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 592 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.93%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
