import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

# 1. Definir el espacio con pasos mucho más finos (0.051) para que las curvas se vean suaves
xa = np.arange(-3, 3.051, 0.051)
ya = np.arange(-3, 3.051, 0.051)

k = 1.0
# Dipolo: Carga positiva y carga negativa
q1, q2 = 1.0, -1.0

x1, y1 = 1.0, 1.0
x2, y2 = -1.0, -1.0

x, y = np.meshgrid(xa, ya)

# 2. Calcular el potencial eléctrico (z).
z = k * q1 / np.sqrt((x - x1) ** 2 + (y - y1) ** 2) + k * q2 / np.sqrt(
    (x - x2) ** 2 + (y - y2) ** 2
)

# 3. Definir los niveles de voltaje
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 50
# Filtramos valores extremadamente altos/bajos cerca de las cargas para que el gráfico sea legible
nivel = np.arange(zmin, zmax + dz, dz)

# 4.
plt.figure()
plt.contour(x, y, z, levels=nivel, cmap="jet")

plt.title("Líneas Equipotenciales - Dipolo (basecounter.m)")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect("equal", adjustable="box")
plt.colorbar(label="Potencial Eléctrico (V)")
plt.grid(True, alpha=0.3)
plt.show()
