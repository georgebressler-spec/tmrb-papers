"""fig1_horizon_soft_hair.py — Z9 torsion-hair lattice on event horizon.

Recreates Figure 1 from the BH Soft Hair paper: nine-node lattice on a circle
representing the bifurcation 2-sphere, with 3-6-9 subgroup nodes (n=0,3,6)
enlarged and starred, dashed BMS spokes to the central singularity, and
weight annotation dim H_hair = 9^{A/(4 l_Pl^2)}.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

NAVY  = '#0D1B2A'
GOLD  = '#C8A84B'
CYAN  = '#00B4D8'
PALE  = '#9EE0EF'
INK   = '#142840'
MUTED = '#8AA0B8'

import matplotlib as mpl
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'mathtext.fontset': 'dejavusans', 'savefig.dpi': 300})

fig, ax = plt.subplots(figsize=(6.6, 6.6))
ax.set_facecolor(NAVY)
fig.patch.set_facecolor('white')

R = 1.0
# Event horizon ring — cyan halo
for w, alp in [(0.06, 0.18), (0.04, 0.30), (0.025, 0.50)]:
    c = Circle((0,0), R, fill=False, edgecolor=CYAN, linewidth=20*w, alpha=alp)
    ax.add_patch(c)
ax.add_patch(Circle((0,0), R, fill=False, edgecolor=CYAN, linewidth=2.0))

# Singularity in the centre
ax.plot(0, 0, marker='x', color='white', markersize=12, mew=2.5)
ax.text(0, -0.12, 'singularity', ha='center', va='top', color='white',
        fontsize=8.5, style='italic')

# Nine torsion nodes
N = 9
angles = 2*np.pi*np.arange(N)/N + np.pi/2  # n=0 at top? actually start from right.
# The figure shows n=0 at lower-right; replicate with theta_0 = 0 rad
angles = 2*np.pi*np.arange(N)/N
for n, th in enumerate(angles):
    x, y = R*np.cos(th), R*np.sin(th)
    is_369 = n in (0, 3, 6)
    color = CYAN if is_369 else GOLD
    size  = 200 if is_369 else 120
    edge  = NAVY
    # Dashed spoke from origin
    ax.plot([0, 0.94*x], [0, 0.94*y], color=GOLD, linestyle='--',
            linewidth=0.8, alpha=0.55, zorder=1)
    ax.scatter([x], [y], s=size, c=color, edgecolors=edge,
               linewidths=1.4, zorder=4)
    if is_369:
        # Star marker overlay
        ax.scatter([x], [y], s=420, marker='*', c=CYAN, edgecolors='white',
                   linewidths=1.2, zorder=5, alpha=0.95)
    # Label theta_n
    lx, ly = 1.18*x, 1.18*y
    suffix = r'$\,\star$' if is_369 else ''
    ax.text(lx, ly, rf'$\theta_{{{n}}}$' + suffix, ha='center', va='center',
            color='white', fontsize=11, fontweight='bold' if is_369 else 'normal')

# Title
ax.text(0, 1.50, r'$\mathbb{Z}_9$ Torsion Hair Lattice on Event Horizon',
        ha='center', va='center', color='white',
        fontsize=12.5, fontweight='bold')

# Hilbert space dimension
ax.text(0, -1.42, r'$\dim\,\mathcal{H}_{\rm hair} = 9^{N_{\rm cell}} = e^{S_{\rm BH}}$',
        ha='center', va='center', color=CYAN, fontsize=12)

# Legend box (bottom right)
leg_handles = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=CYAN,
           markersize=11, markeredgecolor=NAVY, label='3-6-9 subgroup nodes'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=GOLD,
           markersize=10, markeredgecolor=NAVY, label='Standard torsion nodes'),
]
leg = ax.legend(handles=leg_handles, loc='lower right',
                bbox_to_anchor=(1.32, -0.05),
                facecolor=NAVY, edgecolor=GOLD, framealpha=0.95,
                fontsize=8.5, labelcolor='white')

ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.55, 1.55)
ax.set_aspect('equal')
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)

plt.tight_layout()
plt.savefig('fig1_horizon_soft_hair.pdf', dpi=300, bbox_inches='tight',
            facecolor=NAVY)
plt.savefig('fig1_horizon_soft_hair.png', dpi=300, bbox_inches='tight',
            facecolor=NAVY)
print('Wrote fig1_horizon_soft_hair.{pdf,png}')
