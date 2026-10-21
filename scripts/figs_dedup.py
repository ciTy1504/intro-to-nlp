# -*- coding: utf-8 -*-
"""Figure for the LLM data pipeline: the MinHash-LSH S-curve for production configs."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(r"C:\Users\admin\Desktop\intro-to-nlp\Tex\images")

C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"   # validated categorical slots 1-3
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"

plt.rcParams.update({
    "font.family": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2,
    "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2,
    "xtick.labelsize": 8.5, "ytick.labelsize": 8.5,
    "legend.frameon": False, "legend.fontsize": 8.5,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "savefig.bbox": "tight", "savefig.dpi": 220,
})

# P(a pair with Jaccard s is retrieved) = 1 - (1 - s^r)^b
def p_detect(s, b, r):
    return 1.0 - (1.0 - s ** r) ** b

CONFIGS = [
    ("FineWeb:  14 nhóm $\\times$ 8 hàm băm", 14, 8, C1, "-"),
    ("NeMo Curator:  20 $\\times$ 13", 20, 13, C2, "--"),
    ("Cấu hình lỏng:  32 $\\times$ 4", 32, 4, C3, "-."),
]

s = np.linspace(0, 1, 801)
fig, ax = plt.subplots(figsize=(6.4, 3.3))

ax.axvline(0.75, color=INK2, lw=0.9, ls=":", zorder=2)
ax.annotate("ngưỡng FineWeb nhắm tới: 0.75", xy=(0.75, 0.05), xytext=(0.30, 0.055),
            color=INK2, fontsize=8.5)

for label, b, r, color, ls in CONFIGS:
    ax.plot(s, p_detect(s, b, r), ls, color=color, lw=1.8, label=label, zorder=3)

for label, b, r, color, _ in CONFIGS:
    p75 = p_detect(0.75, b, r)
    ax.plot([0.75], [p75], "o", color=color, ms=5.5, mec="white", mew=1.0, zorder=4)
    ax.annotate(f"{p75:.0%}", xy=(0.75, p75), xytext=(0.775, p75 - 0.035),
                color=color, fontsize=9, fontweight="bold")

ax.set_xlabel("độ tương đồng Jaccard thật của một cặp tài liệu")
ax.set_ylabel("xác suất bị phát hiện là trùng")
ax.set_title("Cùng gọi là “khử trùng lặp mờ”, ba cấu hình, ba hành vi khác hẳn")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.04)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
ax.tick_params(length=3, width=0.8)
ax.legend(loc="upper left")

fig.savefig(OUT / "minhash_s_curve.png")
plt.close(fig)

print("P(phat hien) tai cac muc tuong dong:")
print(f"{'cau hinh':<22}" + "".join(f"{x:>9.2f}" for x in (0.5, 0.6, 0.7, 0.75, 0.8, 0.9)))
for label, b, r, _, _ in CONFIGS:
    name = f"b={b}, r={r}"
    print(f"{name:<22}" + "".join(f"{p_detect(x, b, r):>9.1%}"
                                   for x in (0.5, 0.6, 0.7, 0.75, 0.8, 0.9)))
