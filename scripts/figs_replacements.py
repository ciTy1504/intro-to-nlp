# -*- coding: utf-8 -*-
"""Redraw four figures whose content did not match what the book says.

Why each one is being replaced:
  lda_generative_process      the file was a bioinformatics figure about protein
                              modules and metabolic pathways; it only borrowed the
                              word "Topic". Replaced with plate notation for LDA.
  bert_mlm_nsp                showed MLM only, while the caption promises MLM and
                              NSP. Replaced with both objectives.
  transformer_encoder_detailed  showed a Pre-LN block, but it sits in the BERT
                              section and BERT is Post-LN. Replaced with Post-LN
                              plus an explicit Pre-LN contrast panel.
  llm_benchmarks_timeline     showed saturation-vs-human up to 2020 with no
                              LLM-era benchmark, under a caption calling it a
                              development timeline. Replaced with a real timeline.

Benchmark years come from the book's own references.bib where an entry exists, so
the figure cannot contradict the citations printed next to it.
"""
import pathlib
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch

OUT = pathlib.Path(r"C:\Users\admin\Desktop\intro-to-nlp\Tex\images")
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"
FILL1, FILL2, FILL3 = "#dce9f9", "#fbe2d5", "#d7f0e4"

plt.rcParams.update({
    "font.family": ["Times New Roman", "DejaVu Serif"], "font.size": 9,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2,
    "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2,
    "legend.frameon": False, "legend.fontsize": 8.5,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "savefig.bbox": "tight", "savefig.dpi": 220,
})


def box(ax, x, y, w, h, text, fc=FILL1, ec=C1, fs=9, bold=False, r=0.02):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0.004,rounding_size={r}",
                                fc=fc, ec=ec, lw=1.1, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=INK, zorder=3, fontweight="bold" if bold else "normal")


def arrow(ax, p, q, color=INK2, lw=1.1, style="-|>", rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=9,
                                 lw=lw, color=color, zorder=2,
                                 connectionstyle=f"arc3,rad={rad}",
                                 shrinkA=1.5, shrinkB=1.5))


def blank(ax):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")


# ===================================================================== 1. LDA
def fig_lda():
    fig, ax = plt.subplots(figsize=(5.6, 2.5))
    blank(ax)

    # plates: K topics (left), D documents with inner N plate (right)
    ax.add_patch(Rectangle((0.045, 0.14), 0.20, 0.60, fill=False, ec=INK2,
                           lw=1.0, ls="-", zorder=1))
    ax.text(0.225, 0.185, "$K$", fontsize=9.5, color=INK2, ha="right")

    ax.add_patch(Rectangle((0.37, 0.09), 0.57, 0.72, fill=False, ec=INK2, lw=1.0, zorder=1))
    ax.text(0.918, 0.135, "$D$", fontsize=9.5, color=INK2, ha="right")
    ax.add_patch(Rectangle((0.575, 0.18), 0.33, 0.47, fill=False, ec=INK2, lw=1.0, zorder=1))
    ax.text(0.885, 0.222, "$N_d$", fontsize=9.5, color=INK2, ha="right")

    def node(x, y, lab, shaded=False):
        ax.add_patch(Circle((x, y), 0.052, fc=(C2 if shaded else "white"),
                            ec=(C2 if shaded else INK2), lw=1.2, zorder=3,
                            alpha=0.85 if shaded else 1.0))
        ax.text(x, y, lab, ha="center", va="center", fontsize=9.5,
                color=("white" if shaded else INK), zorder=4)

    ax.text(0.022, 0.45, r"$\beta$", fontsize=10, color=INK, ha="center", va="center")
    node(0.145, 0.45, r"$\phi_k$")
    # alpha sits on the same row as theta_d, mirroring beta -> phi_k, so that the
    # phi_k -> w arc overhead cannot be misread as starting at alpha.
    ax.text(0.332, 0.45, r"$\alpha$", fontsize=10, color=INK, ha="center", va="center")
    node(0.465, 0.45, r"$\theta_d$")
    node(0.675, 0.42, r"$z_{d,n}$")
    node(0.835, 0.42, r"$w_{d,n}$", shaded=True)

    arrow(ax, (0.048, 0.45), (0.088, 0.45))
    arrow(ax, (0.358, 0.45), (0.410, 0.45))
    arrow(ax, (0.518, 0.45), (0.620, 0.43))
    arrow(ax, (0.728, 0.42), (0.781, 0.42))
    arrow(ax, (0.160, 0.503), (0.828, 0.473), rad=-0.42)

    ax.text(0.5, 0.955, "Mô hình sinh của LDA (ký hiệu dạng tấm)",
            ha="center", fontsize=10, fontweight="bold", color=INK)
    legend = (r"$\alpha,\beta$: siêu tham số Dirichlet   ·   "
              r"$\theta_d$: phân phối chủ đề của tài liệu $d$   ·   "
              r"$\phi_k$: phân phối từ của chủ đề $k$")
    legend2 = (r"$z_{d,n}$: chủ đề của từ thứ $n$   ·   "
               r"$w_{d,n}$: từ quan sát được (nút tô màu)")
    ax.text(0.5, 0.045, legend, ha="center", fontsize=7.8, color=INK2)
    ax.text(0.5, -0.025, legend2, ha="center", fontsize=7.8, color=INK2)
    fig.savefig(OUT / "lda_generative_process.png")
    plt.close(fig)


# ================================================================ 2. BERT
def fig_bert():
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(6.6, 2.75))
    for ax in (axl, axr):
        blank(ax)

    # ---- MLM
    toks = ["[CLS]", "con", "mèo", "[MASK]", "trên", "thảm", "[SEP]"]
    w, gap = 0.123, 0.016
    x0 = 0.5 - (len(toks) * w + (len(toks) - 1) * gap) / 2
    for i, t in enumerate(toks):
        x = x0 + i * (w + gap)
        fc, ec = (FILL2, C2) if t == "[MASK]" else ("white", INK2)
        # [MASK] is the widest token; drop it a point so it stays inside the box
        box(axl, x, 0.06, w, 0.11, t, fc=fc, ec=ec, fs=6.6 if t == "[MASK]" else 7.2)
        arrow(axl, (x + w / 2, 0.175), (x + w / 2, 0.325))
    box(axl, x0, 0.33, len(toks) * w + (len(toks) - 1) * gap, 0.15,
        "BERT (encoder hai chiều)", fc=FILL1, ec=C1, fs=8.5, bold=True)
    xm = x0 + 3 * (w + gap)
    arrow(axl, (xm + w / 2, 0.485), (xm + w / 2, 0.635), color=C2, lw=1.4)
    box(axl, xm - 0.085, 0.64, w + 0.17, 0.12, "softmax trên từ vựng",
        fc=FILL2, ec=C2, fs=7.8)
    arrow(axl, (xm + w / 2, 0.765), (xm + w / 2, 0.845), color=C2, lw=1.4)
    box(axl, xm - 0.02, 0.85, w + 0.04, 0.10, "ngồi", fc="white", ec=C2, fs=8.5, bold=True)
    axl.text(0.5, 1.02, "Masked Language Modeling (MLM)", ha="center",
             fontsize=9.5, fontweight="bold", color=INK)
    axl.text(0.5, -0.045, "Đoán token bị che từ ngữ cảnh hai phía",
             ha="center", fontsize=7.8, color=INK2)

    # ---- NSP
    segs = [("[CLS]", "white", INK2), ("Câu A", FILL1, C1), ("[SEP]", "white", INK2),
            ("Câu B", FILL3, C3), ("[SEP]", "white", INK2)]
    ws = [0.115, 0.235, 0.115, 0.235, 0.115]
    x0 = 0.5 - (sum(ws) + 4 * gap) / 2
    xs = []
    xc = x0
    for (t, fc, ec), ww in zip(segs, ws):
        box(axr, xc, 0.06, ww, 0.11, t, fc=fc, ec=ec, fs=7.4)
        arrow(axr, (xc + ww / 2, 0.175), (xc + ww / 2, 0.325))
        xs.append(xc)
        xc += ww + gap
    box(axr, x0, 0.33, sum(ws) + 4 * gap, 0.15,
        "BERT (encoder hai chiều)", fc=FILL1, ec=C1, fs=8.5, bold=True)
    xc0 = xs[0] + ws[0] / 2
    arrow(axr, (xc0, 0.485), (xc0, 0.635), color=C3, lw=1.4)
    box(axr, xs[0] - 0.045, 0.64, 0.205, 0.12, "vector [CLS]", fc=FILL3, ec=C3, fs=7.8)
    arrow(axr, (xc0 + 0.058, 0.70), (0.52, 0.70), color=C3, lw=1.4)
    box(axr, 0.53, 0.635, 0.44, 0.13, "IsNext  /  NotNext", fc="white", ec=C3,
        fs=8.5, bold=True)
    axr.text(0.5, 1.02, "Next Sentence Prediction (NSP)", ha="center",
             fontsize=9.5, fontweight="bold", color=INK)
    axr.text(0.5, -0.045, "Phân loại nhị phân: câu B có đi liền sau câu A không",
             ha="center", fontsize=7.8, color=INK2)

    fig.savefig(OUT / "bert_mlm_nsp.png")
    plt.close(fig)


# ========================================================= 3. encoder block
def fig_encoder():
    fig = plt.figure(figsize=(6.8, 3.5))
    axa = fig.add_axes([0.00, 0.0, 0.30, 1.0])
    axb = fig.add_axes([0.345, 0.0, 0.40, 1.0])
    axc = fig.add_axes([0.785, 0.0, 0.215, 1.0])
    for ax in (axa, axb, axc):
        blank(ax)

    # ---- (a) Post-LN block (the original Transformer / BERT)
    axa.text(0.5, 0.975, "(a) khối Encoder, Post-LN", ha="center",
             fontsize=9.5, fontweight="bold", color=INK)
    ys = [0.10, 0.27, 0.42, 0.585, 0.735]
    box(axa, 0.17, ys[0], 0.66, 0.085, "đầu vào $x$", fc="white", ec=INK2, fs=8)
    box(axa, 0.17, ys[1], 0.66, 0.095, "Multi-head\nSelf-Attention", fc=FILL2, ec=C2, fs=8)
    box(axa, 0.17, ys[2], 0.66, 0.085, "Add & Norm", fc=FILL1, ec=C1, fs=8, bold=True)
    box(axa, 0.17, ys[3], 0.66, 0.085, "Feed-Forward", fc=FILL2, ec=C2, fs=8)
    box(axa, 0.17, ys[4], 0.66, 0.085, "Add & Norm", fc=FILL1, ec=C1, fs=8, bold=True)
    arrow(axa, (0.5, ys[0] + 0.085), (0.5, ys[1]))
    arrow(axa, (0.5, ys[1] + 0.095), (0.5, ys[2]))
    arrow(axa, (0.5, ys[2] + 0.085), (0.5, ys[3]))
    arrow(axa, (0.5, ys[3] + 0.085), (0.5, ys[4]))
    arrow(axa, (0.5, ys[4] + 0.085), (0.5, 0.90))
    # residual connections skip only the sub-layer, not the norm
    for a, b in ((ys[0] + 0.085, ys[2] + 0.040), (ys[2] + 0.085, ys[4] + 0.040)):
        axa.plot([0.11, 0.11], [a, b], color=C3, lw=1.2, zorder=1)
        axa.plot([0.11, 0.17], [a, a], color=C3, lw=1.2, zorder=1)
        arrow(axa, (0.11, b), (0.17, b), color=C3, lw=1.2)
    axa.text(0.055, 0.50, "phần dư", rotation=90, ha="center", va="center",
             fontsize=7.5, color=C3)
    axa.text(0.5, 0.925, r"$\times N$", ha="center", fontsize=9, color=INK2)

    # ---- (b) multi-head attention detail
    axb.text(0.5, 0.975, "(b) bên trong Multi-head Self-Attention", ha="center",
             fontsize=9.5, fontweight="bold", color=INK)
    for i, (lab, yy) in enumerate([("Q", 0.74), ("K", 0.58), ("V", 0.42)]):
        box(axb, 0.03, yy, 0.10, 0.085, lab, fc="white", ec=INK2, fs=8.5)
        box(axb, 0.19, yy, 0.17, 0.085, "Linear", fc=FILL3, ec=C3, fs=8)
        arrow(axb, (0.13, yy + 0.042), (0.19, yy + 0.042))
        arrow(axb, (0.36, yy + 0.042), (0.44, 0.60))
    box(axb, 0.44, 0.50, 0.26, 0.20,
        "Scaled\nDot-Product\nAttention\n" + r"($h$ đầu)", fc=FILL2, ec=C2, fs=8)
    box(axb, 0.75, 0.545, 0.14, 0.11, "Concat", fc=FILL1, ec=C1, fs=8)
    arrow(axb, (0.70, 0.60), (0.75, 0.60))
    box(axb, 0.75, 0.355, 0.14, 0.10, "Linear", fc=FILL3, ec=C3, fs=8)
    arrow(axb, (0.82, 0.545), (0.82, 0.455))
    arrow(axb, (0.82, 0.355), (0.82, 0.275))
    axb.text(0.82, 0.235, "đầu ra", ha="center", fontsize=8, color=INK2)
    axb.text(0.5, 0.135,
             r"$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}"
             r"\!\left(\dfrac{QK^{\top}}{\sqrt{d_k}}\right)V$",
             ha="center", fontsize=10, color=INK)

    # ---- (c) Pre-LN contrast
    axc.text(0.5, 0.975, "(c) Pre-LN", ha="center", fontsize=9.5,
             fontweight="bold", color=INK)
    zs = [0.17, 0.35, 0.53, 0.71]
    box(axc, 0.26, zs[0], 0.60, 0.085, "đầu vào $x$", fc="white", ec=INK2, fs=7.5)
    box(axc, 0.26, zs[1], 0.60, 0.085, "LayerNorm", fc=FILL1, ec=C1, fs=7.5, bold=True)
    box(axc, 0.26, zs[2], 0.60, 0.085, "lớp con", fc=FILL2, ec=C2, fs=7.5)
    box(axc, 0.26, zs[3], 0.60, 0.085, r"$\oplus$  cộng dư", fc=FILL3, ec=C3, fs=7.5)
    for a, b in zip(zs, zs[1:]):
        arrow(axc, (0.56, a + 0.085), (0.56, b))
    axc.plot([0.17, 0.17], [zs[0] + 0.085, zs[3] + 0.042], color=C3, lw=1.2, zorder=1)
    axc.plot([0.17, 0.26], [zs[0] + 0.085, zs[0] + 0.085], color=C3, lw=1.2, zorder=1)
    arrow(axc, (0.17, zs[3] + 0.042), (0.26, zs[3] + 0.042), color=C3, lw=1.2)
    axc.text(0.5, 0.045, "chuẩn hóa nằm trong nhánh;\nLLM hiện đại dùng cách này",
             ha="center", va="top", fontsize=7.3, color=INK2)

    fig.savefig(OUT / "transformer_encoder_detailed.png")
    plt.close(fig)


# ===================================================== 4. benchmark timeline
def fig_timeline():
    # Years follow the book's own references.bib where an entry exists, so the
    # figure cannot disagree with the citation printed beside it in the text.
    # Slots are chosen so that two wide labels never land on the same row in
    # adjacent years: SuperGLUE is lifted clear of SQuAD 2.0, AgentBench clear
    # of HELM.
    items = [
        (2016, "SQuAD 1.1", 0), (2018, "SQuAD 2.0", 0), (2018, "GLUE", 1),
        (2019, "SuperGLUE", 2),
        (2021, "MMLU", 0), (2021, "GSM8K", 1), (2021, "MATH", 2),
        (2022, "BIG-bench", 0), (2023, "HELM", 1),
        (2024, "AgentBench", 0), (2024, "GAIA", 1), (2024, "SWE-bench", 2),
    ]
    eras = [(2015.6, 2019.7, "hiểu ngôn ngữ", C1),
            (2020.5, 2023.5, "kiến thức và suy luận", C2),
            (2023.6, 2025.6, "tác tử, kỹ thuật phần mềm", C3)]

    fig, ax = plt.subplots(figsize=(7.1, 2.6))
    ax.set_xlim(2015.2, 2026.0); ax.set_ylim(-1.15, 1.6)
    ax.axis("off")

    for a, b, lab, col in eras:
        ax.add_patch(Rectangle((a, -0.62), b - a, 1.24, fc=col, ec="none",
                               alpha=0.07, zorder=0))
        ax.text((a + b) / 2, -0.80, lab, ha="center", fontsize=8,
                color=col, fontweight="bold")

    ax.annotate("", xy=(2025.9, 0), xytext=(2015.3, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.2))
    for yr in range(2016, 2025):
        ax.plot([yr], [0], marker="|", color=INK2, ms=6)
        ax.text(yr, -0.30, str(yr), ha="center", fontsize=8, color=INK2)

    for yr, name, slot in items:
        col = next(c for a, b, _, c in eras if a <= yr <= b)
        h = 0.34 + 0.345 * slot
        ax.plot([yr, yr], [0.04, h], color=col, lw=1.0, zorder=1)
        ax.plot([yr], [h], "o", color=col, ms=4.2, mec="white", mew=0.8, zorder=3)
        ax.text(yr, h + 0.085, name, ha="center", fontsize=8.2, color=INK)

    ax.text(2015.4, 1.40, "Mốc ra đời của các benchmark tiêu biểu",
            fontsize=10, fontweight="bold", color=INK)
    fig.savefig(OUT / "llm_benchmarks_timeline.png")
    plt.close(fig)


for fn in (fig_lda, fig_bert, fig_encoder, fig_timeline):
    fn()
    print("đã vẽ:", fn.__name__)
