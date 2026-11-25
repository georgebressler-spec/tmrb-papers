"""fig3_golden_ratio_loop.py — phi^-N* exponential UV regulation."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

NAVY = '#0D1B2A'; GOLD = '#C8A84B'; CYAN = '#00B4D8'
INK = '#142840'; LGRAY = '#D5DCE4'; MUTED = '#8AA0B8'
GREEN = '#A8C45A'

mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.edgecolor': INK, 'axes.labelcolor': INK,
                     'axes.titlecolor': INK, 'xtick.color': INK,
                     'ytick.color': INK, 'mathtext.fontset': 'dejavusans',
                     'savefig.dpi': 300})

phi = (1+np.sqrt(5))/2  # 1.6180...
kappa_prop = 0.48

fig, (axL, axR) = plt.subplots(1, 2, figsize=(10, 4))

# Left: loop correction factor vs branching depth
N = np.linspace(0, 20, 300)
G4_pi_lnw = 0.20   # representative G4/pi * ln(w/mu) ~ 0.2
unreg = 1.0 + G4_pi_lnw*np.ones_like(N)
reg = 1.0 + G4_pi_lnw * phi**(-N)
axL.plot(N, unreg, color=GOLD, linestyle='--', linewidth=1.8,
         label=r'Unregulated ($\varphi^{-N_*}\to 1$)')
axL.plot(N, reg, color=CYAN, linewidth=2.0,
         label=r'TMRB regulated $\varphi^{-N_*}$')
axL.fill_between(N, np.ones_like(N), reg, where=(reg<unreg),
                 color=GREEN, alpha=0.20, label='UV suppression')
axL.set_xlabel(r'Branching depth $N_*$')
axL.set_ylabel(r'Loop correction factor')
axL.set_title(r'$\varphi^{-N_*}$ Exponential UV Regulation')
axL.set_xlim(0, 20); axL.set_ylim(0.99, 1.22)
axL.grid(True, alpha=0.35, color=LGRAY)
axL.legend(loc='upper right', fontsize=8.5)
axL.spines['top'].set_visible(False); axL.spines['right'].set_visible(False)

# Right: phi^-N vs e^-kappa_prop N, semi-log
N2 = np.linspace(0, 25, 300)
y_phi = phi**(-N2)
y_exp = np.exp(-kappa_prop * N2)
axR.semilogy(N2, y_phi, color=CYAN, linewidth=2.0, label=r'$\varphi^{-N}$')
axR.semilogy(N2, y_exp, color=GOLD, linestyle='--', linewidth=1.8,
             label=rf'$e^{{-\kappa_{{\rm prop}}N}},\ \kappa_{{\rm prop}}={kappa_prop}$')
axR.set_xlabel(r'$N$')
axR.set_ylabel(r'Suppression factor')
axR.set_title(r'UV Cutoff: $\varphi^{-N}$ vs Exponential')
axR.set_xlim(0, 25); axR.set_ylim(1e-5, 2)
axR.grid(True, which='both', alpha=0.35, color=LGRAY)
axR.legend(loc='upper right', fontsize=8.5)
axR.spines['top'].set_visible(False); axR.spines['right'].set_visible(False)
axR.text(0.97, 0.74, rf'$\varphi = {phi:.4f}$', transform=axR.transAxes,
         ha='right', fontsize=9, color=NAVY,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor=GOLD, linewidth=0.8))

plt.tight_layout()
plt.savefig('fig3_golden_ratio_loop.pdf', dpi=300, bbox_inches='tight')
plt.savefig('fig3_golden_ratio_loop.png', dpi=300, bbox_inches='tight')
print('Wrote fig3_golden_ratio_loop.{pdf,png}')
