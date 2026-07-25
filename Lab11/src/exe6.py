import matplotlib.pyplot as plt
import numpy as np

# Oscilador: a = x - x^3 - c*v
c = 0.1

def hf(t, x, v, c):
    return x - x**3 - c * v

def rk4(t, x, v, h, c):
    k1 = h * hf(t, x, v, c)
    k2 = h * hf(t + h / 2, x + h / 2 * v, v + k1 / 2, c)
    k3 = h * hf(t + h / 2, x + h / 2 * v + h / 4 * k1, v + k2 / 2, c)
    k4 = h * hf(t + h, x + h * v + h / 2 * k2, v + k3, c)

    x = x + h * v + h * (k1 + k2 + k3) / 6
    v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, v

# --- Problema 1 (a = x - x^3, sin amortiguar): medir el periodo ---
# de la oscilacion acotada dentro de un pozo para buscar un w
# adecuado y de ahi aproximar el h de muestreo.
hp = 0.001
xp, vp, tp = 0.5, 0.0, 0.0
cruces = []

while len(cruces) < 2:
    xp2, vp2 = rk4(tp, xp, vp, hp, 0)
    if vp * vp2 < 0:
        # interpolacion lineal para el instante exacto del cruce v = 0
        t_cruce = tp + hp * (-vp) / (vp2 - vp)
        cruces.append(t_cruce)
    xp, vp, tp = xp2, vp2, tp + hp

T = cruces[1]  # segundo cruce por v=0: periodo completo
w = 2 * np.pi / T
print(f"Periodo medido (problema 1): T = {T:.4f}  ->  w = {w:.4f}")

nsub = 50
n_periodos = 50
tfin = n_periodos * T
h = T / nsub

t = 0
x = 0.5
v = 0.0

px = [x]
pv = [v]

while t < tfin:
    x, v = rk4(t, x, v, h, c)
    t = t + h
    px.append(x)
    pv.append(v)

# Grafica: solo los puntos (sin lineas) trazando el espiral
plt.plot(px, pv, ".")
plt.title("Seccion de Poincare: a = x - x^3 - c*v")
plt.grid(True)
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")
plt.savefig("Lab11/img/lab/exe6.png", dpi=300)
plt.show()
