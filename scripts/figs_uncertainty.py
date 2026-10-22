# -*- coding: utf-8 -*-
"""Figures for the measurement-uncertainty section: CI width vs n, and calibration."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(r"C:\Users\admin\Desktop\intro-to-nlp\Tex\images")
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"

plt.rcParams.update({
    "font.family": ["Times New Roman", "DejaVu Serif"], "font.size": 9,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2,
    "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2,
    "xtick.labelsize": 8.5, "ytick.labelsize": 8.5,
    "legend.frameon": False, "legend.fontsize": 8.5,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "savefig.bbox": "tight", "savefig.dpi": 220,
})

fig, (axl, axr) = plt.subplots(1, 2, figsize=(7.2, 2.95))

# ---------------- left: CI half-width vs n, for three accuracy levels
n = np.geomspace(50, 20000, 300)
for acc, color, ls, lab in [(0.70, C1, "-", "accuracy 70%"),
                            (0.90, C2, "--", "accuracy 90%"),
                            (0.98, C3, "-.", "accuracy 98%")]:
    half = 1.96 * np.sqrt(acc * (1 - acc) / n)
    axl.loglog(n, half * 100, ls, color=color, lw=1.8, label=lab)

for nn in (200, 1000, 5000):
    axl.axvline(nn, color=GRID, lw=0.8, ls=":")
h200 = 1.96 * np.sqrt(0.9 * 0.1 / 200) * 100
axl.plot([200], [h200], "o", color=C2, ms=5.5, mec="white", mew=1.0, zorder=5)
axl.annotate(f"n=200 → ±{h200:.1f}%", xy=(200, h200), xytext=(240, 6.2),
             color=C2, fontsize=9, fontweight="bold")
axl.set_xlabel("kích thước tập kiểm thử $n$")
axl.set_ylabel("nửa bề rộng KTC 95% (điểm %)")
axl.set_title("Con số của bạn sai bao nhiêu?")
axl.legend(loc="upper right")
for s in ("top", "right"):
    axl.spines[s].set_visible(False)
axl.tick_params(length=3, width=0.8)

# ---------------- right: reliability diagram, before/after temperature scaling
rng = np.random.default_rng(7)
N = 20000
# a 2-class model whose logit margin is systematically too large (overconfident)
true_margin = rng.normal(0, 1.2, N)
y = (rng.random(N) < 1 / (1 + np.exp(-true_margin))).astype(int)
T_true = 2.3                      # the model's logits are inflated by this factor
logit = true_margin * T_true
p_raw = 1 / (1 + np.exp(-logit))
p_cal = 1 / (1 + np.exp(-logit / T_true))   # temperature scaling with the right T

def reliability(p, y, bins=10):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, bins - 1)
    conf, acc, cnt = [], [], []
    for b in range(bins):
        m = idx == b
        if m.sum() < 20:
            continue
        conf.append(p[m].mean()); acc.append(y[m].mean()); cnt.append(m.sum())
    return np.array(conf), np.array(acc), np.array(cnt)

def ece(p, y, bins=15):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, bins - 1)
    e = 0.0
    for b in range(bins):
        m = idx == b
        if m.sum() == 0:
            continue
        e += m.mean() * abs(y[m].mean() - p[m].mean())
    return e

axr.plot([0, 1], [0, 1], ":", color=INK2, lw=1.0)
axr.annotate("hiệu chuẩn hoàn hảo", xy=(0.55, 0.55), xytext=(0.40, 0.70),
             color=INK2, fontsize=8, rotation=38)
for p, color, ls, mk, lab in [(p_raw, C2, "--", "s", "trước"), (p_cal, C1, "-", "o", "sau")]:
    c, a, _ = reliability(p, y)
    axr.plot(c, a, ls, color=color, lw=1.8, marker=mk, ms=4.5, mec="white", mew=0.7,
             label=f"{lab} (ECE {ece(p, y):.3f})")
axr.set_xlabel("độ tự tin mô hình đưa ra")
axr.set_ylabel("tỷ lệ đúng thực tế")
axr.set_title("Hiệu chuẩn: tự tin $\\neq$ đúng")
axr.set_xlim(0, 1); axr.set_ylim(0, 1)
axr.legend(loc="upper left")
for s in ("top", "right"):
    axr.spines[s].set_visible(False)
axr.tick_params(length=3, width=0.8)

fig.tight_layout(w_pad=2.2)
fig.savefig(OUT / "eval_uncertainty.png")
plt.close(fig)

print("KTC 95% cho accuracy (nua be rong, diem %):")
print(f"{'n':>7} " + "".join(f"{a:>10.0%}" for a in (0.70, 0.90, 0.98)))
for nn in (100, 200, 500, 1000, 2000, 5000, 10000):
    row = "".join(f"{1.96*np.sqrt(a*(1-a)/nn)*100:>10.2f}" for a in (0.70, 0.90, 0.98))
    print(f"{nn:>7} {row}")
print(f"\nECE truoc = {ece(p_raw, y):.4f}   ECE sau = {ece(p_cal, y):.4f}")
