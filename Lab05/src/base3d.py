import matplotlib.pyplot as plt
import numpy as np

# 1. Definir el espacio para el gráfico 3D
xa = np.arange(-2.1, 2.12, 0.12)
ya = np.arange(-2.1, 2.12, 0.12)

k = 1.0
q1, q2 = 1.0, -1.0
x1, y1 = 1.0, 0.0
x2, y2 = -1.0, 0.0

x, y = np.meshgrid(xa, ya)

# 2. Calcular el potencial en 3D
z = k * q1 / np.sqrt((x - x1) ** 2 + y**2) + k * q2 / np.sqrt((x - x2) ** 2 + y**2)

# Para evitar que los picos infinitos arruinen la escala del gráfico 3D,
# limitamos (truncamos) los valores máximos y mínimos muy grandes.
z = np.clip(z, -10, 10)

# 3. Graficar la malla tridimensional "mesh"
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# plot_wireframe hace el mismo efecto de líneas de rejilla que 'mesh' de MATLAB
ax.plot_wireframe(x, y, z, color="blue", linewidth=0.5)

ax.set_title("Relieve del Potencial Eléctrico en 3D (base3d.m)")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Potencial (Z)")

plt.show()
