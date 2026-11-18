import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
R(r"""over 4531~s of
cleaned H1 strain within the 8192~s span GPS""", r"""over the longest gap-free stretch, 4531~s,
of cleaned H1 strain in the 8192~s span GPS""")
R(r"""Gaussian Z$_9$ weights of v3, $C\exp(-\pi n^2/9)$ with $n=0,\dots,8$ (effective stack gain""",
  r"""Gaussian Z$_9$ weights over $n=-4,\dots,4$, the symmetric form adopted in v4 (effective stack gain""")
R(r"""Fitting a single
damped sinusoid to this waveform returns the frequency unchanged and a damping
time \emph{4.6\% shorter} than the GR value for the same mass and spin, at every
mass. For a remnant of spin 0.7 ($Q \approx 3.3$ from the fits
of~\cite{BertiCardosoWill2006}) the shortening is 9.9\%.""",
  r"""Fitting a single
damped sinusoid from the peak returns the frequency unchanged (to $0.2\%$) and a
damping time \emph{4.6\% shorter} than the GR value for the same mass and spin, at
every mass; three independent methods (complex overlap, real-strain least squares,
small-$x$ expansion) give 4.4--4.8\%. The shift grows when the fit starts later,
because the envelope factor falls faster with time: 7\%, 9.5\% and 13\% for starts
at $0.5\tau$, $\tau$ and $2\tau$, so a measurement must quote its start time. For a
remnant of spin 0.7 ($Q \approx 3.3$ from the fits of~\cite{BertiCardosoWill2006})
the shortening from the peak is 9.9\% (9.7--11\% across methods).""")
R(r"""4.6\% shorter than GR (9.9\% at spin 0.7),""", r"""4.6\% shorter than GR for a fit from the peak (9.9\% at spin 0.7; larger for later starts),""")
R(r"""Kerr mode (gold, dashed); the fitted damping time is 4.6\% shorter.}""",
  r"""Kerr mode (gold, dashed); fitted from the peak, the damping time is 4.6\% shorter.}""")
R(r"""so it is of order $10^2$ nats and exceeds $\Delta S_{\rm tors}$.""",
  r"""so it is of order $10^2$ nats and exceeds $\Delta S_{\rm tors}$ in magnitude
whenever $|c_{\log}| > 0.114$ (its sign depends on the field content).""")
R(r"""as input; GWOSC segment contains no merger; Fateev--Zamolodchikov reference corrected.
""", r"""as input; GWOSC segment contains no merger; Fateev--Zamolodchikov reference corrected.
\textit{(xiii)}~Ringdown shift confirmed by three independent methods and stated for a fit
from the peak, with its growth for later start times; the logarithm's dominance stated in
magnitude ($|c_{\log}| > 0.114$); the GWOSC weights described as the script used them
($n=-4,\dots,4$), and the 4531~s stated as the longest gap-free stretch of the 8192~s span.
""")
open(dst, "w").write(s); print("ok")
