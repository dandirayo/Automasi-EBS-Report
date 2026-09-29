# EFS DAILY HEALTH REPORT
**Periode:** 18 July 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260718.xlsx, EFS_Infrastructures_20260718.xlsx, EFS_XLA_20260718.xlsx, EFS_GL_20260718.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `WARNING`
- **XLA Total Records:** 2,198,294
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 605
- **Infrastruktur Status:** 0 Critical, 3 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 605 records. GL Posted mencapai 185,972 (99.90% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.90% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|
| Report Set | 0 | 0.00 | 111.90 | 111.90 | 100.00% | Critical |
| Gather Schema Statistics | 0 | 0.00 | 93.67 | 93.67 | 100.00% | Healthy |
| Accounting Program | 0 | 0.00 | 28.55 | 28.55 | 100.00% | Critical |
| FAH Process | 0 | 0.00 | 26.95 | 26.95 | 100.00% | Critical |
| Create Accounting | 0 | 0.00 | 24.75 | 24.75 | 100.00% | Critical |
| BNI GL Laporan Jurnal Transaksi per Entity V2 | 0 | 0.00 | 23.78 | 23.78 | 100.00% | Healthy |
| BNI FAH Journal Reversal | 0 | 0.00 | 22.70 | 22.70 | 100.00% | Healthy |
| Transfer Journal Entries to GL | 0 | 0.00 | 4.89 | 4.89 | 100.00% | Healthy |
| Create Accounting - Assets | 0 | 0.00 | 2.97 | 2.97 | 100.00% | Healthy |
| Journal Import | 0 | 0.00 | 1.83 | 1.83 | 100.00% | Healthy |

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,198,294 | Volume total harian |
| Processed (P / XLA=S) | 2,197,689 | Sukses diproses (100.00%) |
| Unprocessed (U) | 605 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 186,152
- **FAH Success:** 186,150
- **FAH Error:** 2
- **Not Accounted:** 185,972
- **Posted GL:** 185,972 (99.90% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 185,417 | 2 | 185,256 | 185,256 | 0 |
| CROSS BORDER PAYMENT Custom Application | 460 | 0 | 460 | 460 | 0 |
| TRADE FINANCE Custom Application | 188 | 0 | 188 | 188 | 0 |
| CREDIT CARD Custom Application | 50 | 0 | 33 | 33 | 0 |
| TREASURY Custom Application | 12 | 0 | 12 | 12 | 0 |
| PREPAID SYSTEM Custom Application | 11 | 0 | 9 | 9 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 6 | 0 | 6 | 6 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,343,248 | 1,342,652 | 596 | 0.04% | 21,834,660,375,817.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 253,880 | 253,880 | 0 | 0.00% | 6,422,297,590,908.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 191,629 | 191,629 | 0 | 0.00% | 5,880,922,289,854.00 | Healthy |
| DEP-Q_GLCP_GEND870 | 179,267 | 179,267 | 0 | 0.00% | -53,150,917,214.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 153,758 | 153,758 | 0 | 0.00% | 4,052,679,500.00 | Healthy |
| LON-Q_GLCP_GEND872 | 70,829 | 70,829 | 0 | 0.00% | 70,614,552.00 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 2,491 | 2,491 | 0 | 0.00% | 16,829,946,082.59 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,116 | 2,116 | 0 | 0.00% | 46,627,959,023.00 | Healthy |
| BRA-NQ_ED2P_ELOG | 564 | 564 | 0 | 0.00% | 293,217,009,359.00 | Healthy |
| LON-Q_GLCP_BORV | 143 | 143 | 0 | 0.00% | 119,263,744,566.00 | Healthy |

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
| ebsintsdr01 | App | 1.8% | 2.7% | 15.6% | 0.0% | 0.0% | 0.0% | 21.5% | 21.6% | 22.9% | Healthy |
| ebsintsdr02 | App | 1.9% | 2.2% | 9.4% | 0.0% | 0.0% | 0.0% | 12.5% | 12.6% | 13.9% | Healthy |
| ebsintslp01 | App | 4.6% | 11.1% | 27.2% | 0.0% | 0.0% | 0.0% | 17.9% | 17.9% | 18.0% | Healthy |
| ebsintslp02 | App | 4.5% | 7.3% | 23.3% | 0.0% | 0.0% | 0.0% | 9.9% | 9.9% | 10.4% | Healthy |
| efsdbsdr01 | Database | 34.9% | 40.8% | 63.2% | 0.0% | 0.0% | 0.0% | 67.4% | 67.5% | 67.6% | Warning |
| efsdbsdr02 | Database | 3.4% | 5.7% | 21.0% | 0.0% | 0.0% | 0.0% | 46.5% | 46.5% | 46.6% | Healthy |
| efsdbslp01 | Database | 12.6% | 24.1% | 38.7% | 0.0% | 0.0% | 0.0% | 56.2% | 61.1% | 62.6% | Warning |
| efsdbslp02 | Database | 6.4% | 24.6% | 73.1% | 0.0% | 0.0% | 0.0% | 59.0% | 59.0% | 59.1% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 605 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.90%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
