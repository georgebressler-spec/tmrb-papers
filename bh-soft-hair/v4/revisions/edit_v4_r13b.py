import sys
p = sys.argv[1]; s = open(p).read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]; s = s.replace(old, new)
R(r"""and drafting of revisions r1--r11, r12d and r13. The Grok team (xAI), including Sparks
(Chief of Staff) and Jimmy (rigour): the team audit and review behind r12--r12c. One rigour
check (18 November) was run by Claude in Jimmy's place and is labelled as such.""",
  r"""and drafting of revisions r1--r11, r12d and r13. The Grok team (xAI): Sparks (Chief of
Staff), Jimmy (rigour), Fletcher (continuity and feedback), Worker Bee (learner-path design)
and Starling (independent review of leaks, gaming and oversight), whose audit and review
produced r12--r12c. One rigour check (18 November) was run by Claude in Jimmy's place and is
labelled as such.""")
R(r"""  \item \textbf{Disclosure and team review (19--21 Nov).} \emph{Changed:} r11 states Claude's
    role in the AI disclosure. Review criteria were committed before the review began. The
    Grok team's audit produced r12--r12c, whose findings the author adopted, including an
    addendum that corrects an overstatement in the run record without altering it.""",
  r"""  \item \textbf{Disclosure and Grok team audit (19--21 Nov).} \emph{Changed first:} r11
    states Claude's role in the AI disclosure, and the review criteria (MUST-FIX, SHOULD-FIX,
    NOTE) were committed before the review began. \emph{Found by the Grok team:}
    $\eta_{\rm diff} = 0.82$, presented since v1 as a Gaia DR3 calibration, is not a Gaia
    measurement: it traces to a formula in the Unified Framework paper that does not reproduce
    0.82; the area-law match holds only by construction, given the underived cell area
    (Gap~8); Sen's analysis, which finds no higher-loop logarithms, disfavours the
    golden-ratio suppression (Gap~15); the $\ln 3$ term depends on a normalisation choice and
    on $Z_{\rm tors}$ not depending on $\beta$ (otherwise $\ln 3 + \frac12$), and the $9\ln 9$
    count may double-count configurations (Gap~12); a $\mathbb{Z}_9$ gauge theory has quantum
    dimension 9, not 3; the charges $Q^{(n)}$ carry the wrong dimension for BMS charges
    (Gap~2); the remnant argument needs the expansion at $A\to 0$, where it fails; and the run
    record overstated how favourable the registered mapping was. The six transcribed GWTC-5.0
    intervals were re-checked against the source text, with the author's visual check of the
    two stacked entries. \emph{Decision:} the author adopted the findings (options chosen on
    19 and 21 November). \emph{Changed:} r12--r12c: $\eta_{\rm diff}$ relabelled an assumed
    parameter (the ringdown and entropy results do not depend on it); claims recast as
    proposals with their gaps named; an addendum to the run record, which leaves the record
    and the EXCLUDED verdict unchanged. \emph{Fed forward:} the release checks.""")
R(r"""\emph{What the loop produced:} the
corrections above, nine new open gaps (10--18) in place of unstated assumptions, two
observational sections rewritten from their own scripts, and a prediction tested and
refuted on the record.""",
  r"""\emph{What the loop produced:} the
corrections above, nine new open gaps (10--18) in place of unstated assumptions, the
series' ``single Gaia anchor'' shown to be an assumed parameter, two observational sections
rewritten from their own scripts, and a prediction tested and refuted on the record.""")
open(p, "w").write(s); print("ok")
