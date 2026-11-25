# GRACE, LIGO and Sen checks (Nov 18 2026)

Sources: the Drive folder of the Apr 26 run , containing the real NetCDF (45 MB), `TMRB_GRACE_search_results.png/.pdf` (Apr 26 13:51) and the Apr 27 script. The May 2 script, `results_grace_45coords.csv`, `TMRB_GWOSC_torsion_search.py` and `results_gwosc_o3a.json` are in the project Drive. Sen, arXiv:1205.0971v2, was read in full now that arxiv.org is allowed.

## GRACE
1. **A real run on GRACE data happened (Apr 26).** The PNG shows 2002–2026 water-height residuals of about ±1.5 cm at the best coordinate, a bimodal slope histogram, and a z histogram.
2. **Its "clean null" is guaranteed by the method.** The Apr 27 `detrend_seasonal` fits a mean, a trend and seasonal terms by least squares and subtracts them, so every residual series has a mean of exactly zero. Hence:
   - The per-coordinate "Δg" values (for example −1.91e-19 at the best coordinate) are rounding-level zeros.
   - Every z-score sits near 0 (the PNG histogram falls within ±0.3).
   - A steady anomaly of any size would be removed in the same way, so this test cannot detect the prediction.
3. **Scale:** 6.3e-15 m/s² equals 1.5e-6 cm of water (2πGρh), while GRACE noise is around a centimetre. The prediction is about 10⁶ below GRACE sensitivity. The paper's 4e-9 "95% CL limit" is the gravity of 1 cm of water: a sensible sensitivity scale, but hard-coded, not computed.
4. **The CSV on Drive (May 2) is the demo generator's output, reproduced bit for bit.** All 45 residuals lie in [1e-19, 1e-18], the IQR equals 0.3 × g for every coordinate, and coordinate 21 is forced to α = 0.75. The real run's per-coordinate table was not saved.
5. **Fig. 5's right panel is the synthetic histogram,** drawn from normal(0, 0.40) with the same seed. The real run's z histogram (in the PNG) is narrower.
6. **Not verifiable without re-running:** the real run's mean slope (the paper says 0.692), its count of 4/45 in 0.75 ± 0.05, and coordinate 21's slope. The real slope histogram is bimodal (clusters near 0.3–0.6 and 1.2–1.7); read off the PNG, its mean is about 0.7. The NetCDF is 45 MB, over the Drive connector's download limit, and the laptop folders are still not offered to cloud sessions.

## LIGO (GWOSC)
- **The limit holds.** Recomputed from the run's measured inputs (ASD 6.2498e-24 /√Hz, T = 4531 s, f = 102 Hz, N_eff = 4.242, trials factor 1.860), it is h95 = 1.9501e-25 and Δg = 1.6020e-16 m/s², matching the JSON.
- It is a sensitivity floor (the script never tests specific frequencies). r6 labels it as one.
- Re-measuring the ASD itself was not possible. gwosc.org is now allowed, but its certificate chain ends at the emSign Root CA – G1, which this container's trust store lacks (even after a ca-certificates upgrade), so the TLS check fails. TLS verification was not bypassed.

## Sen
- From eq. (1.2)–(1.5): in pure gravity, D = 4, C_local = 212/45 and ΔS = (212/45 − 3) ln a with A ∝ a², so **c_log = 77/90 ≈ 0.86** times ln A, and it is positive.
- For 10 M☉ that is 157 nats, about 7.5 × ΔS_tors; with φ⁻⁹ it is 2.1 nats. The caveat is confirmed and now stated exactly in r6.
