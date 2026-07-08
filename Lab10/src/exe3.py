import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
sigma = 10
r = 28
b = 8 / 3

# Tiempo
h = 0.01
tfin = 45

# Primera simulación
t = 0
x = 1
y = 1
z = 2.5

pt = [t]
px1 = [x]
py1 = [y]
pz1 = [z]

for t in np.arange(0, tfin, h):
    dx = sigma * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z

    x = x + h * dx
    y = y + h * dy
    z = z + h * dz

    pt.append(t)
    px1.append(x)
    py1.append(y)
    pz1.append(z)

# Segunda simulación
t = 0
x = 1
y = 1
z = 2.500000001

px2 = [x]
py2 = [y]
pz2 = [z]

for t in np.arange(0, tfin, h):
    dx = sigma * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z

    x = x + h * dx
    y = y + h * dy
    z = z + h * dz

    px2.append(x)
    py2.append(y)
    pz2.append(z)

# Gráficas
plt.figure(figsize=(10, 10))
# x vs t
plt.subplot(3, 1, 1)
plt.plot(pt, px1, label="z = 2.5")
plt.plot(pt, px2, "--", label="z = 2.500000001")
plt.title("x vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("x")
plt.grid(True)
plt.legend()

# y vs t
plt.subplot(3, 1, 2)
plt.plot(pt, py1, label="z = 2.5")
plt.plot(pt, py2, "--", label="z = 2.500000001")
plt.title("y vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# z vs t
plt.subplot(3, 1, 3)
plt.plot(pt, pz1, label="z = 2.5")
plt.plot(pt, pz2, "--", label="z = 2.500000001")
plt.title("z vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("z")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("Lab11/img/lab/3.png", dpi=300)
plt.show()
