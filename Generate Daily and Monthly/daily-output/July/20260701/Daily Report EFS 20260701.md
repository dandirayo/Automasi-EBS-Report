# EFS DAILY HEALTH REPORT
**Periode:** 1 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260701.xlsx, EFS_Infrastructures_20260701.xlsx, EFS_XLA_20260701.xlsx, EFS_GL_20260701.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 725,875
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 7,033
- **Infrastruktur Status:** 1 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 7,033 records. GL Posted mencapai 116,621 (98.75% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 98.75% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Depreciation Run | 0 | 0.00 | 281.69 | 281.69 | 100.00% | Healthy |
| Validate Application Accounting Definitions | 0 | 0.00 | 165.19 | 165.19 | 100.00% | Healthy |
| Report Set | 0 | 0.00 | 71.06 | 71.06 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 36.92 | 36.92 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 27.09 | 27.09 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 23.41 | 23.41 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 20.82 | 20.82 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.48 | 5.48 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 3.47 | 3.47 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 2.98 | 2.98 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 725,875 | Volume total harian |
| Processed (P / XLA=S) | 718,842 | Sukses diproses (100.00%) |
| Unprocessed (U) | 7,033 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 118,096
- **FAH Success:** 118,096
- **FAH Error:** 0
- **Not Accounted:** 116,623
- **Posted GL:** 116,621 (98.75% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 117,299 | 0 | 115,846 | 115,844 | 0 |
| CROSS BORDER PAYMENT Custom Application | 531 | 0 | 531 | 531 | 0 |
| TRADE FINANCE Custom Application | 175 | 0 | 175 | 175 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 32 | 32 | 0 |
| JOINT FINANCE Custom Application | 16 | 0 | 16 | 16 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| TREASURY Custom Application | 11 | 0 | 11 | 11 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 3 | 0 | 3 | 3 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 325,764 | 325,633 | 131 | 0.04% | 61,239,335,089,480.28 | Healthy |
| BRA-NQ_ED2P_GLDV | 107,583 | 107,583 | 0 | 0.00% | 25,476,388,075,353.08 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 101,105 | 101,105 | 0 | 0.00% | 3,450,617,137,445.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 80,363 | 80,363 | 0 | 0.00% | -555,788.00 | Healthy |
| LON-Q_GLCP_GEND872 | 63,416 | 63,416 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 21,298 | 21,298 | 0 | 0.00% | 577,916,008.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 11,629 | 11,629 | 0 | 0.00% | 874,868,417,766.92 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,670 | 0 | 5,670 | 100.00% | -29,628,659,051,472.66 | Critical |
| BRA-NQ_ED2P_T_GLDV | 4,265 | 4,265 | 0 | 0.00% | 64,046,595,206,938.45 | Healthy |
| LON-NQ_ED2P_BORV | 1,799 | 966 | 833 | 46.30% | 11,973,659,331,235.14 | Critical |

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
| ebsintsdr01 | App | 1.9% | 2.5% | 9.9% | 0.0% | 0.0% | 0.0% | 16.8% | 17.1% | 18.2% | Healthy |
| ebsintsdr02 | App | 2.0% | 2.4% | 9.7% | 0.0% | 0.0% | 0.0% | 8.6% | 8.7% | 8.7% | Healthy |
| ebsintslp01 | App | 4.2% | 17.7% | 46.0% | 0.0% | 0.0% | 0.0% | 22.9% | 23.3% | 23.8% | Healthy |
| ebsintslp02 | App | 4.1% | 14.0% | 53.4% | 0.0% | 0.0% | 0.0% | 8.7% | 9.0% | 9.9% | Healthy |
| efsdbsdr01 | Database | 16.1% | 22.4% | 34.8% | 0.0% | 0.0% | 0.0% | 65.2% | 65.3% | 65.4% | Warning |
| efsdbsdr02 | Database | 3.2% | 9.9% | 17.1% | 0.0% | 0.0% | 0.0% | 46.3% | 46.3% | 46.3% | Healthy |
| efsdbslp01 | Database | 6.8% | 36.1% | 89.4% | 0.0% | 0.0% | 0.0% | 54.8% | 58.9% | 62.7% | Critical |
| efsdbslp02 | Database | 11.1% | 29.8% | 60.3% | 0.0% | 0.0% | 0.0% | 58.1% | 58.2% | 58.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 7,033 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 98.75%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
