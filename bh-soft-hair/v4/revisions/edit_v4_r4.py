import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
LOG = r"c_{\log}\ln\frac{A}{G_4}"
# ===== 2: one-loop logarithm in the entropy
R(r"""The Bekenstein--Hawking entropy receives a precise, size-independent topological
correction
\[
  S_{\mathrm{TMRB}} = \frac{A}{4G_4} + 9\ln 9 + \ln 3""",
  r"""Beyond the one-loop logarithm $c_{\log}\ln(A/G_4)$, the Bekenstein--Hawking
entropy receives a size-independent topological correction
\[
  S_{\mathrm{TMRB}} = \frac{A}{4G_4} + """ + LOG + r""" + 9\ln 9 + \ln 3""")
R(r"""  \boxed{S_{\mathrm{TMRB}} = \frac{A}{4G_4} + 9\ln 9 + \ln 3""",
  r"""  \boxed{S_{\mathrm{TMRB}} = \frac{A}{4G_4} + """ + LOG + r""" + 9\ln 9 + \ln 3""")
R(r"""For conciseness we write $\Delta S_{\mathrm{tors}} = 9\ln 9 + \ln 3 \approx 20.874$
as the total size-independent torsion correction.""",
  r"""For conciseness we write $\Delta S_{\mathrm{tors}} = 9\ln 9 + \ln 3 \approx 20.874$
as the total size-independent torsion correction.  The term
$c_{\log}\ln(A/G_4)$ is the standard one-loop logarithm, Eq.~\eqref{eq:log_loop},
with $c_{\log}$ a pure number of order one~\cite{Sen2012}; for a $10\,M_\odot$ hole
$\ln(A/G_4) \approx 183$, so it is of order $10^2$ nats and exceeds $\Delta S_{\rm tors}$.
If the proposed factor $\varphi^{-N_*}$ of Section~\ref{sec:loop} holds, at
$N_* = d_{\rm opt} = 9$ it multiplies the logarithm by $\varphi^{-9} \approx 0.013$,
bringing it to about $2.4\,c_{\log}$ nats. $\Delta S_{\rm tors}$ is therefore the
leading correction to the area law only if Gap~15 closes.""")
R(r"""  \item The Bekenstein--Hawking entropy acquires a universal, size-independent
    torsion correction""", r"""  \item The Bekenstein--Hawking entropy acquires, beyond the one-loop logarithm,
    a universal size-independent torsion correction""")
R(r"""generate a
universal size-independent torsion correction""", r"""generate, beyond the
one-loop logarithm, a universal size-independent torsion correction""")
R(r"""sub-dominant for all astrophysical black holes.}""", r"""sub-dominant for all astrophysical black holes.  The one-loop logarithm
$c_{\log}\ln(A/G_4)$ is not drawn.}""")
R(r"""  & $S_{\mathrm{TMRB}} - S_{\mathrm{BH}} = 9\ln 9 + \ln 3 \approx 20.874$""",
  r"""  & $S_{\mathrm{TMRB}} - S_{\mathrm{BH}} = c_{\log}\ln(A/G_4) + 9\ln 9 + \ln 3$;
    constant part $\approx 20.874$""")
# ===== 1: unresolved comb
R(r"""\section{$\mathbb{Z}_9$ QNM Sideband Comb: A Sharper Observational Target}""",
  r"""\section{$\mathbb{Z}_9$ QNM Sidebands: An Unresolved Comb and Its Ringdown Signature}""")
R(r"""inherited from Eq.~\eqref{eq:wn}. In the WKB
approximation the eigenfrequency shifts are proportional to the modulation
amplitude divided by the $\mathbb{Z}_9$ period, giving a sideband spacing""",
  r"""inherited from Eq.~\eqref{eq:wn}. As written, $\delta V(\theta)$ varies with
angle on the horizon, not with time: a static angular modulation mixes angular
modes and shifts frequencies, but does not by itself produce evenly spaced
frequency sidebands. Sidebands need the torsion phase pattern to advance in time,
$\delta V(\theta - 2\pi\Delta f_{\rm tors}\,t)$. This paper assumes that
(Proposed; deriving it is Gap~17), with spacing""")
R(r"""themselves under the $\mathbb{Z}_9$ fusion algebra.

\begin{figure}[ht!]""", r"""themselves under the $\mathbb{Z}_9$ fusion algebra.

\paragraph{The comb is not resolved.} The fundamental $\ell = m = 2$ Schwarzschild
mode has quality factor $Q = \omega_R/(2\omega_I) \approx 2.1$; for $30\,M_\odot$ its
damping time is $\tau = 1.66$~ms and its line width (FWHM) is 192~Hz. The sideband
spacing in line widths is
\begin{equation}
  \frac{\Delta f_{\rm tors}}{\rm FWHM} = \frac{\kappa_{\rm CE}\,Q}{9} \approx 0.094
  \quad\text{for every mass},
  \label{eq:comb_ratio}
\end{equation}
so the nine lines merge into one (Figure~\ref{fig:chladni}). If every sideband
shares the damping time (Gap~18), the waveform is
$h(t) \propto e^{-t/\tau}\cos(2\pi f_0 t)\sum_n w_n\cos(2\pi n\Delta f_{\rm tors} t)$:
the decay envelope picks up a mass-independent factor, equal to $0.975$ at $t = \tau$
($2\pi\Delta f_{\rm tors}\tau = 2\kappa_{\rm CE}Q/9 \approx 0.19$). Fitting a single
damped sinusoid to this waveform returns the frequency unchanged and a damping
time \emph{4.6\% shorter} than the GR value for the same mass and spin, at every
mass. For a remnant of spin 0.7 ($Q \approx 3.3$ from the fits
of~\cite{BertiCardosoWill2006}) the shortening is 9.9\%. The residual mismatch
between the waveform and the best single mode is $6.0\times10^{-5}$
($2.6\times10^{-4}$ at spin 0.7), so the non-exponential shape itself becomes
visible at ringdown signal-to-noise ratio $\rho \approx 90$ ($\approx 44$), from
$\rho^2(1-\mathcal{O}) \approx 1/2$. The testable prediction is therefore a
mass-independent shortening of the $\ell = m = 2$ damping time relative to the GR
value inferred from the inspiral, at the few-percent precision that
third-generation detectors target. (Computed; script \texttt{ringdown\_signature.py}
in the Zenodo record.)

\begin{figure}[ht!]""")
R(r"""\caption{$\mathbb{Z}_9$ QNM sideband comb and supporting structure.""",
  r"""\caption{$\mathbb{Z}_9$ QNM sidebands and supporting structure.""")
R(r"""\textit{Bottom right:} Predicted PSD comb for a $30\,M_\odot$ ringdown — nine
sidebands spaced by $\Delta f_{\rm tors} \approx 18$~Hz flank the main QNM
peak; line heights follow $w_n$, and the outer pairs ($|n| = 3, 4$) are weak.}""",
  r"""\textit{Bottom right:} predicted power spectrum with the true Schwarzschild
line width (FWHM $\approx 10.6\,\Delta f_{\rm tors}$, Eq.~\eqref{eq:comb_ratio}): the
nine sidebands (stems, heights $w_n$) blur into one line (cyan), close to a single
Kerr mode (gold, dashed); the fitted damping time is 4.6\% shorter.}""")
R(r"""This prediction supersedes any naive ``QNM frequency shift'' interpretation:
the observable target is not a single Planck-suppressed shifted frequency but
a \emph{computable comb of 9 sidebands} with spacing fixed by
$\kappa_{\mathrm{CE}}$, detectable at Einstein Telescope and Cosmic Explorer
on the $\sim 2035$ timeline.""",
  r"""This supersedes both the naive ``QNM frequency shift'' and the resolved-comb
reading of v1--v3: the observable is not nine separate lines but the shortened,
slightly non-exponential decay above, set by $\kappa_{\mathrm{CE}}$ and the mode's
quality factor, testable at Einstein Telescope and Cosmic Explorer on the
$\sim 2035$ timeline.""")
R(r"""$\mathbb{Z}_9$ QNM sideband comb
  & 9 sidebands spaced $\Delta f_{\rm tors} = f_{\rm QNM}\kappa_{\rm CE}/9
    \approx 18.0$~Hz ($30\,M_\odot$); heights follow $w_n$, $|n|\le 2$
    carry 97\%; comb identical to celestial Mellin
    spacing~\cite{BresslerCH2026,BresslerMellin2026}
    (see Section~\ref{sec:fluid_gravity}, Figure~\ref{fig:chladni})""",
  r"""Ringdown damping time
  & $\ell=m=2$ damping time 4.6\% shorter than GR (9.9\% at spin 0.7),
    frequency unchanged, same fraction at every mass; from 9 unresolved
    sidebands, spacing $0.094$ line widths, set by the $\kappa_{\rm CE}$ of the
    celestial Mellin comb~\cite{BresslerCH2026,BresslerMellin2026}
    (Section~\ref{sec:fluid_gravity}, Figure~\ref{fig:chladni})""")
R(r"""Ringdown mode count
  & 9 torsion sidebands; 5 ($|n|\le 2$) above 1\% of the weight
  & Next-generation GW detectors (ET, CE)""",
  r"""Ringdown shape
  & Non-exponential decay; mismatch $6.0\times10^{-5}$ to a single mode,
    visible at ringdown SNR ${\gtrsim}\,90$ (44 at spin 0.7)
  & ET, CE (loudest events)""")
R(r"""The quantitative TMRB prediction is
therefore not a single shifted line but the $\mathbb{Z}_9$ sideband
comb Eq.~\eqref{eq:sideband_spacing} of Figure~\ref{fig:chladni}, whose 18~Hz
spacing for a $30\,M_\odot$ ringdown lies squarely in the Einstein
Telescope / Cosmic Explorer band.""",
  r"""The quantitative TMRB prediction is
therefore not a single shifted line but the sideband structure of
Eq.~\eqref{eq:sideband_spacing}: unresolved at every mass
(Eq.~\eqref{eq:comb_ratio}), it shows as the shortened damping time of
Section~\ref{sec:fluid_gravity}.""")
R(r"""The resulting $\mathbb{Z}_9$ QNM sideband
comb --- nine sidebands spaced $\approx 18$~Hz for a $30\,M_\odot$ binary ---
constitutes the most readily detectable near-term gravitational-wave signature
of the framework at Einstein Telescope and Cosmic Explorer.""",
  r"""The resulting nine sidebands are too close to
resolve (0.094 line widths at any mass); their signature is a mass-independent
shortening of the ringdown damping time by about 5--10\%, the framework's most
direct gravitational-wave test at Einstein Telescope and Cosmic Explorer.""")
R(r"""\bibitem{GWOSC2021}""", r"""\bibitem{BertiCardosoWill2006}
  E.~Berti, V.~Cardoso, C.~M.~Will,
  \textit{On gravitational-wave spectroscopy of massive black holes with the space
    interferometer LISA},
  Phys.\ Rev.\ D \textbf{73}, 064030 (2006).
  \href{https://doi.org/10.1103/PhysRevD.73.064030}{doi:10.1103/PhysRevD.73.064030}

\bibitem{GWOSC2021}""")
# ===== 3: prediction count, Hawking row
R(r"""Four
correlated near-term falsifiable predictions are presented,""",
  r"""Four
correlated predictions are presented (three near-term falsifiable; the entropy gap
has no observable yet),""")
R(r"""Four falsifiable predictions and current observational constraints are""",
  r"""Four predictions (three falsifiable near-term) and current observational constraints are""")
R(r"""  & $1/f^{0.75}$ noise modulation at $10^{-3}$--$10^{-2}$~Hz""",
  r"""  & $1/f^{0.75}$ noise modulation at $10^{-3}$--$10^{-2}$~Hz;
    mechanism in~\cite{BresslerQG2026}, not derived here""")
# ===== 4: Gap 5
R(r"""The bijection between $\mathbb{Z}_9$
    torsion phases and $\mathbb{Z}_9$ parafermion primaries is established
    ~\cite{BresslerCH2026};""",
  r"""The map from the nine $\mathbb{Z}_9$
    torsion phases to the 45 parafermion primaries (several primaries per
    charge sector; Gap~13) is stated in~\cite{BresslerCH2026};""")
# ===== 5: GRACE residuals
R(r""", with per-coordinate residual gravity anomalies in the range
$10^{-19}$--$10^{-18}~\mathrm{m\,s^{-2}}$ --- about four orders of magnitude below
the predicted amplitude.""",
  r""". (The per-coordinate residuals reported by the script,
$10^{-19}$--$10^{-18}~\mathrm{m\,s^{-2}}$, cannot be accelerations at the mascon
resolution that sets the limit below, nine orders higher; they are withheld
pending a re-check of the script.)""")
# ===== 6, 7: figure captions
R(r"""95\%~CL upper limits from \eqref{eq:gwosc_ul} and \eqref{eq:grace_ul}.""",
  r"""95\%~CL upper limits from \eqref{eq:gwosc_ul} and \eqref{eq:grace_ul}; the GWOSC
bar bounds only a $\sim 100$~Hz component of $\Delta g$ and does not exclude the
quasi-static prediction (Section~\ref{sec:current_constraints}).""")
R(r"""between the horizon-hair UV regulator and""", r"""between the proposed horizon-hair loop factor (Gap~15) and""")
# ===== 8: charges, units, T0
R(r"""and carry equal weight, $w_{9-k} = w_k$.""",
  r"""and carry equal weight, $w_{9-k} = w_k$.
Because $\theta_n$ is a phase, Eq.~\eqref{eq:Q_super} is defined modulo
$2\pi\eta_{\mathrm{diff}}M_{\mathrm{Pl,11}}^3$ (the label is $e^{i\theta_n}$), so
$Q^{(9-k)} \equiv -Q^{(k)}$.""")
R(r"""& KK hierarchy ratio &""", r"""& KK hierarchy ratio (dimensionful: $G_{11}$ carries length$^9$; units as in~\cite{BresslerBGL2026}) &""")
R(r"""$T_0 = 2\pi/\Delta\lambda \cdot \text{(galactic period unit)}$
~\cite{BresslerGP2026}.""",
  r"""$T_0 = (2\pi/\Delta\lambda)\,t_{\rm gal}$~\cite{BresslerGP2026}, where matching
$T_0 = 230$~Myr sets $t_{\rm gal} \approx 63.3$~Myr, so $T_0$ is an input here, not a
prediction.""")
# ===== 9: GWOSC search design
R(r"""templates. The resulting strain UL""", r"""templates. The segment contains no merger, so the search tests stationary lines at
the comb frequencies, not a ringdown. The resulting strain UL""")
# ===== 10: Fateev-Zamolodchikov reference
R(r"""  \textit{Parafermionic currents in the two-dimensional conformal quantum field theory},
  Nucl.\ Phys.\ B \textbf{280}, 644 (1987).
  \href{https://doi.org/10.1016/0550-3213(87)90003-7}{doi:10.1016/0550-3213(87)90003-7}""",
  r"""  \textit{Nonlocal (parafermion) currents in two-dimensional conformal quantum field
    theory and self-dual critical points in $Z_N$-symmetric statistical systems},
  Sov.\ Phys.\ JETP \textbf{62}, 215 (1985) [Zh.\ Eksp.\ Teor.\ Fiz.\ \textbf{89}, 380 (1985)].""")
# ===== gaps 17, 18
R(r"""    is identified that resolves a size-independent shift of about 21 nats.
\end{enumerate}""", r"""    is identified that resolves a size-independent shift of about 21 nats.

  \item \textbf{Time dependence of the torsion modulation (open, added in v4):}
    Frequency sidebands need the modulation $\delta V$ to advance in time at rate
    $\Delta f_{\rm tors}$; the potential as written varies only with angle.

  \item \textbf{Sideband damping and spin (open, added in v4):} The ringdown
    numbers of Section~\ref{sec:fluid_gravity} assume every sideband shares the
    $\ell = m = 2$ damping time, and are computed for Schwarzschild and, with fit
    formulas, spin 0.7. A Kerr derivation including overtones is open.
\end{enumerate}""")
# ===== change list
R(r"""yet observable (Gap~16); figures 1, 2 and 4 regenerated.
""", r"""yet observable (Gap~16); figures 1, 2 and 4 regenerated.
\textit{(xii)}~The sideband comb is shown to be unresolved (spacing 0.094 line widths at
every mass); the prediction is restated as a mass-independent shortening of the ringdown
damping time (4.6\%, 9.9\% at spin 0.7), with the time dependence and damping assumptions
as Gaps~17 and~18, and Fig.~4 redrawn with the true line width. The one-loop logarithm
$c_{\log}\ln(A/G_4)$ is added to the entropy, so $\Delta S_{\rm tors}$ leads only if Gap~15
closes. Smaller fixes: prediction count; Gap~5 (45 primaries); GRACE residuals withheld;
Fig.~3 and~5 captions; charges defined modulo $2\pi$; units of $G_4/G_{11}$; $T_0$ marked
as input; GWOSC segment contains no merger; Fateev--Zamolodchikov reference corrected.
""")
open(dst, "w").write(s); print("ok")
