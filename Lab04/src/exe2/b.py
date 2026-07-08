import matplotlib.pyplot as plt
import numpy as np

# Parámetros del problema
h = 0.01
tfin = 200
m = 2
K = 0.1

# Constante de amortiguamiento
C = 0.199999
F0 = 0
W = 0

# Condiciones iniciales
t = 0.0
x = -2.0
vx = 0.0


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


# Listas para almacenar datos
pt = []
px = []
pv = []
pa = []

# Contador de cruces por cero
cruces = 0
x_anterior = x

# Simulación
for t in np.arange(0, tfin, h):
    a = axi(x, vx, t)
    vx = vx + a * h
    x = x + vx * h

    # Detectar cruces por x = 0
    if x_anterior * x < 0:
        cruces += 1

    x_anterior = x

    # Guardar datos
    pt.append(t)
    px.append(x)
    pv.append(vx)
    pa.append(a)

print(f"Total de veces que pasó por x=0: {cruces}")
print(f"Valor de C: {C}")

plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection="3d")
ax.plot(pv, px, pt, label="Trayectoria en el espacio de fases", color="blue")
ax.set_xlabel("Velocidad (vx)")
ax.set_ylabel("Posición (x)")
ax.set_title("Posición y velocidad en función del tiempo")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig("img/lab/exe2/b.png")
plt.show()
