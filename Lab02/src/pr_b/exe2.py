import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 10))

# Configuración inicial
h = 0.01
k = 0.05
tfin = 200

# Datos de la circunferencia
r = 3
centro_x, centro_y = 0, 1

# Dibujar el círculo
circulo = plt.Circle(
    (centro_x, centro_y), r, color="black", fill=False, linestyle="-", linewidth=1.5
)
plt.gca().add_patch(circulo)


# Funciones de aceleración
def ax(x, y):
    return -(x - 1) / ((x**2 + y**2) ** (3 / 2))


def ay(x, y):
    return -y / ((x**2 + y**2) ** (3 / 2))


for vx0 in np.arange(0.01, 1.5, k):
    vx = vx0
    vy = 0.0
    x, y = 0.0, -4.0

    px = [x]
    py = [y]

    for t in np.arange(0, tfin, h):
        vx = vx + ax(x, y) * h
        vy = vy + ay(x, y) * h
        x = x + vx * h
        y = y + vy * h

        if np.sqrt((x - centro_x) ** 2 + (y - centro_y) ** 2) <= r:
            px.append(x)
            py.append(y)
            break

        px.append(x)
        py.append(y)

        if abs(x) > 30 or abs(y) > 30:
            break

    # Graficar cada trayectoria
    plt.plot(px, py, linewidth=1)

plt.title("Ejercicio 2 - Simulación de Colisión con Obstáculo Circular")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.gca().set_aspect("equal", adjustable="box")

plt.savefig("TAREA-02/img/pr_b/exe2.png", dpi=300, bbox_inches="tight")
plt.show()
