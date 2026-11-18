"""Ringdown signature of nine unresolved Z9 sidebands (v4 r4).
Model (Proposed): each sideband n=-4..4 is a damped mode at f0 + n*df with the same damping
time tau and amplitude w_|n| (Z9-symmetric periodised Gaussian, sum 1). Schwarzschild l=m=2 n=0.
Compares with the best single damped sinusoid (free f, tau, amplitude, phase); white noise."""
import numpy as np, math
wR, wI, kappa = 0.373672, 0.088962, 2.1/5.2           # Schwarzschild 220 mode; kappa_CE = mu/lambda_rec
Msun_s = 4.925490947e-6
w = np.array([sum(math.exp(-math.pi*(n+9*k)**2/9) for k in range(-6,7))/3 for n in range(-4,5)])
ns = np.arange(-4,5)
def report(Msun):
    M = Msun*Msun_s; f0 = wR/(2*math.pi*M); tau = M/wI; df = f0*kappa/9; fwhm = 1/(math.pi*tau)
    t = np.linspace(0, 12*tau, 40000)
    h = np.exp(-t/tau)*np.sum(w[:,None]*np.exp(2j*math.pi*(f0+ns[:,None]*df)*t), axis=0)
    best = (0,None)
    for fr in np.linspace(0.97,1.03,121):
        for tr in np.linspace(0.85,1.05,201):
            tmpl = np.exp(-t/(tau*tr))*np.exp(2j*math.pi*f0*fr*t)
            o = abs(np.vdot(tmpl,h))/math.sqrt(np.vdot(tmpl,tmpl).real*np.vdot(h,h).real)
            if o > best[0]: best = (o,(fr,tr))
    o,(fr,tr) = best
    env_tau = np.sum(w*np.cos(2*math.pi*ns*df*tau))
    return dict(M=Msun,f0=f0,tau_ms=tau*1e3,df=df,fwhm=fwhm,ratio=df/fwhm,env_at_tau=env_tau,
                mismatch=1-o,dtau=tr-1,dfreq=fr-1,rho_needed=math.sqrt(1/(2*(1-o))))
sig2 = float(np.sum(ns**2*w))
print(f"sigma^2 = sum n^2 w_n = {sig2:.4f}; 2*pi*df*tau = kappa*wR/(9*wI) = {kappa*wR/(9*wI):.4f} (mass independent)")
for m in (10, 30, 60):
    r = report(m)
    print(" ".join(f"{k}={v:.4g}" for k,v in r.items()))
