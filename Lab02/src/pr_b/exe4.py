from math import dist
from sre_compile import dis

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))

# Configuración inicial
h = 0.01
k = 0.05
tfin = 900
r = 3
centro_x, centro_y = 0, 1

circulo = plt.Circle(
    (centro_x, centro_y),
    r,
    color="black",
    fill=False,
    linestyle="-",
    linewidth=1.5,
    label="Circulo (r=3)",
)
plt.gca().add_patch(circulo)


def ax(x, y):
    return -(x) / ((x**2 + y**2) ** (3 / 2))


def ay(x, y):
    return -y / ((x**2 + y**2) ** (3 / 2))


# Listas para almacenar las trayectorias clasificadas
parabolas = []  # Velocidad Baja (Choque)
elipses = []  # Velocidad Media (Órbita)
hiperbolas = []  # Velocidad Alta (Escape)

# parabola_choque_1_x, parabola_choque_1_y = [], []
# parabola_choque_2_x, parabola_choque_2_y = [], []
# elipse_orbita_1_x, elipse_orbita_1_y = [], []
# elipse_orbita_2_x, elipse_orbita_2_y = [], []
# hiperbola_escape_1_x, hiperbola_escape_1_y = [], []
# hiperbola_escape_2_x, hiperbola_escape_2_y = [], []

for vx0 in np.arange(0.1, 3, 0.05):
    # Cambio: vx = vy
    vx = vx0
    vy = vx0
    x, y = 1.5, -8.0

    px = [x]
    py = [y]
    colisiono = False

    for t in np.arange(0, tfin, h):
        vx = vx + ax(x, y) * h
        vy = vy + ay(x, y) * h
        x = x + vx * h
        y = y + vy * h

        dist_obj = np.sqrt((x - centro_x) ** 2 + (y - centro_y) ** 2)

        if dist_obj <= r:
            px.append(x)
            py.append(y)
            colisiono = True
            break

        px.append(x)
        py.append(y)

        # if abs(x) > 100 or abs(y) > 100:
        #     break

    #  Clasificar
    dist_final = np.sqrt(x**2 + y**2)

    if colisiono:
        print(f"Colisionó con el círculo para vx0={vx0:.2f}")
        # if len(parabolas) < 3:
        #     parabolas.append((px, py))
    elif dist_final <= 20:  # Se mantiene cerca (Elipse)
        print(f"Distancia final: {dist_final:.2f} para vx0={vx0:.2f}")
        # if len(elipses) < 3:
        #     elipses.append((px, py))
    else:  # Escapa (Hiperbola)
        if len(hiperbolas) < 3:
            hiperbolas.append((px, py))

# -------- Gráficas --------
for p in parabolas:
    plt.plot(p[0], p[1], color="orange", label="Parábola (Baja/Choque)")
for e in elipses:
    plt.plot(e[0], e[1], color="purple", label="Elipse (Media/Órbita)")
for h_curv in hiperbolas:
    plt.plot(h_curv[0], h_curv[1], color="skyblue", label="Hipérbola (Alta/Escape)")

plt.title("Ejercicio-3: Efecto vx = vy (2 de cada tipo)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
# plt.gca().set_aspect("equal", adjustable="box")

# Evitar duplicados en la leyenda
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.savefig("TAREA-02/img/pr_b/exe4.png", dpi=300, bbox_inches="tight")
plt.show()
