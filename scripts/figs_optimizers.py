# -*- coding: utf-8 -*-
"""Figures for section 5.3 (optimizers) of the NLP book."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT = pathlib.Path(r"C:\Users\admin\Desktop\intro-to-nlp\Tex\images")

# validated categorical slots 1-3 (light surface)
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"

plt.rcParams.update({
    "font.family": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK2,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.frameon": False,
    "legend.fontsize": 8.5,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.bbox": "tight",
    "savefig.dpi": 220,
})


def despine(ax, keep=("left", "bottom")):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)
    ax.tick_params(length=3, width=0.8)


# ============================================================ 1. trajectories
def fig_trajectories():
    a, b = 1.0, 150.0         # ill-conditioned quadratic: narrow ravine
    grad = lambda p: np.array([a * p[0], b * p[1]])
    start = np.array([-9.0, 0.7])
    N = 40

    def run_sgd(lr, mu=0.0):
        p, v, path = start.copy(), np.zeros(2), [start.copy()]
        for _ in range(N):
            v = mu * v + grad(p)
            p = p - lr * v
            path.append(p.copy())
        return np.array(path)

    def run_adam(lr, b1=0.9, b2=0.999, eps=1e-8):
        p, m, v, path = start.copy(), np.zeros(2), np.zeros(2), [start.copy()]
        for t in range(1, N + 1):
            g = grad(p)
            m = b1 * m + (1 - b1) * g
            v = b2 * v + (1 - b2) * g ** 2
            mh, vh = m / (1 - b1 ** t), v / (1 - b2 ** t)
            p = p - lr * mh / (np.sqrt(vh) + eps)
            path.append(p.copy())
        return np.array(path)

    paths = [
        (run_sgd(0.013), C1, "SGD", "-", "o"),
        (run_sgd(0.006, mu=0.9), C2, "SGD + momentum", "--", "s"),
        (run_adam(0.30), C3, "Adam", "-.", "^"),
    ]

    fig, (ax, axl) = plt.subplots(1, 2, figsize=(7.2, 2.9),
                                  gridspec_kw={"width_ratios": [1.45, 1.0]})
    xs = np.linspace(-10.5, 2.2, 400)
    ys = np.linspace(-1.15, 1.15, 400)
    X, Y = np.meshgrid(xs, ys)
    Z = 0.5 * (a * X ** 2 + b * Y ** 2)
    ax.contour(X, Y, Z, levels=np.geomspace(1.0, 100, 9), colors=GRID, linewidths=0.6)

    for path, color, label, ls, mk in paths:
        ax.plot(path[:, 0], path[:, 1], ls, color=color, lw=1.2, zorder=3)
        ax.plot(path[-1, 0], path[-1, 1], mk, color=color, ms=6.0, mec="white",
                mew=1.0, zorder=5)

    ax.annotate("SGD", xy=(-5.3, 0.0), xytext=(-8.4, -0.98), color=C1,
                fontsize=9, fontweight="bold")
    ax.annotate("+ momentum", xy=paths[1][0][-1], xytext=(-3.6, -0.98), color=C2,
                fontsize=9, fontweight="bold")
    ax.annotate("Adam", xy=paths[2][0][-1], xytext=(-3.3, 0.60), color=C3,
                fontsize=9, fontweight="bold")
    ax.plot(0, 0, "*", color=INK, ms=10, zorder=6)
    ax.annotate("cực tiểu", xy=(0, 0), xytext=(0.35, -0.10), color=INK2, fontsize=8)

    ax.set_xlim(-10.5, 2.2)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlabel("hướng phẳng (độ cong nhỏ)")
    ax.set_ylabel("hướng dốc")
    ax.set_title("Quỹ đạo: 40 bước trên thung lũng hẹp")
    despine(ax)

    # --- right panel: loss vs step
    steps = np.arange(len(paths[0][0]))
    for path, color, label, ls, mk in paths:
        loss = 0.5 * (a * path[:, 0] ** 2 + b * path[:, 1] ** 2)
        axl.semilogy(steps, loss, ls, color=color, lw=1.8, label=label, zorder=3)
    axl.set_xlabel("số bước")
    axl.set_ylabel("loss")
    axl.set_title("Loss theo số bước")
    axl.set_xlim(0, N)
    despine(axl)
    axl.legend(loc="upper right")

    fig.tight_layout(w_pad=2.0)
    fig.savefig(OUT / "optimizer_trajectories.png")
    plt.close(fig)
    for path, _, label, _, _ in paths:
        loss = 0.5 * (a * path[:, 0] ** 2 + b * path[:, 1] ** 2)
        print(f"  {label:18s} điểm cuối = ({path[-1,0]:+.3f}, {path[-1,1]:+.3f})  "
              f"loss {loss[0]:.1f} -> {loss[-1]:.3g}")


# ======================================================= 2. bias + sign-step
def fig_bias_and_sign():
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(7.2, 2.9))

    # --- left: bias correction, constant gradient g = 1
    b1 = 0.9
    t = np.arange(1, 41)
    m = 1 - b1 ** t                      # EMA of a constant gradient 1
    mhat = m / (1 - b1 ** t)             # == 1 exactly
    axl.axhline(1.0, color=GRID, lw=0.8)
    axl.plot(t, m, "-", color=C1, lw=1.8, label=r"$m_t$ (chưa hiệu chỉnh)")
    axl.plot(t, mhat, "--", color=C2, lw=1.8, label=r"$\hat{m}_t = m_t/(1-\beta_1^t)$")
    axl.annotate(r"$m_t$", xy=(26, m[25]), xytext=(27, 0.80), color=C1,
                 fontsize=9, fontweight="bold")
    axl.annotate(r"$\hat{m}_t$", xy=(10, 1.0), xytext=(9, 1.045), color=C2,
                 fontsize=9, fontweight="bold")
    axl.set_xlabel("bước $t$")
    axl.set_ylabel("ước lượng moment bậc nhất")
    axl.set_title("Hiệu chỉnh độ lệch, gradient hằng $g=1$")
    axl.set_ylim(0, 1.18)
    axl.set_xlim(1, 40)
    despine(axl)
    axl.legend(loc="lower right")

    # --- right: effective step size vs gradient magnitude
    g = np.geomspace(1e-9, 1e2, 400)
    eta, eps = 1e-3, 1e-8
    axr.loglog(g, eta * g, "-", color=C1, lw=1.8, label="SGD: $\\eta\\,|g|$")
    axr.loglog(g, eta * g / (g + eps), "--", color=C2, lw=1.8,
               label=r"Adam: $\eta\,|g|/(|g|+\epsilon)$")
    axr.axhline(eta, color=GRID, lw=0.8)
    axr.annotate("SGD", xy=(1e-3, 1e-6), xytext=(2e-2, 3e-7), color=C1,
                 fontsize=9, fontweight="bold")
    axr.annotate("Adam", xy=(1e-2, eta), xytext=(1e-6, 4e-3), color=C2,
                 fontsize=9, fontweight="bold")
    axr.annotate(r"trần $\eta$", xy=(40, eta), xytext=(6, 1.6e-4), color=INK2,
                 fontsize=8.5)
    axr.set_xlabel("độ lớn gradient $|g|$")
    axr.set_ylabel("độ lớn bước cập nhật")
    axr.set_title("Adam chặn bước đi, SGD thì không")
    axr.set_ylim(1e-9, 1e-1)
    despine(axr)
    axr.legend(loc="lower left")

    fig.tight_layout(w_pad=2.0)
    fig.savefig(OUT / "adam_bias_and_step.png")
    plt.close(fig)


# ============================================================== 3. memory
def fig_memory():
    rows = [
        ("AdamW",      4, 4, 8),
        ("Adam-mini",  4, 4, 4),
        ("Muon",       4, 4, 4),
    ]
    labels = [r[0] for r in rows]
    y = np.arange(len(rows))[::-1]
    segs = [
        ("Trọng số + gradient (BF16)", [r[1] for r in rows], C1),
        ("Bản sao trọng số FP32",      [r[2] for r in rows], C2),
        ("Trạng thái bộ tối ưu",       [r[3] for r in rows], C3),
    ]

    fig, ax = plt.subplots(figsize=(6.4, 2.35))
    left = np.zeros(len(rows))
    for name, vals, color in segs:
        vals = np.array(vals, dtype=float)
        ax.barh(y, vals - 0.12, left=left + 0.06, height=0.52, color=color,
                label=name, zorder=3)
        for yi, v, l in zip(y, vals, left):
            ax.text(l + v / 2, yi, f"{v:.0f}", ha="center", va="center",
                    color="white", fontsize=8.5, fontweight="bold", zorder=4)
        left = left + vals

    for yi, total in zip(y, left):
        ax.text(total + 0.35, yi, f"{total:.0f} B/tham số   ·   {total*70/1000:.2f} TB cho mô hình 70B",
                va="center", fontsize=8.5, color=INK)

    ax.set_yticks(y, labels, fontsize=9)
    ax.set_xlim(0, 30)
    ax.set_xticks([0, 4, 8, 12, 16])
    ax.set_xlabel("byte trên mỗi tham số")
    ax.set_title("Bộ nhớ huấn luyện (độ chính xác hỗn hợp)")
    despine(ax, keep=("bottom",))
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.34), ncol=3,
              columnspacing=1.4, handlelength=1.1)
    fig.savefig(OUT / "optimizer_memory.png")
    plt.close(fig)


# ==================================================== 4. Newton-Schulz spectrum
def newton_schulz5(X, steps=5):
    a, b, c = 3.4445, -4.7750, 2.0315
    for _ in range(steps):
        A = X @ X.T
        X = a * X + b * (A @ X) + c * (A @ A @ X)
    return X


def fig_muon():
    rng = np.random.default_rng(0)
    n = 128
    U, _ = np.linalg.qr(rng.standard_normal((n, n)))
    V, _ = np.linalg.qr(rng.standard_normal((n, n)))
    sigma = 1.0 / np.arange(1, n + 1) ** 1.0          # phổ luật lũy thừa
    B = U @ np.diag(sigma) @ V.T

    X0 = B / np.linalg.norm(B, "fro")
    X5 = newton_schulz5(X0.copy(), steps=5)
    s0 = np.linalg.svd(X0, compute_uv=False)
    s5 = np.linalg.svd(X5, compute_uv=False)
    print(f"  trước: sigma_max={s0.max():.3f} sigma_min={s0.min():.2e} "
          f"cond={s0.max()/s0.min():.1e}")
    print(f"  sau  : sigma_max={s5.max():.3f} sigma_min={s5.min():.3f} "
          f"cond={s5.max()/s5.min():.2f}")

    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    k = np.arange(1, n + 1)
    ax.semilogy(k, s0, "-", color=C1, lw=1.8, label="trước: $B_t/\\|B_t\\|_F$")
    ax.semilogy(k, s5, "--", color=C2, lw=1.8, label="sau 5 bước Newton–Schulz")
    ax.axhline(1.0, color=GRID, lw=0.8)
    ax.annotate("trước khi trực giao hóa", xy=(70, s0[69]), xytext=(44, 2.2e-3),
                color=C1, fontsize=9, fontweight="bold")
    ax.annotate("sau 5 bước Newton–Schulz", xy=(70, s5[69]), xytext=(26, 2.9),
                color=C2, fontsize=9, fontweight="bold")
    ax.set_xlabel("chỉ số giá trị suy biến $i$")
    ax.set_ylabel("$\\sigma_i$")
    ax.set_title("Trực giao hóa san phẳng phổ giá trị suy biến")
    ax.annotate(r"mọi $\sigma_i \in [0{,}68;\ 1{,}13]$", xy=(96, 0.9),
                xytext=(44, 0.145), color=INK2, fontsize=8.5)
    ax.set_xlim(1, n)
    ax.set_ylim(5e-4, 6)
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda v, _: ("%g" % v) if v >= 0.01 else "$10^{%d}$" % round(np.log10(v))))
    despine(ax)
    ax.legend(loc="lower left")
    fig.savefig(OUT / "muon_newton_schulz.png")
    plt.close(fig)


print("trajectories:")
fig_trajectories()
print("bias/step:")
fig_bias_and_sign()
print("memory:")
fig_memory()
print("muon:")
fig_muon()
print("done")
