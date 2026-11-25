# TMRB Soft-Hair Resolution of the Black-Hole Information Paradox

Paper 10 of the PTRH series. Concept DOI: [10.5281/zenodo.19981840](https://doi.org/10.5281/zenodo.19981840).

| Folder | What it is |
|---|---|
| `v3/` | The published v3, as downloaded from Zenodo record 20331456 (May 21 2026): LaTeX source, PDF, and figure scripts with their outputs. |
| `v4/` | v4 (revision r11, Nov 19 2026), not yet on Zenodo: `bh_soft_hair_v4.tex` and `.pdf`. |
| `v4/figures/` | Figures 1–6. Figures 1, 2, 4 and 5 were regenerated from the v3 scripts, as patched in v4. Fig. 6 is the unchanged output image of the 2026-04-26 GRACE run. |
| `v4/analysis/ringdown/` | `ringdown_signature.py` and `kerr_spin_table.py` (both cited in the paper, §7), and an independent cross-check, `verify_ringdown_independent.py`, each with its output. |
| `v4/analysis/gwosc/` | The LIGO/GWOSC sensitivity-floor script and its saved result (`results_gwosc_o3a.json`). |
| `v4/analysis/grace/` | GRACE material. See the note below. |
| `v4/audits/` | Audits 2–4 of v4 and the Nov 18 GRACE/LIGO/Sen check. |
| `v4/prereg/` | The X24si registration, transcribed input, frozen script, output and result of the LVK ringdown test (§7.1). |
| `v4/review/` | The X24si review packet for the Grok team (pinned hashes, criteria written first) and the review log. |
| `v4/revisions/` | The diffs v3 → r1 → … → r11, and the edit scripts that made each revision. |

## GRACE material (read before reusing)
- `TMRB_GRACE_search_results_2026-04-26.{png,pdf}` is the output of the real run on `GRCTellus.JPL.200204_202602.GLO.RL06.3M.MSCNv04CRI.nc`. The NetCDF is 45 MB and is kept on Drive, not here.
- `TMRB_GRACE_torsion_search_2026-04-27.py` is the closest saved version of the script used for that run. It removes each series' fitted mean before computing the anomaly and z, so both are zero by construction (v4 §8.1).
- `TMRB_GRACE_torsion_search_2026-05-02.py` is a later version. With no data file given, it runs an offline demo that draws seeded random numbers.
- `results_grace_45coords_DEMO_OUTPUT.csv` is that demo's output, reproduced bit for bit. **It is not data.** It is kept only as a record of what v3 printed.

## Rebuilding the v4 PDF
The source expects the figure files next to it: copy `figures/*` beside `bh_soft_hair_v4.tex`, then run `pdflatex` twice. The packages are TeX Live's `latex-recommended`, `latex-extra`, `fonts-recommended` and `science`.
