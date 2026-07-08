import matplotlib.pyplot as plt
import numpy as np

# Constantes
sigma = 10
r = 28
b = 8 / 3
h = 0.01
tfin = 50

# Condiciones iniciales
x0 = 5
y0 = 5
z0 = 25


# Funciones de Lorenz
def fx(x, y):
    return sigma * (y - x)


def fy(x, y, z):
    return x * (r - z) - y


def fz(x, y, z):
    return x * y - b * z


# Método RK4
def rk4(x, y, z, h):

    # k1
    k1x = fx(x, y)
    k1y = fy(x, y, z)
    k1z = fz(x, y, z)

    # k2
    k2x = fx(x + h * k1x / 2, y + h * k1y / 2)
    k2y = fy(x + h * k1x / 2, y + h * k1y / 2, z + h * k1z / 2)
    k2z = fz(x + h * k1x / 2, y + h * k1y / 2, z + h * k1z / 2)

    # k3
    k3x = fx(x + h * k2x / 2, y + h * k2y / 2)
    k3y = fy(x + h * k2x / 2, y + h * k2y / 2, z + h * k2z / 2)
    k3z = fz(x + h * k2x / 2, y + h * k2y / 2, z + h * k2z / 2)

    # k4
    k4x = fx(x + h * k3x, y + h * k3y)
    k4y = fy(x + h * k3x, y + h * k3y, z + h * k3z)
    k4z = fz(x + h * k3x, y + h * k3y, z + h * k3z)

    # Actualización
    x = x + h * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    y = y + h * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
    z = z + h * (k1z + 2 * k2z + 2 * k3z + k4z) / 6

    return x, y, z


# Euler
t = 0
x = x0
y = y0
z = z0

pt = [t]
pxE = [x]
pyE = [y]
pzE = [z]

for _ in np.arange(0, tfin, h):
    dx = fx(x, y)
    dy = fy(x, y, z)
    dz = fz(x, y, z)

    x = x + h * dx
    y = y + h * dy
    z = z + h * dz

    t = t + h

    pt.append(t)
    pxE.append(x)
    pyE.append(y)
    pzE.append(z)

# RK4
x = x0
y = y0
z = z0

pxR = [x]
pyR = [y]
pzR = [z]

for _ in np.arange(0, tfin, h):
    x, y, z = rk4(x, y, z, h)

    pxR.append(x)
    pyR.append(y)
    pzR.append(z)

print("Metricas: Euler vs RK4")
plt.figure(figsize=(10, 12))
# x vs t
plt.subplot(3, 1, 1)
plt.plot(pt, pxE, label="Euler")
plt.plot(pt, pxR, "--", label="RK4")
plt.title("x vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("x")
plt.grid(True)
plt.legend()

# y vs tiempo
plt.subplot(3, 1, 2)
plt.plot(pt, pyE, label="Euler")
plt.plot(pt, pyR, "--", label="RK4")
plt.title("y vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# z vs tiempo
plt.subplot(3, 1, 3)
plt.plot(pt, pzE, label="Euler")
plt.plot(pt, pzR, "--", label="RK4")
plt.title("z vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("z")
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.savefig("Lab10/img/lab/4.png", dpi=300)
plt.show()
