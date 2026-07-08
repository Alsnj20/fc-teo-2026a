import matplotlib.pyplot as plt
import numpy as np

# Parámetros del problema
h = 0.01
tfin = 150
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
    # Integración de Euler
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

# --- Gráficas ---
plt.figure(figsize=(12, 8))

# Gráfico 1: Posición vs Tiempo (x - t)
plt.subplot(2, 2, 1)
plt.plot(pt, px, color="blue")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)  # Línea en x=0
plt.title("Posición vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid(True)

# Gráfico 2: Velocidad vs Tiempo (v - t)
plt.subplot(2, 2, 2)
plt.plot(pt, pv, color="orange")
plt.title("Velocidad vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)

# Gráfico 3: Aceleración vs Tiempo (a - t)
plt.subplot(2, 2, 3)
plt.plot(pt, pa, color="red")
plt.title("Aceleración vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s²)")
plt.grid(True)

# Gráfico 4: Velocidad vs Posición (v - x)
plt.subplot(2, 2, 4)
plt.plot(px, pv, color="green")
plt.title("Velocidad vs Posición (Espacio de Fase)")
plt.xlabel("Posición (m)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)

plt.tight_layout()
plt.savefig("img/lab/exe2/a.png")
plt.show()
