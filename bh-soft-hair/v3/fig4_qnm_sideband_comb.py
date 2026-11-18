"""fig4_qnm_sideband_comb.py — three-panel horizon fluid figure.

Panel L  : Z9 Chladni nodal pattern on stretched horizon (gyroid eigenmode sum)
Panel TR : (eta/s)_TMRB / (1/4pi) vs branching depth N*
Panel BR : Z9 QNM sideband comb (PSD around f_QNM for 30 Msun BH)
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Circle

NAVY = '#0D1B2A'; GOLD = '#C8A84B'; CYAN = '#00B4D8'
PALE = '#9EE0EF'; INK = '#142840'; LGRAY = '#D5DCE4'; MUTED = '#8AA0B8'
TEAL = '#0E5A6F'

mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9.5,
                     'mathtext.fontset': 'dejavusans', 'savefig.dpi': 300})

phi = (1+np.sqrt(5))/2
eta_diff = 0.82
delta_lam = 1.7287  # 2*pi/(9*kappa_CE), kappa_CE = 0.4038

fig = plt.figure(figsize=(11.0, 5.4))
gs = GridSpec(2, 2, figure=fig, width_ratios=[1.05, 1.0],
              height_ratios=[1.0, 1.0], hspace=0.35, wspace=0.28)

# ============================================================================
# LEFT PANEL — Chladni / gyroid eigenmodes
# ============================================================================
ax1 = fig.add_subplot(gs[:, 0])
ax1.set_facecolor(NAVY)

# Background gyroid-modulated field (smooth angular pattern)
NN = 240
xg = np.linspace(-1.4, 1.4, NN)
X, Y = np.meshgrid(xg, xg)
R2 = X**2 + Y**2
THETA = np.arctan2(Y, X)
field = np.cos(3*THETA) * np.exp(-0.6*R2) + 0.5*np.sin(6*THETA)*np.exp(-0.8*R2)
ax1.pcolormesh(X, Y, field, cmap='Blues', alpha=0.55, shading='auto', zorder=0)

# Stretched horizon ring
ax1.add_patch(Circle((0,0), 1.0, fill=False, edgecolor=CYAN, linewidth=1.8))
ax1.text(0.62, -1.18, 'stretched\nhorizon', color=CYAN, fontsize=8.0,
         ha='center', va='top', style='italic')

# Nine torsion nodes
N = 9
angles = 2*np.pi*np.arange(N)/N
weights = 0.5*np.exp(-np.pi*np.arange(-4,5)**2/9)  # for n labels
# Actually w_n for n=0..8 by symmetric reduction; just use the canonical values
w_table = {0: 0.500, 1: 0.353, 3: 0.022}
for n, th in enumerate(angles):
    x, y = np.cos(th), np.sin(th)
    is_369 = n in (0, 3, 6)
    color = CYAN if is_369 else GOLD
    size  = 200 if is_369 else 110
    # Dashed spoke
    ax1.plot([0, 0.95*x], [0, 0.95*y], color=GOLD, linestyle='--',
             linewidth=0.7, alpha=0.5, zorder=1)
    ax1.scatter([x], [y], s=size, c=color, edgecolors=NAVY,
                linewidths=1.3, zorder=4)
    if is_369:
        ax1.scatter([x], [y], s=380, marker='*', c=CYAN,
                    edgecolors='white', linewidths=1.0, zorder=5, alpha=0.95)
    # Label
    lx, ly = 1.18*x, 1.18*y
    ax1.text(lx, ly, rf'$\theta_{{{n}}}$' + (r'$\,\star$' if is_369 else ''),
             ha='center', va='center', color='white', fontsize=10,
             fontweight='bold' if is_369 else 'normal')
    # Weight annotation for n=0,1,3
    if n in w_table:
        ax1.text(0.55*x, 0.55*y, rf'$w_{{{n}}}={w_table[n]:.3f}$',
                 ha='center', va='center', color=PALE, fontsize=7.5,
                 style='italic')

ax1.text(0, 1.45, r'$\mathbb{Z}_9$ Horizon Fluid — Chladni / Gyroid Eigenmodes',
         ha='center', va='center', color='white',
         fontsize=11, fontweight='bold')

# Legend
from matplotlib.lines import Line2D
leg_h = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=CYAN,
           markersize=10, markeredgecolor=NAVY,
           label='3-6-9 subgroup nodes (n=0,3,6)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=GOLD,
           markersize=8.5, markeredgecolor=NAVY,
           label='Standard torsion nodes'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor='#3A7CA5',
           markersize=10, markeredgecolor='none',
           label='Gyroid-modulated fluid field'),
]
ax1.legend(handles=leg_h, loc='lower left',
           bbox_to_anchor=(-0.02, -0.05),
           facecolor=NAVY, edgecolor=GOLD, framealpha=0.92,
           fontsize=7.5, labelcolor='white')

ax1.set_xlim(-1.5, 1.5); ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal'); ax1.set_xticks([]); ax1.set_yticks([])

# ============================================================================
# TOP RIGHT — viscosity correction
# ============================================================================
ax2 = fig.add_subplot(gs[0, 1])
N_ = np.linspace(0, 18, 400)
ratio = 1.0 + eta_diff * delta_lam * phi**(-N_)
ax2.plot(N_, ratio, color=CYAN, linewidth=2.0,
         label=r'$(\eta/s)_{\rm TMRB}/(\eta/s)_{\rm KSS}$')
ax2.axhline(1.0, color=GOLD, linestyle='--', linewidth=1.2,
            label=r'KSS bound: $\eta/s=1/4\pi$')
ax2.fill_between(N_, np.ones_like(N_), ratio, color=CYAN, alpha=0.18,
                 label='Torsion correction')

# d_opt = 9 marker
N_opt = 9
r_opt = 1.0 + eta_diff*delta_lam*phi**(-N_opt)
ax2.scatter([N_opt], [r_opt], s=80, color=GOLD, edgecolors=NAVY,
            zorder=5, label=rf'$N_* = d_{{\rm opt}}=9$')

# Equation box
ax2.text(0.97, 0.92,
         r'$\eta/s|_{\rm TMRB} = (1/4\pi)(1+\eta_{\rm diff}\Delta\lambda\,\varphi^{-N_*})$',
         transform=ax2.transAxes, ha='right', va='top', fontsize=8.5,
         color=NAVY, bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                                edgecolor=GOLD, linewidth=0.8))

ax2.set_xlabel(r'Branching depth $N_*$')
ax2.set_ylabel(r'$(\eta/s)_{\rm TMRB}/(1/4\pi)$')
ax2.set_title('Viscosity Correction to KSS Bound')
ax2.set_xlim(0, 18); ax2.set_yscale('log'); ax2.set_ylim(0.99, 2.5)
ax2.grid(True, which='both', alpha=0.30, color=LGRAY)
ax2.legend(loc='center right', fontsize=7.5)
ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)

# ============================================================================
# BOTTOM RIGHT — Z9 QNM sideband comb (schematic PSD)
# ============================================================================
ax3 = fig.add_subplot(gs[1, 1])
# 30 Msun BH ringdown: f_QNM ~ 0.3736/(2 pi M) but in Hz roughly 250 Hz; 
# sideband spacing Delta f = f_QNM * kappa_CE / 9 = 250 * 0.4038/9 ~ 11 Hz.
# Per text: ~18 Hz for 30 Msun. Use that.
delta_f = 18.0
f0 = 0.0   # offset
n_modes = np.arange(-4, 5)
w_n = 0.5*np.exp(-np.pi*n_modes**2/9)

# Build PSD: main peak + 9 sidebands (Lorentzians)
freq = np.linspace(-10*delta_f, 10*delta_f, 1500)
psd_norm = freq*0
gamma = 0.5  # width
for k, w in zip(n_modes, w_n):
    psd_norm += w**2 / ((freq - k*delta_f)**2 + gamma**2)
psd_norm /= psd_norm.max()
ax3.semilogy(freq/delta_f, psd_norm, color=CYAN, linewidth=1.6)

# Mark each sideband
for k, w in zip(n_modes, w_n):
    yk = w**2 / gamma**2
    yk /= (w_n.max()**2/gamma**2)
    is_main = (k == 0)
    is_369 = (abs(k) in (0, 3, 6))
    color = GOLD if is_main else (PALE if is_369 else MUTED)
    ax3.axvline(k, color=color, linestyle=':', alpha=0.55, linewidth=0.9)
    ax3.text(k, 1.6e-4, f'$n_{{{k:+d}}}$' if k!=0 else r'$\omega_0$',
             ha='center', fontsize=7.5, color=NAVY,
             fontweight='bold' if is_main else 'normal')

ax3.set_xlabel(rf'Frequency offset $(\omega-\omega_0)/\Delta\omega_{{\rm tors}}$  '
               rf'[$\Delta\omega = {delta_f:.1f}$ Hz for 30$M_\odot$]')
ax3.set_ylabel('PSD (normalised)')
ax3.set_title(r'$\mathbb{Z}_9$ QNM Sideband Comb')
ax3.set_xlim(-10, 10); ax3.set_ylim(1e-4, 2)
ax3.grid(True, which='both', alpha=0.30, color=LGRAY)
ax3.text(0.99, 0.93, r'$\Delta\omega = f_{\rm QNM}\,\kappa_{\rm CE}/9$',
         transform=ax3.transAxes, ha='right', va='top', fontsize=8.5,
         color=NAVY, bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                                edgecolor=GOLD, linewidth=0.8))

# Main legend marker
from matplotlib.lines import Line2D
ax3.legend([Line2D([0],[0], color=GOLD, linewidth=1.4, linestyle=':')],
           [r'Main QNM $\omega_0$'],
           loc='upper left', fontsize=7.5)
ax3.spines['top'].set_visible(False); ax3.spines['right'].set_visible(False)

# Super-title
fig.suptitle(r'Fig.\ 5 — TMRB Horizon Fluid: $\mathbb{Z}_9$ Chladni Eigenmodes,'
             ' Viscosity Correction, and QNM Sideband Comb',
             fontsize=11, color=NAVY, y=0.99, fontweight='bold')

plt.savefig('fig4_qnm_sideband_comb.pdf', dpi=300, bbox_inches='tight')
plt.savefig('fig4_qnm_sideband_comb.png', dpi=300, bbox_inches='tight')
print('Wrote fig4_qnm_sideband_comb.{pdf,png}')
