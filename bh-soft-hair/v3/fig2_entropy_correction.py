"""fig2_entropy_correction.py — Bekenstein-Hawking vs TMRB entropy."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

NAVY = '#0D1B2A'; GOLD = '#C8A84B'; CYAN = '#00B4D8'
INK = '#142840'; LGRAY = '#D5DCE4'; MUTED = '#8AA0B8'

mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.edgecolor': INK, 'axes.labelcolor': INK,
                     'axes.titlecolor': INK, 'xtick.color': INK,
                     'ytick.color': INK, 'mathtext.fontset': 'dejavusans',
                     'savefig.dpi': 300})

dS_tors = 9*np.log(9) + np.log(2)   # 20.468

fig, (axL, axR) = plt.subplots(1, 2, figsize=(10, 4))

# Left: linear S vs A
A = np.linspace(0, 200, 400)
S_BH = A/4.0
S_TMRB = A/4.0 + dS_tors
axL.plot(A, S_BH, color=GOLD, linestyle='--', linewidth=1.8, label=r'$S_{\rm BH}=A/4G_4$')
axL.plot(A, S_TMRB, color=CYAN, linewidth=1.8, label=r'$S_{\rm TMRB}=A/4G_4+\Delta S_{\rm tors}$')
axL.fill_between(A, S_BH, S_TMRB, color=CYAN, alpha=0.18)
axL.axhline(dS_tors, color=NAVY, linewidth=0.7, linestyle=':')
axL.text(2, dS_tors+1.5, r'$\Delta S_{\rm tors} \approx 20.47$',
         color=NAVY, fontsize=9)
axL.set_xlabel(r'Area $A$ (units $4G_4$)')
axL.set_ylabel(r'Entropy $S$')
axL.set_title('Entropy Correction')
axL.set_xlim(0, 200); axL.set_ylim(0, 75)
axL.grid(True, alpha=0.35, color=LGRAY)
axL.legend(loc='upper left', fontsize=8.5,
           title=rf'$\Delta S_{{\rm tors}} = 9\ln 9 + \ln 2 \approx {dS_tors:.3f}$',
           title_fontsize=8.5)
axL.spines['top'].set_visible(False); axL.spines['right'].set_visible(False)

# Right: fractional correction (log-log)
A2 = np.logspace(1, 6, 400)
frac = dS_tors/(A2/4.0)
axR.loglog(A2, frac, color=CYAN, linewidth=1.8, label=r'$\delta S/(A/4G_4)$')
axR.axhline(0.01, color=GOLD, linestyle='--', linewidth=1.0, label='1% threshold')
axR.axhline(0.001, color=GOLD, linestyle=':', linewidth=1.0, label='0.1% threshold')
axR.set_xlabel(r'Area $A$ (units $4G_4$)')
axR.set_ylabel(r'Fractional correction $\delta S/S_{\rm BH}$')
axR.set_title('Fractional Torsion Correction')
axR.set_xlim(1e1, 1e6); axR.set_ylim(1e-4, 1e1)
axR.grid(True, which='both', alpha=0.35, color=LGRAY)
axR.legend(loc='upper right', fontsize=8.5)
axR.spines['top'].set_visible(False); axR.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('fig2_entropy_correction.pdf', dpi=300, bbox_inches='tight')
plt.savefig('fig2_entropy_correction.png', dpi=300, bbox_inches='tight')
print('Wrote fig2_entropy_correction.{pdf,png}')
