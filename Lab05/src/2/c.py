import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

k = 1.0
L = 0.01
lado = L / np.sqrt(2)

# Cargas
q1, q2, q3, q4 = +1.0, -1.0, +1.0, -1.0

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

# 1. Definir el espacio para el gráfico 3D
xa = np.arange(-0.015, 0.015 + 0.0006, 0.0006)
ya = np.arange(-0.015, 0.015 + 0.0006, 0.0006)
x, y = np.meshgrid(xa, ya)

z = np.zeros_like(x)

for carga in cargas:
    qi = carga["q"]
    xi = carga["x"]
    yi = carga["y"]

    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2)
    r = np.where(r == 0, 1e-12, r)

    z += k * qi / r

z = np.clip(z, -800, 800)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_wireframe(x, y, z, color="purple", linewidth=0.5)

ax.set_title("Relieve 3D - Potencial Eléctrico Intercalado (+, -, +, -)")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Potencial (Z)")
ax.view_init(elev=25, azim=45)
plt.savefig("Lab05/img/lab/2/2c_relieve_3D.png", dpi=300)

plt.show()
