import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
c = 0.24
b = 1
d = 1
f = 0.68
w = 1.7


def duffing(t, x, v, c, b, d, f, w):
    return b * x - d * x**3 - c * v + f * np.cos(w * t)

# Condiciones iniciales
n = 0
m = 20
t = 0
x = 1
v = -1
tfin = 10000

# Inicio de la simulacion
pt = [t]
pv = [v]
px = [x]
h = 2 * np.pi / (w * m)

while t < tfin:
    n = n + 1
    for i in range(m):
        a = duffing(t, x, v, c, b, d, f, w)
        k1 = h * a

        a = duffing(t + 0.5 * h, x + 0.5 * h * v, v + 0.5 * k1, c, b, d, f, w)
        k2 = h * a

        a = duffing(
            t + 0.5 * h, x + 0.5 * h * (v + 0.5 * k1), v + 0.5 * k2, c, b, d, f, w
        )
        k3 = h * a

        a = duffing(t + h, x + h * v + h * k2 * 0.5, v + k3, c, b, d, f, w)
        k4 = h * a

        x = x + h * v + h * (k1 + k2 + k3) / 6
        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

        if x > np.pi:
            x = x - 2 * np.pi
        if x < -np.pi:
            x = x + 2 * np.pi

    px.append(x)
    pv.append(v)

# Graficas
plt.figure(figsize=(8, 6))
plt.plot(px, pv, ".")
plt.grid(True)
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")
plt.title("Diagrama de fase del oscilador de Duffing")
plt.savefig("Lab11/img/lab/exe3.png", dpi=300)

plt.show()
