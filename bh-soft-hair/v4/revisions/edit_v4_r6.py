import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
# Sen's coefficient, read from arXiv:1205.0971 eq. (1.2)-(1.5)
R(r"""with $c_{\log}$ a pure number of order one~\cite{Sen2012}; for a $10\,M_\odot$ hole
$\ln(A/G_4) \approx 183$, so it is of order $10^2$ nats and exceeds $\Delta S_{\rm tors}$ in magnitude
whenever $|c_{\log}| > 0.114$ (its sign depends on the field content).""",
  r"""with $c_{\log} = 77/90 \approx 0.86$ for a Schwarzschild hole in pure four-dimensional
gravity (Sen's $(212/45 - 3)\ln a$ with $A \propto a^2$; massless matter fields change
it)~\cite{Sen2012}. For a $10\,M_\odot$ hole $\ln(A/G_4) \approx 183$, so the logarithm
is about 157 nats, roughly 7.5 times $\Delta S_{\rm tors}$; it would exceed
$\Delta S_{\rm tors}$ for any $|c_{\log}| > 0.114$.""")
R(r"""bringing it to about $2.4\,c_{\log}$ nats.""", r"""bringing it to about 2.1 nats.""")
# GWOSC: sensitivity floor, not a null search
R(r"""narrowband search whose limit lies below that amplitude but bounds only a
component near 100~Hz, which the prediction does not contain.""",
  r"""narrowband sensitivity floor that lies below that amplitude but applies only to a
component near 100~Hz, which the prediction does not contain.""")
R(r"""\subsection{Current Observational Constraints: GWOSC O3a and GRACE-FO Null Results}""",
  r"""\subsection{Current Observational Constraints: GWOSC O3a Sensitivity Floor and GRACE-FO Null Results}""")
R(r"""Two independent null searches have been performed against existing data products,
targeting""", r"""A sensitivity estimate (GWOSC) and a null search (GRACE) have been made against
existing data products, targeting""")
R(r"""A coherent narrowband search for excess power in the predicted Z$_9$ QNM
sideband comb across 30--174~Hz was performed over the longest gap-free stretch, 4531~s,""",
  r"""A narrowband sensitivity estimate for the predicted Z$_9$ QNM sideband comb
across 30--174~Hz was computed from the longest gap-free stretch, 4531~s,""")
R(r"""templates. The segment contains no merger, so the search tests stationary lines at
the comb frequencies, not a ringdown. The resulting strain UL""",
  r"""templates. The script does not test the strain at specific comb frequencies: it
converts the measured median noise level into the smallest detectable line
amplitude, so the result is a sensitivity floor, not a null detection; the segment
also contains no merger. The resulting strain floor""")
R(r"""The GWOSC UL Eq.~\eqref{eq:gwosc_ul} lies $\sim 39$ times""", r"""The GWOSC sensitivity floor Eq.~\eqref{eq:gwosc_ul} lies $\sim 39$ times""")
R(r"""that amplitude, this search already excludes it.""", r"""that amplitude, data at this sensitivity could test it.""")
R(r"""the GWOSC limit Eq.~\eqref{eq:gwosc_ul} bounds
a $\sim 100$~Hz component of it,""", r"""the GWOSC sensitivity floor Eq.~\eqref{eq:gwosc_ul} applies to
a $\sim 100$~Hz component of it,""")
R(r"""($n=-4,\dots,4$), and the 4531~s stated as the longest gap-free stretch of the 8192~s span.
""", r"""($n=-4,\dots,4$), and the 4531~s stated as the longest gap-free stretch of the 8192~s span.
\textit{(xiv)}~Sen's coefficient stated ($c_{\log} = 77/90$, pure gravity); the GWOSC result
relabelled as a sensitivity floor (recomputed from the run's measured noise level:
$1.602\times10^{-16}~\mathrm{m\,s^{-2}}$).
""")
open(dst, "w").write(s); print("ok")
