import matplotlib.pyplot as plt
import numpy as np

h = 0.0001
tfin = 30

# Condiciones iniciales
t = 0
# x = posicion
x = np.sqrt(2)
# v = velocidad
v = 0

# Listas para almacenar resultados
pt = [t]
px = [x]
pv = [v]
pa = [x - x**3]

for t in np.arange(0, tfin, h):

    # Ecuacion del oscilador (Euler)
    a = x - x**3
    dx = v
    dv = a

    # Metodo de Euler
    x = x + h * dx
    v = v + h * dv

    # Guardar resultados
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(x - x**3)

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

# Grafica 4: en 3d
plt.subplot(2, 2, 4, projection="3d")
plt.plot(px, pv, pt, color="purple")
plt.title("x vs v vs t")
plt.xlabel("x")
plt.ylabel("v")

plt.grid(True)
plt.tight_layout()
plt.savefig("Lab11/img/lab/exe1.png", dpi=300)
plt.show()
