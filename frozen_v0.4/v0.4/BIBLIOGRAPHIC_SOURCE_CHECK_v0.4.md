# No.54 v0.4 — source metadata cross-check (addendum only)

Date: 2026-11-05 (JST). This is a targeted ChatGPT verification record, **not** Claude's firsthand verification and **not** the human author's firsthand verification. This text does not establish uniqueness or priority of No.54.

## HK v2: exact Class 12 correspondence and normalization

- Original paper: Nathanaël Hassler and Sergey Kirgizov, *Emerging consecutive pattern avoidance*, arXiv:2511.02442v2, version dated 10 October 2026. Primary HTML: https://arxiv.org/html/2511.02442v2
- Table 1: six pattern columns, in order 123, 132, 213, 231, 312, 321. The Class 12 row reads (empty, ?, ?, empty, empty, ?), hence the forbidden patterns are 123, 231, 312 and the unknown asymptotic popularity entries are 132, 213, 321.
- Equation (1.1) defines pop with denominator n |A_n|. In the same article, Section 5 calls Classes 10, 12, 13, 14, 15 open and asks about irrational values. This is what the No.54 claims directly address; it is not a statement that later work cannot exist.
- Reviewer provenance: Claude reported v2 unavailable via its allowlist. The previous v0.3 section 8 and this targeted check are attributable to ChatGPT only.

## EKP publisher/institutional metadata

- Richard Ehrenborg, Sergey Kitaev and Peter Perry, *A spectral approach to consecutive pattern-avoiding permutations*, *Journal of Combinatorics* 2 (3) (2011), 305–353, DOI: 10.4310/JOC.2011.v2.n3.a1.
- Institutional bibliographic record from coauthor Sergey Kitaev's University of Strathclyde page: https://pureportal.strath.ac.uk/en/publications/a-spectral-approach-to-consecutive-pattern-avoiding-permutations/
- Manuscript: https://arxiv.org/abs/1009.2119 . Earlier v0.3 ChatGPT review records Section 7 and Theorem 7.5 as concerning the avoidance count n E_(n-1), not a marked consecutive-321 statistic. The current v0.4 checks the *publisher metadata* anew; it does not claim a fresh independent reading of the printed Section 7.
- Reviewer provenance: Claude could not read Section 7; a different assistant session did so. Do not attribute this to Claude.

## Zhao bibliographic metadata and definition boundary

- Alina F. Y. Zhao, *Pattern Popularity in Multiply Restricted Permutations*, *Journal of Integer Sequences* 17 (2014), Article 14.10.3. Publisher issue index: https://cs.uwaterloo.ca/journals/JIS/vol17.html ; publisher abstract: https://cs.uwaterloo.ca/journals/JIS/VOL17/Zhao/zhao3.html . Both show the bibliographic identification.
- Zhao's classical pattern definition uses arbitrary increasing indices i1 < ... < ik (not necessarily adjacent). In contrast, No.54 counts only consecutive indices; the problems are distinct. First-page source: https://cs.uwaterloo.ca/journals/JIS/VOL17/Zhao/zhao3.pdf . Previous ChatGPT check considered the definition; v0.4 independently rechecks metadata against the publisher abstract and issue listing.
- Reviewer provenance: Claude did not access Zhao in its audit.

## Decision boundary

MODEL / PROOF / COMPUTATION: PASS in Claude's **user-supplied v0.2** audit, retained by Claude's v0.3 diff audit; no human peer review. REFERENCES: targeted ChatGPT verification of the above bibliographic data, with Claude firsthand review PARTIAL. NOVELTY: INCONCLUSIVE. PUBLICATION: HOLD. No release authorization is inferred.
