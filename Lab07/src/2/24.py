import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

fig, ax = plt.subplots(figsize=(12, 5))

# Parámetros
a = 1.0
v = 1.0
tfin = 10
dt = 0.03

x_min = 0
x_max = 6 * a

x = np.arange(x_min, x_max, 0.002)

(line,) = ax.plot([], [], "b-", lw=2.5)

ax.set_xlim(x_min, x_max)
ax.set_ylim(-0.05 * a, 1.2 * a)
ax.set_aspect("equal", adjustable="box")
ax.set_xticks([0, a / 2, a, 2 * a, 3 * a])
ax.set_xticklabels(["0", "a/2", "a", "2a", "3a"])
ax.set_yticks([0, a / 4, a])
ax.set_yticklabels(["0", "a/4", "a"])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Problema 2 - Onda Tipo Pirámide")
ax.grid(True, linestyle="--", linewidth=0.7)


def calcular_perfil_onda(x, t, a, v):
    T = 2 * a
    z = (x - v * t) % T

    condiciones = [
        # Tramo 1
        (z >= 0) & (z < a / 2),
        # Tramo 2
        (z >= a / 2) & (z < a),
        # Tramo 3
        (z >= a) & (z < 1.5 * a),
        # Tramo 4
        (z >= 1.5 * a) & (z < 2 * a),
    ]

    funciones = [
        # 0 -> a/4
        lambda z: 0.5 * z,
        # a/4 -> a
        lambda z: 1.5 * z - 0.5 * a,
        # a -> a/4
        lambda z: -1.5 * z + 2.5 * a,
        # a/4 -> 0
        lambda z: -0.5 * z + a,
    ]
    return np.piecewise(z, condiciones, funciones)


plt.ion()

for t in np.arange(0, tfin, dt):
    y = calcular_perfil_onda(x, t, a, v)
    line.set_data(x, y)
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.savefig("Lab07/img/lab/2/24_onda_tipo_piramide.png", dpi=300)
plt.show()
