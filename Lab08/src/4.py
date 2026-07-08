import matplotlib.pyplot as plt
import numpy as np


# Newton-Raphson
def f(x):
    return np.exp(x - 3) - np.log(x)


def df(x):
    return np.exp(x - 3) - 1 / x


def newton(x0, tol=1e-12, maxiter=100):

    x = x0

    for _ in range(maxiter):
        xn = x - f(x) / df(x)
        if abs(xn - x) < tol:
            return xn
        x = xn
    return x


x1 = newton(1.7)
x2 = newton(np.e - 0.1)

print(f"Intersección 1", x1)
print(f"Intersección 2", x2)


# Monte Carlo
veces = 50
m = 100000

ax = x1
bx = x2

ay = np.exp(x1 - 3)
by = np.log(x2)

sa = 0
saa = 0

px_all = []
py_all = []

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)

    condicion = (y >= np.exp(x - 3)) & (y <= np.log(x))

    n = np.sum(condicion)

    px_all.extend(x[condicion])
    py_all.extend(y[condicion])

    area = n * (bx - ax) * (by - ay) / m

    sa += area
    saa += area**2

prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)


xg = np.linspace(0.8, 4.5, 2000)
y_exp = np.exp(xg - 3)
y_log = np.log(xg)
x_area = np.linspace(x1, x2, 2000)
m_graf = 5000

x_mc = np.random.uniform(ax, bx, m_graf)
y_mc = np.random.uniform(ay, by, m_graf)

cond_mc = (y_mc >= np.exp(x_mc - 3)) & (y_mc <= np.log(x_mc))

# Dentro
px = x_mc[cond_mc]
py = y_mc[cond_mc]

# Fuera
pxf = x_mc[~cond_mc]
pyf = y_mc[~cond_mc]

# Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(px, py, s=12, color="purple", alpha=0.8, marker="o", label="Dentro")
plt.plot(xg, y_exp, color="blue", linewidth=3, label=r"$y=e^{x-3}$")
plt.plot(xg, y_log, color="red", linewidth=3, label=r"$y=\ln(x)$")
plt.scatter(
    [x1, x2],
    [ay, by],
    color="magenta",
    s=120,
    zorder=10,
    label="Intersecciones",
)
plt.annotate(
    f"({x1:.4f}, {ay:.4f})", (x1, ay), xytext=(10, 10), textcoords="offset points"
)
plt.annotate(
    f"({x2:.4f}, {by:.4f})", (x2, by), xytext=(10, 10), textcoords="offset points"
)
plt.xlim(0.8, 4.5)
plt.ylim(-0.3, 1.7)
plt.grid(True)
plt.legend()
plt.title("Área entre $e^{x-3}$ y $\\ln(x)$")
plt.savefig("Lab08/img/lab/4.png", dpi=300)
plt.show()
