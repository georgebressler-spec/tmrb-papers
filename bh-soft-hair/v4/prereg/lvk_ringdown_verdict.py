#!/usr/bin/env python3
"""FROZEN decision script for PREREG_LVK_RINGDOWN.md (written before any LVK result was read).

Input: a JSON file of numbers transcribed from the source paper AFTER registration:
  {"source": "...", "analyses": [
     {"name": "...", "quantity": "dtau_220" | "domegaI_220",
      "median": float, "lo90": float, "hi90": float,
      "t0_over_tau": float or null, "common_deviation": true|false, "notes": "..."}]}
Output: predicted d(tau)_220 and a verdict per analysis; the PRIMARY verdict is printed last.

TMRB prediction (v4 r8, Table 2): fractional change of the fitted l=m=2 damping time,
tau_fit/tau_GR - 1, by remnant spin and fit start time t0 (units of tau), exact Kerr QNMs.
"""
import json, sys

T0 = [0.0, 0.5, 1.0, 2.0]
TABLE = {  # spin: shifts at T0 (from kerr_spin_table_output.txt)
    0.00: [-0.044, -0.070, -0.095, -0.129],
    0.50: [-0.070, -0.101, -0.135, -0.198],
    0.69: [-0.095, -0.140, -0.181, -0.253],
    0.80: [-0.126, -0.190, -0.239, -0.314],
    0.90: [-0.191, -0.270, -0.344, -0.442],
}
SPIN_POINT, SPIN_LO, SPIN_HI = 0.69, 0.50, 0.80   # registered point and band

def interp_t0(row, t0):
    t0 = max(0.0, min(2.0, t0))
    for k in range(len(T0) - 1):
        if T0[k] <= t0 <= T0[k + 1]:
            f = (t0 - T0[k]) / (T0[k + 1] - T0[k])
            return row[k] + f * (row[k + 1] - row[k])

def prediction(t0):
    t0 = 0.0 if t0 is None else t0          # IMR-based analyses: start at the peak (t0 = 0)
    p = interp_t0(TABLE[SPIN_POINT], t0)
    band = sorted([interp_t0(TABLE[SPIN_LO], t0), interp_t0(TABLE[SPIN_HI], t0)])
    return p, band

def to_dtau(a):
    if a["quantity"] == "dtau_220":
        return a["median"], a["lo90"], a["hi90"]
    if a["quantity"] == "domegaI_220":     # tau = 1/omega_I  =>  dtau = 1/(1+domega) - 1 (monotone decreasing)
        c = lambda x: 1.0 / (1.0 + x) - 1.0
        return c(a["median"]), c(a["hi90"]), c(a["lo90"])
    raise ValueError(a["quantity"])

def verdict(lo, hi, p, band):
    p_in = lo <= p <= hi
    band_out = band[1] < lo or band[0] > hi
    zero_in = lo <= 0.0 <= hi
    if band_out:
        return "EXCLUDED"
    if not p_in:
        return "DISFAVORED"
    return "CONSISTENT, NOT DISCRIMINATING" if zero_in else "FAVORED OVER GR"

def main(path):
    d = json.load(open(path))
    print("source:", d["source"])
    results = []
    for a in d["analyses"]:
        m, lo, hi = to_dtau(a)
        p, band = prediction(a.get("t0_over_tau"))
        v = verdict(lo, hi, p, band)
        results.append((a, v))
        print(f"- {a['name']}: dtau median {m:+.3f}, 90% [{lo:+.3f}, {hi:+.3f}]; "
              f"TMRB {p:+.3f} (band {band[0]:+.3f}..{band[1]:+.3f}); "
              f"common deviation: {a['common_deviation']} -> {v}")
    prim = [r for r in results if r[0].get("primary")]
    if len(prim) != 1:
        sys.exit("exactly one analysis must be marked primary by the registered rule")
    print("PRIMARY VERDICT:", prim[0][0]["name"], "->", prim[0][1])

if __name__ == "__main__":
    main(sys.argv[1])
