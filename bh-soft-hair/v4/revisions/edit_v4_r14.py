import sys
p = sys.argv[1]; s = open(p).read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]; s = s.replace(old, new)
R(r"""In the v4 review, Grok (xAI) review agents proposed corrections; the author chose which to adopt.}}""",
  r"""In the v4 review, Grok (xAI) review agents proposed corrections, Perplexity checked the sources cited for the method, and Gemini (Google) gave a blind review whose suggested text was not used; the author chose what to adopt.}}""")
R(r"""  \item Registration files, analysis scripts and GitHub's push records are included in the
    Zenodo record; the full revision trail (r1--r12c) and audits are in the public repository""",
  r"""  \item Registration files, analysis scripts, GitHub's push records and the X24si process
    record (with the Perplexity and Gemini records) are included in the Zenodo record; the
    full revision trail (r1--r14) and audits are in the public repository""")
R(r"""\noindent\textbf{Participants.} The author: every decision. Claude (Anthropic):
audits~1--4, the numerical checks, the registered test of Section~\ref{sec:x24si_test},
and drafting of revisions r1--r11, r12d and r13. The Grok team (xAI): Sparks (Chief of
Staff), Jimmy (rigour), Fletcher (continuity and feedback), Worker Bee (learner-path design)
and Starling (independent review of leaks, gaming and oversight), whose audit and review
produced r12--r12c. One rigour check (18 November) was run by Claude in Jimmy's place and is
labelled as such.""",
  r"""\noindent\textbf{A first application.} This paper is the first application of the X24si
method to a research paper. It is a first, partial expression of the method's intent, not
its full form: the process record logs 31 deviations from the planned protocol, each
recorded rather than repaired, and no human domain specialist took part. The record, with
its roles, outside clocks, decisions, deviations and after-action reviews, is published with
this version.

\smallskip
\noindent\textbf{Participants: the AI swarm and the human.} The SI participants came from four
model families; agreement within a family counts as one correlated source.
\begin{itemize}[leftmargin=*, itemsep=1pt]
  \item \textbf{The author:} every decision.
  \item \textbf{Claude (Anthropic):} audits~1--4, the numerical checks, the registered test of
    Section~\ref{sec:x24si_test}, and drafting of revisions r1--r11, r12d, r13 and r14. One
    rigour check (18 November) was run by Claude in Jimmy's place and is labelled as such.
  \item \textbf{The Grok team (xAI):} Sparks (coordinator and merger of the team review;
    16 findings), Jimmy (the X24si test and the logarithmic term; 6), Fletcher (the mapping,
    overclaims and citations; 19), Worker Bee (GRACE and clarity; 7), each reviewing
    independently; and Starling (the referee and symbolic-check pass behind r12b--r12c). Grok
    also co-wrote the v1--v3 mathematics, so its agreement on that part is coordination.
  \item \textbf{Perplexity:} an outside check of the 24 sources cited for the method, given
    no paper text: 14 claims supported, 6 partly, none unsupported, and 4 not verifiable (all
    X24si's own pages, which it could not open).
  \item \textbf{Gemini (Google):} a blind review of revision r11 (Stage G1), the most
    independent seat available. Gemini was also used for the Z9 cold reads, which are
    separate work.
\end{itemize}""")
R(r"""    two stacked entries. \emph{Decision:} the author adopted the findings (options chosen on""",
  r"""    two stacked entries. \emph{Outside checks:} Perplexity's source check (above) agreed with
    16 of the 24 source labels and proposed sources that test the method; Gemini's blind review
    independently agreed with several of the team's diagnoses, but claimed source checks it
    had not done and proposed paper text built on them. The author cancelled Gemini's planned
    informed re-check and used none of its suggested text: a false claim caught at the human
    decision step. \emph{Decision:} the author adopted the findings (options chosen on""")
R(r"""    \emph{Changed:} r12d and r13 (this appendix and the title).""",
  r"""    \emph{Changed:} r12d and r13 (this appendix and the title); r14 completes the list of
    participants and publishes the process record.""")
open(p, "w").write(s); print("ok")
