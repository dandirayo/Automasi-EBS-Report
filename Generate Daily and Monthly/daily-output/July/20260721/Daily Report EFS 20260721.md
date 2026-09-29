# EFS DAILY HEALTH REPORT
**Periode:** 21 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260721.xlsx, EFS_Infrastructures_20260721.xlsx, EFS_XLA_20260721.xlsx, EFS_GL_20260721.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,457,951
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 4,120
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 4,120 records. GL Posted mencapai 217,161 (99.82% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.82% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 142.20 | 142.20 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 51.35 | 51.35 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 33.44 | 33.44 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 33.04 | 33.04 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 31.48 | 31.48 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 23.52 | 23.52 | 100.00% | Healthy |
| Depreciation Run | 0 | 0.00 | 11.69 | 11.69 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 9.83 | 9.83 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 7.03 | 7.03 | 100.00% | Critical |
| BNI GL Revaluasi Harian | 0 | 0.00 | 5.49 | 5.49 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,457,951 | Volume total harian |
| Processed (P / XLA=S) | 2,453,831 | Sukses diproses (100.00%) |
| Unprocessed (U) | 4,120 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 217,554
- **FAH Success:** 217,552
- **FAH Error:** 2
- **Not Accounted:** 217,161
- **Posted GL:** 217,161 (99.82% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 216,914 | 2 | 216,542 | 216,542 | 0 |
| CROSS BORDER PAYMENT Custom Application | 377 | 0 | 377 | 377 | 0 |
| TRADE FINANCE Custom Application | 178 | 0 | 178 | 178 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 31 | 31 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,346,154 | 1,345,516 | 638 | 0.05% | 172,091,237,128,254.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 486,420 | 486,420 | 0 | 0.00% | 14,249,742,083,071.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 218,300 | 218,300 | 0 | 0.00% | 42,298,267,553,125.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,726 | 182,726 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 86,578 | 86,578 | 0 | 0.00% | 1,515,644,398.00 | Healthy |
| LON-Q_GLCP_GEND872 | 68,026 | 68,026 | 0 | 0.00% | 2,056,704,125.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,330 | 42,330 | 0 | 0.00% | 53,345,726,721,127.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 7,236 | 7,236 | 0 | 0.00% | 57,343,192,282,442.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,875 | 5,875 | 0 | 0.00% | -39,794,268,581,739.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,018 | 4,018 | 0 | 0.00% | 2,668,791,272,745.00 | Healthy |

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
| ebsintsdr01 | App | 1.7% | 2.3% | 9.9% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 23.1% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.4% | 9.1% | 0.0% | 0.0% | 0.0% | 12.6% | 12.6% | 14.2% | Healthy |
| ebsintslp01 | App | 4.4% | 16.6% | 47.9% | 0.0% | 0.0% | 0.0% | 17.9% | 18.0% | 18.0% | Healthy |
| ebsintslp02 | App | 4.7% | 15.3% | 52.0% | 0.0% | 0.0% | 0.0% | 9.9% | 10.0% | 10.1% | Healthy |
| efsdbsdr01 | Database | 35.2% | 41.2% | 61.2% | 0.0% | 0.0% | 0.0% | 67.7% | 67.8% | 67.9% | Warning |
| efsdbsdr02 | Database | 3.4% | 6.1% | 19.4% | 0.0% | 0.0% | 0.0% | 46.5% | 46.6% | 46.7% | Healthy |
| efsdbslp01 | Database | 18.9% | 42.8% | 74.9% | 0.0% | 0.0% | 0.0% | 57.9% | 61.1% | 65.0% | Warning |
| efsdbslp02 | Database | 19.3% | 30.6% | 63.8% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 4,120 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.82%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
