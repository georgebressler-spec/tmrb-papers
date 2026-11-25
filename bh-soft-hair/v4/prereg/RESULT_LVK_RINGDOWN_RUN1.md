# Result: TMRB ringdown prediction against GWTC-5.0 (run 1 of 1)

Registered in commit `76d92c7` (pushed 16:06 UTC Nov 18 2026). Input transcribed and committed in `d590909` before the run. Frozen script `lvk_ringdown_verdict.py` (sha256 `b956efa6…`, unchanged). Run once; output in `lvk_ringdown_RUN1_output.txt`.

## Verdict: **EXCLUDED** (primary and all five secondaries)

| Analysis (GWTC-5.0, pSEOBNRv5PHM, Eq. 18 definition) | δτ̂₂₂₀ median | 90% interval | Verdict |
|---|---|---|---|
| **All events, multiplied posteriors (eq. 21) — primary** | **+0.07** | **[+0.02, +0.13]** | **EXCLUDED** |
| All events, hierarchical mean (eq. 22) | +0.09 | [+0.03, +0.16] | EXCLUDED |
| All events, hierarchical population marginal (eq. 22) | +0.09 | [−0.01, +0.22] | EXCLUDED |
| Five highest-SNR events, multiplied (p. 24) | +0.02 | [−0.06, +0.10] | EXCLUDED |
| Five highest-SNR without GW250114, multiplied (p. 24) | +0.08 | [−0.04, +0.22] | EXCLUDED |
| All events without GW250114, multiplied (p. 24) | +0.11 | [+0.04, +0.20] | EXCLUDED |

The registered TMRB prediction was δτ̂₂₂₀ = −0.095 at t₀ = 0 (band −0.126 to −0.070 for spins 0.50–0.80). Every combined interval in the source lies entirely above the band. The data point the other way: where they deviate from GR, damping times are *longer*. LVK themselves attribute this partly to selection effects and to the influence of single events.

**Failures stand.** Nothing in the registration is changed after reading.

## What this means (as registered)
Under its stated assumptions (Gap 17: the torsion modulation advances in time; Gap 18: every sideband shares the ℓ=m=2 damping time), the v4 ringdown prediction is **disfavoured by published data**. The paper must say so in §7 and in the abstract, and cannot present the prediction as a 2035 test.

## Robustness of the verdict (*reasoning*; not part of the registered rule)
- **The registered mapping was the one most favourable to TMRB.** Mapping the inspiral-merger-ringdown analysis to t₀ = 0 gives the smallest predicted shortening; later start times predict larger shortening, which is further from the data.
- **The tightest margin is the five highest-SNR subset.** Its lower bound is −0.06, against the band's upper edge of −0.070. That subset is the least affected by low-SNR selection effects. A non-spinning population (−0.044, outside the registered band) would sit inside that one interval; this is **exploratory** only, since it falls outside the registered band.
- **The template is not the TMRB waveform.** pSEOBNR changes the ℓ=m=2 damping time inside a full inspiral-merger-ringdown model. Its δτ̂₂₂₀ is the closest published analogue to the Table 2 single-mode fit, not an identical quantity.

## AAR
1. **Supposed to happen:** a pre-registered comparison, run once, with an outcome that stands, and with every rule written before any number was read. **We know it worked:** the registration (`76d92c7`) precedes the input (`d590909`) and the run, and the script hash is unchanged.
2. **What happened:** the test ran exactly as registered and gave a clear negative result on the paper's headline gravitational-wave prediction.
3. **Why it differs from what the paper expected:** v4 r8 assumed the comparison would be decided by ET/CE around 2035. Published GWTC-5.0 bounds were already about 5% wide (multiplied posteriors) and sit on the opposite side of GR.
4. **Sustain:** title-only source selection before registration; numbers transcribed and committed before running; one run. **Change:** check what existing data already constrain before calling a prediction "future".

## Impacts (future-paced)
- **1st order:** v4 §7, Table 2, the predictions table, the abstract and the conclusion must report that the ringdown prediction is disfavoured by GWTC-5.0.
- **2nd order:** Gaps 17 and 18 stop being bookkeeping. The prediction survives only if the torsion modulation does not shorten the fitted damping time, which removes the paper's gravitational-wave test.
- **3rd order:** the κ_CE "structural identity" between the celestial comb and the horizon sidebands (§7) loses its only observable consequence in current data.
- **4th order:** for the programme as a whole, the X24si loop worked as designed. A claim met an outside instrument, with criteria written first, and the refutation is recorded, not repaired.
