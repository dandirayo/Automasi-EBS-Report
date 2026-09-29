# EFS DAILY HEALTH REPORT
**Periode:** 17 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260717.xlsx, EFS_Infrastructures_20260717.xlsx, EFS_XLA_20260717.xlsx, EFS_GL_20260717.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,282,000
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 3,974
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 3,974 records. GL Posted mencapai 214,271 (99.77% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.77% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 121.68 | 121.68 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 31.52 | 31.52 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 30.97 | 30.97 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 30.60 | 30.60 | 100.00% | Critical |
| BNI FAH Journal Reversal | 0 | 0.00 | 21.97 | 21.97 | 100.00% | Healthy |
| Gather Schema Statistics | 0 | 0.00 | 19.11 | 19.11 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 4.83 | 4.83 | 100.00% | Healthy |
| BNI GL Revaluasi Harian | 0 | 0.00 | 3.40 | 3.40 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.49 | 2.49 | 100.00% | Healthy |
| Create Accounting - Receiving | 0 | 0.00 | 2.27 | 2.27 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,282,000 | Volume total harian |
| Processed (P / XLA=S) | 2,278,026 | Sukses diproses (100.00%) |
| Unprocessed (U) | 3,974 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 214,771
- **FAH Success:** 214,769
- **FAH Error:** 2
- **Not Accounted:** 214,271
- **Posted GL:** 214,271 (99.77% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 213,921 | 2 | 213,440 | 213,440 | 0 |
| CROSS BORDER PAYMENT Custom Application | 582 | 0 | 582 | 582 | 0 |
| TRADE FINANCE Custom Application | 181 | 0 | 181 | 181 | 0 |
| CREDIT CARD Custom Application | 51 | 0 | 34 | 34 | 0 |
| TREASURY Custom Application | 13 | 0 | 13 | 13 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,251,346 | 1,250,704 | 642 | 0.05% | 243,315,992,458,371.53 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 440,897 | 440,897 | 0 | 0.00% | 13,965,264,586,912.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 193,846 | 193,846 | 0 | 0.00% | 43,400,608,225,050.25 | Healthy |
| DEP-Q_GLCP_GEND870 | 182,018 | 182,018 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,970 | 84,970 | 0 | 0.00% | 1,556,174,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 67,676 | 67,676 | 0 | 0.00% | 1,287,776,572.80 | Healthy |
| DEP-NQ_ED2P_T_INVV | 42,839 | 42,839 | 0 | 0.00% | 52,572,101,170,321.00 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 4,824 | 4,824 | 0 | 0.00% | 58,290,445,099,229.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 4,271 | 4,271 | 0 | 0.00% | 3,445,250,124,501.54 | Healthy |
| LON-Q_GLCP_BORV | 3,731 | 2,604 | 1,127 | 30.21% | 3,771,205,945,250.00 | Critical |

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
| ebsintsdr01 | App | 1.8% | 2.4% | 10.4% | 0.0% | 0.0% | 0.0% | 21.5% | 21.5% | 22.8% | Healthy |
| ebsintsdr02 | App | 1.8% | 2.3% | 14.6% | 0.0% | 0.0% | 0.0% | 12.5% | 12.5% | 13.9% | Healthy |
| ebsintslp01 | App | 4.4% | 18.9% | 56.5% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.6% | Healthy |
| ebsintslp02 | App | 4.4% | 15.8% | 45.0% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.1% | Healthy |
| efsdbsdr01 | Database | 35.0% | 40.3% | 54.3% | 0.0% | 0.0% | 0.0% | 67.3% | 67.4% | 67.4% | Warning |
| efsdbsdr02 | Database | 3.2% | 8.1% | 17.4% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.6% | Healthy |
| efsdbslp01 | Database | 16.2% | 37.0% | 79.6% | 0.0% | 0.0% | 0.0% | 57.3% | 60.4% | 63.3% | Warning |
| efsdbslp02 | Database | 10.6% | 30.8% | 62.0% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 3,974 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.77%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
