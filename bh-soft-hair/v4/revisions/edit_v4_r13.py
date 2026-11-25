import sys
p = sys.argv[1]; s = open(p).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:90]); s = s.replace(old, new)
# --- title
R(r"""  \textbf{Discrete $\mathbb{Z}_9$ Torsion Hair, Finite Microstate Counting,}\\[4pt]
  \textbf{and the $9\ln 9$ Topological Correction in 11D M-Theory}%""",
  r"""  \textbf{Discrete $\mathbb{Z}_9$ Torsion Hair, the $9\ln 9 + \ln 3$ Correction,}\\[4pt]
  \textbf{and a Ringdown Prediction Refuted by a Pre-Registered Test}%""")
R(r"""  pdftitle={A Proposed TMRB Soft-Hair Resolution of the Black-Hole Information Paradox},""",
  r"""  pdftitle={A Proposed TMRB Soft-Hair Resolution of the Black-Hole Information Paradox: Discrete Z9 Torsion Hair, the 9 ln 9 + ln 3 Correction, and a Ringdown Prediction Refuted by a Pre-Registered Test},""")
# --- abstract: both the failure and the method, plainly
R(r"""The primary verdict holds for every spin and start time in Table~\ref{tab:ringdown_spin}.

\smallskip
\noindent\textbf{Keywords:}""",
  r"""The primary verdict holds for every spin and start time in Table~\ref{tab:ringdown_spin}.
No prediction of this paper has yet passed a test. What worked is the method: applied
across v4, the same human-in-the-loop, future-paced, AI-swarm self-recursive loop (X24si)
found and corrected the paper's own errors, turned nine unproven steps into stated open
gaps, and refuted its own prediction on the record. Appendix~\ref{app:x24si} traces
each turn.

\smallskip
\noindent\textbf{Keywords:}""")
# --- change list: method name in (i), pointer item
R(r"""the X24si method} (human-in-the-loop self-recursive reasoning, anchored by an outside
    clock and outside data).""",
  r"""the X24si method} (human-in-the-loop, future-paced, AI-swarm self-recursive reasoning,
    anchored by an outside clock and outside data).""")
R(r"""\begin{enumerate}[leftmargin=*, label=\textit{(\roman*)}, itemsep=1pt, topsep=2pt]
  \item \textbf{Ringdown prediction tested""",
  r"""\noindent\textit{Every change below came from one turn of the X24si loop; Appendix~\ref{app:x24si}
traces each turn: what was found, who decided, what changed and what it fed forward.}
\begin{enumerate}[leftmargin=*, label=\textit{(\roman*)}, itemsep=1pt, topsep=2pt]
  \item \textbf{Ringdown prediction tested""")
# --- §7.1: full name, defined in Appendix B
R(r"""with the X24si method~\cite{BresslerX24si2026}: human-in-the-loop self-recursive
reasoning.""", r"""with the X24si method~\cite{BresslerX24si2026}: human-in-the-loop, future-paced,
AI-swarm self-recursive reasoning (each term is defined in Appendix~\ref{app:x24si}).""")
# --- Appendix B
R(r"""rather than removing entanglement degeneracy.

% ── Bibliography""", r"""rather than removing entanglement degeneracy.

\needspace{6\baselineskip}
\section{How v4 Was Made: the X24si Loop}
\label{app:x24si}

Version~4 was produced with the X24si method~\cite{BresslerX24si2026}:
\emph{human-in-the-loop, future-paced, AI-swarm self-recursive reasoning}.
\begin{itemize}[leftmargin=*, itemsep=1pt]
  \item \textbf{Human-in-the-loop.} The author makes every decision. SI participants
    provide decision support; their words are filed as evidence, never executed as
    instructions.
  \item \textbf{Future-paced.} Before a new choice, strategy or behaviour is adopted, its
    first- to fourth-order impacts, and those of its outcomes, are written down. Afterwards
    an after-action review (AAR) asks what was supposed to happen, what happened, why the
    two differ, and what to sustain or change.
  \item \textbf{AI swarm.} Several SI systems from different model families work on the
    same claims in distinct roles. Agreement among them is weighed by where it comes from
    (reasoning, retrieval or execution), never counted; a model checking its own work is
    coordination, not corroboration.
  \item \textbf{Self-recursive.} Each turn ends in something learned or a named stuck
    point, and that outcome becomes the next turn's input. The loop is anchored outside
    itself, by instruments, published data and an outside clock, so it can refute its own
    claims rather than only confirm them.
\end{itemize}

\noindent\textbf{Participants.} The author: every decision. Claude (Anthropic):
audits~1--4, the numerical checks, the registered test of Section~\ref{sec:x24si_test},
and drafting of revisions r1--r11, r12d and r13. The Grok team (xAI), including Sparks
(Chief of Staff) and Jimmy (rigour): the team audit and review behind r12--r12c. One rigour
check (18 November) was run by Claude in Jimmy's place and is labelled as such.

\smallskip
\noindent\textbf{The turns.} Each entry gives what was found, the author's decision, what
changed, and what the turn fed forward.
\begin{enumerate}[leftmargin=*, label=\textbf{T\arabic*.}, itemsep=3pt]
  \item \textbf{Audit 1 (17 Nov).} \emph{Found:} $Z_{\rm tors}$ equals 2 to $10^{-12}$
    (not $3\times10^{-4}$ off); torsion cell $8.79\,\ell_{\rm Pl}^2$ (not 9.66); sideband share
    85\% (not ${>}92\%$); the firewall state leaves the Hawking pair unentangled; the
    conservation law fixes at most $\ln 9$ nats. \emph{Decision:} fix the paper first.
    \emph{Changed:} r1; Gaps~10--13; ``resolves'' becomes ``proposes a resolution''.
    \emph{Fed forward:} a second audit of r1.
  \item \textbf{Audit 2 (17 Nov).} \emph{Found:} eight consistency errors (among them
    ``per Planck area'' against the stated cell size, and a footer DOI pointing at v2) and
    four physics problems: $\ln 2$ came from weights that break $\mathbb{Z}_9$ symmetry;
    the remnant argument failed at $A\to 0$; the loop bound was wrong; the GWOSC limit was
    read backwards. \emph{Decision:} fix them all. \emph{Changed:} r2--r3:
    $\mathbb{Z}_9$-symmetric weights ($\ln 3$; $\Delta S_{\rm tors} \approx 20.874$), the
    remnant claim narrowed (Gap~14), the loop factor marked unproven (Gap~15), the torsion
    classes attributed to $H^3$, the entropy gap marked untestable (Gap~16).
    \emph{Fed forward:} a third audit.
  \item \textbf{Audit 3 (17--18 Nov).} \emph{Found:} the nine sidebands cannot be resolved
    in a ringdown; the entropy formula omitted the one-loop logarithm. \emph{Decision:} fix
    them all. \emph{Changed:} r4: the prediction restated as a shortening of the damping
    time; Gaps~17--18; the logarithm added. \emph{Fed forward:} confirmation of the two new
    statements.
  \item \textbf{Audit 4 and source checks (18 Nov).} \emph{Found:} the shortening depends on
    the fit start time; Sen's coefficient is $77/90$ (read from the source); the analysis
    scripts showed the GWOSC figure is a sensitivity estimate, the published GRACE table came
    from the script's demonstration mode, and the real 26 April run returns zero by
    construction. \emph{Decision:} check before removing anything; keep the GWOSC figure as a
    sensitivity floor; rewrite the GRACE paragraph from the real run. \emph{Changed:} r5--r7;
    the synthetic histogram removed from Fig.~\ref{fig:constraints}; the run's own output
    added as Fig.~\ref{fig:grace_run}. \emph{Fed forward:} a rigour check.
  \item \textbf{Rigour check (18 Nov; Claude in Jimmy's place).} \emph{Found:} with exact Kerr
    frequencies the shortening runs from 4.4\% (no spin) to 19\% (spin 0.9), about 10--18\%
    for typical remnants, possibly within reach of existing data. \emph{Decision:} add the
    table, then test against existing data, registered first. \emph{Changed:} r8,
    Table~\ref{tab:ringdown_spin}. \emph{Fed forward:} the registered test.
  \item \textbf{Registered test (18 Nov).} \emph{Future-paced:} the meaning of each possible
    outcome for this paper, with its first- to fourth-order impacts, was written before any
    result was read; the registration was pushed at 16:05~UTC and the test run once.
    \emph{Found:} EXCLUDED (Section~\ref{sec:x24si_test}). \emph{Decision:} report it as an
    X24si result, prominently. \emph{Changed:} r9--r10. \emph{Fed forward:} Gaps~17--18 now
    carry the refutation.
  \item \textbf{Disclosure and team review (19--21 Nov).} \emph{Changed:} r11 states Claude's
    role in the AI disclosure. Review criteria were committed before the review began. The
    Grok team's audit produced r12--r12c, whose findings the author adopted, including an
    addendum that corrects an overstatement in the run record without altering it.
  \item \textbf{Release checks (25 Nov).} \emph{Found:} one sentence claimed material the
    Zenodo record would not hold, and the title named a term the paper had replaced.
    \emph{Changed:} r12d and r13 (this appendix and the title).
\end{enumerate}

\noindent\textbf{Outcome.} \emph{What failed:} the paper's one near-term gravitational-wave
prediction; no prediction of v4 has yet passed a test. \emph{What the loop produced:} the
corrections above, nine new open gaps (10--18) in place of unstated assumptions, two
observational sections rewritten from their own scripts, and a prediction tested and
refuted on the record. \emph{Stuck points carried forward:} deriving the horizon
$\mathbb{Z}_9$ labels and the cell area (Gaps~7--8), the unitary map (Gap~11), the loop
factor (Gap~15), and the ringdown assumptions (Gaps~17--18).

% ── Bibliography""")
open(p, "w").write(s); print("ok")
