import matplotlib.pyplot as plt
import numpy as np

c = 0.05
h = 0.005
tfin = 60

# Ecuacion del oscilador (aceleracion)
def hf(t, x, v):
    return x - x**3 - c * v

# Metodo RK4 para el oscilador de duffing
def rk4(t, x, v, h):

    k1 = h * hf(t, x, v)
    k2 = h * hf(t + h / 2, x + h / 2 * v, v + k1 / 2)
    k3 = h * hf(t + h / 2, x + h / 2 * v + h / 4 * k1, v + k2 / 2)
    k4 = h * hf(t + h, x + h * v + h / 2 * k2, v + k3)

    x = x + h * v + h * (k1 + k2 + k3) / 6
    v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, v

def simular(x0, v0):
    t = 0
    x = x0
    v = v0

    pt = [t]
    px = [x]
    pv = [v]
    pa = [hf(t, x, v)]

    for t in np.arange(0, tfin, h):
        x, v = rk4(t, x, v, h)

        pt.append(t)
        px.append(x)
        pv.append(v)
        pa.append(hf(t, x, v))

    return pt, px, pv, pa


pt, px, pv, pa = simular(0.0, -1.2)  # termina en el pozo derecho (x = 1)
pt, pxL, pvL, pa = simular(0.0, 1.2)  # termina en el pozo izquierdo (x = -1)

# Graficas
plt.figure(figsize=(15, 8))

# Grafica 1: x vs t
plt.subplot(2, 3, 1)
plt.plot(pt, px, color="blue")
plt.title("x vs t")
plt.xlabel("t")
plt.ylabel("x")
plt.grid(True)

# Grafica 2: v vs t
plt.subplot(2, 3, 2)
plt.plot(pt, pv, color="red")
plt.title("v vs t")
plt.xlabel("t")
plt.ylabel("v")
plt.grid(True)

# Grafica 3: a vs t
plt.subplot(2, 3, 3)
plt.plot(pt, pa, color="green")
plt.title("a vs t")
plt.xlabel("t")
plt.ylabel("a")
plt.grid(True)

# Grafica 4: x vs v, espiral final a la derecha (x = 1)
plt.subplot(2, 3, 4, projection="3d")
plt.plot(px, pv, pt, color="purple")
plt.title("x vs v vs t (espiral derecha)")
plt.xlabel("x")
plt.ylabel("v")
plt.grid(True)

# Grafica 5: x vs v, espiral final a la izquierda (x = -1)
plt.subplot(2, 3, 5, projection="3d")
plt.plot(px, pv, pt, color="orange")
plt.title("x vs v vs t (espiral izquierda)")
plt.xlabel("x")
plt.ylabel("v")
plt.grid(True)

plt.tight_layout()
plt.savefig("Lab11/img/lab/exe2.png", dpi=300)
plt.show()
