import matplotlib.pyplot as plt
import numpy as np

# Parámetros generales
h = 0.01
tfin = 80.0

m1, m2 = 1.0, 1.0

# Condiciones iniciales
x0, vx0 = 1.0, 2.36
y0, vy0 = 1.0, 0.0


# --- 2. Función de Aceleración ---
def calcular_a(pos, k_m, m):
    """Calcula la aceleración a = -(k/m) * posicion"""
    return -(k_m / m) * pos


# Casos a fabricar (l, n)
casos = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 5), (5, 6)]

# --- 3. Ejecución y Graficación ---
plt.figure(figsize=(15, 10))

for i, (l, n) in enumerate(casos, 1):
    # k/m definidos por l^2 y n^2
    km1 = l**2
    km2 = n**2

    x, vx = x0, vx0
    y, vy = y0, vy0

    px, py = [], []

    for t in np.arange(0, tfin, h):
        ax = calcular_a(x, km1, m1)
        ay = calcular_a(y, km2, m2)

        vx += ax * h
        vy += ay * h
        x += vx * h
        y += vy * h

        px.append(x)
        py.append(y)

    # Crear Subplot para cada caso
    plt.subplot(3, 3, i)
    plt.plot(px, py, label=f"l={l}, n={n}", color="purple")
    plt.title(f"Figura de Lissajous: l={l}, n={n}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.axis("equal")

plt.tight_layout()
plt.savefig("img/lab/exe4/4_lissajous_figures.png")
plt.show()
