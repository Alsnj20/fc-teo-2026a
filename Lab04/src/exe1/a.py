import matplotlib.pyplot as plt
import numpy as np

# Variables de simulación
h = 0.01
tfin = 20

m = 0.2

# Constantes
K = 0.1
C = 0
F0 = 0
W = 0


def axi(x, vx, t):
    return (-K * x - C * vx + F0 * np.cos(W * t)) / m


def main():
    x, vx = -2.0, 0.0
    pax, pvx, px = [], [], []
    t_array = np.arange(0, tfin, h)
    for t in t_array:
        ax = axi(x, vx, t)
        vx += ax * h
        x += vx * h
        pax.append(ax)
        pvx.append(vx)
        px.append(x)

    plt.figure(figsize=(12, 8))

    # Gráfica 1: Posición vs Tiempo (Fila 2, Columnas 2, Posición 1)
    plt.subplot(2, 2, 1)
    plt.plot(t_array, px, color="green")
    plt.title("Posición vs Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")
    plt.grid(True)

    # Gráfica 2: Velocidad vs Tiempo (Fila 2, Columnas 2, Posición 2)
    plt.subplot(2, 2, 2)
    plt.plot(t_array, pvx, color="blue")
    plt.title("Velocidad vs Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.grid(True)

    # Gráfica 3: Aceleración vs Tiempo (Fila 2, Columnas 2, Posición 3)
    plt.subplot(2, 2, 3)
    plt.plot(t_array, pax, color="red")
    plt.title("Aceleración vs Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Aceleración (m/s²)")
    plt.grid(True)

    # Gráfica 4: Velocidad vs Posición (Fila 2, Columnas 2, Posición 4)
    plt.subplot(2, 2, 4)
    plt.plot(px, pvx, color="purple")
    plt.title("Velocidad vs Posición")
    plt.xlabel("Posición (m)")
    plt.ylabel("Velocidad (m/s)")
    plt.grid(True)

    # Guardar y mostrar
    plt.savefig("img/lab/exe1/a.png")
    plt.show()


if __name__ == "__main__":
    main()
