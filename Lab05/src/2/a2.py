import matplotlib.pyplot as plt
import numpy as np

k = 1.0
lado = 0.01 / np.sqrt(2)

# VALORES DE LAS 4 CARGAS
q1, q2, q3, q4 = +1.0, -1.0, +1.0, +1.0

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

xa = np.linspace(-0.012, 0.012, 100)
ya = np.linspace(-0.012, 0.012, 100)
x, y = np.meshgrid(xa, ya)

z = np.zeros_like(x)
Ex_total = np.zeros_like(x)
Ey_total = np.zeros_like(y)

for carga in cargas:
    qi = carga["q"]
    xi = carga["x"]
    yi = carga["y"]

    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2)
    r = np.where(r == 0, 1e-12, r)

    z += k * qi / r

    # Acumulamos Campo Eléctrico (Vectorial)
    Ex_total += k * qi * (x - xi) / r**3
    Ey_total += k * qi * (y - yi) / r**3

magnitud = np.sqrt(Ex_total**2 + Ey_total**2)
magnitud = np.where(magnitud == 0, 1e-12, magnitud)

Ex_norm = Ex_total / magnitud
Ey_norm = Ey_total / magnitud

zmax = np.max(z)
zmin = np.min(z)

z_min_plot = np.percentile(z, 1)
z_max_plot = np.percentile(z, 99.7)

dz = (z_max_plot - z_min_plot) / 45
nivel = np.arange(z_min_plot, z_max_plot + dz, dz)

# Graficar
plt.figure(figsize=(10, 10))
plt.plot([x1, x2], [y1, y2], "k--", alpha=0.4, linewidth=1.2)
plt.plot([x2, x3], [y2, y3], "k--", alpha=0.4, linewidth=1.2)
plt.plot([x3, x4], [y3, y4], "k--", alpha=0.4, linewidth=1.2)
plt.plot([x4, x1], [y4, y1], "k--", alpha=0.4, linewidth=1.2)

# 1. Graficar líneas equipotenciales (Contornos)
plt.contour(x, y, z, levels=nivel, cmap="jet")

# 2. Graficar flechas del campo eléctrico PERFECTAMENTE NORMALIZADAS
plt.quiver(x, y, Ex_norm, Ey_norm, color="blue", pivot="middle", scale=25, alpha=0.8)

# Dibujar las cargas dinámicamente desde la lista
for carga in cargas:
    color = "ro" if carga["q"] > 0 else "bo"
    plt.plot(carga["x"], carga["y"], color, markersize=9)


plt.title("Ejercicio 2(a): Líneas Equipotenciales y Campo Eléctrico - Cuadrupolo")
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.gca().set_aspect("equal", adjustable="box")
plt.colorbar(label="Potencial Eléctrico (V)")
plt.grid(True, alpha=0.2)
plt.show()
