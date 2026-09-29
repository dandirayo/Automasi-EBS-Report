# EFS DAILY HEALTH REPORT
**Periode:** 2 August 2026  
**Organisasi:** PT Bank Negara Indonesia (Persero) Tbk | IT Application Services (APS)  
**Departemen:** Core Banking System (CBS) | Ledger: BNI_LEDGER_IDR  
**Sumber Data:** EFS_Transactions_20260802.xlsx, EFS_Infrastructures_20260802.xlsx, EFS_XLA_20260802.xlsx, EFS_GL_20260802.xlsx

---

## 01. Ringkasan Eksekutif (Executive Overview)
- **Overall Status:** `CRITICAL`
- **XLA Total Records:** 2,518,987
- **XLA Success Rate:** 100.00%
- **XLA Error Records:** 0
- **XLA Unprocessed (Queue):** 18,251
- **Infrastruktur Status:** 3 Critical, 2 Warning

> **Temuan Utama:** Residual XLA tercatat sebanyak 18,251 records. GL Posted mencapai 146,597 (99.92% intake).

---

## 02. Reliability Framework & Service Level Objective (SLO)
| Sinyal | Metrik | Target | Aktual | Verdict |
|---|---|---|---|---|
| Errors | XLA code success | >=99.5% | 100.00% | WARNING |
| Latency | Program P99 | Dalam baseline | 213,31 min | GAGAL |
| Saturation | CPU Max | <80% | 98,30% | GAGAL |
| GL | Posted / Intake | >=99.5% | 99.92% | WARNING |

---

## 03. Concurrent Job dan Latency Program
| Program | Hits | Avg (min) | P95 (min) | P99 (min) | Success % | Status |
|---|---|---|---|---|---|---|

---

## 04. Status Data XLA dan Event Processing
| Status Code / Dimensi | Total Records | Keterangan |
|---|---|---|
| Total Records | 2,518,987 | Volume total harian |
| Processed (P / XLA=S) | 2,500,734 | Sukses diproses (100.00%) |
| Unprocessed (U) | 18,251 | Antrean residual |
| XLA Error (E) | None | Record error |
| Invalid / Void (V) | 180,830 | Void / cancelled records |

---

## 05. General Ledger Posting Funnel
- **Masuk FAH:** 146,714
- **FAH Success:** 146,714
- **FAH Error:** 0
- **Not Accounted:** 146,597
- **Posted GL:** 146,597 (99.92% intake)

### Detail Per Application:
| Application | Masuk FAH | FAH Error | Not Accounted | Posted | Unposted |
|---|---|---|---|---|---|
| ICONS Custom Application | 146,537 | 0 | 146,422 | 146,422 | 0 |
| CROSS BORDER PAYMENT Custom Application | 133 | 0 | 133 | 133 | 0 |
| CREDIT CARD Custom Application | 25 | 0 | 25 | 25 | 0 |
| PREPAID SYSTEM Custom Application | 9 | 0 | 7 | 7 | 0 |
| JOINT FINANCE Custom Application | 6 | 0 | 6 | 6 | 0 |
| SUPPLY CHAIN FINANCING Custom Application | 2 | 0 | 2 | 2 | 0 |
| TREASURY Custom Application | 2 | 0 | 2 | 2 | 0 |

---

## 06. Breakdown Entity, Application, dan Event Class
| Event Class | Total | Processed | U | Unproc % | Amount | Status |
|---|---|---|---|---|---|---|
| DEP-NQ_ED2P_INVV | 1,250,888 | 1,241,667 | 9,221 | 0.74% | 35,084,030,234,999.47 | Warning |
| DEP-Q_GLCP_GEND870 | 412,039 | 411,889 | 150 | 0.04% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_BFST | 411,402 | 411,402 | 0 | 0.00% | 10,914,357,823,511.00 | Healthy |
| BRA-NQ_ED2P_GLDV | 172,417 | 172,417 | 0 | 0.00% | 5,423,471,348,869.00 | Healthy |
| LON-Q_GLCP_GEND872 | 148,962 | 148,962 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_SC_ELOG | 84,650 | 84,650 | 0 | 0.00% | 1,651,767,050.00 | Healthy |
| LON-Q_GLCP_LOND2140 | 11,523 | 11,523 | 0 | 0.00% | -1,440,574,542,529.16 | Healthy |
| LON-NQ_ED2P_BORV | 10,007 | 3,028 | 6,979 | 69.74% | 233,881,745,753.00 | Critical |
| LON-Q_GLCP_GLIF | 5,392 | 5,392 | 0 | 0.00% | 0.00 | Healthy |
| DEP-NQ_ED2P_T_INVV | 4,342 | 4,342 | 0 | 0.00% | 95,780,724,022.84 | Healthy |

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
| efsdbslp02 | Database | 35.8% | 56.3% | 95.0% | 57.5% | 57.8% | 58.4% | 50.4% | 50.4% | 50.6% | Critical |
| efsdbsdr01 | Database | 26.9% | 31.7% | 62.3% | 51.1% | 51.6% | 52.3% | 70.2% | 70.3% | 70.5% | Warning |
| efsdbsdr02 | Database | 2.4% | 6.2% | 28.5% | 48.8% | 49.1% | 49.8% | 43.2% | 43.3% | 43.3% | Healthy |
| ebsintslp02 | App | 20.0% | 24.7% | 93.8% | 41.8% | 42.3% | 43.7% | 10.7% | 10.7% | 10.7% | Critical |
| efsdbslp01 | Database | 10.0% | 28.7% | 92.0% | 51.6% | 52.4% | 53.1% | 51.0% | 54.9% | 58.8% | Critical |
| ebsintslp01 | App | 3.7% | 7.6% | 75.4% | 49.3% | 49.7% | 50.4% | 15.8% | 15.8% | 15.9% | Warning |

---

## 09. Dampak Proses Bisnis dan Reliability Scorecard
| Temuan Teknis | Proses Terdampak | Potensi Dampak | Severity |
|---|---|---|---|
| 18,251 residual XLA | Create Accounting & final sweep | Backlog dapat menunda downstream accounting | Sedang |
| P99 hingga 213,31 menit | Pelaporan dan batch | Risiko keterlambatan proses dan laporan | Tinggi |
| CPU peak >80% pada 3 node | Batch accounting dan reporting | Risiko contention pada beban puncak | Tinggi |
| GL Posted 99.92%; Unposted 0 | Posting GL | Posting selesai, residual upstream perlu dipantau | Sedang |

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
