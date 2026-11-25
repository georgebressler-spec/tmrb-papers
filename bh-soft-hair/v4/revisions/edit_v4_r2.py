import sys
p=sys.argv[1]; s=open(p).read()
def R(old,new,count=1):
    global s
    n=s.count(old); assert n==count,(n,old[:60]); s=s.replace(old,new)
# 1 v3 item (iii) displaced below the v4 list -> back into the v3 list
stray="""\\textit{(iii)}~All cross-citation DOIs updated to concept DOIs (always resolve
to latest version) throughout.
"""
R(stray,"")
R("""relevant argument is now inline at Eq.~\\eqref{eq:N_hair}.
""","""relevant argument is now inline at Eq.~\\eqref{eq:N_hair}.
"""+stray)
# 2 footer DOI pointed at the v2 record -> concept DOI
R("doi:10.5281/zenodo.20326236","doi:10.5281/zenodo.19981840")
# 3 nine sectors per torsion cell, not per Planck area (v3/v4's own cell area)
R("nine orthogonal channels per Planck-area patch\nof the horizon","nine orthogonal channels per torsion cell\n(about nine Planck areas) of the horizon")
R("The event horizon carries exactly nine quantised soft-hair charge sectors per\nPlanck area","The event horizon carries exactly nine quantised soft-hair charge sectors per\ntorsion cell")
R("The horizon carries exactly \\emph{nine} quantised soft-hair charge sectors\n    per Planck area","The horizon carries exactly \\emph{nine} quantised soft-hair charge sectors\n    per torsion cell")
R("nine soft-hair charge sectors per Planck\narea on the event horizon","nine soft-hair charge sectors per torsion\ncell on the event horizon")
R("permutes the nine torsion states in each Planck cell","permutes the nine torsion states in each torsion cell")
# 4 Term 2 still used the v1/v2 tile count
R("Each of the $N_{\\rm tiles} = A/(4\\ell_{\\rm Pl}^2)$ Planck cells on the horizon\ncarries nine independent torsion states.  The $N_{\\rm tiles}$ cells are",
  "Each of the $N_{\\rm cell} = A/(4G_4\\ln 9)$ torsion cells on the horizon\ncarries nine independent torsion states.  The $N_{\\rm cell}$ cells are")
R("$(A/4\\ell_{\\rm Pl}^2)\\ln 9$ in Eq.~\\eqref{eq:N_hair}","$N_{\\rm cell}\\ln 9 = A/(4G_4)$ in Eq.~\\eqref{eq:N_hair}")
# 5 Gap 8 and the appendix: say plainly the appendix is the v1/v2 count
R("Appendix~\\ref{app:microstate} recovers $S_{\\mathrm{micro}} = S_{\\mathrm{BH}}$\n    at the ``natural identification''",
  "The v1/v2 count (Appendix~\\ref{app:microstate}) recovers $S_{\\mathrm{micro}} = S_{\\mathrm{BH}}$\n    only at the identification")
R("This matches $S_{\\mathrm{BH}} = A/(4G_4)$ at the identification\n$G_4 = \\ell_{\\mathrm{Pl}}^2/\\ln 9$, a natural Planck-unit convention.",
  "This matches $S_{\\mathrm{BH}} = A/(4G_4)$ only at the identification\n$G_4 = \\ell_{\\mathrm{Pl}}^2/\\ln 9$, which is not a unit convention but Gap~8.\nThis is the v1/v2 count; from v3 on the paper tiles the horizon by\n$N_{\\mathrm{cell}} = A/(4G_4\\ln 9)$ cells, giving $S_{\\mathrm{micro}} = A/(4G_4)$\ndirectly (Eq.~\\eqref{eq:N_hair}).")
# 6 Gap 9 contradicted Gap 11
R("the modular-invariant partition function Eq.~\\eqref{eq:Z_torus} together\n    guarantee unitarity across the full evaporation, recovering information\n    from the Hawking spectrum after the Page time.",
  "the modular-invariant partition function Eq.~\\eqref{eq:Z_torus} are\n    necessary conditions for unitarity across the full evaporation; whether\n    they suffice is Gap~11.")
# 7 arithmetic: 1e-18 vs 6.3e-15 is under four orders, not nine
R("$10^{-19}$--$10^{-18}~\\mathrm{m\\,s^{-2}}$ --- nine orders of magnitude below\nthe predicted amplitude.","$10^{-19}$--$10^{-18}~\\mathrm{m\\,s^{-2}}$ --- about four orders of magnitude below\nthe predicted amplitude.")
# 8 bibliography page number
R("JHEP \\textbf{2009}, 063 (2009).","JHEP \\textbf{2009}, 073 (2009).")
# 9 change list
R("""``proposes a resolution'', matching the open gaps.
""","""``proposes a resolution'', matching the open gaps.
\\textit{(x)}~Consistency pass: nine sectors per torsion cell (not per Planck area)
throughout; Term~2 of \\S\\ref{sec:entropy} and Gap~8 use the v3 cell count; Gap~9 no
longer claims sufficiency; the appendix is labelled as the v1/v2 count; footer DOI set to
the concept DOI; two arithmetic and citation fixes.
""")
open(p.replace("v4.tex","v4_r2.tex"),"w").write(s); print("ok")
