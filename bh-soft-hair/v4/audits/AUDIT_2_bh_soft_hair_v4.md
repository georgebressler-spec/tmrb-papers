# Audit 2 of the soft-hair paper, v4 (Nov 17 2026)

Audited file: `bh_soft_hair_v4.tex` sha256 `c8cc8954…` (v4 r1, not yet on Zenodo).
Every number below was recomputed (execution) unless marked *retrieval* (from memory of the literature, no page opened) or *reasoning*.

## A. Fixed in v4 r2 (consistency and arithmetic; no physics claim changed)
`bh_soft_hair_v4_r2.tex` sha256 `6b1290c2…`, PDF `fe036756…` (19 pages, no undefined references), diff r1→r2 `6cd93dea…`.

1. **Nine sectors "per Planck area"** in prologue, abstract, introduction, encoding section and conclusion contradicted v3/v4's own cell area (8.79 ℓ_Pl²). Now "per torsion cell".
2. **Term 2 of §4** still used the v1/v2 tile count A/(4ℓ_Pl²) and wrote the area term as (A/4ℓ_Pl²) ln 9. Now uses N_cell = A/(4G₄ ln 9).
3. **Appendix A** still presented the v1/v2 count, calling G₄ = ℓ_Pl²/ln 9 "a natural Planck-unit convention", while Gap 8 calls the same identification the highest-priority open gap. The appendix is now labelled the v1/v2 count.
4. **Gap 9** said conservation plus modular invariance "together guarantee unitarity". That contradicts Gap 11 (added in v4). Now "necessary conditions; sufficiency is Gap 11".
5. **The footer DOI** (10.5281/zenodo.20326236) is the **v2** record, verified on Zenodo; v3 shipped with it too. Now the concept DOI 10.5281/zenodo.19981840.
6. **A v3 change item** ("concept DOIs") had been displaced below the v4 list by the v4 edit. It is back under v3.
7. **GRACE paragraph:** residuals of 10⁻¹⁸ versus a prediction of 6.3×10⁻¹⁵ is a gap of about four orders of magnitude, not "nine".
8. **Banerjee & Modak:** the page number is 073, not 063 (it already matched the DOI).

## B. Physics findings: George decides (not edited)
Ranked by how much they move the paper.

1. **The GWOSC limit contradicts the paper's own conclusion.** UL 1.6×10⁻¹⁶ m s⁻² (conversion recomputed: 1.60×10⁻¹⁶) is **39 times below** the predicted 6.3×10⁻¹⁵. §7.1 says this correctly ("a factor of ~39 below the Gaia-calibrated prediction"). The Interpretation paragraph then says the prediction "lies ~39× below the GWOSC UL" and that neither null result is in tension. Taken at face value, the paper's own search **excludes** its predicted amplitude at 95% CL. The other reading is that the strain-to-Δg conversion does not apply: a static Δg at Earth hotspots is not a 30–174 Hz strain line. Either way the current text cannot stand. Also: the GPS range spans 8192 s while the text says 4531 s (*execution*).
2. **The ln 2 term rests on weights that break the ℤ₉ symmetry.** With n = 0…8 and n² not periodic, w₈ ≪ w₁ (0.0000 vs 0.353), although §3.1 says n and 9−n are conjugate. The one-sided weights are **not** a DFT fixed point: max deviation 0.57 (*execution*). The ℤ₉-symmetric (periodised) weights are a fixed point (deviation 9×10⁻¹⁶) and sum to **3**, not 2. That gives ln Z_tors = **ln 3 ≈ 1.099**, so ΔS = 9 ln 9 + ln 3 ≈ 20.87, not 20.47. The paper cannot keep both "DFT fixed point / modular covariant" and "Z_tors = 2".
3. **The remnant argument fails at its own limit.** As A→0, S_TMRB → 9 ln 9 + ln 2 ≈ 20.5 nats, which is about 7.7×10⁸ states and is size-independent. That is exactly a finite-capacity remnant. The sentence that the correction is "dominated by the area term" holds for large holes, not at A→0 (*reasoning + execution*).
4. **The loop-convergence bound is wrong.** max_n w_n = w₀ = C, not C e^{−π/9}. And because the normalised weights sum to 1, the sum over branch labels at each loop order is 1, so weights alone give no decay with order (*reasoning*). Separately, φ^{−N*} no longer follows from w_n: v-history says the φ form was replaced by the Gaussian. The abstract's "golden-ratio weight suppresses loops" has no derivation in the current paper.
5. **Discrete-torsion citation.** Vafa's discrete torsion is classified by H²(G, U(1)), which is **trivial** for cyclic ℤ₉. H³(ℤ₉, U(1)) ≅ ℤ₉ is true, but it is the Dijkgraaf–Witten class (1990), not Vafa 1986 (*retrieval*). §2.2 and Gap 7 need the right object and citation.
6. **"Standard holomorphic criterion for unitarity"** (§5.1): modular invariance of Z(τ) is a consistency condition, not unitarity. Also τ = β/2π is real; a torus modulus must be in the upper half-plane (τ = iβ/2πL). "The diagonal invariant is the unique choice" is asserted, not shown (*retrieval*).
7. **The topological entanglement entropy comparison:** a ℤ₉ abelian topological order has total quantum dimension D = 3 (γ = ln 3), not 9⁹. "Quantum dimension 387,420,489" mislabels the count (*retrieval*).
8. **The entropy-gap prediction** (20.5 nats via "primordial BH merger statistics ~2030") has no stated observable. A 20-nat shift is invisible against S_BH ~ 10⁷⁸ for stellar holes (*reasoning*).
9. **Smaller items:**
   - In Eq. (sideband), Δω = f·κ/9 mixes ω and f. The 18 Hz is correct as a frequency spacing (computed 18.06).
   - Q^(n) = η θ M³ has no free coefficient, yet the text says the coefficient "is fixed by" the KK scale.
   - "Exactly 9 sub-dominant modes" while w₄…w₈ < 0.2%.
   - The 3-6-9 subgroup is called "dominant", but w₁ = 0.353 > w₃ = 0.022.
   - The loop formula S = (G₄/π) ln(ω/μ) is not dimensionless.
   - BanerjeeGuptaSen2008 is cited for logarithmic corrections, but it points to a non-logarithmic Lovelock paper.
   - The rhetoric "universe kept the receipt" and "the score is complete" outruns Gap 11.

## C. Checked and correct (execution)
- Z_tors one-sided is 2 + 1.05×10⁻¹².
- S_tors is 1.0681.
- The weights are 0.500, 0.353, 0.124, 0.022, and w₀+w₁ = 0.853.
- w₀+w₃+w₆ = 0.522.
- A_cell is 8.789.
- 9 ln 9 + ln 2 = 20.468.
- f_QNM(30 M☉) is 402.5 Hz, and the spacing is 18.06 Hz.
- Δλ is 1.7287.
- c(ℤ₉ PF) = 16/11.
- The model has 45 primaries.
- ln φ = 0.481 ≈ κ_prop is flagged in the paper as a coincidence, correctly.
- The GWOSC conversion arithmetic is 1.60×10⁻¹⁶.
- The GPS start is 2019-04-01.

Bibliography (*retrieval*): Hawking, AMPS, Penington, HPS, Page, Susskind, Donnay, Damour, CKW, Gibbons–Hawking, Vafa, Gepner–Qiu, AJL ×2, Levin–Wen, Kitaev–Preskill, Sen, Gaia DR3, GWOSC O3 and Wiese match their journals. Fateev–Zamolodchikov NPB 280, 644 is unverified: the parafermion paper I know is JETP 62 (1985) 215.

## D. Resolution (George: "Fix them all"), v4 r3
`bh_soft_hair_v4_r3.tex` sha256 `454475fc…`, PDF `336f0ad5…` (20 pages, no undefined references), diff r2→r3 `22d7b58e…`, figures `figs_v4_scripts_and_pdfs.tar.gz` `d98bfb4b…` (Zenodo v3 scripts, patched).

1. **GWOSC:** kept the number and stated that it lies 39× below the prediction. The conversion assumes Δg oscillating at ~102 Hz, while the prediction is quasi-static, so the limit bounds a ~100 Hz component only. Abstract, Interpretation and Conclusion now say this. The span reads "4531 s within the 8192 s span" (*still to confirm against the script*).
2. **Weights:** these are now the ℤ₉-symmetric periodised Gaussian: Z_tors = 3, the boundary term is ln 3, and ΔS_tors = 9 ln 9 + ln 3 ≈ 20.874. Other numbers follow from it: S_tors 1.598; sideband weights 0.333/0.235/0.083/0.014/0.001; w₀+2w₁ ≈ 80%; |n|≤2 97%; 3-6-9 lines 36%. **Chosen:** the alternative was to keep ln 2 and drop the DFT and conjugation claims. ℤ₉ conjugation is stated in the paper, so the symmetric form is the consistent one. The GWOSC paragraph still records the v3 weights the search actually used.
3. **Remnants:** only information-carrying remnants are excluded, by the capacity bound of about 21 nats. The endpoint is Gap 14.
4. **Loops:** corrected the bound; summed over labels, the weights give no suppression. φ^{−N*} is "proposed, not derived" (Gap 15). The section is retitled "Proposed …".
5. **Other fixes:**
   - H³ is now credited to Dijkgraaf–Witten 1990; the Aspinwall–Morrison citation is removed.
   - Modular invariance is called a consistency condition, and τ = iβ/2π.
   - The diagonal invariant is "adopted", not "unique".
   - Quantum dimension D = 3. ln Z_tors = ln 3 matches γ in magnitude; whether that means more is flagged as open.
   - Entropy gap is "not testable now" (Gap 16).
   - Δω → Δf; the Q coefficient is a consistency check.
   - The loop formula is now dimensionless (c_log ln(A/G₄)), and the Lovelock citation is removed.
   - The cross-scale "independent check" is now "structural link (Chosen input)".
   - Prologue and conclusion rhetoric are conditioned on Gaps 10–11.
   - Fig. 4 caption: "top right" now describes the panel actually drawn.
   - Fig. 1 label: dim H = 9^{N_cell}.
