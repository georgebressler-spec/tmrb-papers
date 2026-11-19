# Audit 4 of the soft-hair paper, v4 r4 → r5 (Nov 18 2026)

Audited: `bh_soft_hair_v4_r4.tex`, plus, for the first time, the two analysis scripts the paper cites. They are on Drive in the project Drive: `TMRB_GWOSC_torsion_search.py` (modified May 2), `results_gwosc_o3a.json` and `TMRB_GRACE_torsion_search.py`.

## 1. Confirmations George asked for

### 1a. Ringdown damping time (*execution*, two scripts using different methods)
| Method | Schwarzschild | Spin 0.7 (BCW fits) |
|---|---|---|
| Complex overlap, free f, τ, amplitude, phase (`ringdown_signature.py`) | −4.6% | −9.9% |
| Real-strain least squares, scipy (`verify_ringdown_independent.py`) | −4.4% | −9.7% |
| Small-x analytic expansion | −4.8% | −11.1% |

- **Confirmed:** the damping time is about 4.6% shorter, with frequency unchanged to 0.2%. The result is mass-independent, because Δf/FWHM = κQ/9 and 2πΔfτ = 2κQ/9.
- **Qualification added in r5:** the shift depends on where the fit starts. It is −7.0%, −9.5% and −12.9% for starts at 0.5τ, τ and 2τ (spin 0.7: −14%, −18%, −26%). The paper now says "for a fit from the peak" and that a measurement must quote its start time.
- **Assumptions still open:** every sideband shares the damping time (Gap 18), and the pattern advances in time (Gap 17). The BCW fit coefficients and Schwarzschild ωM = 0.37367 − 0.08896i are *retrieval*. The BCW fits reproduce the Schwarzschild values to 1.5%.

### 1b. Log-term caveat
- **Confirmed** (*execution*): ln(A/G) = 183.3 for 10 M☉; φ⁻⁹ = 0.01316, which gives 183 × 0.0132 = 2.41.
- **Qualification added in r5:** the log term exceeds ΔS_tors = 20.87 **in magnitude** whenever |c_log| > 0.114, and its sign depends on the field content.
- **Not verified here:** Sen's exact coefficient (*retrieval*; arxiv.org is outside this session's network). It is order one for pure gravity, so the caveat stands.

### 1c. LIGO segment length (*execution*, reading the script and its saved output)
- **Confirmed.** The script loads the two 4096 s files (GPS 1238163456 and 1238167552, an 8192 s span), masks the gaps and keeps the longest gap-free stretch. `results_gwosc_o3a.json` records `T_obs_s: 4531.0`.
- r5 now says "the longest gap-free stretch, 4531 s, of the 8192 s span".
- **My r3 error, fixed in r5:** the script used the symmetric weights n = −4…4, not the one-sided n = 0…8 I had written. The stack gain is √N_eff = 2.06, which I recomputed from the script's own weights.

## 2. New findings from the scripts (not edited: George decides)

1. **The published GRACE numbers come from the script's offline-demo generator, not from GRACE data.**
   - With no `--grace-file` argument the script runs `offline_demo_results()`. That function draws residuals uniformly in [1e-19, 1e-18], slopes from normal(0.692, 0.18) and z-scores from normal(0, 0.40), all from seed 20260426. It also **sets coordinate 21's slope to exactly 0.75**.
   - These are exactly the values the paper reports: residuals 10⁻¹⁹–10⁻¹⁸, mean slope 0.692, and coordinate 21 at "α = 0.75, exactly matching".
   - The real-data path cannot produce them. It converts water thickness to gravity with 2πGρh, so 1 cm of water gives 4.2×10⁻⁹ m/s², and real hydrology signals are tens of cm.
   - The "95% CL upper limit 4×10⁻⁹" is a **hard-coded constant**, equal to 1 cm of water. The verdict `clean_null` is also hard-coded.
   - Whether a real run was ever made cannot be checked from these files.
2. **The right panel of Fig. 5 is synthetic too.** `fig5_constraints.py` draws its histogram from `rng.normal(0, 0.40, 45)` with the same seed.
3. **The GWOSC "null search" is a sensitivity projection, not a search.**
   - The script computes h₀ from the median noise level of the band and the observing time. It never tests the strain at any comb frequency.
   - Its verdict string, `clean_null`, is hard-coded.
   - The 45 "templates" are Earth coordinates, which one strain channel cannot tell apart, so the Bonferroni factor (×1.75) only makes the number more conservative.
   - The figure, 1.6e-16, is a sensitivity floor and should be called one.
4. **The paper says both scripts are "included in the Zenodo record for this paper".** The v3 record (20331456) contains neither; I listed its files on Nov 17.

## 3. For Jimmy (rigour check)
- Re-derive Δf/FWHM = κQ/9 and the envelope factor Σ wₙ cos(2πnΔf t). Then check that a single-mode fit shortens τ by 4.4–4.8% from the peak (scripts in `scripts/`).
- Judge whether "fit from the peak" is the right reference, given how real ringdown analyses choose their start time.
- Check Sen's coefficient against arXiv:1205.0971, and whether its sign matters for the caveat.
- Read the two analysis scripts (§2) and say whether the GRACE section can stand in any form without a real run.
