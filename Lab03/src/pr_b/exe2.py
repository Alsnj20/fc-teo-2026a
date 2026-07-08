import matplotlib.pyplot as plt
import numpy as np

# Datos iniciales
r = 1.0
h = 0.1
k = 0.1
tfin = 30.0

plt.rcParams.update({"font.size": 8, "lines.linewidth": 0.8})
plt.figure(figsize=(12, 6))

# Circunferencia 1
b1, c1 = 3, -2
theta = np.linspace(0, 2 * np.pi, 100)
x_circ = b1 + np.cos(theta)
y_circ = c1 + np.sin(theta)
plt.plot(x_circ, y_circ, "black", linewidth=2, label=f"Masa1 en ({b1}, {c1})")

# Circunferencia 2
b2, c2 = -3, -2
x_circ2 = b2 + np.cos(theta)
y_circ2 = c2 + np.sin(theta)
plt.plot(x_circ2, y_circ2, "black", linewidth=2, label=f"Masa2 en ({b2}, {c2})")


# Funciones de aceleración
def ax(x, y):
    if x == 0 and y == 0:
        return 0
    return -x / ((x**2 + y**2) ** (3 / 2))


def ay(x, y):
    if x == 0 and y == 0:
        return 0
    return -y / ((x**2 + y**2) ** (3 / 2))


for vx0 in np.arange(0.2, 1.5, k):
    x, y = 0.0, -4.0
    vx, vy = vx0, 0.0

    px = [x]
    py = [y]

    for t in np.arange(0, tfin, h):
        vx += ax(x, y) * h
        vy += ay(x, y) * h

        x += vx * h
        y += vy * h

        px.append(x)
        py.append(y)

    plt.plot(px, py)

# Configuración de la gráfica
plt.title("Laboratorio 3 - Ejercicio 2")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(False)
plt.legend()
plt.gca().set_aspect("equal", adjustable="datalim")
plt.savefig("img/pr_b/exe2.png", dpi=300, bbox_inches="tight")
plt.show()
