"""fig5_constraints.py — TMRB BH Soft Hair: current observational constraints.

v4: one panel. Log-scale sensitivity ladder of operational/planned/proposed gravity
missions, with the TMRB Gaia-calibrated prediction, the GWOSC O3a sensitivity floor
(applies to a ~100 Hz component only) and the GRACE scale (gravity of 1 cm of water).
The v3 right panel (a seeded random z histogram) is removed; the real Apr 26 GRACE
run is shown as its own figure (fig6).

House style: navy/gold/cyan, DejaVu Sans, 300 DPI. Author: G. Bressler.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# --- House style -------------------------------------------------------------
NAVY  = '#0D1B2A'
GOLD  = '#C8A84B'
CYAN  = '#00B4D8'
INK   = '#142840'
MUTED = '#8AA0B8'
LGRAY = '#D5DCE4'
PALE_CYAN = '#9EE0EF'

mpl.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 9.5,
    'axes.titlesize': 10.5, 'axes.labelsize': 9.5,
    'axes.edgecolor': INK, 'axes.linewidth': 0.9,
    'axes.labelcolor': INK, 'axes.titlecolor': INK,
    'xtick.color': INK, 'ytick.color': INK,
    'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5,
    'legend.fontsize': 8.5, 'savefig.dpi': 300,
    'mathtext.fontset': 'dejavusans',
})

# --- Mission sensitivity ladder (m/s^2) -------------------------------------
missions = [
    ('GRACE-FO (operational)',     1e-11,   'op'),
    ('GRACE-C (2028+)',            5e-12,   'plan'),
    ('ESA NGGM (2030s)',           1e-12,   'plan'),
    ('AEDGE (proposed)',           1e-15,   'prop'),
    ('MAQRO (proposed)',           5e-17,   'prop'),
    ('Stanford QGG (proposed)',    1e-17,   'prop'),
    ('TMRB requirement',           1e-17,   'req'),
]
labels    = [m[0] for m in missions]
sens      = np.array([m[1] for m in missions])
kinds     = [m[2] for m in missions]

color_map = {'op': MUTED, 'plan': CYAN, 'prop': GOLD, 'req': NAVY}
colors    = [color_map[k] for k in kinds]

# TMRB Gaia-calibrated prediction
TMRB_PRED = 6.3e-15
GWOSC_UL  = 1.6e-16
GRACE_UL  = 4.0e-9

fig, axL = plt.subplots(1, 1, figsize=(7.2, 4.4))

# =============================================================================
# LEFT — sensitivity ladder
# =============================================================================
y = np.arange(len(missions))[::-1]   # top = most sensitive
bars = axL.barh(y, sens, color=colors, edgecolor=NAVY, linewidth=0.9,
                height=0.62, log=True)

# Value labels on bars
for yi, s, k in zip(y, sens, kinds):
    axL.text(s*1.6, yi, f'{s:.0e}', va='center', ha='left',
             fontsize=8, color=NAVY,
             fontweight='bold' if k == 'req' else 'normal')

axL.set_yticks(y)
axL.set_yticklabels(labels, fontsize=8.8)
axL.set_xscale('log')
axL.set_xlim(1e-19, 5e-7)
axL.set_xlabel(r'Sensitivity $\Delta g$  (m s$^{-2}$)')
axL.set_title('Mission sensitivity vs current limits\n'
              r'(TMRB prediction $\Delta g = 6.3\times 10^{-15}$ m s$^{-2}$, gold band)',
              pad=10, fontsize=10.5)
axL.grid(True, axis='x', which='both', alpha=0.35, color=LGRAY)
axL.spines['top'].set_visible(False)
axL.spines['right'].set_visible(False)

# Gaia-calibrated TMRB prediction band — gold vertical band (no inline label, in title)
axL.axvspan(TMRB_PRED*0.7, TMRB_PRED*1.4, color=GOLD, alpha=0.18, zorder=0)
axL.axvline(TMRB_PRED, color=GOLD, linewidth=1.6, linestyle='--', zorder=1)

# Existing 95% CL upper limits — cyan crossbars
axL.axvline(GWOSC_UL, color=CYAN, linewidth=1.4, linestyle=':', zorder=1)
axL.axvline(GRACE_UL, color=CYAN, linewidth=1.4, linestyle=':', zorder=1)

# Place both UL labels in the bottom margin BELOW the bars, well-separated
axL.text(GWOSC_UL, -1.0,
         'GWOSC O3a floor\n'+r'$1.6\!\times\!10^{-16}$ (~100 Hz)',
         color=NAVY, fontsize=7.8, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                   edgecolor=CYAN, linewidth=0.8, alpha=0.95))

axL.text(GRACE_UL, -1.0,
         'GRACE scale\n'+r'$4\!\times\!10^{-9}$ (1 cm w.e.)',
         color=NAVY, fontsize=7.8, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                   edgecolor=CYAN, linewidth=0.8, alpha=0.95))

axL.set_ylim(-1.7, len(missions)-0.4)

# Legend
from matplotlib.lines import Line2D
leg_handles = [
    Line2D([0],[0], color=MUTED, lw=8, label='Operational'),
    Line2D([0],[0], color=CYAN,  lw=8, label='Planned'),
    Line2D([0],[0], color=GOLD,  lw=8, label='Proposed'),
    Line2D([0],[0], color=NAVY,  lw=8, label='TMRB requirement'),
]
axL.legend(handles=leg_handles, loc='upper center',
           bbox_to_anchor=(0.5, -0.18),
           ncol=4, frameon=True,
           framealpha=0.92, edgecolor=MUTED, fontsize=7.8)

plt.tight_layout()
plt.savefig('fig5_constraints.pdf', dpi=300, bbox_inches='tight')
plt.savefig('fig5_constraints.png', dpi=300, bbox_inches='tight')
print('Wrote fig5_constraints.{pdf,png}')
