# EFS DAILY HEALTH REPORT
**Periode:** 26 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260726.xlsx, EFS_Infrastructures_20260726.xlsx, EFS_XLA_20260726.xlsx, EFS_GL_20260726.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 238,965
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 0
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 0 records. GL Posted mencapai 12,627 (99.50% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.50% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 55.07 | 55.07 | 100.00% | Healthy |
| Create Accounting | 0 | 0.00 | 35.28 | 35.28 | 100.00% | Critical |
| Accounting Program | 0 | 0.00 | 34.33 | 34.33 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 34.32 | 34.32 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 20.08 | 20.08 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 19.03 | 19.03 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 5.84 | 5.84 | 100.00% | Critical |
| Create Accounting - Assets | 0 | 0.00 | 2.17 | 2.17 | 100.00% | Healthy |
| BNI GL Bugla EFS Outbound F1 | 0 | 0.00 | 1.90 | 1.90 | 100.00% | Healthy |
| BNI GL Interface Kurs Harian | 0 | 0.00 | 1.73 | 1.73 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 238,965 | Volume total harian |
| Processed (P / XLA=S) | 238,965 | Sukses diproses (100.00%) |
| Unprocessed (U) | 0 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 12,690
- **FAH Success:** 12,690
- **FAH Error:** 0
- **Not Accounted:** 12,627
- **Posted GL:** 12,627 (99.50% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 12,517 | 0 | 12,454 | 12,454 | 0 |
| CROSS BORDER PAYMENT Custom Application | 139 | 0 | 139 | 139 | 0 |
| CREDIT CARD Custom Application | 17 | 0 | 17 | 17 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| PREPAID SYSTEM Custom Application | 5 | 0 | 5 | 5 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 4 | 0 | 4 | 4 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-Q_GLCP_GEND870 | 195,753 | 195,753 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_GEND872 | 37,474 | 37,474 | 0 | 0.00% | 0.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,726 | 5,726 | 0 | 0.00% | -40,462,400,612,110.00 | Healthy |
| JS10 | 6 | 6 | 0 | 0.00% | 13,490.00 | Healthy |
| ACCRUAL JF | 4 | 4 | 0 | 0.00% | 0.00 | Healthy |
| JS06 | 2 | 2 | 0 | 0.00% | 450,000.00 | Healthy |

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
| ebsintslp01 | App | 4.3% | 7.5% | 19.8% | 0.0% | 0.0% | 0.0% | 18.0% | 18.0% | 18.5% | Healthy |
| ebsintslp02 | App | 4.4% | 7.5% | 19.5% | 0.0% | 0.0% | 0.0% | 10.0% | 10.1% | 10.1% | Healthy |
| efsdbsdr01 | Database | 9.0% | 12.6% | 18.5% | 0.0% | 0.0% | 0.0% | 66.8% | 66.9% | 66.9% | Warning |
| efsdbsdr02 | Database | 3.4% | 10.2% | 19.2% | 0.0% | 0.0% | 0.0% | 47.4% | 47.4% | 47.5% | Healthy |
| efsdbslp01 | Database | 13.0% | 27.6% | 59.9% | 0.0% | 0.0% | 0.0% | 58.8% | 62.0% | 73.5% | Warning |
| efsdbslp02 | Database | 36.2% | 50.5% | 70.2% | 0.0% | 0.0% | 0.0% | 59.1% | 59.1% | 59.2% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 0 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.50%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
