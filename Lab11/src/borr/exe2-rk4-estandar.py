import matplotlib.pyplot as plt
import numpy as np

# Oscilador: a = x - x^3 - c*v

c = 0.15
h = 0.001
tfin = 60


# Ecuaciones del oscilador
def fx(v):
    return v


def fa(x, v):
    return x - x**3 - c * v


# Metodo RK4
def rk4(x, v, h):

    # k1
    k1x = h * fx(v)
    k1v = h * fa(x, v)

    # k2
    k2x = h * fx(v + 0.5 * k1v)
    k2v = h * fa(x + 0.5 * k1x, v + 0.5 * k1v)

    # k3
    k3x = h * fx(v + 0.5 * k2v)
    k3v = h * fa(x + 0.5 * k2x, v + 0.5 * k2v)

    # k4
    k4x = h * fx(v + k3v)
    k4v = h * fa(x + k3x, v + k3v)

    # Actualizacion
    x = x + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    v = v + (k1v + 2 * k2v + 2 * k3v + k4v) / 6

    return x, v


# Condiciones iniciales
t = 0
# x = posicion
x = 0.5
# v = velocidad
v = 0

# Listas para almacenar resultados
pt = [t]
px = [x]
pv = [v]
pa = [fa(x, v)]

for t in np.arange(0, tfin, h):
    x, v = rk4(x, v, h)

    # Guardar resultados
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(fa(x, v))

# Graficas
plt.figure(figsize=(12, 8))

# Grafica 1: x vs t
plt.subplot(2, 2, 1)
plt.plot(pt, px, color="blue")
plt.title("x vs t")
plt.xlabel("t")
plt.ylabel("x")
plt.grid(True)

# Grafica 2: v vs t
plt.subplot(2, 2, 2)
plt.plot(pt, pv, color="red")
plt.title("v vs t")
plt.xlabel("t")
plt.ylabel("v")
plt.grid(True)

# Grafica 3: a vs t
plt.subplot(2, 2, 3)
plt.plot(pt, pa, color="green")
plt.title("a vs t")
plt.xlabel("t")
plt.ylabel("a")
plt.grid(True)

# Grafica 4: x vs v (diagrama de fase)
plt.subplot(2, 2, 4, projection="3d")
plt.plot(px, pv, pt, color="purple")
plt.title("x vs v vs t")
plt.xlabel("x")
plt.ylabel("v")
# plt.zlabel("t")
plt.grid(True)
plt.tight_layout()
# plt.savefig("Lab11/img/lab/exe2.png", dpi=300)
plt.show()
