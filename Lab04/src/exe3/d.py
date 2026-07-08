import matplotlib.pyplot as plt
import numpy as np

h = 0.01
tfin = 100
m = 0.5

K, C = 0.1, 0.15
F0, W = 0.01, 0.2


def axi(x, vx, t):
    return (-K * x - C * vx + F0 * np.cos(W * t)) / m


def main():
    fig, o_ax = plt.subplots(figsize=(10, 8))
    x, vx = -1, 0.0
    px = []
    t_array = np.arange(0, tfin, h)

    # Con F0
    for t in t_array:
        ax = axi(x, vx, t)
        vx += ax * h
        x += vx * h
        px.append(x)

    o_ax.plot(t_array, px, label="Con F0")

    # Sin F0
    global F0
    F0 = 0
    x, vx = -1, 0.0
    px2 = []

    point_marked = False

    for n, t in enumerate(t_array):
        ax = axi(x, vx, t)
        vx += ax * h
        x += vx * h

        px2.append(x)

        if not point_marked and t > 5.0:
            diferencia_actual = px[n] - px2[n]
            diferencia_previa = px[n - 1] - px2[n - 1]

            if np.sign(diferencia_actual) != np.sign(diferencia_previa):
                o_ax.plot(
                    t,
                    px[n],
                    "ro",
                    markersize=8,
                    label=f"Cruce en t={t:.2f}s, x={px[n]:.2f}",
                )
                point_marked = True

    o_ax.plot(t_array, px2, label="Sin F0")

    o_ax.set_xlabel("Tiempo (s)")
    o_ax.set_title("Posición, Velocidad y Aceleración")
    o_ax.set_xlim(0, 20)
    o_ax.legend()
    o_ax.grid()

    plt.savefig("img/lab/exe3/d.png")
    plt.show()


if __name__ == "__main__":
    main()
