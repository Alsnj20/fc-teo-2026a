import matplotlib.pyplot as plt
import numpy as np

# Parámetros
h = 0.01
tfin = 100
m, K, C = 0.5, 0.1, 0.15
F0, W = 0.01, 0.2
x0, v0 = -1.0, 0.0

# Simulación CON Fuerza
t_arr = np.arange(0, tfin, h)
px_con, x, v = [], x0, v0
for t in t_arr:
    a = (-K * x - C * v + F0 * np.cos(W * t)) / m
    v += a * h
    x += v * h
    px_con.append(x)

# Simulación SIN Fuerza
px_sin, x, v = [], x0, v0
for t in t_arr:
    a = (-K * x - C * v) / m
    v += a * h
    x += v * h
    px_sin.append(x)

plt.figure(figsize=(10, 5))
plt.plot(t_arr, px_con, label="Con Fuerza Externa", color="blue")
plt.plot(t_arr, px_sin, label="Sin Fuerza Externa", color="red", linestyle="--")
plt.title("Simulación: Con vs Sin Fuerza Externa")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid(True)
plt.legend()
plt.savefig("img/lab/exe3/a.png")
plt.show()
