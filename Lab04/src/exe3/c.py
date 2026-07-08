import matplotlib.pyplot as plt
import numpy as np

h = 0.01
tfin = 60
m = 0.5

K, C = 0.1, 0.05
F0, W = 0.01, 0.2

x, v = -1.0, 0.0


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


def axisf(x, v, t):
    return (-K * x - C * v) / m


# Con fuerza externa
pt, px, pv = [], [], []
for t in np.arange(0, tfin, h):
    a = axi(x, v, t)
    v += a * h
    x += v * h
    pt.append(t)
    px.append(x)
    pv.append(v)

# Sin fuerza externa
pt2, px2, pv2 = [], [], []
x1, v1 = -1.0, 0.0
for t in np.arange(0, tfin, h):
    a = axisf(x1, v1, t)
    v1 += a * h
    x1 += v1 * h
    pt2.append(t)
    px2.append(x1)
    pv2.append(v1)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot(px, pv, pt, color="blue", label="Con FO")
ax.plot(px2, pv2, pt2, color="orange", label="Sin FO")
ax.set_xlabel("Posición (x)")
ax.set_ylabel("Velocidad (v)")
ax.set_zlabel("Tiempo (t)")
ax.legend()
plt.title("Gráfica 3D: v - x - t")
plt.savefig("img/lab/exe3/c.png")
plt.show()
