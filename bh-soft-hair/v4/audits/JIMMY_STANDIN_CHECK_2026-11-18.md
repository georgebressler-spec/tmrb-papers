# Rigour check standing in for Jimmy (Nov 18 2026; Jimmy is down for 2 more days)

The checklist from `AUDIT_4` §3, worked through by Claude. Jimmy should still re-check it when he is back: one model family checking itself is coordination, not corroboration.

## 1. Ringdown derivation (*execution*: `jimmy_check_kerr_exact.py`, exact Kerr QNMs from Leaver's continued fraction via the `qnm` package)
- **Identities:** Δf/FWHM = κQ/9 and 2πΔfτ = 2κQ/9 hold exactly, so the result is mass-independent for a given spin.
- **The BCW fits are accurate:** at spin 0.7 the exact ωM is 0.53260 − 0.08079i, against 0.5350 − 0.0814i from the fits (0.4% and 0.7% off).
- **The fitted damping-time shift (least squares on the real strain, free amplitude, phase, f and τ):**

| spin | Q | from peak | t₀ = 0.5τ | t₀ = τ | t₀ = 2τ |
|---|---|---|---|---|---|
| 0.00 | 2.10 | −4.4% | −7.0% | −9.5% | −12.9% |
| 0.50 | 2.71 | −7.0% | −10.1% | −13.5% | −19.8% |
| 0.69 | 3.25 | −9.5% | −14.0% | −18.1% | −25.3% |
| 0.80 | 3.87 | −12.6% | −19.0% | −23.9% | −31.4% |
| 0.90 | 5.18 | −19.1% | −27.0% | −34.4% | −44.2% |

- **Finding:** the shift depends strongly on the remnant's spin and on the fit's start time. The paper leads with Schwarzschild from the peak (4.6%). Typical binary-merger remnants have spin around 0.7, and ringdown analyses usually start at or after the peak, so the representative prediction is about **10–18%**. The paper should quote the prediction as a function of spin and start time; this table is that function.
- **Testability (*reasoning*, to verify):** a 10–20% shortening may be close to what existing LVK ringdown tests of general relativity already constrain on δτ̂₂₂₀ when events are combined. If so, the prediction could be confronted with published GWTC results, pre-registered and run once, rather than waiting for ET/CE.

## 2. "Fit from the peak" as the reference
It is the most conservative choice: it gives the smallest shift. It is not the usual practice, since analyses start after the peak to avoid nonlinear and overtone content. The table covers the realistic start times.

## 3. Sen's coefficient (*retrieval*, read from arXiv:1205.0971v2, eqs. 1.2–1.5)
- Pure gravity, D = 4: C_local = 212/45 and ΔS = (212/45 − 3) ln a with A ∝ a², which gives c_log = 77/90 (positive).
- Light matter fields change it: (1/90)(2n_S − 26n_V + 7n_F − 233n_{3/2}/2) is added. The caveat holds for |c_log| > 0.114, so it fails only if matter cancels the coefficient almost exactly.

## 4. The GRACE section
Covered in `GRACE_LIGO_SEN_CHECK_2026-11-18.md`; r7 is consistent with it.

## Not done here
- Jimmy's separate pending item on the Z9 proof path (the DK4 4a argument).
