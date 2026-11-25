import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
R(r"""quantitative upper limits: a GRACE/GRACE-FO mascon search consistent with the
framework's predicted quasi-static bulk-gravity-leakage amplitude, and a GWOSC O3a""",
  r"""two sensitivity scales: GRACE/GRACE-FO mascon gravity (about
$4\times10^{-9}~\mathrm{m\,s^{-2}}$, roughly $10^{6}$ times above the framework's predicted
quasi-static bulk-gravity-leakage amplitude), and a GWOSC O3a""")
R(r"""\subsection{Current Observational Constraints: GWOSC O3a Sensitivity Floor and GRACE-FO Null Results}""",
  r"""\subsection{Current Observational Constraints: GWOSC O3a Sensitivity Floor and GRACE Scale}""")
R(r"""A sensitivity estimate (GWOSC) and a null search (GRACE) have been made against
existing data products,""", r"""A sensitivity estimate (GWOSC) and a mascon run (GRACE) have been made against
existing data products,""")
R(r"""102$~Hz; under that assumption the search excludes the predicted amplitude at
95\%~CL. The predicted anomaly is quasi-static (it is what the GRACE search and the
planned gradiometers look for)""", r"""102$~Hz; under that assumption a signal at the predicted amplitude would lie
above the floor. The predicted anomaly is quasi-static (it is what GRACE and the
planned gradiometers measure)""")
i = s.index(r"""\paragraph{GRACE and GRACE-FO mascon gravity (2002-04 -- 2026-02).}""")
j = s.index(r"""\paragraph{Interpretation.}""")
s = s[:i] + r"""\paragraph{GRACE and GRACE-FO mascon gravity (2002-04 -- 2026-02).}
\sloppy
On 2026-04-26 the JPL RL06.3M Mascon product
(\texttt{GRCTellus.JPL.200204\_202602.GLO.RL06.3M.MSCNv04CRI.nc}) was searched at the
45 hotspot coordinates (Figure~\ref{fig:grace_run}). At each coordinate the script
fits and removes a mean, a linear trend and annual and semi-annual cycles, then
reports the mean of the residual series as the anomaly, with its $z$-score. Because
the fitted mean has been removed, both are zero by construction: the reported
anomalies (${\sim}10^{-19}~\mathrm{m\,s^{-2}}$) and $|\bar z| \approx 0.00$ are
rounding-level zeros, and a steady anomaly of any size would be removed in the same
way. The run is therefore not a test of the prediction. What it does establish is
the scale: the residual series vary at the centimetre level of water-equivalent
height, and 1~cm of water corresponds to $2\pi G\rho_w h \approx
4\times10^{-9}~\mathrm{m\,s^{-2}}$, so
\begin{equation}
  \Delta g^{\mathrm{GRACE}}_{\rm scale} \approx 4\times10^{-9}~\mathrm{m\,s^{-2}}
  \quad (\text{1~cm water equivalent}),
  \label{eq:grace_ul}
\end{equation}
a sensitivity scale, not a computed upper limit. The prediction,
$6.3\times10^{-15}~\mathrm{m\,s^{-2}}$, is the gravity of about $1.5\times10^{-6}$~cm
of water, roughly $10^{6}$ times below it. The run also fitted a power-spectrum slope
$\alpha$ at each coordinate; the distribution is bimodal
(Figure~\ref{fig:grace_run}, bottom centre), with a mean near 0.7 read from the
histogram. The run's per-coordinate table was not saved, so the slope count and the
single-coordinate slope quoted in v3 are withdrawn until the run is repeated. A test
of the prediction needs a method that keeps a steady offset (for example, hotspot
against control coordinates) and an instrument about $10^{6}$ times more sensitive.

""" + s[j:]
R(r"""The GRACE-FO null is not in tension with the framework: the predicted
$6.3\times10^{-15}~\mathrm{m\,s^{-2}}$ lies $\sim 6\times10^{5}$ times below its UL
Eq.~\eqref{eq:grace_ul}.""", r"""The GRACE run neither supports nor tests the framework: the predicted
$6.3\times10^{-15}~\mathrm{m\,s^{-2}}$ lies $\sim 6\times10^{5}$ times below the scale
Eq.~\eqref{eq:grace_ul}.""")
R(r"""the framework becomes unambiguously falsifiable. Both analysis scripts
(\texttt{TMRB\_GWOSC\_torsion\_search.py} and
\texttt{TMRB\_GRACE\_torsion\_search.py}, operating on the identical
45-coordinate set) and full reproducibility metadata are included
in the Zenodo record for this paper.""", r"""the framework becomes unambiguously falsifiable. Both analysis scripts
(\texttt{TMRB\_GWOSC\_torsion\_search.py} and the GRACE script used for the run,
operating on the identical 45-coordinate set), the GWOSC result file and the GRACE
run's output figure are included in the Zenodo record for this version.""")
i = s.index(r"""\includegraphics[width=0.94\textwidth]{fig5_constraints.pdf}""")
j = s.index(r"""\label{fig:constraints}""")
s = s[:i] + r"""\includegraphics[width=0.72\textwidth]{fig5_constraints.pdf}
\caption{Current and projected sensitivity for the predicted
$\Delta g_{\mathrm{TMRB}}=6.3\times10^{-15}~\mathrm{m\,s^{-2}}$ bulk-gravity anomaly:
log-scale sensitivity of operational, planned and proposed missions; the gold band
marks the Gaia-calibrated TMRB prediction; dotted lines mark the GWOSC sensitivity
floor Eq.~\eqref{eq:gwosc_ul} (applies only to a $\sim 100$~Hz component) and the
GRACE scale Eq.~\eqref{eq:grace_ul} (gravity of 1~cm of water). The v3 right panel, a
$z$-score histogram, was produced by a seeded random draw rather than taken from the
run, and is removed.}
""" + s[j:]
R(r"""\label{fig:constraints}
\end{figure}
""", r"""\label{fig:constraints}
\end{figure}

\begin{figure}[ht!]
\centering
\includegraphics[width=\textwidth]{fig6_grace_run_2026-04-26.png}
\caption{Output of the 2026-04-26 GRACE run on the real mascon product, reproduced
unchanged with the run script's own panel titles. Each coordinate's series has its
fitted mean, trend and seasonal cycles removed before its mean anomaly and $z$-score are
computed, so both are zero by construction: the $z$-scores cluster at 0 (top right) and
the ring means are 0 (bottom left; dashed line: the prediction). Bottom centre:
power-spectrum slopes $\alpha$. Bottom right: the residual series at one coordinate,
varying at the centimetre level.}
\label{fig:grace_run}
\end{figure}
""")
R(r"""The GRACE-FO null limit Eq.~\eqref{eq:grace_ul} is consistent with the
predicted bulk-gravity-leakage amplitude at the 45 hotspot
coordinates~\cite{BresslerBGL2026},""", r"""The GRACE scale Eq.~\eqref{eq:grace_ul} lies about $10^{6}$ times above the
predicted bulk-gravity-leakage amplitude at the 45 hotspot
coordinates~\cite{BresslerBGL2026}, so GRACE cannot test it;""")
R(r"""$1.602\times10^{-16}~\mathrm{m\,s^{-2}}$).
""", r"""$1.602\times10^{-16}~\mathrm{m\,s^{-2}}$).
\textit{(xv)}~GRACE paragraph rewritten from the 2026-04-26 run itself: its zero anomaly and
$z$-scores follow from removing the fitted mean, so the run does not test the prediction;
$4\times10^{-9}~\mathrm{m\,s^{-2}}$ is stated as the 1~cm water-equivalent scale, not an
upper limit; the per-coordinate slope count and the coordinate-21 slope are withdrawn
until the run is repeated; the synthetic $z$ histogram is removed from Fig.~5 and the
run's own output is shown as Fig.~6.
""")
open(dst, "w").write(s); print("ok")
