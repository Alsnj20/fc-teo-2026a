import matplotlib.pyplot as plt
import numpy as np

plt.close("all")
plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))

a = 1.0
v = 1.0
tfin = 10.0
dt = 0.03

x_min = 0
x_max = 4 * a
x = np.arange(x_min, x_max, 0.005)

(line,) = ax.plot([], [], "b-", lw=2.5)
ax.set_xlim(x_min, x_max)
ax.set_ylim(-0.2, a + 0.2)

ax.set_aspect("equal", adjustable="box")

ax.set_xticks(np.arange(x_min, x_max + 0.5, 0.5))
ax.set_yticks(np.arange(0, a + 0.5, 0.5))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Onda Viajera - Problema 1 (Grilla Simétrica Calibrada)")
ax.grid(True, which="both", linestyle="--", linewidth=0.7)

for t in np.arange(0, tfin, dt):
    argumento = (x - v * t) % a
    y = -argumento + a
    line.set_data(x, y)

    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.savefig("Lab07/img/lab/1/11_onda_viajera.png", dpi=300)
plt.show()
