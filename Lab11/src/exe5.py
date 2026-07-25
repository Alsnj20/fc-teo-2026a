import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema (movimiento subamortiguado)
k = 0.1
m = 200
c = 0.15

w0 = np.sqrt(k / m)
alpha = c / (2 * m)
w1 = np.sqrt(w0**2 - alpha**2)

def sub(t, x, v):
    return -(k / m) * x - (c / m) * v

# Condiciones iniciales
n = 0
nsub = 20
t = 0
x = 1
v = 1

# Se muestrea una vez por cada periodo amortiguado T1 = 2*pi/w1
n_periodos = 30
T1 = 2 * np.pi / w1
tfin = n_periodos * T1

# Inicio de la simulacion
pt = [t]
pv = [v]
px = [x]
h = 2 * np.pi / (nsub * w1)

while t < tfin:
    n = n + 1
    for i in range(nsub):
        a = sub(t, x, v)
        k1 = h * a

        a = sub(t + 0.5 * h, x + 0.5 * h * v, v + 0.5 * k1)
        k2 = h * a

        a = sub(t + 0.5 * h, x + 0.5 * h * (v + 0.5 * k1), v + 0.5 * k2)
        k3 = h * a

        a = sub(t + h, x + h * v + h * k2 * 0.5, v + k3)
        k4 = h * a

        x = x + h * v + h * (k1 + k2 + k3) / 6
        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = t + h

    px.append(x)
    pv.append(v)

# Grafica: solo los puntos de la seccion de Poincare (sin el espiral)
plt.plot(px, pv, ".")
plt.title("Seccion de Poincare: movimiento subamortiguado")
plt.grid(True)
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")
plt.savefig("Lab11/img/lab/exe5.png", dpi=300)
plt.show()
