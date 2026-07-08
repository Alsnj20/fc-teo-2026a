import matplotlib.pyplot as plt
import numpy as np

veces = 50
m = 10000

ay = 2 - np.sqrt(6)
by = 2 + np.sqrt(6)

ax = -1
bx = 6

sa = 0
saa = 0

px_all = []
py_all = []

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)

    condicion = (x >= y**2 / 2 - y) & (x <= y + 1)

    n = np.sum(condicion)

    px_all.extend(x[condicion])
    py_all.extend(y[condicion])

    area = n * (bx - ax) * (by - ay) / m

    sa += area
    saa += area**2

prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)

y_curva = np.linspace(ay, by, 500)
x_parabola = y_curva**2 / 2 - y_curva
x_recta = y_curva + 1

# Gráfico
plt.figure(figsize=(8, 6))

# Región encerrada
plt.fill_betweenx(
    y_curva, x_parabola, x_recta, color="purple", alpha=0.5, label="Área buscada"
)

# Parábola
plt.plot(x_parabola, y_curva, color="blue", linewidth=2, label=r"$x=\frac{y^2}{2}-y$")

# Recta
plt.plot(x_recta, y_curva, color="red", linewidth=2, label=r"$x=y+1$")

# Puntos Monte Carlo
plt.scatter(
    px_all, py_all, s=1, marker=".", color="purple", alpha=0.4, label="Puntos aceptados"
)

plt.title("Método de Monte Carlo")
plt.xlabel("x")
plt.ylabel("y")

plt.text(0.2, by + 0.2, f"Área ≈ {prom:.4f} ± {desv:.4f}")

plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("Lab08/img/lab/1_monte_carlo.png", dpi=300)
plt.show()

print("Área estimada =", prom)
print("Desviación =", desv)
print("Área exacta =", 4 * np.sqrt(6))
