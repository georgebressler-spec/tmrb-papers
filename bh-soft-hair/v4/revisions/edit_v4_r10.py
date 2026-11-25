import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
def R(old, new, count=1):
    global s
    n = s.count(old); assert n == count, (n, old[:100]); s = s.replace(old, new)
R(r"""with the X24si method~\cite{BresslerX24si2026}, a recursive human-in-the-loop protocol
in which each step is fixed before the next can be seen:""",
  r"""with the X24si method~\cite{BresslerX24si2026}: human-in-the-loop self-recursive
reasoning. Semi-autonomous synthetic-intelligence (SI) participants do the work; the
human makes the decisions. Each turn ends in something learned or a named stuck point,
and that outcome becomes the next turn's input. The loop is anchored outside itself, by
instruments and an outside clock, so it can refute its own claims rather than only
confirm them. Here the recursion ran: an audit found the sideband comb unresolved, so
the prediction was restated; an exact Kerr check exposed its dependence on spin; the
resulting table showed that existing data could already test it; and the test below,
whose outcome now stands in Gaps~17 and~18. Within the test, each step was fixed before
the next could be seen:""")
R(r"""\item \textbf{Ringdown prediction tested against published data and disfavoured, by
    the X24si method.}""", r"""\item \textbf{Ringdown prediction tested against published data and disfavoured, by
    the X24si method} (human-in-the-loop self-recursive reasoning, anchored by an outside
    clock and outside data).""")
R(r"""\textit{(vii)}~The full revision trail (r1--r9)""", r"""\textit{(vii)}~The full revision trail (r1--r10)""", 0) if False else None
R(r"""  \item The full revision trail (r1--r9), audits,""", r"""  \item The full revision trail (r1--r10), audits,""")
open(dst, "w").write(s); print("ok")
