import matplotlib.pyplot as plt
import numpy as np

# Configuración del dominio y parámetros
x_min = 0
x_max = 10
v = 1.0
tfin = 10.0
dt = 0.5  # Paso temporal

fig, ax = plt.subplots()

# Bucle externo: Controla el TIEMPO (t)
for t in np.arange(0, tfin, dt):
    px = []
    py = []

    # Bucle interno: Controla el ESPACIO (x)
    # Recorremos el dominio de x_min a x_max
    for x in np.arange(x_min, x_max, 0.05):
        # 'xi' es la posición relativa a la onda (x - vt)
        periodo = 5.0
        xi = (x - v * t) % periodo

        # Definición de la forma de onda mediante condiciones
        if xi > 1:
            y = -0.75 * (xi) + 15 / 4
        else:
            y = 3 * xi

        px.append(x)
        py.append(y)

    # Graficación
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.5, 3.5)
    ax.grid(True)
    ax.plot(px, py, "purple")
    plt.title(f"Tiempo t = {t:.1f}")

    plt.pause(0.05)  # Pausa necesaria para ver la animación

plt.show()
