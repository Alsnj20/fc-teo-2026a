import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

k = 1.0
longitud_alambre = 0.05  # 5 cm = 0.05 m
num_cargas = 100
q_total = 1.0
q_individual = q_total / num_cargas

# El alambre va desde -2.5 cm hasta +2.5 cm
x_inicio = -longitud_alambre / 2
x_fin = longitud_alambre / 2

x_cargas = np.linspace(x_inicio, x_fin, num_cargas)
y_cargas = np.zeros(num_cargas)

cargas = []
for i in range(num_cargas):
    cargas.append({"q": q_individual, "x": x_cargas[i], "y": y_cargas[i]})

xa = np.linspace(-0.04, 0.04, 29)
ya = np.linspace(-0.04, 0.04, 29)
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
z_max_plot = np.percentile(z, 85)

dz = (z_max_plot - z_min_plot) / 45
nivel = np.arange(z_min_plot, z_max_plot + dz, dz)

plt.figure(figsize=(11, 9))

plt.contour(x, y, z, levels=nivel, cmap="jet", alpha=0.6)
plt.quiver(x, y, Ex_norm, Ey_norm, color="blue", pivot="middle", scale=32, alpha=0.7)
for carga in cargas:
    plt.plot(carga["x"], carga["y"], "ro", markersize=3)
plt.plot([x_inicio, x_fin], [0, 0], "k-", alpha=0.5, linewidth=1.5)

plt.xlim(-0.035, 0.035)
plt.ylim(-0.035, 0.035)
plt.title(
    "Ejercicio 4: Alambre Recto de 5 cm (100 cargas uniformes) - Campo y Potencial"
)
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.gca().set_aspect("equal", adjustable="box")
plt.colorbar(label="Potencial Eléctrico (V)")
plt.grid(True, alpha=0.2)
plt.savefig("Lab05/img/lab/4/4a_campo_potencial.png", dpi=300)
plt.show()
