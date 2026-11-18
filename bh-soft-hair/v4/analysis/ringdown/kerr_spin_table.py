"""Rigour check standing in for Jimmy (Nov 18 2026).
1. Exact Kerr l=m=2 n=0 QNMs (Leaver continued fraction via the `qnm` package) instead of
   Berti-Cardoso-Will fits; 2. damping-time shift of a single-mode fit for start times
   t0 = 0, 0.5, 1, 2 tau; 3. algebraic identities used in the paper."""
import math, numpy as np, qnm
from scipy.optimize import least_squares
kappa = 2.1/5.2
ns = np.arange(-4, 5)
w = np.array([sum(math.exp(-math.pi*(n+9*k)**2/9) for k in range(-6, 7)) for n in ns])/3
mode = qnm.modes_cache(s=-2, l=2, m=2, n=0)
def shift(wR, wI, t0f):
    f0 = wR/(2*math.pi); tau = 1/wI; df = f0*kappa/9; t0 = t0f*tau
    t = np.linspace(t0, t0+8*tau, 6000)
    h = np.exp(-t/tau)*np.sum(w[:, None]*np.cos(2*math.pi*(f0+ns[:, None]*df)*t), axis=0)
    res = lambda p: p[0]*np.exp(-(t-t0)/p[3])*np.cos(2*math.pi*p[2]*t+p[1]) - h
    A0 = math.exp(-t0f)
    s = least_squares(res, [A0, 0, f0, tau], x_scale=[A0, 1, f0, tau], xtol=1e-14, ftol=1e-14)
    return s.x[3]/tau-1, s.x[2]/f0-1
print("spin   wR M     wI M     Q      df/FWHM  2pi df tau | dtau/tau for t0 = 0, 0.5, 1, 2 tau")
for a in (0.0, 0.5, 0.69, 0.7, 0.8, 0.9):
    om, _, _ = mode(a=a)
    wR, wI = om.real, -om.imag
    Q = wR/(2*wI)
    row = [shift(wR, wI, t0)[0] for t0 in (0, 0.5, 1, 2)]
    print(f"{a:4.2f}  {wR:.5f}  {wI:.5f}  {Q:.3f}  {kappa*Q/9:.4f}   {2*kappa*Q/9:.4f}    | " + "  ".join(f"{x:+.3f}" for x in row))
# identity checks
wR, wI = 0.373672, 0.088962; Q = wR/(2*wI); M = 1
f0 = wR/(2*math.pi*M); fwhm = wI/(math.pi*M); df = f0*kappa/9
print("identity df/FWHM == kappa*Q/9:", abs(df/fwhm - kappa*Q/9) < 1e-15, "; 2pi*df*tau == 2kappa Q/9:", abs(2*math.pi*df*(M/wI) - 2*kappa*Q/9) < 1e-15)
