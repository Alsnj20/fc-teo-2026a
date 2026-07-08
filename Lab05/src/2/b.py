import matplotlib.pyplot as plt
import numpy as np

k = 1.0
lado = 0.01 / np.sqrt(2)

# Cargas
q1, q2, q3, q4 = -1.0, -1.0, -1.0, -1.0

x1, y1 = lado, 0.0
x2, y2 = 0.0, lado
x3, y3 = -lado, 0.0
x4, y4 = 0.0, -lado

cargas = [
    {"q": q1, "x": x1, "y": y1},
    {"q": q2, "x": x2, "y": y2},
    {"q": q3, "x": x3, "y": y3},
    {"q": q4, "x": x4, "y": y4},
]

xa = np.linspace(-0.02, 0.02, 60)
ya = np.linspace(-0.02, 0.02, 60)
x, y = np.meshgrid(xa, ya)
v = np.zeros_like(x)

for carga in cargas:
    qi = carga["q"]
    xi = carga["x"]
    yi = carga["y"]

    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2)
    r = np.where(r == 0, 1e-12, r)
    v += k * qi / r

vmax = np.max(v)
vmin = np.min(v)
niveles = np.linspace(vmin, vmax, 50)

plt.figure(figsize=(10, 10))

plt.contour(x, y, v, levels=niveles, cmap="jet")
for carga in cargas:
    cq = carga["q"]
    vx = carga["x"]
    vy = carga["y"]
    color = "red" if cq > 0 else "blue"
    plt.plot(vx, vy, "o", color=color, markersize=8, zorder=5)
    plt.text(
        vx + 0.1, vy + 0.1, f"{cq:+.1f} C", fontsize=8, color=color, fontweight="bold"
    )

plt.title("Ejercicio 2(b): Líneas Equipotenciales y Campo Eléctrico")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True, alpha=0.3)
plt.colorbar(label="V")
plt.savefig("Lab05/img/lab/2/2b_campo_equipotencial.png", dpi=300)
plt.show()
