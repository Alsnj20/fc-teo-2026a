import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 8, "lines.linewidth": 0.8})
plt.figure(figsize=(8, 8))

# Datos iniciales
r = 1.0
h = 0.0025
k = 0.01
tfin = 300

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


def ax(x, y, xc1, yc1, xc2, yc2):
    den1 = ((x - xc1) ** 2 + (y - yc1) ** 2) ** (3 / 2)
    den2 = ((x - xc2) ** 2 + (y - yc2) ** 2) ** (3 / 2)
    if den1 == 0 or den2 == 0:
        return 0.0
    return (-(x - xc1) / den1) - ((x - xc2) / den2)


def ay(x, y, xc1, yc1, xc2, yc2):
    den1 = ((x - xc1) ** 2 + (y - yc1) ** 2) ** (3 / 2)
    den2 = ((x - xc2) ** 2 + (y - yc2) ** 2) ** (3 / 2)

    if den1 == 0 or den2 == 0:
        return 0.0
    return (-(y - yc1) / den1) - ((y - yc2) / den2)


contador = 0

for vx0 in np.linspace(0.01, 3, int(3 / k)):
    if contador >= 4:
        break

    x, y = 0.0, 7.0
    vx, vy = vx0, 0

    px = [x]
    py = [y]

    seEscapo = False
    colapso = False

    for t in np.arange(0, tfin, h):
        if (
            np.sqrt((x - b1) ** 2 + (y - c1) ** 2) <= r
            or np.sqrt((x - b2) ** 2 + (y - c2) ** 2) <= r
        ):
            colapso = True
            break

        if abs(y) > 50 or abs(x) > 50:
            seEscapo = True
            break

        vx += ax(x, y, b1, c1, b2, c2) * h
        vy += ay(x, y, b1, c1, b2, c2) * h
        x += vx * h
        y += vy * h

        px.append(x)
        py.append(y)

    if not seEscapo and not colapso:
        plt.plot(px, py, label=f"Trayectoria {contador + 1}")
        contador += 1

# Configuración de la gráfica
plt.title("Laboratorio 3 - Ejercicio 5")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(False)
plt.legend(loc="upper right")
plt.gca().set_aspect("equal", adjustable="box")
plt.savefig("img/pr_b/exe5.png", dpi=300, bbox_inches="tight")
plt.show()
