import matplotlib.pyplot as plt
import numpy as np

MU0 = 4 * np.pi * 1e-7

c = 20
R = 1  # Radio del cilindro
theta = np.linspace(0, 2 * np.pi, c, endpoint=False)
x_w = R * np.cos(theta)
y_w = R * np.sin(theta)

total_current = 1.0  # Corriente total
current_magnitude = total_current / c  # Corriente por hilo
Q = np.ones(c) * current_magnitude


def calcular_campo(x, y):
    Bx = np.zeros_like(x, dtype=float)
    By = np.zeros_like(y, dtype=float)

    for xw, yw, curr in zip(x_w, y_w, Q):
        dx = x - xw
        dy = y - yw
        d_i = dx**2 + dy**2

        d_i = np.where(np.isclose(d_i, 0.0), np.nan, d_i)

        factor = MU0 * curr / (2 * np.pi * d_i)
        Bx += factor * (-dy)
        By += factor * dx

    return Bx, By


grid_step = 0.03
xa = np.arange(-2.2, 2.2 + grid_step, grid_step)
ya = np.arange(-2.2, 2.2 + grid_step, grid_step)
x, y = np.meshgrid(xa, ya)

# Calcular el campo magnético
Bx, By = calcular_campo(x, y)

mag = np.sqrt(Bx**2 + By**2)
mag = np.where(np.isfinite(mag), mag, np.nan)

Bref = np.nanpercentile(mag, 92)
arrow_len = 0.16

scale_factor = np.where(
    np.isfinite(mag) & (Bref > 0),
    arrow_len * np.clip(mag / Bref, 0.08, 1.2) / np.where(mag == 0, 1.0, mag),
    0.0,
)

Bx_final = Bx * scale_factor
By_final = By * scale_factor

Umag = np.sqrt(Bx_final**2 + By_final**2)
max_arrow = 0.15
limit_factor = np.where(Umag > max_arrow, max_arrow / Umag, 1.0)
Bx_final *= limit_factor
By_final *= limit_factor


plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(9, 9), constrained_layout=True)
ax.set_facecolor("#fbfbfd")

ax.quiver(
    x,
    y,
    Bx_final,
    By_final,
    color="#005F76",
    angles="xy",
    scale_units="xy",
    scale=1,
    alpha=0.78,
    width=0.0034,
    zorder=2,
)

cilindro = plt.Circle((0, 0), R, fill=False, color="#222222", linewidth=2.2, zorder=4)
ax.add_patch(cilindro)

ax.scatter(
    x_w,
    y_w,
    s=90,
    marker="o",
    facecolors="#DCEBEF",
    edgecolors="tab:orange",
    linewidths=1.0,
    zorder=6,
    label="Corrientes de Superficie",
)

ax.scatter([0], [0], color="#000000", s=70, zorder=8, label="Centro")

ax.set_ylim(-2.2, 2.2)
ax.set_aspect("equal", adjustable="box")

plt.title(
    "Cilindro hueco infinito formado por corrientes infinitas",
    fontsize=12,
)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.22)
plt.legend(loc="upper right", frameon=True)
plt.savefig("Lab06/img/lab/4.png", dpi=300, bbox_inches="tight")

plt.show()
