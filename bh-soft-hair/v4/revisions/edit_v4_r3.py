import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:90])
    s = s.replace(old, new)
W_OLD = r"$w_n = C\exp(-\pi n^2/9)$"
W_NEW = r"$w_n = C\exp(-\pi d(n)^2/9)$"
# ---------- protect the GWOSC record (it used the v3 weights), then swap the rest
R(r"Gaussian Z$_9$ weights $w_n = C\exp(-\pi n^2/9)$ (effective stack gain",
  r"Gaussian Z$_9$ weights of v3, $C\exp(-\pi n^2/9)$ with $n=0,\dots,8$ (effective stack gain")
R(W_OLD, W_NEW, 6)
# ---------- 2: Z9-symmetric weights, ln 3
R(r"9\ln 9 + \ln 2", r"9\ln 9 + \ln 3", 13)
R("20.468", "20.874", 7)
R(r"\ln 2 \approx 0.693", r"\ln 3 \approx 1.099", 3)
R(r"$\ln Z_{\mathrm{tors}} = \ln 2$", r"$\ln Z_{\mathrm{tors}} = \ln 3$", 2)
R(r"$\ln 2 = \ln Z_{\mathrm{tors}}$", r"$\ln 3 = \ln Z_{\mathrm{tors}}$")
R(r"""  w_n = C\exp\!\left(-\frac{\pi n^2}{9}\right),""",
  r"""  w_n = C\sum_{k\in\mathbb{Z}}\exp\!\left(-\frac{\pi (n+9k)^2}{9}\right)
      \simeq C\exp\!\left(-\frac{\pi\, d(n)^2}{9}\right),
  \qquad d(n) = \min(n,\,9-n),""")
R(r"""a \emph{DFT fixed-point Gaussian}: the discrete $\mathbb{Z}_9$ Fourier transform
of $\{w_n\}_{n=0}^{8}$ reproduces the same functional form up to normalisation
(it is a Jacobi theta function $\vartheta_3(0\,|\,i/9)$ evaluated on the
$\mathbb{Z}_9$ lattice), ensuring""",
  r"""the Gaussian periodised on $\mathbb{Z}_9$. It is an exact fixed point of the
$\mathbb{Z}_9$ discrete Fourier transform,
$w_n = \frac{1}{3}\sum_{m} w_m e^{-2\pi i mn/9}$ (checked numerically to $10^{-15}$),
and it respects $\mathbb{Z}_9$ conjugation, $w_{9-n} = w_n$. The one-sided form
$\exp(-\pi n^2/9)$, $n = 0,\dots,8$, used through v3 is neither: it misses the
fixed point by $0.57$ and gives $w_8 \ll w_1$. The periodised form ensures""")
R(r"""  Z_{\mathrm{tors}} &= \sum_{n=0}^{8} \exp\!\left(-\frac{\pi n^2}{9}\right) = \frac{1}{C} = 2 + \mathcal{O}\!\left(e^{-9\pi}\right)
    \quad \bigl(\text{equal to 2 to about }10^{-12}\bigr),""",
  r"""  Z_{\mathrm{tors}} &= \sum_{n=0}^{8}\sum_{k\in\mathbb{Z}} e^{-\pi (n+9k)^2/9}
    = \sum_{m\in\mathbb{Z}} e^{-\pi m^2/9} = \vartheta_3\!\left(0\,\middle|\,\tfrac{i}{9}\right)
    = \frac{1}{C} = 3 + \mathcal{O}\!\left(e^{-9\pi}\right),""")
R(r"\approx 1.068,", r"\approx 1.598,")
R(r"""By Poisson summation, $\sum_{n\in\mathbb{Z}} e^{-\pi n^2/9} = 3\sum_{k\in\mathbb{Z}} e^{-9\pi k^2}$,
so the one-sided sum in Eq.~\eqref{eq:Z_tors_val} is $2 + \mathcal{O}(e^{-9\pi})$; the value 2 is
exact for every practical purpose.""",
  r"""By Poisson summation, $\sum_{m\in\mathbb{Z}} e^{-\pi m^2/9} = 3\sum_{k\in\mathbb{Z}} e^{-9\pi k^2}$,
so $Z_{\rm tors} = 3$ to about $10^{-12}$; $3 = \sqrt{9}$ is also the total quantum
dimension of $\mathbb{Z}_9$ (Section~\ref{sec:entropy}). Through v3 the one-sided sum
was used, which gives 2 and $\ln 2$; it breaks $\mathbb{Z}_9$ conjugation and is withdrawn.""")
R(r"where $Z_{\mathrm{tors}} = \sum_{n=0}^8 \exp(-\pi n^2/9) = 2$ to about $10^{-12}$",
  r"where $Z_{\mathrm{tors}} = \sum_{m\in\mathbb{Z}} \exp(-\pi m^2/9) = 3$ to about $10^{-12}$")
R(r"""by $\mathbb{Z}_9$ conjugation.""", r"""by $\mathbb{Z}_9$ conjugation and carry equal weight, $w_{9-k} = w_k$.""")
R(r"""carry the dominant
weight $w_0+w_3+w_6 \approx 52\%$ of the total Gaussian weight distribution.""",
  r"""carry $w_0+w_3+w_6 \approx 36\%$ of the total weight (the largest single
weights are $w_0 = 1/3$ and $w_1 = w_8 \approx 0.235$).""")
# ---------- 7: quantum dimension
R(r"""Identifying $9\ln 9 = \ln(9^9)$, the total hair quantum dimension is
$\mathcal{D}_{\mathrm{TMRB}} = 9^9 = 387{,}420{,}489$.""",
  r"""The count $9^9 = 387{,}420{,}489$ is a number of states, not a quantum
dimension: a $\mathbb{Z}_9$ abelian topological order has total quantum dimension
$\mathcal{D} = \sqrt{9} = 3$ and $\gamma = \ln 3$~\cite{KitaevPreskill2006}. The
boundary term $\ln Z_{\rm tors} = \ln 3$ equals this $\gamma$ in magnitude with the
opposite sign; whether that is more than the shared $\sqrt{9}$ of Poisson
summation is open.""")
R(r"it counts the $9^9 = \mathcal{D}_{\rm TMRB}$", r"it counts the $9^9$")
# ---------- abstract / intro / prologue claims
R(r"""torsion and golden-ratio modular-covariant branching weights
$w_n = C\exp(-\pi d(n)^2/9)$—has delivered the first discrete holographic dual
for flat spacetime and explicitly closed the infrared triangle linking the""",
  r"""torsion and modular-covariant Gaussian branching weights
$w_n = C\exp(-\pi d(n)^2/9)$—has proposed a discrete holographic dual
for flat spacetime and an explicit closure of the infrared triangle linking the""")
R(r"""The golden-ratio weight
$\varphi^{-N_*}$ ($\varphi = (1+\sqrt{5})/2$) exponentially suppresses
logarithmic soft-graviton loop corrections (Section~\ref{sec:loop}), while""",
  r"""A golden-ratio factor
$\varphi^{-N_*}$ ($\varphi = (1+\sqrt{5})/2$) is proposed to suppress
logarithmic soft-graviton loop corrections; it is not yet derived from the
weights (Section~\ref{sec:loop}, Gap~15), while""")
R(r"""Remnants are excluded by the vanishing of the area term; whether""",
  r"""Information-carrying remnants are excluded by a capacity bound of
$\Delta S_{\rm tors} \approx 20.9$ nats; whether""")
R(r"""quantitative upper limits from coherent narrowband searches of GWOSC O3a
strain data and JPL RL06.3M GRACE-FO mascons that are consistent with --- and
provide a quantitative sensitivity floor for --- the framework's predicted
bulk-gravity-leakage amplitude.""",
  r"""quantitative upper limits: a GRACE/GRACE-FO mascon search consistent with the
framework's predicted quasi-static bulk-gravity-leakage amplitude, and a GWOSC O3a
narrowband search whose limit lies below that amplitude but bounds only a
component near 100~Hz, which the prediction does not contain.""")
R(r"""  \item Golden-ratio branching weights $w_n = C\exp(-\pi d(n)^2/9)$ exponentially
    suppress logarithmic soft-graviton loop corrections
    (Section~\ref{sec:loop}).""",
  r"""  \item A golden-ratio factor $\varphi^{-N_*}$ is proposed to suppress logarithmic
    soft-graviton loop corrections (Section~\ref{sec:loop}); it is not yet derived
    from the weights $w_n = C\exp(-\pi d(n)^2/9)$ (Gap~15).""")
R(r"""confirming holographic consistency (Section~\ref{sec:unitarity}).""",
  r"""supporting holographic consistency (Section~\ref{sec:unitarity}; Gap~13).""")
R(r"""same nine channels, in exactly the order the information arrived.""",
  r"""same nine channels, in the order the information arrived --- that is the
claim this paper proposes.""")
R(r"""The universe kept the receipt.""", r"""If that task is done, the universe kept the receipt.""")
R(r"""$\eta_{\mathrm{diff}} = 0.82 \pm 0.02$, which fixes every parameter in the
framework and connects""", r"""$\eta_{\mathrm{diff}} = 0.82 \pm 0.02$, which fixes the framework's
normalisation and connects""")
R(r"""smallest meaningful scale in physics. That is not a coincidence. That is the
universe telling you something.""", r"""smallest meaningful scale in physics. Whether that link is more than a
coincidence is what the predictions below are built to test.""")
# ---------- 5: discrete torsion classification
R(r"""arising from $H^3(\mathbb{Z}_9, U(1)) \cong \mathbb{Z}_9$~\cite{Vafa1986,AspinwallMorrison1995}.""",
  r"""labelled by the classes of $H^3(\mathbb{Z}_9, U(1)) \cong \mathbb{Z}_9$, the
Dijkgraaf--Witten classification of $\mathbb{Z}_9$ three-cocycles~\cite{DijkgraafWitten1990},
the natural home of a discrete C-field phase. (Vafa's discrete
torsion~\cite{Vafa1986} is classified by $H^2(G, U(1))$, which is trivial for cyclic
$G = \mathbb{Z}_9$; ``torsion'' in this paper means the $H^3$ class.)""")
R(r"""~\cite{Vafa1986,AspinwallMorrison1995} are preserved""", r"""~\cite{DijkgraafWitten1990} are preserved""")
R(r"""$H^3(\mathbb{Z}_9, U(1)) \cong \mathbb{Z}_9$~\cite{Vafa1986,AspinwallMorrison1995}.""",
  r"""$H^3(\mathbb{Z}_9, U(1)) \cong \mathbb{Z}_9$~\cite{DijkgraafWitten1990}.""")
R(r"""\bibitem{AspinwallMorrison1995}
  P.~S.~Aspinwall, D.~R.~Morrison,
  \textit{String theory on K3 surfaces},
  in \textit{Mirror Symmetry II}, AMS (1997).
  \href{https://arxiv.org/abs/hep-th/9404151}{arXiv:hep-th/9404151}""",
  r"""\bibitem{DijkgraafWitten1990}
  R.~Dijkgraaf, E.~Witten,
  \textit{Topological gauge theories and group cohomology},
  Commun.\ Math.\ Phys.\ \textbf{129}, 393 (1990).
  \href{https://doi.org/10.1007/BF02096988}{doi:10.1007/BF02096988}""")
# ---------- small: Q normalisation, encoding, cross-scale
R(r"""The numerical coefficient is fixed by requiring that $Q^{(n=1)}$ equals the
minimal KK mass scale set by the gyroid compactification.""",
  r"""Equation~\eqref{eq:Q_super} has no free coefficient; that $Q^{(n=1)}$ then
matches the minimal KK mass scale of the gyroid compactification is a
consistency condition still to be checked (Gap~2).""")
R(r"""Because
the $\mathbb{Z}_9$ permutation is unitary and invertible, information is encoded
bijectively into the hair configuration.""",
  r"""The proposal is that this map is unitary and invertible, so that information
is encoded bijectively into the hair configuration; showing it is Gap~11.""")
R(r"""These two independent appearances of the
$\mathbb{Z}_9$ scale --- one in black-hole entropy, one in galactic dynamics
--- constitute a non-trivial structural consistency check spanning
$10^{23}$~m.""",
  r"""Both appearances use the same Chosen input, the order 9 of the torsion
group, so they are a structural link between black-hole entropy and galactic
dynamics, not an independent consistency check.""")
# ---------- 4: loops
R(r"""\section{Golden-Ratio Regulation of Loop Corrections}""", r"""\section{Proposed Golden-Ratio Regulation of Loop Corrections}""")
R(r"""  S^{(\log)}_{\mathrm{loop}} = \frac{G_4}{\pi}\ln\!\frac{\omega}{\mu},
  \label{eq:log_loop}
\end{equation}
where $\omega$ is the graviton energy and $\mu$ is an IR regulator.""",
  r"""  S^{(\log)}_{\mathrm{loop}} = c_{\log}\,\ln\!\frac{A}{G_4},
  \label{eq:log_loop}
\end{equation}
where $c_{\log}$ is a pure number fixed by the massless field
content~\cite{Sen2012}.""")
R(r"""~\cite{Sen2012,BanerjeeGuptaSen2008}.""", r"""~\cite{Sen2012}.""")
R(r"""The branching weight $w_n$ evaluated at depth $N_*$ introduces an exponential
suppression factor $\varphi^{-N_*}$ on each loop vertex.  The corrected soft
theorem reads
\begin{equation}
  S_{\mathrm{TMRB}}^{(\log)} = S_{\mathrm{Weinberg}} \times
    \Bigl[1 + \frac{G_4}{\pi}\ln\!\frac{\omega}{\mu}\cdot\varphi^{-N_*}\Bigr].
  \label{eq:regulated_loop}
\end{equation}
Since $\varphi^{-N_*} \to 0$ exponentially for $N_* \to \infty$, the loop
correction is exponentially suppressed at large branching depth, eliminating the
divergence without a UV cutoff and without supersymmetry.""",
  r"""The proposal is that each loop vertex at branching depth $N_*$ carries a factor
$\varphi^{-N_*}$, so that
\begin{equation}
  S_{\mathrm{TMRB}}^{(\log)} = c_{\log}\,\ln\!\frac{A}{G_4}\cdot\varphi^{-N_*}.
  \label{eq:regulated_loop}
\end{equation}
If that factor holds, the loop correction is exponentially suppressed at large
branching depth, without a UV cutoff and without supersymmetry. The factor is
carried over from the pre-v2 weight $\varphi^{-\lambda n}$; it does not follow from
the Gaussian weights Eq.~\eqref{eq:wn}, and deriving or replacing it is Gap~15.""")
R(r"""Each loop diagram of order $\ell$ acquires a factor
\[
  \prod_{j=1}^{\ell} w_{n_j} \leq \left(\max_n w_n\right)^{\ell} \leq C^\ell \exp(-\pi\ell/9).
\]
The sum over loop orders converges absolutely for any $C < e^{\pi/9}$, which holds
for the normalised weight, \emph{assuming} the 11D CDT loop measure factorises
over branching vertices in the same way as the 4D case.  This factorisation
is the unproven step; see Section~\ref{sec:gaps}, gap~4.""",
  r"""A loop diagram of order $\ell$ with fixed branch labels acquires
\[
  \prod_{j=1}^{\ell} w_{n_j} \leq \left(\max_n w_n\right)^{\ell} = w_0^{\ell} = 3^{-\ell}.
\]
Summed over labels, however, the normalised weights give
$\prod_j \sum_{n_j} w_{n_j} = 1$ at every order, so the weights alone supply no
suppression with loop order. Convergence therefore needs the number of order-$\ell$
diagrams in each fixed-label sector to grow more slowly than $3^{\ell}$,
\emph{and} the 11D CDT loop measure to factorise over branching vertices as in 4D.
Both are unproven; see Section~\ref{sec:gaps}, gaps~4 and~15.""")
R(r"""Solid cyan: TMRB-regulated
correction with $\varphi^{-N_*}$ suppression.""", r"""Solid cyan: correction with the
proposed $\varphi^{-N_*}$ factor (not yet derived; Gap~15).""")
# ---------- 6: unitarity section
R(r"""$\tau = \beta/(2\pi)$ with""", r"""$\tau = i\beta/(2\pi)$ (spatial circle of length $2\pi$), with""")
R(r"""The diagonal invariant is the unique choice consistent with the $\mathbb{Z}_9$
charge conservation law Eq.~\eqref{eq:charge_conservation}.""",
  r"""The diagonal invariant is adopted here; Gepner and Qiu classify other
modular invariants of the parafermion theory~\cite{GepnerQiu1987}, and excluding
them is not attempted.""")
R(r"""Eq.~\eqref{eq:Z_torus} is the standard holomorphic criterion for
unitarity in 2D CFT~\cite{DiFrancesco1997}.  It holds here because:""",
  r"""Modular invariance of Eq.~\eqref{eq:Z_torus} is a consistency condition, not a
proof of unitarity~\cite{DiFrancesco1997}; unitarity rests on the parafermion CFT
itself being unitary~\cite{GepnerQiu1987}. In the nine-sector reduction the
invariance holds because:""")
R(r"""is the $\mathbb{Z}_9$ modular $S$-matrix.  The Gaussian weight $w_n$ transforms
under $\tau\to -1/\tau$ as $w_n \to w_n' = \frac{1}{3}\sum_m w_m e^{-2\pi i mn/9}$,
which by the Jacobi theta identity reproduces the same Gaussian form up to
normalisation — confirming DFT fixed-point self-consistency.""",
  r"""is the $S$-matrix of the nine-sector abelian reduction (the full parafermion
$S$-matrix acts on 45 characters; Gap~13).  The weights are left unchanged by the
same matrix, $w_n = \frac{1}{3}\sum_m w_m e^{-2\pi i mn/9}$, exactly for the
periodised Gaussian Eq.~\eqref{eq:wn} (numerically to $10^{-15}$).""")
# ---------- 3: remnants
R(r"""Remnants are excluded because the microstate \emph{entropy}
$S_{\mathrm{micro}} = A/(4G_4) \to 0$ as $A\to 0$,
leaving no finite-entropy state to store information at sub-Planckian areas.
The torsion correction $\Delta S_{\mathrm{tors}}$ is size-independent and
does not prevent this vanishing — it is dominated by the area term for any
macroscopic black hole.""",
  r"""The area term $S_{\mathrm{micro}} = A/(4G_4)$ vanishes as $A\to 0$, but the
size-independent term does not: at the endpoint
$S_{\mathrm{TMRB}} \to \Delta S_{\mathrm{tors}} \approx 20.9$ nats, that is
$9^9\cdot 3 = 3^{19} \approx 1.2\times10^{9}$ states. The construction therefore does
not exclude a Planck-scale relic. It does exclude an \emph{information-carrying}
remnant: a black hole that began with $S_{\mathrm{BH}} \gg 21$ nats cannot hand its
information to an object whose capacity is bounded by about 21 nats, so that
information must leave in the radiation. Whether the last $\Delta S_{\mathrm{tors}}$
nats are radiated or remain is open (Gap~14).""")
# ---------- QNM section, units and weights
R(r"""  \Delta\omega_{{\rm tors}} = \frac{f_{\rm QNM} \cdot \kappa_{\rm CE}}{9}""",
  r"""  \Delta f_{{\rm tors}} = \frac{f_{\rm QNM} \cdot \kappa_{\rm CE}}{9}""")
R(r"""402$~Hz gives $\Delta\omega/(2\pi) \approx 18$~Hz with the dominant sidebands
($n=0$, $\pm 1$, $\pm 3$, $\pm 6$) carrying weights $w_n \in \{0.500,\,0.353,\,
0.022,\,\sim 0\}$ — the 3-6-9 subgroup channels that close among themselves
under the $\mathbb{Z}_9$ fusion algebra. The $n=0$ and $n=1$ sidebands
carry about $85\%$ of the total spectral weight ($w_0 + w_1 \approx 0.853$).""",
  r"""402$~Hz gives $\Delta f_{\rm tors} \approx 18$~Hz, with sidebands
$n = 0, \pm1, \pm2, \pm3, \pm4$ carrying weights
$w_{|n|} \approx 0.333,\ 0.235,\ 0.083,\ 0.014,\ 0.001$ ($n = -k$ is the
$\mathbb{Z}_9$ conjugate $9-k$). The central line and its two neighbours carry
about $80\%$ of the weight ($w_0 + 2w_1 \approx 0.804$) and $|n| \le 2$ carry
$97\%$; the 3-6-9 subgroup lines ($n = 0, \pm 3$) carry $36\%$ and close among
themselves under the $\mathbb{Z}_9$ fusion algebra.""")
R(r"""\textit{Top right:} Sketch of the Gaussian weight envelope $w_n$ vs.\ branching
depth, illustrating the exponential suppression of high-$|n|$ modes.""",
  r"""\textit{Top right:} the deferred viscosity correction
$(\eta/s)/(1/4\pi) = 1 + \eta_{\rm diff}\Delta\lambda\,\varphi^{-N_*}$ (companion
paper; not used here).""")
R(r"""sidebands spaced by $\Delta\omega/(2\pi) \approx 18$~Hz flank the main QNM
peak; 3-6-9 sidebands (cyan) are enhanced by the $w_n$ weighting.""",
  r"""sidebands spaced by $\Delta f_{\rm tors} \approx 18$~Hz flank the main QNM
peak; line heights follow $w_n$, and the outer pairs ($|n| = 3, 4$) are weak.""")
R(r"""a kinematical consequence of the soft-hair sector Eq.~\eqref{eq:firewall_state}""",
  r"""a kinematical consequence of the soft-hair sectors of Section~\ref{sec:hair}""")
R(r"""9 sidebands spaced $\Delta\omega/(2\pi) = f_{\rm QNM}\kappa_{\rm CE}/9
    \approx 18.0$~Hz ($30\,M_\odot$); 3-6-9 sidebands enhanced by $w_n$
    weighting;""",
  r"""9 sidebands spaced $\Delta f_{\rm tors} = f_{\rm QNM}\kappa_{\rm CE}/9
    \approx 18.0$~Hz ($30\,M_\odot$); heights follow $w_n$, $|n|\le 2$
    carry 97\%;""")
R(r"""  & Exactly 9 sub-dominant torsion modes""", r"""  & 9 torsion sidebands; 5 ($|n|\le 2$) above 1\% of the weight""")
R(r"""  & Primordial BH merger statistics
  & $\sim$2030 \\""", r"""  & None identified: 21~nats beside $S_{\rm BH}\sim10^{78}$ for a stellar hole (Gap~16)
  & Not testable now \\""")
R(r"""lists four predictions that are correlated through""",
  r"""lists four predictions (the entropy gap has no observable yet) that are correlated through""")
# ---------- 1: GWOSC
R(r"""Two independent null searches have been performed against existing data products,
constraining --- but not yet excluding --- the predicted bulk-gravity-leakage
amplitude""", r"""Two independent null searches have been performed against existing data products,
targeting the predicted bulk-gravity-leakage amplitude""")
R(r"""over a contiguous 4531~s
segment of cleaned H1 strain (GPS 1238163456--1238171648, frame""",
  r"""over 4531~s of
cleaned H1 strain within the 8192~s span GPS 1238163456--1238171648 (frame""")
R(r"""a factor of $\sim 39$ below the Gaia-calibrated prediction.""",
  r"""a factor of $\sim 39$ below the Gaia-calibrated prediction. The conversion
treats $\Delta g$ as a test-mass acceleration oscillating at $f_{\rm eff}\approx
102$~Hz; under that assumption the search excludes the predicted amplitude at
95\%~CL. The predicted anomaly is quasi-static (it is what the GRACE search and the
planned gradiometers look for) with no 30--174~Hz component, so this result bounds
a $\sim 100$~Hz component of $\Delta g$, not $\Delta g_{\rm TMRB}$ itself.""")
R(r"""\paragraph{GRACE-FO mascon gravity""", r"""\paragraph{GRACE and GRACE-FO mascon gravity""")
R(r"""Neither null result is in tension with the framework: the predicted
$6.3\times10^{-15}~\mathrm{m\,s^{-2}}$ signal lies $\sim 39\times$ below the
GWOSC strain UL Eq.~\eqref{eq:gwosc_ul} and $\sim 10^{6}\times$ below the
GRACE-FO mascon UL Eq.~\eqref{eq:grace_ul}.""",
  r"""The GRACE-FO null is not in tension with the framework: the predicted
$6.3\times10^{-15}~\mathrm{m\,s^{-2}}$ lies $\sim 6\times10^{5}$ times below its UL
Eq.~\eqref{eq:grace_ul}. The GWOSC UL Eq.~\eqref{eq:gwosc_ul} lies $\sim 39$ times
\emph{below} the prediction; it is consistent with the framework only because it
bounds a $\sim 100$~Hz component that the quasi-static prediction does not have. If
a later version of the bulk-leakage model gives $\Delta g$ such a component at
that amplitude, this search already excludes it.""")
# ---------- conclusion
R(r"""Third, the golden-ratio factor $\varphi^{-N_*}$
exponentially suppresses logarithmic soft-graviton loop corrections, while""",
  r"""Third, a proposed golden-ratio factor $\varphi^{-N_*}$ would
exponentially suppress logarithmic soft-graviton loop corrections (Gap~15), while""")
R(r"""Remnants are excluded; firewall""", r"""Information-carrying remnants are excluded by a capacity bound; firewall""")
R(r"""$\mathbb{Z}_9$ mathematics that closes the infrared triangle""", r"""$\mathbb{Z}_9$ mathematics proposed to close the infrared triangle""")
R(r"""The two existing
null limits Eqs.~\eqref{eq:gwosc_ul} and~\eqref{eq:grace_ul} already constrain the
predicted bulk-gravity-leakage amplitude at the 45 hotspot
coordinates~\cite{BresslerBGL2026} and define""",
  r"""The GRACE-FO null limit Eq.~\eqref{eq:grace_ul} is consistent with the
predicted bulk-gravity-leakage amplitude at the 45 hotspot
coordinates~\cite{BresslerBGL2026}, the GWOSC limit Eq.~\eqref{eq:gwosc_ul} bounds
a $\sim 100$~Hz component of it, and together they define""")
R(r"""The universe is a living 9/4-time symphony.  With information conserved at the
horizon, the score is complete.""", r"""The universe is a living 9/4-time symphony.  If Gaps~10 and~11 close, with
information conserved at the horizon, the score is complete.""")
# ---------- gaps
R(r"""The convergence argument is valid given 4D CDT measure factorisation;""",
  r"""The convergence argument needs 4D-like measure factorisation and a
    bound on diagram growth (Gap~15);""")
R(r"""    with modular invariance, remains to be checked.
\end{enumerate}""", r"""    with modular invariance, remains to be checked.

  \item \textbf{Endpoint of the size-independent term (open, added in v4):} As
    $A\to 0$ the entropy tends to $\Delta S_{\rm tors}\approx 20.9$ nats, not zero.
    Whether these last nats are radiated or remain in a Planck-scale relic is
    not determined.

  \item \textbf{Golden-ratio loop factor (open, added in v4):} The factor
    $\varphi^{-N_*}$ of Section~\ref{sec:loop} does not follow from the Gaussian
    weights, and the weights alone give no suppression with loop order. Either
    $\varphi^{-N_*}$ is derived, or a bound on diagram growth slower than
    $3^{\ell}$ is shown.

  \item \textbf{Observable for the entropy gap (open, added in v4):} No measurement
    is identified that resolves a size-independent shift of about 21 nats.
\end{enumerate}""")
# ---------- change list
R(r"""\textit{(i)}~$Z_{\rm tors}$ equals 2 to about $10^{-12}$ by Poisson summation; the
earlier ``deviation ${\approx}3\times10^{-4}$'' is withdrawn.""",
  r"""\textit{(i)}~Weights made $\mathbb{Z}_9$-symmetric (the periodised Gaussian,
$w_{9-n} = w_n$), which makes the DFT fixed-point claim exact; $Z_{\rm tors} = 3$ to
about $10^{-12}$ by Poisson summation, so the boundary term is $\ln 3$ and
$\Delta S_{\rm tors} = 9\ln 9 + \ln 3 \approx 20.874$ (v3: one-sided weights, ${\approx}2$,
$\ln 2$, 20.468).""")
R(r"""\textit{(iii)}~Spectral weight of the $n=0,1$ sidebands corrected to ${\approx}85\%$ (was ${>}92\%$).""",
  r"""\textit{(iii)}~Sideband weights recomputed: $w_0 + 2w_1 \approx 80\%$, $|n|\le 2$ about $97\%$ (v3 stated ${>}92\%$ for $n=0,1$).""")
R(r"""\textit{(vii)}~Remnant argument updated to the v3 entropy $S_{\rm micro} = A/(4G_4)$.""",
  r"""\textit{(vii)}~Remnant argument corrected: the size-independent term leaves about 21~nats as $A\to 0$, so only information-carrying remnants are excluded (Gap~14).""")
R(r"""two arithmetic and citation fixes.
""", r"""two arithmetic and citation fixes.
\textit{(xi)}~The GWOSC limit lies ${\sim}39\times$ below the predicted $\Delta g$ and is
now stated to bound only a ${\sim}100$~Hz component; loop bound corrected and
$\varphi^{-N_*}$ marked as not derived (Gap~15); torsion classes attributed to
$H^3$ (Dijkgraaf--Witten), since Vafa's $H^2$ is trivial for $\mathbb{Z}_9$; modular
invariance no longer called a unitarity criterion; $\tau$ made imaginary; the
quantum-dimension comparison corrected ($\mathcal{D} = 3$); the entropy gap marked as not
yet observable (Gap~16); figures 1, 2 and 4 regenerated.
""")
# ---------- bibliography: drop the mis-cited Lovelock paper
i = s.index(r"\bibitem{BanerjeeGuptaSen2008}"); j = s.index(r"\bibitem{GWOSC2021}")
s = s[:i] + s[j:]
open(dst, "w").write(s); print("ok")
