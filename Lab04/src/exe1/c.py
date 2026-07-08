import matplotlib.pyplot as plt
import numpy as np

# Condiciones de simulación
h = 0.01
tfin = 60
m = 0.2

# COnstantes
K = 0.1
C = 0
F0 = 0
W = 0

t = 0
x = -2.0
vx = 0.0


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


# --- Listas para almacenar los resultados ---
px = []
pvx = []
# --- Ciclo de simulación (Método de Euler) ---
for t in np.arange(0, tfin, h):
    ax = axi(x, vx, t)
    vx = vx + ax * h
    x = x + vx * h

    # Guardar datos
    px.append(x)
    pvx.append(vx)

# --- Gráficas ---
fig = plt.figure(figsize=(12, 8))
plano3d = fig.add_subplot(111, projection="3d")
plano3d.plot(pvx, px, np.arange(0, tfin, h))
plano3d.set_xlabel("Velocidad (vx)")
plano3d.set_ylabel("Posición (x)")
plano3d.set_zlabel("Tiempo (t)")
plano3d.set_title("Posición y velocidad en función del tiempo")
plano3d.grid(True)

# Ajustar márgenes y guardar
plt.tight_layout()
plt.savefig("img/lab/exe1/c.png")
plt.show()
