"""r12c edits (George 4:51 PM ET Nov 21 2026, option 1): F-M1, F-M2, F-S1, F-S2, F-S3, F-S4, F-S6, F-S8."""
import sys
p = "bh_soft_hair_v4.tex"; s = open(p).read()
E = [
 # F-M1 (a) l.249
 ("F-M1a", r"where $\ln 3$ follows from the weights and $9\ln 9$ from counting the orbit once",
           r"where $\ln 3$ is the logarithm of the unit-prefactor boundary sum (a normalisation choice) and $9\ln 9$ from counting the orbit once"),
 # F-M1 (b) l.1316
 ("F-M1b", r"$\ln 3 = \ln Z_{\mathrm{tors}}$ follows from the weights and $9\ln 9$",
           r"$\ln 3 = \ln Z_{\mathrm{tors}}$ is the logarithm of the unit-prefactor boundary sum (a normalisation choice) and $9\ln 9$"),
 # F-M1 (c) after l.577
 ("F-M1c", "(see Eq.~\\eqref{eq:Z_tors_val}).  This term arises",
           "(see Eq.~\\eqref{eq:Z_tors_val}).  The value $\\ln 3$ uses the boundary sum with unit prefactor,\n"
           "$\\sum_m e^{-\\pi m^2/9}$; the normalised weights $w_n$ have $\\sum_n w_n = 1$, so this\n"
           "normalisation is a choice. $\\ln Z_{\\rm tors}$ is an entropy contribution only if $Z_{\\rm tors}$\n"
           "does not depend on $\\beta$, since $S = (1-\\beta\\partial_\\beta)\\ln Z$; reading the exponent as\n"
           "$\\beta E$ would instead give $\\ln 3 + \\tfrac12 \\approx 1.599$. Both points are part of Gap~12.\n"
           "This term arises"),
 # F-M1 (d) + F-S6 (b) Gap 12
 ("F-M1d/F-S6b", "    choice to be derived from the boundary path integral.\n",
           "    choice to be derived from the boundary path integral, and to show that it does not\n"
           "    double-count configurations already included in $9^{N_{\\rm cell}}$. The $\\ln 3$ term\n"
           "    likewise depends on the normalisation of the boundary sum and on $Z_{\\rm tors}$ being\n"
           "    $\\beta$-independent.\n"),
 # F-M2 l.485
 ("F-M2", r"Equation~\eqref{eq:Q_super} has no free coefficient; that $Q^{(n=1)}$ then",
          r"Its normalisation is set by the assumed parameter $\eta_{\mathrm{diff}}$; that $Q^{(n=1)}$ then"),
 # F-S1 l.479-484
 ("F-S1", "The charges $Q^{(n)}$ carry dimensions of\n$[\\text{mass}]^3$ in natural units (equivalently, $[\\text{length}]^{-3}$ with\n"
          "$\\hbar = c = 1$); this is the natural dimension of BMS supertranslation charges\n"
          "in 11D — specifically the stress-energy flux integrated over the bifurcation\n"
          "2-sphere times the 7D gyroid volume $V_7$, which upon dimensional reduction\n"
          "gives $Q^{(n)} \\sim M_{\\mathrm{Pl,4}}$ after absorbing factors of $G_4/G_{11}$.\n",
          "As written, $Q^{(n)}$ has dimension $[\\text{mass}]^3$ in natural units, whereas BMS\n"
          "supertranslation charges are energies; the reduction that would relate $Q^{(n)}$ to a\n"
          "four-dimensional charge of order $M_{\\mathrm{Pl,4}}$ is not derived here (Gap~2).\n"),
 # F-S2 l.346
 ("F-S2", r"The remaining parameters are derived or independently motivated (Table~\ref{tab:params}).",
          r"The remaining parameters are taken from the companion papers (Table~\ref{tab:params}); $\lambda_{\rm rec}$, $\mu$ and $\kappa_{\rm prop}$ are fitted or chosen there, and $T_0$ is an input."),
 # F-S3 l.664-665
 ("F-S3", "— also fixes\nthe galactic disk-wave period through",
          "— also enters\nthe galactic disk-wave model through"),
 # F-S4 l.418-419
 ("F-S4a", "$3 = \\sqrt{9}$ is also the total quantum\ndimension of $\\mathbb{Z}_9$ (Section",
           "$3 = \\sqrt{9}$ is also the total quantum\ndimension of a nine-anyon abelian theory (Section"),
 # F-S4 l.654-655
 ("F-S4b", "dimension: a $\\mathbb{Z}_9$ abelian topological order has total quantum dimension\n"
           "$\\mathcal{D} = \\sqrt{9} = 3$ and $\\gamma = \\ln 3$~\\cite{KitaevPreskill2006}.",
           "dimension: an abelian topological order with nine anyons (for example the $\\nu = 1/9$\n"
           "Laughlin state) has $\\mathcal{D} = \\sqrt{9} = 3$ and $\\gamma = \\ln 3$, whereas a\n"
           "$\\mathbb{Z}_9$ gauge (Dijkgraaf--Witten) theory has 81 anyons, $\\mathcal{D} = 9$ and\n"
           "$\\gamma = \\ln 9$~\\cite{KitaevPreskill2006}."),
 # F-S6 (a) l.585-587
 ("F-S6a", "Planck cells — is therefore\n", "Planck cells — is taken to be\n"),
 # F-S8 bib
 ("F-S8", "  \\textit{Spectral dimension of the universe in quantum gravity},\n  Phys.\\ Rev.\\ D \\textbf{72}, 064014 (2005).\n"
          "  \\href{https://doi.org/10.1103/PhysRevD.72.064014}{doi:10.1103/PhysRevD.72.064014}\n",
          "  \\textit{The spectral dimension of the universe is scale dependent},\n  Phys.\\ Rev.\\ Lett.\\ \\textbf{95}, 171301 (2005).\n"
          "  \\href{https://doi.org/10.1103/PhysRevLett.95.171301}{doi:10.1103/PhysRevLett.95.171301}\n"),
]
for tag, old, new in E:
    n = s.count(old)
    if n != 1: sys.exit(f"{tag}: expected 1 match, found {n}")
    s = s.replace(old, new); print("applied", tag)
open(p, "w").write(s)
