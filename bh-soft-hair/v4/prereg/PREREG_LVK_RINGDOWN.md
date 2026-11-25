# Pre-registration: TMRB ringdown prediction against published LVK ringdown tests

Registered by Claude for George Bressler, Nov 18 2026. **The outside clock is the GitHub push time of the commit that adds this file.** At registration no LVK result on the ℓ=m=2 damping time had been read in this session; only paper titles and arXiv IDs had been listed.

## Claim (from v4 r8, §7 and Table 2)
Nine unresolved ℤ₉ sidebands, each sharing the ℓ=m=2 damping time (Gap 18) and advancing in time (Gap 17), make a single-mode fit return a damping time shorter than the GR value. The fractional change δτ̂₂₂₀ = τ_fit/τ_GR − 1 is the same for every event at a given spin and start time, so it is a **common deviation** across events.

- **Registered point:** remnant spin 0.69, giving δτ̂ = −0.095 at t₀ = 0.
- **Registered band:** spins 0.50–0.80, giving −0.126 to −0.070 at t₀ = 0. Other start times are interpolated in Table 2.
- **Frozen script:** `lvk_ringdown_verdict.py`, sha256 `b956efa655363c70ca64a09a7fdceed22fae033ff74712e4b9ff8692214c29da`.

## Source rule (fixed now)
Use the first source in this list that reports, as numbers in text or a table, a result for the ℓ=m=2 damping-time deviation combined over events:
1. GWTC-5.0: Tests of General Relativity, arXiv:2607.19293v1.
2. GWTC-4.0: Tests of General Relativity. III. Tests of the Remnants, arXiv:2603.19021v1.
3. Tests of General Relativity with GWTC-3, arXiv:2112.06861v3.

A source that shows the combined result only in a figure counts as "not reported"; figures are not digitized.

## Primary-analysis rule (fixed now)
Among the combined ℓ=m=2 damping-time results in the chosen source:
1. Prefer a **common-deviation** combination (joint likelihood or multiplied posteriors) over a hierarchical one. If only hierarchical results exist, use the population mean's 90% interval.
2. Then prefer an **inspiral-merger-ringdown-based** parameterized analysis (pSEOBNR type), mapped to t₀ = 0, over ringdown-only analyses.
3. Then prefer the one with **the most events**. On a tie, take the first listed in the paper.

All other combined damping-time results are reported as secondary, with their own verdicts.

## Transcription and conversion
- Numbers are copied by hand from the source, with page and table or equation references, into `lvk_ringdown_input.json`. That file is committed before the script runs.
- If the source reports a damping-*rate* deviation δω̂_I, the script converts it with δτ̂ = 1/(1+δω̂_I) − 1. If the source defines the parameter differently, the definition is quoted and converted in the same way.
- **Ringdown-only analyses:** a start time in units of remnant mass converts as t₀/τ = t₀[M]·ω_I M = t₀[M] × 0.0812 (spin 0.69). If no start time is stated, t₀ = 0 is used and noted.

## Decision rule (90% credible interval [lo, hi] of δτ̂; point p; band [b₋, b₊])
| Verdict | Condition |
|---|---|
| **EXCLUDED** | the whole band lies outside [lo, hi] |
| **DISFAVORED** | p lies outside [lo, hi], but part of the band lies inside |
| **CONSISTENT, NOT DISCRIMINATING** | p and 0 (GR) both lie inside [lo, hi] |
| **FAVORED OVER GR** | p lies inside [lo, hi] and 0 does not |

## Run rule
Run once, on the primary and secondary analyses together, after the input file is committed. The result and its output are committed as they come. **Failures stand.** No change to the band, the spin, the source order or the rules after reading.

## What each outcome would mean (written now)
- **EXCLUDED or DISFAVORED:** published data already disfavor the v4 ringdown prediction under its stated assumptions (Gaps 17–18). The paper must say so in §7 and in the abstract, and the prediction cannot be presented as a 2035 test.
- **CONSISTENT, NOT DISCRIMINATING:** the data cannot yet tell the prediction from GR. The paper states the interval width needed to discriminate.
- **FAVORED OVER GR:** published data prefer a shorter damping time. That would **not** confirm TMRB, because many effects shorten a fitted damping time (overtones, start-time choice, systematics). It would call for an independent replication by a person outside this model family before any claim is made.

## Known limitations, stated in advance
- LVK templates are not the TMRB waveform. Mapping their δτ̂₂₂₀ to the single-mode fit of Table 2 is approximate, especially for inspiral-merger-ringdown analyses.
- The remnant spins of the combined events vary. The registered band (0.50–0.80) stands in for that spread.
- This is one AI model registering and running its own test, so its convergence with the paper is not corroboration. Jimmy reviews it when he is back.
