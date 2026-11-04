# No.54 - Exact Consecutive-Pattern Popularity in the Class Avoiding 123, 231 and 312

**Ryutaro Yonezu - Independent Researcher**  
Preprint manuscript v1.0, 2026-11-05. **All rights reserved.**

## Publication and downloads

This is the owner-authorized v1.0 release payload. The current public release and Zenodo DOI, once published, are linked from the live repository README: https://github.com/yonezaemon1-hub/no54-class12-consecutive-pattern-popularity. No DOI is predicted in this immutable payload.

- PDF: paper/No54_v1.0_PREPRINT_20261105.pdf.
- Reproducibility: source code, frozen v0.4 archive, earlier archives, audit report and user-supplied Windows console log are included here.
- Intended GitHub tag: v1.0. Publication type: Preprint.

## Exact result and restricted scope

For n >= 3 in the **consecutive**-pattern avoidance class Av_n(123,231,312):

- |A_n| = n E_(n-1), a known avoidance count attributed to Kitaev-Mansour.
- N_n(321) = E_(n+1) - 2 E_n.
- N_n(132) = N_n(213) = ((n-2)n E_(n-1) - E_(n+1) + 2 E_n)/2.
- With denominator n|A_n|, pop(321) = 4/pi^2 and pop(132) = pop(213) = 1/2 - 2/pi^2.

N_n(p) counts all consecutive occurrences over all permutations and positions, including overlapping occurrences. This solves only the specified finite totals and asymptotic limits in this class. Euler numbers, the A000708 sequence and EGF, and the circular-difference integral operator are existing work. No general permutation-pattern problem, originality certification or priority over all prior work is claimed.

## Audit, execution and limitations

| Item | Status and attribution |
|---|---|
| MODEL / PROOF / COMPUTATION | PASS in the supplied Claude Sonnet 5.5 v0.2 report |
| v0.3 differential audit | PASS in the supplied Claude report |
| Claude's firsthand references | PARTIAL: HK v2, EKP Section 7 and Zhao were not inspected by Claude |
| Primary-source checks | Recorded by ChatGPT separately; not attributed to Claude or personal inspection by the human author |
| Windows PowerShell reproduction | PASS in the owner's supplied v0.4.1 console record; not executed by Claude or the publication assistant |
| Human peer review | NOT PERFORMED / Not human peer-reviewed |
| Novelty | INCONCLUSIVE |
| Google Scholar / OpenAlex | Not checked |

The supplied independent report is preserved byte-for-byte under evidence/. It reports independent C enumeration through n=13; that C source was not supplied or rerun here. Publication-session checks passed for original permutation enumeration n=3..9, independent exact rational simplex counting n=3..22, the 27-entry v0.4 manifest and 19 frozen v0.3 files. Values printed at n=10,20,40,60,100,120 by the first arithmetic script are formula evaluations, not independent occurrence counts.

The reviewer recommended HOLD at the time of review. The owner subsequently explicitly authorized public release. Historical HOLD and Windows-untested statements remain frozen and distinguishable from the current release evidence.

## Reproduce with standard-library Python 3.10+

From the extracted supplement root on Linux or macOS:

```sh
python3 -I frozen_v0.4/v0.4/verify_delta_v0.4.py
python3 -I code/No54_v0.1_VERIFY_20261105.py
python3 -I code/No54_v0.1_INDEPENDENT_ATTACK_20261105.py
python3 -I verify_typeset_core.py
```

On Windows, place original_archives/No54_Audit_v04.zip and original_archives/No54_Run_Windows_v041.ps1 in your Downloads directory, then run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\No54_Run_Windows_v041.ps1"
```

Windows v0.4.1 is a path-separator fix only. It normalizes three path conversions in memory, preserves the original ZIP and on-disk verifier, and makes no mathematical change. Original ZIP SHA256: `9fca07c3ce4f15bfa7c9022660cab8051a175149291a0c38e605dce1c5adc446`.

## Prior work

See the manuscript bibliography and frozen v0.4 source-check record for Hassler-Kirgizov, Class 12 / Table 1 / equation (1.1); Ehrenborg-Kitaev-Perry, Theorem 7.5; the known Kitaev-Mansour count; Zhao (2014)'s classical nonconsecutive-pattern setting; and OEIS A000708. A failure to locate a directly duplicating theorem does not establish novelty.

## Rights and citation

Copyright (C) 2026 Ryutaro Yonezu. All rights reserved, including code and supplementary material. Human peer review has not been performed. Cite the live CITATION.cff and final DOI linked in the live repository; the citation file within this immutable ZIP was prepared before DOI registration.
