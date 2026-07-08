import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

k = 1.0
L = 0.01
lado = L / np.sqrt(2)

x1, y1 = lado, 0.0
x2, y2 = 0.0, lado
x3, y3 = -lado, 0.0
x4, y4 = 0.0, -lado

num_cargas_por_lado = 8
q = 1.0

t = np.linspace(0, 1, num_cargas_por_lado, endpoint=False)

x_lado = x1 + t * (x2 - x1)
y_lado = y1 + t * (y2 - y1)

cargas = []

# Lado 1: De Vértice 1 a Vértice 2
for i in range(num_cargas_por_lado):
    cargas.append({"q": q, "x": x_lado[i], "y": y_lado[i]})

# Lado 2: De Vértice 2 a Vértice 3
for i in range(num_cargas_por_lado):
    x_c = x2 + t[i] * (x3 - x2)
    y_c = y2 + t[i] * (y3 - y2)
    cargas.append({"q": q, "x": x_c, "y": y_c})

# Lado 3: De Vértice 3 a Vértice 4
for i in range(num_cargas_por_lado):
    x_c = x3 + t[i] * (x4 - x3)
    y_c = y3 + t[i] * (y4 - y3)
    cargas.append({"q": q, "x": x_c, "y": y_c})

# Lado 4: De Vértice 4 a Vértice 1
for i in range(num_cargas_por_lado):
    x_c = x4 + t[i] * (x1 - x4)
    y_c = y4 + t[i] * (y1 - y4)
    cargas.append({"q": q, "x": x_c, "y": y_c})


xa = np.linspace(-0.015, 0.015, 27)
ya = np.linspace(-0.015, 0.015, 27)
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
    Ex_total += k * qi * (x - xi) / r**3
    Ey_total += k * qi * (y - yi) / r**3

magnitud = np.sqrt(Ex_total**2 + Ey_total**2)
magnitud = np.where(magnitud == 0, 1e-12, magnitud)

Ex_norm = Ex_total / magnitud
Ey_norm = Ey_total / magnitud

z_min_plot = np.percentile(z, 5)
z_max_plot = np.percentile(z, 88)

dz = (z_max_plot - z_min_plot) / 45
nivel = np.arange(z_min_plot, z_max_plot + dz, dz)


plt.figure(figsize=(10, 10))

plt.plot([x1, x2], [y1, y2], "k--", alpha=0.3, linewidth=1.0)
plt.plot([x2, x3], [y2, y3], "k--", alpha=0.3, linewidth=1.0)
plt.plot([x3, x4], [y3, y4], "k--", alpha=0.3, linewidth=1.0)
plt.plot([x4, x1], [y4, y1], "k--", alpha=0.3, linewidth=1.0)

plt.contour(x, y, z, levels=nivel, cmap="jet", alpha=0.6)

plt.quiver(x, y, Ex_norm, Ey_norm, color="blue", pivot="middle", scale=28, alpha=0.7)

for carga in cargas:
    color = "ro" if carga["q"] > 0 else "bo"
    plt.plot(carga["x"], carga["y"], color, markersize=5)

plt.xlim(-0.013, 0.013)
plt.ylim(-0.013, 0.013)
plt.title("Ejercicio 3(a): Espira Rómbica (8 cargas por lado) - Campo y Potencial 2D")
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.gca().set_aspect("equal", adjustable="box")
plt.colorbar(label="Potencial Eléctrico (V)")
plt.grid(True, alpha=0.2)
plt.savefig("Lab05/img/lab/3/3a_campo_potencial.png", dpi=300)
plt.show()
