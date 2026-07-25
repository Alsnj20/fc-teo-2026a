import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
r = 28
b = 8 / 3
sigma = 10

h = 0.01
tfin = 30

# Condiciones iniciales
t = 0
# x = Intensidad del movimiento en el eje x
x = 1
# y = Diferencias de temperatura en el eje y
y = 1
# z = Distribucion vertical de la temperatura en el eje z
z = 1

# Listas para almacenar resultados
pt = [t]
px = [x]
py = [y]
pz = [z]

for t in np.arange(0, tfin, h):
    # Ecuaciones de Lorenz (Euler)

    dx = sigma * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z

    # Método de Euler
    x = x + h * dx
    y = y + h * dy
    z = z + h * dz

    # Guardar resultados
    pt.append(t)
    px.append(x)
    py.append(y)
    pz.append(z)

# Graficas
plt.figure(figsize=(12, 8))

# Grafica 1: x vs y
plt.subplot(2, 2, 1)
plt.plot(px, py, color="blue")
plt.title("x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Grafica 2: x vs z
plt.subplot(2, 2, 2)
plt.plot(px, pz, color="red")
plt.title("x vs z")
plt.xlabel("x")
plt.ylabel("z")
plt.grid(True)

# Grafica 3: y vs z
plt.subplot(2, 2, 3)
plt.plot(py, pz, color="green")
plt.title("y vs z")
plt.xlabel("y")
plt.ylabel("z")
plt.grid(True)

# Grafica 4: Atractor de Lorenz (x,z)
plt.subplot(2, 2, 4)
plt.plot(px, pz, color="purple")
plt.title("Atractor de Lorenz")
plt.xlabel("x")
plt.ylabel("z")
plt.grid(True)

plt.tight_layout()
plt.gca().set_aspect("equal", adjustable="box")

plt.savefig("Lab10/img/lab/1.png", dpi=300)
plt.show()
