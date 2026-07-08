import matplotlib.pyplot as plt
import numpy as np

h = 0.01
tfin = 100
m, K, C = 0.5, 0.1, 0.15
F0, W = 0.01, 0.2
x0, v0 = -1.0, 0.0

# COn FO
pt, px, pv, pa = [], [], [], []
# Sin FO
pt2, px2, pv2, pa2 = [], [], [], []


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


def axisf(x, v, t):
    return (-K * x - C * v) / m


for t in np.arange(0, tfin, h):
    a = axi(x0, v0, t)
    v0 += a * h
    x0 += v0 * h
    pt.append(t)
    px.append(x0)
    pv.append(v0)
    pa.append(a)

# Simulación sin fuerza externa
x1, v1 = -1.0, 0.0
for t in np.arange(0, tfin, h):
    a = axisf(x1, v1, t)
    v1 += a * h
    x1 += v1 * h
    pt2.append(t)
    px2.append(x1)
    pv2.append(v1)
    pa2.append(a)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(pt, px, color="blue")
plt.title("Posición vs Tiempo")
plt.plot(pt2, px2, color="red", linestyle="--")

plt.subplot(2, 2, 2)
plt.plot(pt, pv, color="orange")
plt.title("Velocidad vs Tiempo")
plt.plot(pt2, pv2, color="green", linestyle="--")

plt.subplot(2, 2, 3)
plt.plot(pt, pa, color="red")
plt.title("Aceleración vs Tiempo")
plt.plot(pt2, pa2, color="purple", linestyle="--")

plt.subplot(2, 2, 4)
plt.plot(px, pv, color="blue")
plt.title("Velocidad vs Posición")
plt.plot(px2, pv2, color="green", linestyle="--")
for ax in plt.gcf().get_axes():
    ax.grid(True)
plt.tight_layout()
plt.title("Simulación con Fuerza Externa")
plt.savefig("img/lab/exe3/b.png")
plt.show()
