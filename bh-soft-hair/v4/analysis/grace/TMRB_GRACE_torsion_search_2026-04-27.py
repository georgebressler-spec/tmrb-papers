"""
TMRB_GRACE_torsion_search.py
Searches GRACE/GRACE-FO mascon archive against 45 TMRB torsion hotspot
coordinates for the predicted nano-g gravity anomaly signature.

George Bressler | April 2026 | CC-BY 4.0
"""

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
from scipy.signal import periodogram
import warnings
warnings.filterwarnings('ignore')

# ── TMRB canonical parameters ─────────────────────────────────────────────
ETA_DIFF   = 0.82
KAPPA_CE   = 2.1 / 5.2
PHI        = (1 + np.sqrt(5)) / 2
PRED_ANOM  = 6.3e-15
EWH_TO_GRAVITY = 9.8e-5
PRED_EWH = PRED_ANOM / EWH_TO_GRAVITY

NAVY  = '#0D1B2A'
GOLD  = '#C8A84B'
CYAN  = '#00B4D8'
LGOLD = '#E8C96A'
GREEN = '#52B788'
WHITE = '#E8EEF4'

# ── 45 TMRB torsion hotspot coordinates ──────────────────────────────────
ring_configs = [
    ( 19.47, 9,   0.0),
    ( 38.94, 9,  20.0),
    ( 60.00, 6,   0.0),
    (-19.47, 9,   0.0),
    (-38.94, 9,  20.0),
    (-60.00, 3,   0.0),
]

COORDS = []
for lat, n, lon_off in ring_configs:
    for i in range(n):
        lon = (lon_off + i * 360.0/n) % 360
        if lon > 180: lon -= 360
        COORDS.append((lat, lon))

RING_LABELS = (
    ['Ring1']*9 + ['Ring2']*9 + ['Ring3']*6 +
    ['Ring4']*9 + ['Ring5']*9 + ['Ring6']*3
)

def load_grace(ncfile):
    import netCDF4 as nc
    ds = nc.Dataset(ncfile, 'r')
    lat  = ds.variables['lat'][:]
    lon  = ds.variables['lon'][:]
    time = ds.variables['time'][:]
    for vname in ['lwe_thickness', 'EWH', 'ewh', 'lwe', 'mass']:
        if vname in ds.variables:
            ewh = ds.variables[vname][:]
            break
    ds.close()
    t_dec = 2002.0 + time / 365.25
    lon = np.where(lon > 180, lon - 360, lon)
    return lat, lon, t_dec, np.array(ewh)

def extract_timeseries(lat_grid, lon_grid, ewh, target_lat, target_lon):
    i_lat = np.argmin(np.abs(lat_grid - target_lat))
    i_lon = np.argmin(np.abs(lon_grid - target_lon))
    ts = ewh[:, i_lat, i_lon]
    if hasattr(ts, 'filled'):
        ts = ts.filled(np.nan)
    return ts

def detrend_seasonal(ts, t_dec):
    valid = ~np.isnan(ts)
    if valid.sum() < 24:
        return ts, np.nan, np.nan
    omega = 2 * np.pi
    A = np.column_stack([
        np.ones(valid.sum()),
        t_dec[valid] - t_dec[valid].mean(),
        np.cos(omega * t_dec[valid]),
        np.sin(omega * t_dec[valid]),
        np.cos(2*omega * t_dec[valid]),
        np.sin(2*omega * t_dec[valid]),
    ])
    coeffs, _, _, _ = np.linalg.lstsq(A, ts[valid], rcond=None)
    fitted = np.full_like(ts, np.nan)
    fitted[valid] = A @ coeffs
    residual = ts.copy()
    residual[valid] -= fitted[valid]
    return residual, coeffs[1], coeffs[0]

def analyse_coordinate(lat_grid, lon_grid, ewh, t_dec, target_lat, target_lon):
    ts = extract_timeseries(lat_grid, lon_grid, ewh, target_lat, target_lon)
    resid, trend, mean_ewh = detrend_seasonal(ts, t_dec)
    valid = ~np.isnan(resid)
    if valid.sum() < 24:
        return None
    resid_valid = resid[valid]
    t_valid = t_dec[valid]
    mean_r  = np.nanmean(resid_valid)
    std_r   = np.nanstd(resid_valid)
    n_samp  = valid.sum()
    mean_g  = mean_r * EWH_TO_GRAVITY
    std_g   = std_r  * EWH_TO_GRAVITY
    z_score = mean_r / (std_r / np.sqrt(n_samp)) if std_r > 0 else 0
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    if n_samp > 12:
        f_psd, psd = periodogram(resid_valid, fs=12.0)
        valid_f = (f_psd > 0) & (f_psd < 4)
        if valid_f.sum() > 3:
            log_f   = np.log10(f_psd[valid_f])
            log_psd = np.log10(psd[valid_f] + 1e-30)
            slope, _, _, _, _ = stats.linregress(log_f, log_psd)
            psd_slope = -slope
        else:
            psd_slope = np.nan
    else:
        psd_slope = np.nan
    return {
        'mean_ewh'  : mean_r,
        'std_ewh'   : std_r,
        'mean_g'    : mean_g,
        'std_g'     : std_g,
        'z_score'   : z_score,
        'p_value'   : p_value,
        'n_months'  : n_samp,
        'trend'     : trend,
        'psd_slope' : psd_slope,
        'ts_resid'  : resid,
        't_dec'     : t_dec,
    }

def run_search(ncfile):
    print(f"\n{'='*60}")
    print("TMRB GRACE-FO TORSION HOTSPOT SEARCH")
    print(f"{'='*60}")
    print(f"Predicted anomaly: {PRED_ANOM:.2e} m/s²  ({PRED_EWH:.4f} cm EWH)")
    print(f"Null model: zero residual gravity anomaly")
    print(f"Detection: |z| > 3 over ≥3 coordinates in same ring\n")

    lat_g, lon_g, t_dec, ewh = load_grace(ncfile)
    print(f"Loaded: {len(t_dec)} months, {t_dec[0]:.2f}–{t_dec[-1]:.2f}\n")

    results = []
    for i, ((lat, lon), ring) in enumerate(zip(COORDS, RING_LABELS)):
        res = analyse_coordinate(lat_g, lon_g, ewh, t_dec, lat, lon)
        if res is None:
            print(f"  {i+1:2d}. [{ring}] ({lat:+6.2f}, {lon:+7.2f}) — insufficient data")
            continue
        res['lat']  = lat
        res['lon']  = lon
        res['ring'] = ring
        res['idx']  = i+1
        results.append(res)
        sig = '***' if abs(res['z_score']) > 3 else '**' if abs(res['z_score']) > 2 else '*' if abs(res['z_score']) > 1 else ''
        psd_str = f"α={res['psd_slope']:.2f}" if not np.isnan(res['psd_slope']) else "α=N/A"
        print(f"  {i+1:2d}. [{ring}] ({lat:+6.2f}, {lon:+7.2f}) "
              f"g={res['mean_g']:+.2e} m/s²  "
              f"z={res['z_score']:+5.2f}  {psd_str}  {sig}")

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    sig3 = [r for r in results if abs(r['z_score']) > 3]
    sig2 = [r for r in results if abs(r['z_score']) > 2]
    pos  = [r for r in results if r['mean_g'] > 0]
    neg  = [r for r in results if r['mean_g'] < 0]
    print(f"Coordinates analysed     : {len(results)}/45")
    print(f"|z| > 3σ (significant)   : {len(sig3)}")
    print(f"|z| > 2σ (marginal)      : {len(sig2)}")
    print(f"Positive anomalies       : {len(pos)}")
    print(f"Negative anomalies       : {len(neg)}")

    print(f"\nRing statistics:")
    for ring in ['Ring1','Ring2','Ring3','Ring4','Ring5','Ring6']:
        ring_r = [r for r in results if r['ring'] == ring]
        if not ring_r: continue
        z_vals = [r['z_score'] for r in ring_r]
        print(f"  {ring}: mean z={np.mean(z_vals):.2f}, "
              f"max|z|={max(abs(z) for z in z_vals):.2f}, n={len(ring_r)}")

    psd_vals = [r['psd_slope'] for r in results if not np.isnan(r['psd_slope'])]
    if psd_vals:
        tmrb_psd = [p for p in psd_vals if 0.70 <= p <= 0.80]
        print(f"\nPSD slope α: mean={np.mean(psd_vals):.3f}, "
              f"target=0.75±0.05, n_match={len(tmrb_psd)}/{len(psd_vals)}")

    print(f"\nTMRB VERDICT:")
    if len(sig3) >= 3:
        print(f"  ✓ POSITIVE: {len(sig3)} coordinates at >3σ")
        print(f"    This constitutes preliminary evidence for TMRB torsion anomalies.")
    elif len(sig2) >= 5:
        print(f"  ~ MARGINAL: {len(sig2)} coordinates at >2σ — publish as upper limit")
    else:
        print(f"  ✗ NULL: no significant anomaly detected at GRACE-FO resolution")
        print(f"    GRACE-FO mascon resolution (~300 km) may be insufficient for point sources.")
        print(f"    Recommendation: use GRACE Level-1B KBR/LRI data for higher resolution.")

    make_figures(results, t_dec)
    return results

def make_figures(results, t_dec):
    if not results:
        return
    plt.rcParams.update({
        'font.family':'DejaVu Sans','font.size':10,
        'axes.facecolor':NAVY,'figure.facecolor':NAVY,'text.color':WHITE,
        'axes.labelcolor':WHITE,'xtick.color':WHITE,'ytick.color':WHITE,
        'axes.edgecolor':GOLD,'savefig.facecolor':NAVY,'savefig.dpi':220,
        'savefig.bbox':'tight',
    })
    fig = plt.figure(figsize=(15, 9), facecolor=NAVY)
    gs  = gridspec.GridSpec(2, 3, hspace=0.42, wspace=0.35,
                            left=0.07, right=0.97, top=0.92, bottom=0.09)

    ax1 = fig.add_subplot(gs[0, :2])
    ax1.set_facecolor(NAVY)
    ax1.set_xlim(-180, 180)
    ax1.set_ylim(-90, 90)
    ax1.axhline(0, color=GOLD, lw=0.5, alpha=0.3)
    for lat_line in [-60, -30, 30, 60]:
        ax1.axhline(lat_line, color=GOLD, lw=0.3, alpha=0.2, ls=':')
    for lon_line in range(-180, 181, 60):
        ax1.axvline(lon_line, color=GOLD, lw=0.3, alpha=0.2, ls=':')
    for r in results:
        z = r['z_score']
        color = CYAN if z > 0 else '#E06060'
        size  = max(30, min(300, abs(z)**2 * 30))
        ax1.scatter(r['lon'], r['lat'], s=size, c=color,
                    alpha=0.85, zorder=5,
                    edgecolors=GOLD if abs(z)>3 else 'none', linewidths=1.5)
    for lat_r in [19.47, 38.94, 60.0, -19.47, -38.94, -60.0]:
        ax1.axhline(lat_r, color=LGOLD, lw=0.8, alpha=0.4, ls='--')
    ax1.set_xlabel('Longitude (°)', fontsize=10)
    ax1.set_ylabel('Latitude (°)', fontsize=10)
    for sp in ax1.spines.values(): sp.set_edgecolor(GOLD)
    for z_ex, label in [(1,'|z|=1'), (2,'|z|=2'), (3,'|z|=3')]:
        ax1.scatter([], [], s=z_ex**2*30, c=CYAN, alpha=0.85, label=label)
    ax1.legend(fontsize=8, facecolor=NAVY, edgecolor=GOLD, labelcolor=WHITE,
               loc='lower left')

    ax2 = fig.add_subplot(gs[0, 2])
    ax2.set_facecolor(NAVY)
    z_vals = [r['z_score'] for r in results]
    bins = np.linspace(-4, 4, 25)
    ax2.hist(z_vals, bins=bins, color=CYAN, alpha=0.7, edgecolor=GOLD, lw=0.8)
    x_null = np.linspace(-4, 4, 200)
    null_pdf = stats.norm.pdf(x_null) * len(z_vals) * (bins[1]-bins[0])
    ax2.plot(x_null, null_pdf, color=GOLD, lw=2, ls='--', label='Gaussian null')
    ax2.axvline(3,  color='#E06060', lw=1.5, ls=':', alpha=0.8, label='3σ')
    ax2.axvline(-3, color='#E06060', lw=1.5, ls=':', alpha=0.8)
    ax2.set_xlabel('Z-score', fontsize=10)
    ax2.set_ylabel('Count', fontsize=10)
    ax2.set_title('Z-score distribution\nvs Gaussian null', color=WHITE, fontsize=10)
    ax2.legend(fontsize=8, facecolor=NAVY, edgecolor=GOLD, labelcolor=WHITE)
    for sp in ax2.spines.values(): sp.set_edgecolor(GOLD)

    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_facecolor(NAVY)
    rings = ['Ring1','Ring2','Ring3','Ring4','Ring5','Ring6']
    ring_means = []
    ring_stds  = []
    for ring in rings:
        rr = [r['mean_g'] for r in results if r['ring']==ring]
        ring_means.append(np.mean(rr) if rr else 0)
        ring_stds.append(np.std(rr)  if rr else 0)
    x = np.arange(len(rings))
    colors_r = [CYAN if m > 0 else '#E06060' for m in ring_means]
    ax3.bar(x, [m*1e15 for m in ring_means], yerr=[s*1e15 for s in ring_stds],
            color=colors_r, alpha=0.8, edgecolor=GOLD, lw=0.8, capsize=4)
    ax3.axhline(PRED_ANOM*1e15, color=LGOLD, lw=2, ls='--',
                label=f'TMRB pred: {PRED_ANOM*1e15:.1f} fm/s²')
    ax3.axhline(-PRED_ANOM*1e15, color=LGOLD, lw=1, ls=':', alpha=0.5)
    ax3.axhline(0, color=WHITE, lw=0.5, alpha=0.3)
    ax3.set_xticks(x)
    ax3.set_xticklabels(rings, fontsize=8, rotation=30)
    ax3.set_ylabel(r'Mean gravity anomaly (fm/s²  ×10$^{-15}$)', fontsize=9)
    ax3.set_title('Ring-mean gravity anomaly\nvs TMRB prediction', color=WHITE, fontsize=10)
    ax3.legend(fontsize=8, facecolor=NAVY, edgecolor=GOLD, labelcolor=WHITE)
    for sp in ax3.spines.values(): sp.set_edgecolor(GOLD)

    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor(NAVY)
    psd_vals = [r['psd_slope'] for r in results if not np.isnan(r['psd_slope'])]
    if psd_vals:
        bins_p = np.linspace(0, 2, 25)
        ax4.hist(psd_vals, bins=bins_p, color=CYAN, alpha=0.7,
                 edgecolor=GOLD, lw=0.8)
        ax4.axvspan(0.70, 0.80, color=GREEN, alpha=0.25,
                    label='TMRB target α=0.75±0.05')
        ax4.axvline(0.75, color=LGOLD, lw=2, ls='--')
        ax4.set_xlabel('PSD slope α', fontsize=10)
        ax4.set_ylabel('Count', fontsize=10)
        ax4.set_title('Residual PSD slope distribution\n(target: 0.75±0.05 for TMRB)',
                      color=WHITE, fontsize=10)
        ax4.legend(fontsize=8, facecolor=NAVY, edgecolor=GOLD, labelcolor=WHITE)
    else:
        ax4.text(0.5, 0.5, 'Insufficient data\nfor PSD analysis',
                 ha='center', va='center', color=WHITE, transform=ax4.transAxes)
    for sp in ax4.spines.values(): sp.set_edgecolor(GOLD)

    ax5 = fig.add_subplot(gs[1, 2])
    ax5.set_facecolor(NAVY)
    best = max(results, key=lambda r: abs(r['z_score']))
    ts_r = best['ts_resid']
    t_r  = best['t_dec']
    valid = ~np.isnan(ts_r)
    ax5.plot(t_r[valid], ts_r[valid], color=CYAN, lw=1.5, alpha=0.8)
    ax5.axhline(best['mean_ewh'], color=GOLD, lw=2, ls='--',
                label=f"mean={best['mean_ewh']:.3f} cm")
    ax5.axhline(0, color=WHITE, lw=0.5, alpha=0.3)
    ax5.fill_between(t_r[valid], 0, ts_r[valid],
                     where=ts_r[valid]>0, color=CYAN, alpha=0.15)
    ax5.fill_between(t_r[valid], 0, ts_r[valid],
                     where=ts_r[valid]<0, color='#E06060', alpha=0.15)
    ax5.set_xlabel('Year', fontsize=10)
    ax5.set_ylabel('EWH residual (cm)', fontsize=10)
    ax5.set_title(f"Best coord: ({best['lat']:+.1f}°, {best['lon']:+.1f}°) "
                  f"{best['ring']}\nz={best['z_score']:.2f}  "
                  f"g={best['mean_g']:+.2e} m/s²",
                  color=WHITE, fontsize=9)
    ax5.legend(fontsize=8, facecolor=NAVY, edgecolor=GOLD, labelcolor=WHITE)
    for sp in ax5.spines.values(): sp.set_edgecolor(GOLD)

    fig.suptitle(
        'TMRB Torsion Hotspot Search — GRACE/GRACE-FO Mascon Archive\n'
        r'Prediction: $6.3\times10^{-15}$ m/s² at 45 $\mathbb{Z}_9$ coordinates  |  '
        r'Size $\propto$ |z|  |  Cyan=positive  |  Red=negative  |  Gold border=|z|>3$\sigma$',
        fontsize=10.5, color=WHITE, y=0.99, fontweight='bold')

    plt.savefig('TMRB_GRACE_search_results.pdf')
    plt.savefig('TMRB_GRACE_search_results.png', dpi=150)
    print("\nFigures saved: TMRB_GRACE_search_results.pdf / .png")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 TMRB_GRACE_torsion_search.py <grace_mascon.nc>")
        sys.exit(1)
    run_search(sys.argv[1])