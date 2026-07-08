import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
plt.figure(figsize=(10, 8))

# Datos iniciales
r = 1.0

h = 0.01
tfin = 800
x0, y0 = 0.0, 7.0
vx0, vy0 = 0.00000080, 0.00000001

# Posiciones de las masas
b1, c1 = 3, -2
b2, c2 = -3, -2

# Dibujar masas
theta = np.linspace(0, 2 * np.pi, 100)
plt.plot(b1 + np.cos(theta), c1 + np.sin(theta), "black", label="Masa 1")
plt.plot(b2 + np.cos(theta), c2 + np.sin(theta), "black", label="Masa 2")


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


# Definimos las dos naves
naves = [
    {"x": x0, "y": y0, "color": "blue", "label": "Nave A (x)"},
    {"x": x0 + 0.01, "y": y0, "color": "red", "label": "Nave B (x + 0.01)"},
]

for nave in naves:
    x, y = nave["x"], nave["y"]
    vx, vy = vx0, vy0
    tray_x, tray_y = [x], [y]

    for t in np.arange(0, tfin, h):
        acx = ax(x, y, b1, c1, b2, c2)
        acy = ay(x, y, b1, c1, b2, c2)
        vx += acx * h
        vy += acy * h
        x += vx * h
        y += vy * h
        tray_x.append(x)
        tray_y.append(y)

        dist1 = np.sqrt((x - b1) ** 2 + (y - c1) ** 2)
        dist2 = np.sqrt((x - b2) ** 2 + (y - c2) ** 2)

        if dist1 <= r or dist2 <= r:
            break

    plt.plot(tray_x, tray_y, color=nave["color"], label=nave["label"], alpha=0.8)

plt.title("Ejercicio 6: Trayectorias y naves")
plt.legend()
plt.grid(True)
plt.gca().set_aspect("equal")
plt.savefig("img/pr_b/exe6.png", dpi=300)
plt.show()
