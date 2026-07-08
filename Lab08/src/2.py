import matplotlib.pyplot as plt
import numpy as np

veces = 50
m = 10000

ax, bx = 0, 3
ay, by = 0, 9

sa = 0
saa = 0

px_all = []
py_all = []

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)

    condicion = (y >= x**3 / 3) & (y <= x**2)

    n = np.sum(condicion)

    px_all.extend(x[condicion])
    py_all.extend(y[condicion])

    area = n * (bx - ax) * (by - ay) / m

    sa += area
    saa += area**2

prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)
xg = np.linspace(0, 3, 1000)
y_parabola = xg**2
y_cubica = xg**3 / 3

# Gráfico
plt.figure(figsize=(8, 6))
plt.fill_between(
    xg, y_cubica, y_parabola, color="lightgreen", alpha=0.7, label="Área buscada"
)
plt.plot(xg, y_parabola, color="blue", linewidth=3, label=r"$y=x^2$")
plt.plot(xg, y_cubica, color="red", linewidth=3, label=r"$y=\frac{x^3}{3}$")
plt.scatter(
    px_all,
    py_all,
    s=1,
    color="purple",
    alpha=0.15,
    label="Puntos Monte Carlo",
    marker="o",
)
plt.scatter([0, 3], [0, 9], s=100, color="magenta", zorder=5, label="Intersecciones")
plt.text(0.1, 0.2, "(0,0)")
plt.text(3.02, 9, "(3,9)")
plt.title("Área entre $y=x^2$ y $y=x^3/3$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.text(0.2, 8.3, f"Área ≈ {prom:.4f} ± {desv:.4f}")
plt.savefig("Lab08/img/lab/2.png", dpi=300)
plt.show()

print("Área estimada =", prom)
print("Desviación =", desv)
print("Área exacta =", 9 / 4)
