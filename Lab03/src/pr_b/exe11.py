import matplotlib.pyplot as plt
import numpy as np

# Datos iniciales
b1, c1 = 3, -2
r = 1.0

h = 0.1
tfin = 30.0


plt.rcParams.update({"font.size": 8, "lines.linewidth": 0.8})
plt.figure(figsize=(8, 8))

# Dibujar la circunferencia
theta = np.linspace(0, 2 * np.pi, 100)
x_circ = b1 + np.cos(theta)
y_circ = c1 + np.sin(theta)
plt.plot(x_circ, y_circ, "black", linewidth=2, label=f"Masa1 en ({b1}, {c1})")


# def ax(x, y, xc, yc):
#     dx = x - xc
#     dy = y - yc
#     r3 = (dx**2 + dy**2) ** 1.5
#     return -dx / r3


# def ay(x, y, xc, yc):
#     dx = x - xc
#     dy = y - yc
#     r3 = (dx**2 + dy**2) ** 1.5
#     return -dy / r3


# Funciones de aceleración
def ax(x, y):
    if x == 0 and y == 0:
        return 0
    return -x / ((x**2 + y**2) ** (3 / 2))


def ay(x, y):
    if x == 0 and y == 0:
        return 0
    return -y / ((x**2 + y**2) ** (3 / 2))


for vx0 in np.arange(0.1, 1.5, h):
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
plt.title("Laboratorio 3 - Ejercicio 1")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.show()


# EXE 6
# # # Prueba 1
# tfin = 150
# x0, y0 = 0.0, 7.0
# vx0, vy0 = 0.62, 0.45

# # Choques con 1ra circunferencia
# h = 0.01
# tfin = 150
# x0, y0 = 0.0, 5.0
# vx0, vy0 = 0.005, -0.1

# PRUEBA2: Choques con 2da circunferencia
# r = 1.0
# h = 0.01
# tfin = 800
# x0, y0 = 0.0, -7.0
# vx0, vy0 = 0.04264, 0.0
