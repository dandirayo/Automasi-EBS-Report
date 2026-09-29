# EFS DAILY HEALTH REPORT
**Periode:** August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_202608.xlsx, EFS_Infrastructures_202608.xlsx, EFS_XLA_202608.xlsx, EFS_GL_202608.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 80,630,587
- **XLA Success Rate:** 94.76%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 1,034,245
- **Infrastruktur Status:** 7 Critical, 0 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 1,034,245 records. GL Posted mencapai 6,227,519 (96.30% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 94.76% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 96.30% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 959.92 | 959.92 | 100.00% | Critical |
| BNI GL Drilldown Detail Report | 0 | 0.00 | 305.85 | 305.85 | 100.00% | Healthy |
| FAH Process | 0 | 0.00 | 192.72 | 192.72 | 100.00% | Critical |
| Validate Application Accounting Definitions | 0 | 0.00 | 184.80 | 184.80 | 100.00% | Healthy |
| BNI GL Interface Kurs Harian | 0 | 0.00 | 184.47 | 184.47 | 100.00% | Healthy |
| Gather Schema Statistics | 0 | 0.00 | 164.58 | 164.58 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 142.13 | 142.13 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 116.55 | 116.55 | 100.00% | Critical |
| Transfer Journal Entries to GL | 0 | 0.00 | 107.77 | 107.77 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 65.26 | 65.26 | 100.00% | Critical |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 80,630,587 | Volume total bulanan |
| Processed (P / XLA=S) | 76,013,071 | Sukses diproses (94.76%) |
| Unprocessed (U) | 1,034,245 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 6,466,817
- **FAH Success:** 6,238,498
- **FAH Error:** 4,330
- **Not Accounted:** 6,228,053
- **Posted GL:** 6,227,519 (96.30% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 6,447,139 | 3,341 | 6,209,790 | 6,209,256 | 211 |
| CROSS BORDER PAYMENT Custom Application | 11,474 | 1 | 11,473 | 11,473 | 0 |
| TRADE FINANCE Custom Application | 3,410 | 0 | 3,405 | 3,405 | 0 |
| PSAK 71 Custom Application | 2,505 | 988 | 1,514 | 1,514 | 0 |
| CREDIT CARD Custom Application | 1,354 | 0 | 998 | 998 | 0 |
| PREPAID SYSTEM Custom Application | 317 | 0 | 255 | 255 | 0 |
| TREASURY Custom Application | 266 | 0 | 266 | 266 | 0 |
| JOINT FINANCE Custom Application | 240 | 0 | 240 | 240 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 112 | 0 | 112 | 112 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 41,902,810 | 38,930,135 | 771,214 | 1.84% | 4,830,896,791,368,694.00 | Warning |
| DEP-NQ_ED2P_SC_BFST | 14,541,444 | 13,846,024 | 0 | 0.00% | 463,787,322,083,251.06 | Healthy |
| DEP-Q_GLCP_GEND870 | 9,034,164 | 8,807,006 | 1,904 | 0.02% | 0.00 | Warning |
| BRA-NQ_ED2P_GLDV | 6,735,452 | 6,510,835 | 30 | 0.00% | 1,408,152,464,931,943.00 | Healthy |
| LON-Q_GLCP_GEND872 | 3,299,060 | 3,294,207 | 1,635 | 0.05% | 0.00 | Warning |
| DEP-NQ_ED2P_SC_ELOG | 2,933,536 | 2,799,014 | 0 | 0.00% | 68,707,210,453.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 947,505 | 881,730 | 0 | 0.00% | 1,158,663,149,252,506.00 | Healthy |
| LON-NQ_ED2P_BORV | 292,690 | 95,113 | 189,731 | 64.82% | 118,932,902,369,864.98 | Critical |
| LON-Q_GLCP_LOND2140 | 261,787 | 261,769 | 0 | 0.00% | -622,527,830,595,744.62 | Healthy |
| BRA-NQ_ED2P_T_GLDV | 151,670 | 144,524 | 0 | 0.00% | 1,308,430,135,343,931.25 | Healthy |

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
| ebsintsdr01 | App | 0.7% | 2.1% | 88.6% | 4.8% | 5.8% | 7.8% | 41.2% | 41.2% | 42.3% | Critical |
| ebsintsdr02 | App | 0.8% | 2.0% | 83.0% | 4.5% | 5.6% | 7.7% | 24.3% | 24.3% | 25.4% | Critical |
| ebsintslp01 | App | 3.5% | 15.9% | 99.7% | 43.5% | 50.6% | 61.0% | 15.8% | 15.8% | 16.4% | Critical |
| ebsintslp02 | App | 3.1% | 19.8% | 100.0% | 36.8% | 44.0% | 54.6% | 10.6% | 10.7% | 11.2% | Critical |
| efsdbsdr01 | Database | 26.9% | 40.0% | 85.4% | 50.6% | 57.4% | 63.5% | 70.1% | 70.2% | 71.0% | Critical |
| efsdbsdr02 | Database | 2.4% | 8.8% | 54.9% | 48.8% | 49.9% | 51.6% | 43.2% | 43.4% | 44.0% | Healthy |
| efsdbslp01 | Database | 3.4% | 39.6% | 99.6% | 49.5% | 53.5% | 62.6% | 44.1% | 56.1% | 79.8% | Critical |
| efsdbslp02 | Database | 8.6% | 45.5% | 98.2% | 48.5% | 54.9% | 65.1% | 50.2% | 50.5% | 51.4% | Critical |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 1,034,245 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 96.30%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
