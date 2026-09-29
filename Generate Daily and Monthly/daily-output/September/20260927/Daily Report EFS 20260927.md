# EFS DAILY HEALTH REPORT
**Periode:** 27 September 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260927.xlsx, EFS_Infrastructures_20260927.xlsx, EFS_XLA_20260927.xlsx, EFS_GL_20260927.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 1,170,103
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 740
- **Infrastruktur Status:** 1 Critical, 5 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 740 records. GL Posted mencapai 114,769 (99.82% intake).

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

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 1,170,103 | Volume total harian |
| Processed (P / XLA=S) | 1,169,363 | Sukses diproses (100.00%) |
| Unprocessed (U) | 740 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 114,976
- **FAH Success:** 114,899
- **FAH Error:** 76
- **Not Accounted:** 114,769
- **Posted GL:** 114,769 (99.82% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 114,733 | 0 | 114,613 | 114,613 | 0 |
| CROSS BORDER PAYMENT Custom Application | 146 | 0 | 146 | 146 | 0 |
| PSAK 71 Custom Application | 76 | 76 | 0 | 0 | 0 |
| CREDIT CARD Custom Application | 11 | 0 | 0 | 0 | 0 |
| JOINT FINANCE Custom Application | 8 | 0 | 8 | 8 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 683,795 | 683,076 | 719 | 0.11% | 15,158,805,836,127.98 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 249,655 | 249,655 | 0 | 0.00% | 6,982,794,229,096.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 100,260 | 100,260 | 0 | 0.00% | 3,865,112,169,889.80 | Healthy |
| LON-Q_GLCP_GEND872 | 74,228 | 74,228 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 51,342 | 51,342 | 0 | 0.00% | 1,035,535,555.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 5,746 | 5,746 | 0 | 0.00% | -42,155,473,225,358.68 | Healthy |
| DEP-NQ_ED2P_T_INVV | 2,485 | 2,485 | 0 | 0.00% | 135,858,727,248.99 | Healthy |
| DEP-NQ_ED2P_CC_INVV | 1,902 | 1,902 | 0 | 0.00% | 6,134,342,510.72 | Healthy |
| BRA-NQ_ED2P_ELOG | 408 | 408 | 0 | 0.00% | 345,551,895,195.00 | Healthy |
| BRA-NQ_ED2P_CC_GLDV | 90 | 90 | 0 | 0.00% | 91,323,553.00 | Healthy |

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
| efsdbslp02 | Database | 9.6% | 15.0% | 60.5% | 61.4% | 62.0% | 62.8% | 51.6% | 51.7% | 51.7% | Warning |
| efsdbsdr01 | Database | 13.4% | 14.8% | 34.5% | 70.1% | 70.3% | 71.2% | 70.7% | 70.7% | 71.1% | Warning |
| efsdbsdr02 | Database | 0.8% | 3.4% | 12.7% | 50.6% | 51.0% | 51.8% | 43.8% | 43.8% | 43.9% | Healthy |
| ebsintslp02 | App | 2.3% | 5.8% | 99.6% | 43.9% | 44.1% | 45.7% | 10.8% | 10.8% | 11.0% | Critical |
| efsdbslp01 | Database | 9.9% | 17.1% | 79.3% | 58.8% | 59.3% | 60.3% | 53.1% | 57.0% | 61.8% | Warning |
| ebsintsdr01 | App | 0.5% | 1.4% | 65.4% | 7.4% | 7.6% | 8.9% | 41.3% | 41.3% | 41.6% | Warning |
| ebsintsdr02 | App | 0.6% | 1.5% | 62.5% | 7.2% | 7.4% | 8.9% | 24.4% | 24.4% | 24.6% | Warning |
| ebsintslp01 | App | 2.9% | 6.0% | 56.3% | 49.8% | 50.1% | 51.6% | 15.9% | 15.9% | 16.4% | Healthy |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 740 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
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
