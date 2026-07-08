import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

fig, ax = plt.subplots(figsize=(12, 5))

# Parámetros
a = 1.0
v = 1.0
tfin = 10
dt = 0.03

# Dominio espacial
x_min = -a
x_max = 5 * a
x = np.arange(x_min, x_max, 0.002)

(line,) = ax.plot([], [], "r-", lw=2.5)

ax.set_ylim(-1.2 * a, 1.2 * a)
ax.set_xticks([-a, 0, a, 2 * a, 3 * a, 4 * a])
ax.set_xticklabels(["-a", "0", "a", "2a", "3a", "4a"])
ax.set_yticks([-a, 0, a])
ax.set_yticklabels(["-a", "0", "a"])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Problema 2 - Onda Triangular Viajera")

ax.grid(True, linestyle="--", linewidth=0.7)


def calcular_perfil_onda_p2(x, t, a, v):

    T = 4 * a
    z = (x - v * t) % T

    condiciones = [
        # 0 -> a
        (z >= 0) & (z < a),
        # a -> 3a
        (z >= a) & (z < 3 * a),
        # 3a -> 4a
        (z >= 3 * a) & (z < 4 * a),
    ]

    funciones = [
        lambda z: z,
        lambda z: -z + 2 * a,
        lambda z: z - 4 * a,
    ]

    return np.piecewise(z, condiciones, funciones)


plt.ion()

for t in np.arange(0, tfin, dt):
    y = calcular_perfil_onda_p2(x, t, a, v)
    line.set_data(x, y)
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.savefig("Lab07/img/lab/2/23_onda_viajera.png", dpi=300)
plt.show()
