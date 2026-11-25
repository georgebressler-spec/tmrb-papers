import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)

# ---- concise change list from v3 (last version on Zenodo), X24si result first
i = s.index(r"""\noindent\textbf{Changes in v4:}""")
j = s.index(r"""% ─────────────────────────────────────────────────────────────────────────────
\needspace{6\baselineskip}
\section{TMRB Framework Recap}""")
s = s[:i] + r"""\noindent\textbf{Changes in v4 (from v3, the last version on Zenodo):}
\begin{enumerate}[leftmargin=*, label=\textit{(\roman*)}, itemsep=1pt, topsep=2pt]
  \item \textbf{Ringdown prediction tested against published data and disfavoured, by
    the X24si method.} Before any result was read, a test of this paper's ringdown
    prediction against LIGO--Virgo--KAGRA data was registered with an outside clock (a
    timestamped GitHub commit): the claim, the data source, the decision rule and a frozen
    decision script. Run once on GWTC-5.0, the combined result
    $\delta\hat\tau_{220} = 0.07^{+0.06}_{-0.05}$ excludes the predicted shortening
    ($-0.095$; band $-0.126$ to $-0.070$), and all five secondary combinations agree. The
    result stands as run (Section~\ref{sec:x24si_test}).
  \item \textbf{Entropy correction revised.} The weights are made $\mathbb{Z}_9$-symmetric,
    so $\ln Z_{\rm tors} = \ln 3$ and $\Delta S_{\rm tors} = 9\ln 9 + \ln 3 \approx 20.874$
    (v3: $\ln 2$, 20.468). The one-loop logarithm $c_{\log}\ln(A/G_4)$, with
    $c_{\log} = 77/90$, is added; it exceeds $\Delta S_{\rm tors}$ unless Gap~15 closes.
  \item \textbf{Claims matched to what is shown.} ``Resolves'' becomes ``proposes a
    resolution''. Firewall avoidance, the unitary map, orbit counting, the 45-primary
    partition function, the remnant endpoint, the golden-ratio loop factor, the entropy-gap
    observable and the ringdown assumptions are listed as open Gaps~10--18. Only
    information-carrying remnants are excluded.
  \item \textbf{Ringdown prediction restated.} The nine sidebands are unresolved (0.094
    line widths at every mass); the prediction is a shortening of the damping time, given
    by remnant spin and fit start time in Table~\ref{tab:ringdown_spin} (exact Kerr
    frequencies).
  \item \textbf{Observational sections rewritten from the analysis scripts.} The GWOSC
    result is a sensitivity floor ($1.6\times10^{-16}~\mathrm{m\,s^{-2}}$, for a
    ${\sim}100$~Hz component only). The GRACE run of 2026-04-26 is described as done: its
    zero result follows from its method, and $4\times10^{-9}~\mathrm{m\,s^{-2}}$ is the
    1~cm water scale. A synthetic histogram is removed from Fig.~5; the run's own output
    is Fig.~6.
  \item \textbf{Corrections.} Torsion cell area $8.79\,\ell_{\rm Pl}^2$; sideband weights;
    loop bound; torsion classes in $H^3$ (Dijkgraaf--Witten); modular invariance as a
    consistency condition; imaginary $\tau$; quantum dimension 3; charges modulo $2\pi$;
    footer DOI set to the concept DOI; references corrected and added.
  \item The full revision trail (r1--r9), audits, registration files and analysis scripts
    are included in the Zenodo record.
\end{enumerate}

""" + s[j:]

# ---- §7: point to the test, then add the X24si subsection at the end of §7
R(r"""the inspiral. A shortening of 10--18\% may already be within reach of combined
ringdown tests of general relativity on existing LIGO--Virgo--KAGRA catalogues; such a
comparison, set up in advance and run once, is proposed here, not claimed.""",
  r"""the inspiral. Section~\ref{sec:x24si_test} tests it against published
LIGO--Virgo--KAGRA results.""")
R(r"""quality factor, testable at Einstein Telescope and Cosmic Explorer on the
$\sim 2035$ timeline.""", r"""quality factor. Under the assumptions of Gaps~17 and~18 it is already
disfavoured by GWTC-5.0 (Section~\ref{sec:x24si_test}).""")
R(r"""a kinematical consequence of the soft-hair sectors of Section~\ref{sec:hair}
and does not require it.
""", r"""a kinematical consequence of the soft-hair sectors of Section~\ref{sec:hair}
and does not require it.

\subsection{Test against published data by the X24si method}
\label{sec:x24si_test}

The damping-time prediction was tested against published LIGO--Virgo--KAGRA results
with the X24si method~\cite{BresslerX24si2026}, a recursive human-in-the-loop protocol
in which each step is fixed before the next can be seen:
\begin{enumerate}[leftmargin=*, label=\arabic*.]
  \item \textbf{Claim, pinned.} $\delta\hat\tau_{220} \equiv \tau_{\rm fit}/\tau_{\rm GR} - 1
    = -0.095$ for remnant spin 0.69 and a fit from the peak, with a band of $-0.126$ to
    $-0.070$ for spins 0.50--0.80 (Table~\ref{tab:ringdown_spin}), as a deviation common to
    all events. Pinned to revision r8 of this paper and to a frozen decision script,
    identified by its SHA-256 hash; each input is labelled as computed or read from the
    literature.
  \item \textbf{Criteria first.} Before any damping-time result was read (the sources
    were chosen from titles alone), the registration fixed the source order (GWTC-5.0,
    then GWTC-4.0 remnant tests, then GWTC-3); the primary analysis (a common-deviation
    combination of an inspiral--merger--ringdown analysis, mapped to a fit from the peak,
    which is the mapping most favourable to the prediction); four outcomes (EXCLUDED if the
    whole band lies outside the 90\% credible interval; DISFAVORED; CONSISTENT, NOT
    DISCRIMINATING; FAVORED OVER GR); and what each outcome would mean for this paper.
  \item \textbf{Outside clock.} The registration was committed and pushed to GitHub
    (commit \texttt{76d92c7}, 16:06~UTC, 18 November 2026) before the source was opened.
    The transcribed numbers were committed (\texttt{d590909}) before the script ran.
  \item \textbf{Instrument, run once.} The frozen script compared the transcribed
    intervals with the registered prediction, once. Failures stand.
  \item \textbf{Human decision.} The author decided how this paper reports the outcome;
    the decision is recorded as a decision, not as evidence.
\end{enumerate}

\noindent\textbf{Result.} For the pSEOBNRv5PHM analysis with posteriors multiplied
across all events, GWTC-5.0 reports $\delta\hat\tau_{220} = 0.07^{+0.06}_{-0.05}$ at
90\% credibility~\cite{GWTC5TGR}. The whole predicted band lies below this interval:
\textbf{EXCLUDED}. The five secondary combinations in the source (the hierarchical mean
and population, the five highest-SNR events with and without GW250114, and all events
without GW250114) are also excluded. The closest is the five highest-SNR subset,
$0.02 \pm 0.08$, whose lower bound of $-0.06$ lies just above the band's edge. Where the
data depart from GR, the damping time is longer, not shorter. Under the assumptions of
Gaps~17 and~18 the ringdown prediction is therefore disfavoured by published data. The
LIGO--Virgo--KAGRA waveform model is not the TMRB waveform, so the mapping is approximate;
it was fixed in advance as the one most favourable to the prediction. The registration,
transcribed input, frozen script, output and result record are included in the Zenodo
record.
""")

# ---- abstract, table, conclusion, gaps
R(r"""component near 100~Hz, which the prediction does not contain.""",
  r"""component near 100~Hz, which the prediction does not contain. The ringdown
prediction was tested against published LIGO--Virgo--KAGRA data by the X24si method
(registered with an outside clock before any result was read, and run once): GWTC-5.0
gives $\delta\hat\tau_{220} = 0.07^{+0.06}_{-0.05}$, which excludes the predicted
shortening, so under its stated assumptions that prediction is disfavoured.""")
R(r"""    (Section~\ref{sec:fluid_gravity}, Figure~\ref{fig:chladni})
  & Einstein Telescope, Cosmic Explorer
  & $\sim$2035 \\""", r"""    (Section~\ref{sec:fluid_gravity}, Figure~\ref{fig:chladni})
  & Tested on GWTC-5.0~\cite{GWTC5TGR} (X24si, Section~\ref{sec:x24si_test})
  & Excluded (2026) \\""")
R(r"""resolve (0.094 line widths at any mass); their signature is a mass-independent
shortening of the ringdown damping time by about 10--18\% for typical remnants
(Table~\ref{tab:ringdown_spin}), the framework's most
direct gravitational-wave test at Einstein Telescope and Cosmic Explorer.""",
  r"""resolve (0.094 line widths at any mass). Their predicted signature, a
mass-independent shortening of the ringdown damping time by about 10--18\% for typical
remnants (Table~\ref{tab:ringdown_spin}), was tested by the X24si method against
GWTC-5.0 and is excluded under the assumptions of Gaps~17 and~18
(Section~\ref{sec:x24si_test}).""")
R(r"""$\Delta f_{\rm tors}$; the potential as written varies only with angle.""",
  r"""$\Delta f_{\rm tors}$; the potential as written varies only with angle. The
    prediction made under this assumption is disfavoured by the test of
    Section~\ref{sec:x24si_test}.""")
R(r"""(Table~\ref{tab:ringdown_spin}). Unequal sideband damping and overtones are open.""",
  r"""(Table~\ref{tab:ringdown_spin}). Unequal sideband damping and overtones are open.
    The prediction made under this assumption is disfavoured by the test of
    Section~\ref{sec:x24si_test}.""")
R(r"""\bibitem{BresslerSurvey2026}""", r"""\bibitem{BresslerX24si2026}
  G.~Bressler,
  \textit{X24si},
  \href{https://x24si.com}{https://x24si.com} (2026).

\bibitem{GWTC5TGR}
  A.~G.~Abac et al.\ (LIGO Scientific, Virgo and KAGRA Collaborations),
  \textit{GWTC-5.0: Tests of General Relativity},
  arXiv:2607.19293 (2026).
  \href{https://arxiv.org/abs/2607.19293}{arXiv:2607.19293}

\bibitem{BresslerSurvey2026}""")
open(dst, "w").write(s); print("ok")
