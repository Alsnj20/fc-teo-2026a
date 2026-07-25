import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema (MAS: a = -(k/m) * x, w = sqrt(k/m))
k = 0.1
m = 200
w = np.sqrt(k / m)

def mas(t, x, v):
    return -(k / m) * x

# Condiciones iniciales
n = 0
t = 0
x = 1
v = 0

nsub = 100
tfin = 100

pt = [t]
pv = [v]
px = [x]
h = 2 * np.pi / (nsub * w)

while t < tfin:
    n = n + 1
    for i in range(nsub):
        a = mas(t, x, v)
        k1 = h * a

        a = mas(t + 0.5 * h, x + 0.5 * h * v, v + 0.5 * k1)
        k2 = h * a

        a = mas(t + 0.5 * h, x + 0.5 * h * (v + 0.5 * k1), v + 0.5 * k2)
        k3 = h * a

        a = mas(t + h, x + h * v + h * k2 * 0.5, v + k3)
        k4 = h * a

        x = x + h * v + h * (k1 + k2 + k3) / 6
        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

    px.append(x)
    pv.append(v)

# Grafica
plt.plot(px, pv, ".")
plt.title("MAS: x vs v")
plt.grid(True)
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")
pad = 0.5
plt.xlim(px[-1] - pad, px[-1] + pad)
plt.ylim(pv[-1] - pad, pv[-1] + pad)
plt.savefig("Lab11/img/lab/exe4.png", dpi=300)
plt.show()
