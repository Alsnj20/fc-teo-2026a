import matplotlib.pyplot as plt
import numpy as np

k = 1.0
lado = 0.01 / np.sqrt(2)

# Valores de las 4 cargas
q1 = +1.0
q2 = +1.0
q3 = +1.0
q4 = -1.0

x1, y1 = lado, 0.0
x2, y2 = 0.0, lado
x3, y3 = -lado, 0.0
x4, y4 = 0.0, -lado

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


# Calcular el campo eléctrico
# Campo debido a Carga 1
r1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
r1 = np.where(r1 == 0, 1e-12, r1)
Ex1 = k * q1 * (x - x1) / r1**3
Ey1 = k * q1 * (y - y1) / r1**3

# Campo debido a Carga 2
r2 = np.sqrt((x - x2) ** 2 + (y - y2) ** 2)
r2 = np.where(r2 == 0, 1e-12, r2)
Ex2 = k * q2 * (x - x2) / r2**3
Ey2 = k * q2 * (y - y2) / r2**3

# Campo debido a Carga 3
r3 = np.sqrt((x - x3) ** 2 + (y - y3) ** 2)
r3 = np.where(r3 == 0, 1e-12, r3)
Ex3 = k * q3 * (x - x3) / r3**3
Ey3 = k * q3 * (y - y3) / r3**3

# Campo debido a Carga 4
r4 = np.sqrt((x - x4) ** 2 + (y - y4) ** 2)
r4 = np.where(r4 == 0, 1e-12, r4)
Ex4 = k * q4 * (x - x4) / r4**3
Ey4 = k * q4 * (y - y4) / r4**3

Ex_total = Ex1 + Ex2 + Ex3 + Ex4
Ey_total = Ey1 + Ey2 + Ey3 + Ey4

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

plt.title("Ejercicio 1(a): Cargas Positivas")
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.grid(True, alpha=0.2)
plt.savefig("Lab05/img/lab/1/1a_cargas_positivas.png", dpi=300)
plt.show()
