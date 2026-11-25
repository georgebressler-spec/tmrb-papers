"""Independent check of the v4 r4 ringdown claim (4.6% shorter damping time, Schwarzschild;
9.9% at spin 0.7). Method differs from ringdown_signature.py:
 (A) analytic small-x expansion of the envelope, weighted least squares in closed form;
 (B) scipy least_squares on the real strain h(t) with free amplitude, phase, f, tau;
 (C) dependence on the fit start time t0 (real analyses start after the peak)."""
import numpy as np, math
from scipy.optimize import least_squares
kappa = 2.1/5.2
ns = np.arange(-4, 5)
w = np.array([sum(math.exp(-math.pi*(n+9*k)**2/9) for k in range(-6, 7)) for n in ns])/3
sig2 = float(np.sum(ns**2*w))
def run(label, wR, wI):
    Q = wR/(2*wI); x = 2*kappa*Q/9          # 2*pi*df*tau, mass independent
    # (A) envelope M(s) ~ 1 - sig2 x^2 s^2/2, s=t/tau. Fit ln-env residual by a + b s with weight e^{-2s}
    # Weighted LSQ of -c s^2 by a + b s, weight e^{-2s}: moments m_k = k!/2^{k+1}
    m = [math.factorial(k)/2**(k+1) for k in range(5)]
    A = np.array([[m[0], m[1]], [m[1], m[2]]]); rhs = np.array([m[2], m[3]])
    a, b = np.linalg.solve(A, rhs)          # fit s^2 ~ a + b s
    dgam_analytic = (sig2*x*x/2)*b          # extra decay rate in units of 1/tau
    print(f"{label}: Q={Q:.3f}  2pi*df*tau={x:.4f}  (A) analytic tau shortening = {dgam_analytic/(1+dgam_analytic):.4f}")
    # (B) and (C): numerical fit on real strain, units M=1
    M = 1.0; f0 = wR/(2*math.pi); tau = 1/wI; df = f0*kappa/9
    for t0 in (0.0, 0.5*tau, 1.0*tau, 2.0*tau):
        t = np.linspace(t0, t0 + 8*tau, 6000)
        h = np.exp(-t/tau)*np.sum(w[:, None]*np.cos(2*math.pi*(f0+ns[:, None]*df)*t), axis=0)
        def res(p):
            A_, ph, f, ta = p
            return A_*np.exp(-(t-t0)/ta)*np.cos(2*math.pi*f*t+ph) - h
        A0 = np.exp(-t0/tau)
        sol = least_squares(res, [A0, 0.0, f0, tau], x_scale=[A0, 1, f0, tau], xtol=1e-14, ftol=1e-14)
        _, _, f, ta = sol.x
        print(f"    (B) fit from t0={t0/tau:.1f} tau: tau_fit/tau-1 = {ta/tau-1:+.4f}   f_fit/f0-1 = {f/f0-1:+.2e}")
run("Schwarzschild", 0.373672, 0.088962)
F = 1.5251 - 1.1568*(0.3)**0.1292; Qk = 0.7 + 1.4187*(0.3)**(-0.4990)   # Berti-Cardoso-Will fits, j=0.7
run("Kerr j=0.7 (BCW fits)", F, F/(2*Qk))
