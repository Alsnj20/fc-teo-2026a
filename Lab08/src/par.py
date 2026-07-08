import matplotlib.pyplot as plt
import numpy as np

veces = 50
m = 10000

ax = 0
bx = 1
ay = np.exp(-1)
by = np.exp(1)

sa = 0
saa = 0

px_all = []
py_all = []

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)

    condicion = (y >= np.exp(-x)) & (y <= np.exp(x))

    n = np.sum(condicion)

    px_all.extend(x[condicion])
    py_all.extend(y[condicion])

    area = n * (bx - ax) * (by - ay) / m

    sa += area
    saa += area**2

prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)

plt.figure(figsize=(7, 7))
plt.scatter(px_all, py_all, s=1, color="purple")

plt.title("Monte Carlo: Área entre e^x y e^-x")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

print("Área estimada =", prom)
print("Desviación =", desv)

area_exacta = np.e + np.exp(-1) - 2
print("Área exacta =", area_exacta)
