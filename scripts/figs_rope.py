# -*- coding: utf-8 -*-
"""Figure for section 4.4 (RoPE scaling): wavelength of each RoPE dimension pair."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(r"C:\Users\admin\Desktop\intro-to-nlp\Tex\images")

C1, C2 = "#2a78d6", "#eb6834"          # validated categorical slots 1-2
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

D_HEAD = 128
L_TRAIN = 8192
i = np.arange(D_HEAD // 2)


def wavelength(base):
    return 2 * np.pi * base ** (2 * i / D_HEAD)


fig, ax = plt.subplots(figsize=(6.4, 3.2))
lam10k, lam500k = wavelength(10_000), wavelength(500_000)

ax.axhspan(L_TRAIN, 1e7, color=GRID, alpha=0.45, zorder=0)
ax.axhline(L_TRAIN, color=INK2, lw=0.9, ls=":", zorder=2)

ax.semilogy(i, lam10k, "-", color=C1, lw=1.8, label=r"$b = 10\,000$ (RoPE gốc)", zorder=3)
ax.semilogy(i, lam500k, "--", color=C2, lw=1.8, label=r"$b = 500\,000$ (ABF, Llama 3)", zorder=3)

n10 = int((lam10k > L_TRAIN).sum())
n500 = int((lam500k > L_TRAIN).sum())

ax.annotate(r"$b = 10\,000$", xy=(50, lam10k[50]), xytext=(41, 330),
            color=C1, fontsize=9, fontweight="bold")
ax.annotate(r"$b = 500\,000$", xy=(30, lam500k[30]), xytext=(8, 2.1e4),
            color=C2, fontsize=9, fontweight="bold")
ax.annotate("chưa quay trọn một vòng trong lúc huấn luyện", xy=(2, 3e5),
            color=INK2, fontsize=8.5)
ax.annotate(f"ngữ cảnh huấn luyện $L = {L_TRAIN}$", xy=(33, L_TRAIN),
            xytext=(1, 2600), color=INK2, fontsize=8.5)

ax.set_xlabel("chỉ số cặp chiều $i$ (đầu attention 128 chiều)")
ax.set_ylabel("bước sóng $\\lambda_i$ (số token)")
ax.set_title("Mỗi cặp chiều RoPE là một chiếc kim quay với tốc độ riêng")
ax.set_xlim(0, D_HEAD // 2 - 1)
ax.set_ylim(3, 1e7)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(length=3, width=0.8)
ax.legend(loc="lower right")

fig.savefig(OUT / "rope_wavelengths.png")
plt.close(fig)

print(f"b=10000 : {n10}/{D_HEAD//2} cặp chiều có lambda > {L_TRAIN}")
print(f"b=500000: {n500}/{D_HEAD//2} cặp chiều có lambda > {L_TRAIN}")
for idx in (0, 32, 63):
    print(f"  i={idx:2d}: lambda(10k)={lam10k[idx]:12,.0f}   lambda(500k)={lam500k[idx]:14,.0f}")
