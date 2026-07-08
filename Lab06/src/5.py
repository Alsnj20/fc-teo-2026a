import matplotlib.pyplot as plt
import numpy as np

MU0 = 4 * np.pi * 1e-7


def campo_espira_cuadrada(x, I, L):
    x = np.asarray(x, dtype=float)
    denominador = 2 * np.pi * (x**2 + L**2 / 4.0) * np.sqrt(x**2 + L**2 / 2.0)
    return (MU0 * I * L**2) / denominador


def campo_solenoide_cuadrado(x, I, L, n_espiras=20, separacion=None):
    """Suma de campos de n_espiras cuadradas ubicadas a lo largo del eje z."""
    if separacion is None:
        separacion = L / 2.0

    centros = (np.arange(n_espiras) - (n_espiras - 1) / 2.0) * separacion
    B_total = np.zeros_like(np.asarray(x, dtype=float))

    for z0 in centros:
        B_total += campo_espira_cuadrada(x - z0, I, L)

    return B_total, centros


def main():
    I = 1.0  # A
    L = 0.02  # m, lado de la espira cuadrada
    separacion = 0.005  # distancia entre espiras (d)

    x = np.linspace(-0.4, 0.4, 1200)

    lista_espiras = [1, 5, 10, 15, 20, 50]

    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    colores = ["red", "orange", "green", "blue", "purple", "brown"]

    for n_espiras, color in zip(lista_espiras, colores):
        B_solenoide, centros = campo_solenoide_cuadrado(
            x, I, L, n_espiras=n_espiras, separacion=separacion
        )

        # Imprimir resultados en la terminal
        B0_solenoide = float(
            campo_solenoide_cuadrado(0.0, I, L, n_espiras, separacion)[0]
        )
        print(f"B(0) solenoide con {n_espiras:2d} espiras = {B0_solenoide:.6e} T")

        # Graficar cada solenoide
        ax.plot(
            x,
            B_solenoide,
            label=f"Solenoide de {n_espiras} espiras",
            color=color,
            linewidth=2.2,
        )

    ax.set_title("Campo magnetico B en funcion de x (Efecto Meseta)")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("B (T)")
    ax.legend()
    ax.grid(True, alpha=0.35)
    ax.set_ylim(bottom=0)
    plt.savefig("Lab06/img/lab/5.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
