# No.54 v0.4 — Claude differential audit request

Please audit **ONLY the two editorial status-line changes plus the new bibliographic metadata appendix**, preserving your earlier mathematical audit scope.

1. Verify all paths in SHA256SUMS_v0.4.txt (and nested frozen v0.3 manifest), exact path inventory, no missing or extra files. Run `python -I v0.4/verify_delta_v0.4.py`.
2. Compare frozen v0.3 proof `frozen_v0.3/v0.3/No54_v0.3_PROOF_REFERENCES_20261105.md` and current `v0.4/No54_v0.4_PROOF_REFERENCES_STATUS_20261105.md`. Apply DIFF_v0.3_to_v0.4.patch; the only changes must be the top-level audit status line and the parenthetical annotation in the theorem header. No mathematical claims, formulas, proof, code, or references changed.
3. Check attribution: v0.2 MODEL/PROOF/COMPUTATION PASS is a user-supplied *Claude audit report*; v0.3 delta passed per the user-supplied Claude review. Claude did not independently fetch HK v2/EKP §7/Zhao as recorded. No claim of human peer review.
4. For BIBLIOGRAPHIC_SOURCE_CHECK_v0.4.md, verify against source pages **only where accessible**. If blocked, mark personal firsthand REFERENCES=PARTIAL, and separately state bibliographic facts checked by ChatGPT. No credit to the human owner for inspections not performed.
5. Report PACKAGE/DIFF/ATTRIBUTION/REFERENCES/NOVELTY and OVERALL separately. Keep NOVELTY=INCONCLUSIVE and RELEASE=HOLD. Windows=UNTESTED unless actually run on Windows.

This is not a request to publish, or to re-run mathematical computations that were byte-frozen. If any substantive mathematical error is noticed, flag it independently.
