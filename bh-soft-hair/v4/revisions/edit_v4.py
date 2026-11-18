import sys
p=sys.argv[1]; t=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global t
    c=t.count(a); assert c==n,(c,a[:70]); t=t.replace(a,b)
rep("\\date{April 2026 (v2: May 2026; v3: May 2026)}","\\date{April 2026 (v2: May 2026; v3: May 2026; v4: November 2026)}")
rep("This paper answers that question.","This paper proposes an answer to that question.")
rep("The\n$\\mathbb{Z}_9$ conservation law ensures not a single note is lost.","The\n$\\mathbb{Z}_9$ conservation law is the bookkeeping every playback must respect;\nshowing that it is enough to lose no note is the open task (Gap~11).")
rep("This work completes the UV-to-IR loop by resolving the black-hole information\nparadox within the identical construction.","This work proposes a resolution of the black-hole information paradox within\nthe identical construction, and states which of its steps remain open.")
rep("while\nholographic unitarity is established by torus partition function factorisation\n$Z(\\tau)=|\\chi_{\\mathbb{Z}_9}(\\tau)|^2$ (Section~\\ref{sec:unitarity}),\ntogether ruling out firewalls and remnants.",
    "while\nholographic consistency is argued from torus partition function factorisation\n$Z(\\tau)=|\\chi_{\\mathbb{Z}_9}(\\tau)|^2$ (Section~\\ref{sec:unitarity}).\nRemnants are excluded by the vanishing of the area term; whether the construction\navoids firewalls, and the full unitary map from infalling state to radiation,\nare open (Section~\\ref{sec:gaps}, Gaps~10 and~11).")
rep("This paper demonstrates that:","This paper argues that:")
rep("  Z_{\\mathrm{tors}} &= \\sum_{n=0}^{8} \\exp\\!\\left(-\\frac{\\pi n^2}{9}\\right) = \\frac{1}{C} \\approx 2\n    \\quad \\bigl(\\text{deviation from 2 is }{\\approx}3\\times10^{-4}\\bigr),",
    "  Z_{\\mathrm{tors}} &= \\sum_{n=0}^{8} \\exp\\!\\left(-\\frac{\\pi n^2}{9}\\right) = \\frac{1}{C} = 2 + \\mathcal{O}\\!\\left(e^{-9\\pi}\\right)\n    \\quad \\bigl(\\text{equal to 2 to about }10^{-12}\\bigr),")
rep("Here $\\mathcal{S}_{\\mathrm{tors}}$ is the Shannon entropy","By Poisson summation, $\\sum_{n\\in\\mathbb{Z}} e^{-\\pi n^2/9} = 3\\sum_{k\\in\\mathbb{Z}} e^{-9\\pi k^2}$,\nso the one-sided sum in Eq.~\\eqref{eq:Z_tors_val} is $2 + \\mathcal{O}(e^{-9\\pi})$; the value 2 is\nexact for every practical purpose.\nHere $\\mathcal{S}_{\\mathrm{tors}}$ is the Shannon entropy")
rep("$Z_{\\mathrm{tors}} = \\sum_{n=0}^8 \\exp(-\\pi n^2/9) \\approx 2$ (deviation ${\\approx}3\\times10^{-4}$;\nsee Eq.~\\eqref{eq:Z_tors_val}).","$Z_{\\mathrm{tors}} = \\sum_{n=0}^8 \\exp(-\\pi n^2/9) = 2$ to about $10^{-12}$\n(see Eq.~\\eqref{eq:Z_tors_val}).")
rep("9.66\\,\\ell_{\\mathrm{Pl}}^2","8.79\\,\\ell_{\\mathrm{Pl}}^2",2)
rep("which carries the imprint of the infalling state, restoring unitarity.","which every evaporation history must respect.  A single mod-9 conservation law\nfixes one number, so it carries at most $\\ln 9 \\approx 2.2$ nats about the\ninfalling state; it is a necessary condition for the proposed encoding, not by\nitself a demonstration of unitarity.  The full map from infalling state to\nradiation is open (Gap~11 in Section~\\ref{sec:gaps}).")
rep("$\\ln(9^9)$.\n\nThe two terms are orthogonal","$\\ln(9^9)$.  Counting the orbit once is the choice that fixes this term;\nderiving that count from the path integral is open (Gap~12).\n\nThe two terms are orthogonal")
rep("where $\\chi_a(\\tau)$ are the nine $\\mathbb{Z}_9$ parafermion characters and","where $\\chi_a(\\tau)$ are the characters of the nine $\\mathbb{Z}_9$ charge sectors and")
rep("The diagonal invariant is the unique choice consistent with the $\\mathbb{Z}_9$\ncharge conservation law Eq.~\\eqref{eq:charge_conservation}.",
    "The diagonal invariant is the unique choice consistent with the $\\mathbb{Z}_9$\ncharge conservation law Eq.~\\eqref{eq:charge_conservation}.\nThe $\\mathbb{Z}_9$ parafermion theory ($SU(2)_9/U(1)$) has $k(k+1)/2 = 45$\nprimary fields, so each charge sector collects several primaries; writing\nEq.~\\eqref{eq:Z_torus} over all 45 characters and checking its modular\ninvariance is open (Gap~13).")
rep("\\subsection{No Firewall, No Remnant}","\\subsection{Firewalls and Remnants}")
rep("The monogamy constraint\napplies to \\emph{bipartite} entanglement; the three-way entanglement Eq.~\\eqref{eq:firewall_state}\nis not monogamy-constrained.  Early radiation $R$ is entangled with the hair sector\n$|q_n\\rangle$, not directly with $b$ or $\\tilde{b}$, so the AMPS argument does not apply.\nThe three-way entanglement structure Eq.~\\eqref{eq:firewall_state} recovers the\nPage curve~\\cite{Page1993} when the gravitational entropy is replaced by\n$S_{\\mathrm{TMRB}}$ in the island formula~\\cite{Penington2020}.",
    "Tracing out the hair sector in Eq.~\\eqref{eq:firewall_state} leaves\n$\\rho_{b\\tilde b} = \\sum_n |\\alpha_n|^2\\, |b_n\\tilde b_n\\rangle\\langle b_n\\tilde b_n|$,\nwhich is separable: as written, the state does not keep $b$ entangled with\n$\\tilde b$, and smoothness of the horizon in the AMPS sense requires exactly that\nentanglement.  Monogamy of entanglement also constrains multipartite\nstates~\\cite{CKW2000}.  Avoiding the firewall therefore needs a different\nhair-sector structure, in which $b$ stays entangled with $\\tilde b$ while the\nearly radiation $R$ purifies the hair; constructing it is open (Gap~10).\nWhether replacing the gravitational entropy by $S_{\\mathrm{TMRB}}$ in the island\nformula~\\cite{Penington2020} reproduces the Page curve~\\cite{Page1993} is\nlikewise still to be shown.")
rep("$S_{\\mathrm{micro}} = (A/4\\ell_{\\mathrm{Pl}}^2)\\ln 9 \\to 0$ as $A\\to 0$,","$S_{\\mathrm{micro}} = A/(4G_4) \\to 0$ as $A\\to 0$,")
rep("The dominant $|n|\\leq 1$ sidebands\ncarry $> 92\\%$ of the total spectral weight.","The $n=0$ and $n=1$ sidebands\ncarry about $85\\%$ of the total spectral weight ($w_0 + w_1 \\approx 0.853$).")
rep("The TMRB framework resolves the black-hole information paradox through three\ninterconnected mechanisms.","The TMRB framework proposes a resolution of the black-hole information paradox\nthrough three interconnected mechanisms.")
rep("while\nholographic unitarity follows from torus partition function factorisation\n$Z(\\tau)=|\\chi_{\\mathbb{Z}_9}(\\tau)|^2$, together ruling out firewalls and\nremnants.",
    "while\nholographic consistency is argued from torus partition function factorisation\n$Z(\\tau)=|\\chi_{\\mathbb{Z}_9}(\\tau)|^2$.  Remnants are excluded; firewall\navoidance and the full unitary map remain open (Gaps~10 and~11).")
rep("    remains open.\n\\end{enumerate}",
"""    remains open.

  \\item \\textbf{Firewall avoidance (open, added in v4):} The state
    Eq.~\\eqref{eq:firewall_state} is of GHZ type; tracing out the hair leaves the
    Hawking pair $b,\\tilde b$ unentangled.  A hair-sector state that keeps $b$
    entangled with $\\tilde b$ while the early radiation purifies the hair is
    required and not yet constructed.

  \\item \\textbf{Unitary map (open, added in v4):} The $\\mathbb{Z}_9$ conservation
    law Eq.~\\eqref{eq:charge_conservation} is necessary but carries at most
    $\\ln 9$ nats; an explicit unitary map from infalling state to Hawking radiation
    through the hair sector is required.

  \\item \\textbf{Orbit counting (open, added in v4):} The size-independent term
    $9\\ln 9$ follows from counting the nine-node orbit once; that count is a
    choice to be derived from the boundary path integral.

  \\item \\textbf{Full parafermion partition function (open, added in v4):} The
    $\\mathbb{Z}_9$ parafermion theory has 45 primary fields; Eq.~\\eqref{eq:Z_torus}
    is written over the nine charge sectors, and its form over all 45 characters,
    with modular invariance, remains to be checked.
\\end{enumerate}""")
rep("relevant argument is now inline at Eq.~\\eqref{eq:N_hair}.",
"""relevant argument is now inline at Eq.~\\eqref{eq:N_hair}.

\\smallskip
\\noindent\\textbf{Changes in v4:}
\\textit{(i)}~$Z_{\\rm tors}$ equals 2 to about $10^{-12}$ by Poisson summation; the
earlier ``deviation ${\\approx}3\\times10^{-4}$'' is withdrawn.
\\textit{(ii)}~Torsion cell area corrected to $4G_4\\ln 9 \\approx 8.79\\,\\ell_{\\rm Pl}^2$ (was 9.66).
\\textit{(iii)}~Spectral weight of the $n=0,1$ sidebands corrected to ${\\approx}85\\%$ (was ${>}92\\%$).
\\textit{(iv)}~Firewall section rewritten: the state Eq.~\\eqref{eq:firewall_state} leaves the
Hawking pair unentangled, and monogamy constrains multipartite states; firewall avoidance
is now Gap~10.
\\textit{(v)}~The $\\mathbb{Z}_9$ conservation law is stated as a necessary condition
carrying at most $\\ln 9$ nats; the unitary map is now Gap~11.
\\textit{(vi)}~Orbit counting for $9\\ln 9$ and the 45-primary parafermion partition
function added as Gaps~12 and~13.
\\textit{(vii)}~Remnant argument updated to the v3 entropy $S_{\\rm micro} = A/(4G_4)$.
\\textit{(viii)}~Abstract, introduction and conclusion reworded from ``resolves'' to
``proposes a resolution'', matching the open gaps.""")
rep("\\bibitem{AMPS2013}","""\\bibitem{CKW2000}
  V.~Coffman, J.~Kundu, W.~K.~Wootters,
  \\textit{Distributed entanglement},
  Phys.\\ Rev.\\ A \\textbf{61}, 052306 (2000).

\\bibitem{AMPS2013}""")
open(p,'w',encoding='utf-8').write(t)
print("ok")
