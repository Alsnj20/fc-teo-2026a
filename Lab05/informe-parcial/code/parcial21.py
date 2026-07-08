import matplotlib.pyplot as plt
import numpy as np

k = 1.0
lado = 1.0

# Cargas
q1, q2, q3 = +1.0, +0.8, +0.8

# Posiciones para formar el triángulo
x1, y1 = -lado, 0.0  # Carga izquierda
x2, y2 = lado, 0.0  # Carga derecha
x3, y3 = 0.0, lado  # Carga superior

cargas = [
    {"q": q1, "x": x1, "y": y1},
    {"q": q2, "x": x2, "y": y2},
    {"q": q3, "x": x3, "y": y3},
]

xa = np.linspace(-3, 3, 300)
ya = np.linspace(-3, 3, 300)
x, y = np.meshgrid(xa, ya)

# Inicializamos el potencial en cero
z = np.zeros_like(x)

for carga in cargas:
    qi, xi, yi = carga["q"], carga["x"], carga["y"]
    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2)
    r = np.where(r == 0, 1e-15, r)
    z += k * qi / r

# Calcular el Campo Eléctrico
Ex = np.zeros_like(x)
Ey = np.zeros_like(x)
for carga in cargas:
    qi, xi, yi = carga["q"], carga["x"], carga["y"]
    dx, dy = x - xi, y - yi
    r = np.sqrt(dx**2 + dy**2)

    # Límite mínimo para evitar que el campo se dispare a infinito
    r_safe = np.maximum(r, 0.05)
    Ex += k * qi * dx / r_safe**3
    Ey += k * qi * dy / r_safe**3

z_min_plot = np.percentile(z, 5)
z_max_plot = np.percentile(z, 99.5)

dz = (z_max_plot - z_min_plot) / 20
nivel = np.arange(z_min_plot, z_max_plot + dz, dz)

# Graficar
plt.figure(figsize=(10, 10))

# líneas guía del triángulo isósceles
plt.plot([x1, x2], [y1, y2], "k--", alpha=0.5, linewidth=1.0)
plt.plot([x2, x3], [y2, y3], "k--", alpha=0.5, linewidth=1.0)
plt.plot([x3, x1], [y3, y1], "k--", alpha=0.5, linewidth=1.0)

# Graficar contornos
plt.contour(x, y, z, levels=nivel, cmap="Purples_r", linewidths=2.0)
for carga in cargas:
    cq = carga["q"]
    vx = carga["x"]
    vy = carga["y"]
    color = "red" if cq > 0 else "blue"
    plt.plot(vx, vy, "o", color=color, markersize=8, zorder=5)
    plt.text(
        vx + 0.1, vy + 0.1, f"{cq:+.1f} C", fontsize=10, color=color, fontweight="bold"
    )

# Graficar las líneas de campo eléctrico
plt.streamplot(xa, ya, Ex, Ey, color="gray", linewidth=0.6, density=1.3, arrowsize=1.0)

plt.gca().set_aspect("equal", adjustable="box")

plt.title("Equipotenciales y Campo Eléctrico - 3 Cargas (+)")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
