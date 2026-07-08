import matplotlib.pyplot as plt
import numpy as np

k = 1.0
lado = 0.01 / np.sqrt(2)

# VALORES DE LAS 4 CARGAS
q1 = -1.0
q2 = -1.0
q3 = -1.0
q4 = -1.0

x1, y1 = lado, 0.0
x2, y2 = 0.0, lado
x3, y3 = -lado, 0.0
x4, y4 = 0.0, -lado

cargas = [q1, q2, q3, q4]
posiciones_x = [x1, x2, x3, x4]
posiciones_y = [y1, y2, y3, y4]

# Comprobación de que los lados son iguales
lado12 = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
lado23 = np.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
lado34 = np.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
lado41 = np.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)

print("--- Comprobación de Lados (90°) ---")
print(f"Lado 1-2: {lado12 * 100:.2f} cm")
print(f"Lado 2-3: {lado23 * 100:.2f} cm")
print(f"Lado 3-4: {lado34 * 100:.2f} cm")
print(f"Lado 4-1: {lado41 * 100:.2f} cm\n")

# Definir el espacio
xa = np.linspace(-0.015, 0.015, 23)
ya = np.linspace(-0.015, 0.015, 23)
x, y = np.meshgrid(xa, ya)

Ex_total = np.zeros_like(x)
Ey_total = np.zeros_like(y)

for q_i, x_i, y_i in zip(cargas, posiciones_x, posiciones_y):
    r = np.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)
    r = np.where(r == 0, 1e-12, r)

    Ex_total += k * q_i * (x - x_i) / r**3
    Ey_total += k * q_i * (y - y_i) / r**3

# Normalizar el campo eléctrico
magnitud = np.sqrt(Ex_total**2 + Ey_total**2)
magnitud = np.where(magnitud == 0, 1e-12, magnitud)

Ex_norm = Ex_total / magnitud
Ey_norm = Ey_total / magnitud

# Grafica
fig, ax = plt.subplots(figsize=(7, 7))

ax.plot([x1, x2], [y1, y2], "k--", alpha=0.5, linewidth=1.5)
ax.plot([x2, x3], [y2, y3], "k--", alpha=0.5, linewidth=1.5)
ax.plot([x3, x4], [y3, y4], "k--", alpha=0.5, linewidth=1.5)
ax.plot([x4, x1], [y4, y1], "k--", alpha=0.5, linewidth=1.5)

ax.quiver(x, y, Ex_norm, Ey_norm, color="blue", pivot="middle", scale=25)

ax.plot(x1, y1, "ro", markersize=9, label="q1 (+)")
ax.plot(x2, y2, "ro", markersize=9, label="q2 (+)")
ax.plot(x3, y3, "ro", markersize=9, label="q3 (+)")
ax.plot(x4, y4, "ro", markersize=9, label="q4 (+)")

ax.set_aspect("equal", adjustable="box")

plt.title("Ejercicio 1(b): Cargas Negativas")
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.grid(True, alpha=0.2)
plt.savefig("Lab05/img/lab/1/1b_cargas_negativas.png", dpi=300)
plt.show()
