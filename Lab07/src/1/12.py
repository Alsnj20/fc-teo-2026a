import matplotlib.pyplot as plt
import numpy as np

plt.close("all")
fig, ax = plt.subplots(figsize=(10, 5))

a = 1.0
v = 1.0
tfin = 10.0
dt = 0.03

x_min = 0
x_max = 4 * a
x = np.arange(x_min, x_max, 0.002)

(line,) = ax.plot([], [], "b-", lw=2.5)
ax.set_xlim(x_min, x_max)
ax.set_ylim(-0.2 * a, a + 0.2 * a)

ax.set_aspect("equal", adjustable="box")
ax.set_xticks([0, a / 2, a, 1.5 * a, 2 * a, 2.5 * a, 3 * a, 3.5 * a, 4 * a])
ax.set_xticklabels(["0", "a/2", "a", "3a/2", "2a", "5a/2", "3a", "7a/2", "4a"])
ax.set_yticks([0, a])
ax.set_yticklabels(["0", "a"])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Onda Viajera Trapezoidal Periódica")
ax.grid(True, which="both", linestyle="--", linewidth=0.7)


def calcular_perfil_onda(x, t, a, v):
    periodo = 2 * a
    arg = (x - v * t) % periodo

    condiciones = [
        # Tramo constante alto (0 a a/2)
        (arg >= 0) & (arg < a / 2),
        # Bajada lineal (a/2 a a)
        (arg >= a / 2) & (arg < a),
        # Subida lineal (a a 3a/2)
        (arg >= a) & (arg < 1.5 * a),
        # Tramo constante alto (3a/2 a 2a)
        (arg >= 1.5 * a) & (arg <= 2 * a),
    ]

    funciones = [
        lambda u: a,
        lambda u: -2 * a / a * (u - a / 2) + a,
        lambda u: 2 * a / a * (u - a),
        lambda u: a,
    ]

    return np.piecewise(arg, condiciones, funciones)


for t in np.arange(0, tfin, dt):
    y = calcular_perfil_onda(x, t, a, v)
    line.set_data(x, y)
    plt.draw()
    plt.pause(0.01)
plt.ioff()
plt.savefig("Lab07/img/lab/1/12_onda_viajera.png", dpi=300)
plt.show()
