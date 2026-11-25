# Audit 3 of the soft-hair paper, v4 r3 (Nov 17 2026)

Audited file: `bh_soft_hair_v4_r3.tex` sha256 `454475fc…`. Provenance is marked as execution, retrieval or reasoning.

## Passed
- **Weight-dependent numbers all agree with the symmetric weights** (*execution*):
  - The weights are 0.333/0.235/0.083/0.014/0.001, with a sum of 1 + 1e-12.
  - ΔS is 20.874, and 3^19 = 1.16e9 states.
  - S_tors is 1.598.
  - The sideband shares are 80%, 97% and 36%.
- **No stale ln 2 or 20.468** appears outside the change history.
- **Build:** clean, 20 pages, no undefined references.
- **Cross-references:** all 16 gaps referenced in the text exist.

## Findings, ranked
1. **The 9-line comb cannot be resolved in a ringdown.** For 30 M☉, the ℓ=2 mode has f = 402.5 Hz and damping time 1.66 ms. That gives a quality factor Q ≈ 2.1 and a linewidth (FWHM) of **192 Hz** (*execution*). The comb spacing is 18 Hz, about 0.09 of one linewidth, so the nine lines merge into a single line whose shape is slightly distorted. Fig. 4 draws the lines with 9 Hz half-width, about 10 times too narrow.
   Separately, the modulation δV(θ) varies with angle on the horizon, not with time. A modulation in angle mixes angular modes; an evenly spaced comb in frequency needs a modulation in time (*reasoning*).
   This is the paper's headline observational prediction.
2. **The entropy expansion skips the logarithm.** S_TMRB = A/4G + ΔS + O(G/A) leaves out the one-loop c_log ln(A/G) term, which is non-zero for Schwarzschild holes (Sen 2012, *retrieval*). §5 of the paper writes the same term itself. For a 10 M☉ hole, ln(A/G) = 183, so the log term is of order 10² nats (*execution*, with an order-one coefficient). The constant ΔS ≈ 21 is therefore not the leading correction unless the φ^{−N*} factor of Gap 15 holds. The equation should carry the log term, or say that it is dropped on that assumption.
3. **"Four near-term falsifiable predictions"** in the abstract and introduction contradicts the table, which now marks the entropy gap untestable. The "Hawking spectrum mod." row gives no link between Hawking radiation and 10⁻³–10⁻² Hz noise on a satellite in low Earth orbit (*reasoning*).
4. **Gap 5 claims a bijection between the 9 torsion phases and the parafermion primaries.** The parafermion theory has 45 primaries, as §5.1 and Gap 13 say.
5. **GRACE residuals versus the limit:** per-site residuals of 10⁻¹⁹ to 10⁻¹⁸ m/s² sit beside a 95% limit of 4×10⁻⁹. That is a gap of nine to ten orders. Either the residual is a different quantity, or one of the two numbers is wrong; the script decides.
6. **Fig. 5 draws the GWOSC limit below the prediction band,** which reads as exclusion. The caption must say that it bounds only a ~100 Hz component.
7. **The Fig. 3 caption** still calls φ^{−N*} "the horizon-hair UV regulator". It should say "proposed (Gap 15)".
8. **Charges:**
   - Q⁽ⁿ⁾ = η θₙ M³ with θₙ ∈ [0, 2π) gives Q⁽⁹⁻ᵏ⁾ ≠ −Q⁽ᵏ⁾, although §3 calls them conjugates. The charge is defined only modulo 2π η M³; equivalently, the phase e^{iθ} is the label.
   - G₄/G₁₁ is quoted without units, although G₁₁ has units of length⁹.
   - "T₀ = 2π/Δλ × (galactic period unit)" implies an undefined unit of 63.3 Myr.
9. **The GWOSC search design:** it looked for a ringdown comb in 4531 s of strain that contains no merger, so it tests steady lines, not the model's comb (*reasoning*). Recorded in the text only as far as the Δg reinterpretation.
10. **Fateev–Zamolodchikov, NPB 280, 644** is still unverified; Crossref is outside this session's network.

## Resolution (George: "1, fix them all"), v4 r4
`bh_soft_hair_v4_r4.tex`, PDF 21 pages, no undefined references, no overfull boxes (the r3 table overrun is also fixed).
1. **Ringdown:** §7 is retitled "An Unresolved Comb and Its Ringdown Signature".
   - The paper now states that the angle-only modulation gives no frequency comb, and assumes a time-advancing pattern (Proposed, Gap 17).
   - New Eq. (comb_ratio): Δf/FWHM = κQ/9 ≈ 0.094 at every mass.
   - Prediction: the ℓ=m=2 damping time is **4.6% shorter** than GR (9.9% at spin 0.7, from the Berti–Cardoso–Will fits), with the frequency unchanged, at every mass. The mismatch to a single mode is 6.0e-5 (2.6e-4 at spin 0.7); the shape is visible at SNR ≈ 90 (44). *Execution:* `ringdown_signature.py`, `ringdown_signature_a07.py`.
   - The shared-damping and spin assumptions are Gap 18. Fig. 4's bottom right is redrawn with the true line width. The table, the naive-shift note and the conclusion are updated.
2. **Entropy:** c_log ln(A/G₄) is added to the abstract equation and the boxed equation. The text states that the log is ~10² nats for 10 M☉ and that φ⁻⁹ ≈ 0.013 would reduce it to ~2.4 c_log; ΔS leads only if Gap 15 closes. The intro, the conclusion, the Fig. 2 caption and the table row are updated.
3. **Other fixes:**
   - The prediction count and table caption now say three are near-term falsifiable.
   - The Hawking row marks its mechanism as not derived here.
   - Gap 5 now gives 45 primaries.
   - The GRACE residuals are withheld pending a script re-check.
   - The Fig. 5 caption carries the GWOSC caveat; the Fig. 3 caption says "proposed".
   - Charges are defined modulo 2π, so Q⁽⁹⁻ᵏ⁾ ≡ −Q⁽ᵏ⁾.
   - The units of G₄/G₁₁ are flagged.
   - T₀ is marked as an input (t_gal ≈ 63.3 Myr).
   - The GWOSC segment is stated to contain no merger.
   - The Fateev–Zamolodchikov reference is now JETP 62, 215 (1985) (*retrieval*).
   - Berti–Cardoso–Will 2006 is added.
