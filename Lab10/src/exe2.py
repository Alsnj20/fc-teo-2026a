import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
sigma = 10
r = 28
b = 8 / 3
h = 0.01

# Condiciones iniciales
t = 0
x = 1
y = 1
z = 1
tfin = 40

# Listas
pt = [t]
px = [x]
py = [y]
pz = [z]

# Método de Euler
for t in np.arange(0, tfin, h):
    dx = sigma * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z

    x = x + h * dx
    y = y + h * dy
    z = z + h * dz

    pt.append(t)
    px.append(x)
    py.append(y)
    pz.append(z)

# GRAFICAS
fig = plt.figure(
    figsize=(12, 8),
)

# x - y - t
ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.plot(px, py, pt)
ax.set_title("x - y - t")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Valor")
ax.grid(True)

# y - z - t
ax = fig.add_subplot(2, 2, 2, projection="3d")
ax.plot(py, pz, pt)
ax.set_title("y - z - t")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Valor")
ax.grid(True)

# x - z - t
ax = fig.add_subplot(2, 2, 3, projection="3d")
ax.plot(px, pz, pt)
ax.set_title("x - z - t")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Valor")
ax.grid(True)


# x - y - z (3D)
ax = fig.add_subplot(2, 2, 4, projection="3d")
ax.plot(px, py, pz)
ax.set_title("x - y - z")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.tight_layout()
plt.savefig("Lab10/img/lab/2.png", dpi=300)
plt.show()
