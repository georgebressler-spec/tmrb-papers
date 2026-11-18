import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
i = s.index(r"""Fitting a single
damped sinusoid from the peak returns""")
j = s.index(r"""The residual mismatch
between the waveform""")
s = s[:i] + r"""Fitting a single
damped sinusoid returns the frequency unchanged (to $0.2\%$) and a damping time
\emph{shorter} than the GR value for the same mass and spin. The shortening does not
depend on mass, but it depends on the remnant's spin, through $Q$, and on the time
$t_0$ after the peak at which the fit starts, because the envelope factor falls faster
with time. Table~\ref{tab:ringdown_spin} gives it for exact Kerr $\ell = m = 2$
frequencies (Leaver's continued fraction~\cite{Leaver1985}, computed with the
\texttt{qnm} package~\cite{Stein2019}; the fits of~\cite{BertiCardosoWill2006} agree
to $0.7\%$). For a non-spinning remnant fitted from the peak it is $4.4\%$ (three
independent methods give 4.4--4.8\%). For a typical binary-merger remnant, of spin
about 0.7, it is about $10\%$ from the peak and about $18\%$ from $t_0 = \tau$, where
ringdown analyses usually start. The prediction is therefore a $10$--$18\%$
shortening for typical remnants, and a measurement must state the remnant's spin and
its fit start time.

\begin{table}[ht]
\centering
\caption{Predicted shortening of the $\ell = m = 2$ damping time, from fitting a
single damped sinusoid (least squares on the strain; free amplitude, phase, frequency
and damping time) to the nine-sideband ringdown, by remnant spin and fit start time
$t_0$ after the peak. Exact Kerr frequencies; the same at every mass. Assumes every
sideband shares the damping time (Gap~18).}
\label{tab:ringdown_spin}
\begin{tabular}{cccccccc}
\toprule
Spin & $\omega_R M$ & $\omega_I M$ & $Q$ & $t_0 = 0$ & $t_0 = 0.5\tau$ & $t_0 = \tau$ & $t_0 = 2\tau$ \\
\midrule
0.00 & 0.3737 & 0.0890 & 2.10 & 4.4\%  & 7.0\%  & 9.5\%  & 12.9\% \\
0.50 & 0.4641 & 0.0856 & 2.71 & 7.0\%  & 10.1\% & 13.5\% & 19.8\% \\
0.69 & 0.5282 & 0.0812 & 3.25 & 9.5\%  & 14.0\% & 18.1\% & 25.3\% \\
0.80 & 0.5860 & 0.0756 & 3.87 & 12.6\% & 19.0\% & 23.9\% & 31.4\% \\
0.90 & 0.6716 & 0.0649 & 5.18 & 19.1\% & 27.0\% & 34.4\% & 44.2\% \\
\bottomrule
\end{tabular}
\end{table}

""" + s[j:]
R(r"""$\rho^2(1-\mathcal{O}) \approx 1/2$. The testable prediction is therefore a
mass-independent shortening of the $\ell = m = 2$ damping time relative to the GR
value inferred from the inspiral, at the few-percent precision that
third-generation detectors target. (Computed; script \texttt{ringdown\_signature.py}
in the Zenodo record.)""",
  r"""$\rho^2(1-\mathcal{O}) \approx 1/2$. The testable prediction is a mass-independent
shortening of the $\ell = m = 2$ damping time relative to the GR value inferred from
the inspiral. A shortening of 10--18\% may already be within reach of combined
ringdown tests of general relativity on existing LIGO--Virgo--KAGRA catalogues; such a
comparison, set up in advance and run once, is proposed here, not claimed.
(Computed; scripts \texttt{ringdown\_signature.py} and \texttt{kerr\_spin\_table.py}
in the Zenodo record.)""")
R(r"""Kerr mode (gold, dashed); fitted from the peak, the damping time is 4.6\% shorter.}""",
  r"""Kerr mode (gold, dashed); for this non-spinning case, fitted from the peak, the
damping time is 4.4--4.8\% shorter (spinning remnants: Table~\ref{tab:ringdown_spin}).}""")
R(r"""  & $\ell=m=2$ damping time 4.6\% shorter than GR for a fit from the peak (9.9\% at spin 0.7; larger for later starts),
    frequency unchanged, same fraction at every mass;""",
  r"""  & $\ell=m=2$ damping time shorter than GR: about 10\% from the peak and 18\% from
    $t_0 = \tau$ for a typical remnant spin of 0.7 (4.4\% with no spin;
    Table~\ref{tab:ringdown_spin}); frequency unchanged, same at every mass;""")
R(r"""shortening of the ringdown damping time by about 5--10\%,""",
  r"""shortening of the ringdown damping time by about 10--18\% for typical remnants
(Table~\ref{tab:ringdown_spin}),""")
R(r"""numbers of Section~\ref{sec:fluid_gravity} assume every sideband shares the
    $\ell = m = 2$ damping time, and are computed for Schwarzschild and, with fit
    formulas, spin 0.7. A Kerr derivation including overtones is open.""",
  r"""numbers of Section~\ref{sec:fluid_gravity} assume every sideband shares the
    $\ell = m = 2$ damping time; they use exact Kerr frequencies for spins 0--0.9
    (Table~\ref{tab:ringdown_spin}). Unequal sideband damping and overtones are open.""")
R(r"""run's own output is shown as Fig.~6.
""", r"""run's own output is shown as Fig.~6.
\textit{(xvi)}~Ringdown prediction stated as a function of remnant spin and fit start time
(Table~\ref{tab:ringdown_spin}, exact Kerr frequencies): about 10--18\% for typical
remnants, 4.4\% for a non-spinning remnant fitted from the peak; a comparison with
existing LIGO--Virgo--KAGRA ringdown tests is proposed.
""")
R(r"""\bibitem{BertiCardosoWill2006}""", r"""\bibitem{Leaver1985}
  E.~W.~Leaver,
  \textit{An analytic representation for the quasi-normal modes of Kerr black holes},
  Proc.\ R.\ Soc.\ Lond.\ A \textbf{402}, 285 (1985).
  \href{https://doi.org/10.1098/rspa.1985.0119}{doi:10.1098/rspa.1985.0119}

\bibitem{Stein2019}
  L.~C.~Stein,
  \textit{qnm: A Python package for calculating Kerr quasinormal modes, separation
    constants, and spherical-spheroidal mixing coefficients},
  J.\ Open Source Softw.\ \textbf{4}, 1683 (2019).
  \href{https://doi.org/10.21105/joss.01683}{doi:10.21105/joss.01683}

\bibitem{BertiCardosoWill2006}""")
open(dst, "w").write(s); print("ok")
