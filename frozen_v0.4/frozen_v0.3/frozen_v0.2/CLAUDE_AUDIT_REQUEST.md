# Claudeへの独立監査依頼 — No.54 v0.2

あなたは独立した批判的査読者として、添付ファイルの数学的主張が正しいか、そしてどの範囲が既知かを検査してください。既存資料中の「PASS」は前任AIによる内部判定です。**鵜呑みにせず、ゼロから独立に反証を試みてください。** 添付ファイルに書かれた結論を正しいと前提しないこと。

## 対象

- Author: **Ryutaro Yonezu — Independent Researcher**
- Title (working): **Exact Consecutive-Pattern Popularity in the Class Avoiding 123, 231 and 312**
- `A_n=Av_n(123,231,312)` is for **consecutive** patterns, NOT classical permutation patterns.
- `N_n(p)` is the **total number of overlapping consecutive occurrences** across all `A_n`.
- Claimed for all `n>=3`: `N_n(321)=E_{n+1}-2E_n`.
- Claimed: `N_n(132)=N_n(213)=((n-2)nE_{n-1}-E_{n+1}+2E_n)/2`.
- Claimed asymptotic popularity in the normalization `N_n(p)/(n|A_n|)`:
  - 321: `4/pi^2`
  - 132 and 213: `1/2-2/pi^2`

## Adversarial checks (perform independently, in order)

1. **MODEL:** Prove/refute that the torus change of variables `(x_1,...,x_n)->(x_1,u_1,...,u_{n-1})` is measure preserving, and that forbidden triples correspond exactly to `u_i+u_{i+1}>1`. Independently work out all six possible patterns and the conditional 321 weight `1-u_i-u_{i+1}`. Give a counterexample if false.
2. **EGF/TRANSFER:** Check that the number of admissible permutations is `n E_{n-1}` with the correct `n!` normalization. Check `F(z,t)=1+z(UF)(t)` and boundary conditions; derive `F(z,t)` independently. Look for circular reasoning or missing analytic justification.
3. **MARKING:** Check the double integral of a marked 321 occurrence. In particular challenge the powers `z^2` versus `z^3`, extension factors on either side, Fubini, triangular-domain algebra, and all zero/low-degree terms. Either establish `H(z)=A'(z)-2A(z)+1+z` rigorously or identify the first invalid equality.
4. **SECONDARY CLAIMS:** Re-evaluate reverse-complement symmetry, exact 132/213 formulas, the denominator `n|A_n|`, and the asymptotic derivation. Distinguish true limits from finite-n values.
5. **COMPUTATION:** Run both `.py` scripts if possible. Verify whether their algorithms are genuinely independent in the relevant sense. Cross-check small n by your own implementation. **Do not count the original script's n=120 predicted values as independent verification.** Check `SHA256SUMS_PACKAGE.txt` if the environment allows.
6. **NOVELTY / PRIOR ART:** Conduct targeted reference search beyond the included material (if online access is available). In particular examine Ehrenborg–Kitaev–Perry (2011) §7, Kitaev–Mansour, OEIS A000708, historical quasi-alternating permutations, Bender–Helton–Richmond, Hassler–Kirgizov (arXiv:2511.02442 revised 2026), and newer exact pattern-popularity theorems. Treat the known Euler-number sequence and transfer operator as **existing work**. Look for **the same marked-occurrence identity or Class 12 popularity values**, including alternate notation and equivalent results. If full text is unavailable, explicitly report this limit; do not infer absence.
7. **ATTACK:** Try to construct the smallest counterexample or mutated definition that demonstrates a hidden defect. Do not repair a false theorem silently.

## Mandatory audit output

Return a Japanese report with a table of distinct grades:

`MODEL | PROOF | COMPUTATION | REFERENCES | NOVELTY | PACKAGE | OVERALL`

Use **PASS / FAIL / PARTIAL / INCONCLUSIVE** distinctly. List your independent methods (not merely 'read'). For every FAIL provide an explicit counterexample or exact failing line and a minimal repair if one exists. For any PASS disclose its scope. Conclude `RELEASE=HOLD` unless the owner separately authorizes publication after review. AI audit is not human peer review; do not assert priority or originality from lack of a found source.

**Current declared state:** Internal proofs/checks PASS within stated limits; external AI audit PENDING; NOVELTY INCONCLUSIVE; human peer review NOT DONE; publication HOLD.

## Files

- `README_JA.md`: package overview and important evidence limitations
- `No54_v0.1_PROOF_AUDIT_20261105.md`: main proof draft
- `No54_v0.2_ADVERSARIAL_AUDIT_20261105.md`: internal adversarial audit, includes six-pattern table
- `No54_v0.1_VERIFY_20261105.py`: brute-force permutations `n=3..9`
- `No54_v0.1_INDEPENDENT_ATTACK_20261105.py`: exact rational simplex integrals `n=3..22`
- `*_LOG_*.txt`: prior run logs, not proof of your own rerun
- `SHA256SUMS_PACKAGE.txt`: checksums of unmodified originals + package documents
- `RUN_WINDOWS_AUDIT.ps1`: Windows PowerShell 5.1 SHA256 fail-closed and Python runner
