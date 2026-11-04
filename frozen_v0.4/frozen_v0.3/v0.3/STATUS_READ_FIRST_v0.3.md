# No.54 v0.3 — read first / status and provenance

**Purpose:** bibliography-and-attribution-only revision of the previous v0.2 Claude audit bundle, not a new mathematical draft. Date: 2026-11-05 (JST). Research author: **Ryutaro Yonezu — Independent Researcher**. Prepared by ChatGPT from the user's Claude audit report and linked original bibliographic sources.

- **MODEL / PROOF / COMPUTATION:** Claude v0.2 independent AI audit reported **PASS**, including its own C enumeration `n=3..13`, symbolic checks and mathematical derivations. The current v0.3 does **not** claim that those independent checks were rerun by Claude on v0.3. See the user's full external review for original details; that full report was not supplied as a separate file for this package.
- **REFERENCES:** Primary-source crosscheck of HK v2 Table 1 / Eq. (1.1), EKP Section 7 / Theorem 7.5, and Zhao 2014 introduction performed by **ChatGPT in a web session**. Claude reported it had **NOT** fetched/verified those sources in its environment. Distinguish `REFERENCES=PASS (ChatGPT side, targeted three-source checks)` from `REFERENCES=PARTIAL (Claude first-hand audit)`. Do not attribute these source checks to the human researcher without confirmation.
- **NOVELTY:** **INCONCLUSIVE**. Same marked-321 theorem was not found in the targeted sources but exhaustive priority verification is impossible.
- **PEER REVIEW:** Not human peer-reviewed.
- **RELEASE:** **HOLD**. This ZIP is for Claude differential audit only, not publication.
- **WINDOWS:** Runner added for PowerShell 5.1 but Windows execution has **not** been tested in this container.

**What changed:** Section 8 only of the v0.1 proof file has been replaced in `v0.3/No54_v0.3_PROOF_REFERENCES_20261105.md`. Sections 1–7 and 9, including the theorem statement, all mathematical identities, and computation descriptions, are byte-for-byte the same when the input is split at the two section-heading boundaries. The old original and all 12 v0.2 package files are preserved byte-for-byte under `frozen_v0.2/`.

**Historical wording:** `frozen_v0.2/README_JA.md`, `frozen_v0.2/CLAUDE_AUDIT_REQUEST.md`, and the v0.1 proof header say 'independent AI audit pending' because they are unmodified history. This `STATUS_READ_FIRST_v0.3.md` supersedes them for current status; do not change the frozen records.

**Evidence URLs:**

- https://arxiv.org/html/2511.02442v2 (HK Table 1, Eq. 1.1, Section 5)
- https://www.ms.uky.edu/~jrge/papers/Ehrenborg_Kitaev_Perry_A_spectral_approach.pdf (EKP printed pp.346-349)
- https://cs.uwaterloo.ca/journals/JIS/VOL17/Zhao/zhao3.pdf (Zhao p.1 definition / Table 1)
- https://oeis.org/A000708 (preexisting sequence)

See `CLAUDE_DELTA_AUDIT_REQUEST.md`, `DIFF_SECTION8_v0.2_to_v0.3.patch`, and `verify_delta_v0.3.py` before using the proof.
