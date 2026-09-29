# EFS DAILY HEALTH REPORT
**Periode:** 10 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260710.xlsx, EFS_Infrastructures_20260710.xlsx, EFS_XLA_20260710.xlsx, EFS_GL_20260710.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,712,305
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 5,417
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 5,417 records. GL Posted mencapai 227,551 (99.80% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.80% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Gather Schema Statistics | 0 | 0.00 | 694.38 | 694.38 | 100.00% | Critical |
| Report Set | 0 | 0.00 | 106.41 | 106.41 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 42.79 | 42.79 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 26.39 | 26.39 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 25.54 | 25.54 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 22.72 | 22.72 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 7.18 | 7.18 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 7.11 | 7.11 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 2.96 | 2.96 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.45 | 2.45 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,712,305 | Volume total harian |
| Processed (P / XLA=S) | 2,706,888 | Sukses diproses (100.00%) |
| Unprocessed (U) | 5,417 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 228,005
- **FAH Success:** 228,001
- **FAH Error:** 4
- **Not Accounted:** 227,551
- **Posted GL:** 227,551 (99.80% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 227,286 | 4 | 226,852 | 226,852 | 0 |
| CROSS BORDER PAYMENT Custom Application | 443 | 0 | 443 | 443 | 0 |
| TRADE FINANCE Custom Application | 186 | 0 | 186 | 186 | 0 |
| CREDIT CARD Custom Application | 49 | 0 | 31 | 31 | 0 |
| TREASURY Custom Application | 16 | 0 | 16 | 16 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,518,374 | 1,517,251 | 1,123 | 0.07% | 220,082,725,465,188.62 | Warning |
| DEP-NQ_ED2P_SC_BFST | 535,717 | 535,717 | 0 | 0.00% | 17,270,564,845,988.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 230,879 | 230,879 | 0 | 0.00% | 49,451,153,621,929.33 | Healthy |
| DEP-Q_GLCP_GEND870 | 181,211 | 181,211 | 0 | 0.00% | -10,012,083.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 98,341 | 98,341 | 0 | 0.00% | 1,987,940,384.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,221 | 68,221 | 0 | 0.00% | -51,836,707.06 | Healthy |
| DEP-NQ_ED2P_T_INVV | 50,495 | 50,495 | 0 | 0.00% | 63,014,940,030,997.52 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,901 | 7,901 | 0 | 0.00% | 65,837,874,040,090.59 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,987 | 4,987 | 0 | 0.00% | 2,306,727,968,804.01 | Healthy |
| LON-NQ_ED2P_BORV | 4,821 | 2,032 | 2,789 | 57.85% | 21,139,388,590,087.47 | Critical |

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
| ebsintsdr01 | App | 2.1% | 2.8% | 10.7% | 0.0% | 0.0% | 0.0% | 20.6% | 20.6% | 21.3% | Healthy |
| ebsintsdr02 | App | 2.1% | 2.5% | 9.9% | 0.0% | 0.0% | 0.0% | 12.4% | 12.4% | 13.3% | Healthy |
| ebsintslp01 | App | 4.4% | 18.8% | 40.7% | 0.0% | 0.0% | 0.0% | 23.1% | 23.5% | 24.4% | Healthy |
| ebsintslp02 | App | 5.1% | 13.9% | 39.7% | 0.0% | 0.0% | 0.0% | 10.1% | 10.1% | 10.2% | Healthy |
| efsdbsdr01 | Database | 53.8% | 60.5% | 78.5% | 0.0% | 0.0% | 0.0% | 66.4% | 66.6% | 66.6% | Warning |
| efsdbsdr02 | Database | 3.3% | 10.1% | 27.4% | 0.0% | 0.0% | 0.0% | 46.4% | 46.5% | 46.5% | Healthy |
| efsdbslp01 | Database | 22.4% | 47.6% | 90.5% | 0.0% | 0.0% | 0.0% | 57.0% | 61.4% | 64.8% | Critical |
| efsdbslp02 | Database | 26.0% | 44.5% | 72.6% | 0.0% | 0.0% | 0.0% | 58.7% | 58.8% | 58.8% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 5,417 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.80%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
