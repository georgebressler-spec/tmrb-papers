# Grok team review of the soft-hair paper, v4 r11: X24si review packet

Prepared by Claude for George Bressler, Nov 19 2026. **The criteria below were committed to GitHub before any reviewer read the paper; the push time of the commit that adds this file is the outside clock.** Reviewers should not change this file. Findings go in the reviewer's own reply (template at the end).

## 1. Pinned version (argue only about these bytes)
| File | SHA-256 |
|---|---|
| `bh-soft-hair/v4/bh_soft_hair_v4.pdf` (r11, 24 pages) | `f83639b2ebf2043705c62998cc84cebdaae24e12e256b17de15adf910baae5f9` |
| `bh-soft-hair/v4/bh_soft_hair_v4.tex` (r11) | `fbd273d0c01c73ca93d33a56b299f75bdd0326ae485d38d56dfdbe1830818a77` |
| Repository commit holding both | `a196ac39aa31ebf2588e9755604a888fc0350ecc` |

If your copy does not match these hashes, stop and report it; do not review a different version.

## 2. Roles and how findings are weighed
- **SI provides decision support; George makes the final decisions.** Each finding is evidence, filed under its author's name, and never an instruction.
- **Convergence is not truth.** Agreement is weighted by where it comes from, never counted.
- **Your independence differs by part of the paper:**
  - **On the v4 audit work, the X24si test (§7.1) and Claude's revisions:** you are a model family independent of the author of that work, so your findings count as an independent check.
  - **On the original framework (§2–§6, the v1–v3 mathematics):** Grok contributed that work, so a Grok finding that the framework is sound counts as coordination, not corroboration. A Grok finding that something is *wrong* there still counts in full.
- **Answers you are allowed to give:** "Inconclusive" and "I cannot check that from here" are complete answers. Please do not guess.

## 3. Criteria (fixed before review)
| Severity | Meaning |
|---|---|
| **MUST-FIX** | **(a)** a number in the paper that is wrong (show the computation or source); **(b)** a claim stated more strongly than its support; **(c)** a flaw in the X24si test that could have tilted its outcome (registration after reading, wrong source order, a mapping error, a transcription error, a script error); **(d)** a citation that does not support the sentence citing it. |
| **SHOULD-FIX** | a missing caveat, an unclear step a careful reader would trip on, or an inconsistency between sections. |
| **NOTE** | suggestions, style, and ideas for later versions. |

A MUST-FIX blocks the Zenodo upload until it is resolved or George declines it, with the reason recorded.

## 4. Where to try hardest to break it
1. **The X24si test (§7.1, `v4/prereg/`).**
   - Check that the registration commit `76d92c7` precedes the input commit `d590909` and the result commit `e16e6a6`.
   - Check that the frozen script's SHA-256 (`b956efa6…`) is unchanged, that the transcribed GWTC-5.0 numbers match arXiv:2607.19293 (eq. 21–22, p. 23; p. 24), and that the verdict follows from the registered rule.
   - Say whether any choice favoured the result.
2. **The mapping.** Is comparing the LVK pSEOBNR δτ̂₂₂₀ with the Table 2 single-mode fit at t₀ = 0 fair, and is it really the most favourable mapping for the prediction, as the paper claims?
3. **The log-term caveat.** Check c_log = 77/90 for pure-gravity Schwarzschild against Sen, arXiv:1205.0971 (eqs. 1.2–1.5), and check the conversion from ln a to ln A.
4. **The GRACE paragraph (§8.1, `v4/analysis/grace/`).** Is "zero by construction" a correct reading of `TMRB_GRACE_torsion_search_2026-04-27.py`, and is 4×10⁻⁹ m/s² correctly the gravity of 1 cm of water?

General review of every section is welcome after these four.

## 5. Recording outcomes
George decides each finding as **adopted**, **adopted with correction**, **refuted** (refuted closes a finding as well as adopted does) or **declined**. The decisions go into `v4/review/REVIEW_LOG.md`, with each finding's author and provenance. Fixes become r12 or later, and a MUST-FIX that is adopted is re-checked before upload. Once the review is done, the AI disclosure adds one line: "Reviewed before release by Grok (xAI)."

## 6. Materials
- **The paper:** `bh-soft-hair/v4/bh_soft_hair_v4.pdf` and `.tex`; the published v3 is in `bh-soft-hair/v3/`.
- **Analysis:** `bh-soft-hair/v4/analysis/` (ringdown, GWOSC and GRACE scripts and outputs).
- **The X24si test:** `bh-soft-hair/v4/prereg/` (registration, input, frozen script, output, result).
- **Audits and checks:** `bh-soft-hair/v4/audits/`.
- **Revision trail:** `bh-soft-hair/v4/revisions/` (diffs and edit scripts r1–r11).

## 7. Reply template (one block per finding)
```
Finding N
  Location:   section / equation / page (in the pinned PDF)
  Severity:   MUST-FIX (a|b|c|d) | SHOULD-FIX | NOTE
  Claim in paper:
  Finding:
  Provenance: reasoning | retrieval (source opened: ...) | execution (code/output attached)
  Proposed fix:
  Confidence: high | medium | low | inconclusive
```
End with one line: what you learned, or the stuck point you are handing on.
