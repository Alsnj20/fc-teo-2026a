import matplotlib.pyplot as plt
import numpy as np

veces = 50
m = 100000

ax, bx = 0, 6
ay, by = 0, 4
az, bz = 0, 8

sa = 0
saa = 0

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)
    z = np.random.uniform(az, bz, m)

    condicion = (2 * x + 3 * y <= 12) & (z <= y**2 / 2)

    n = np.sum(condicion)

    volumen = n * (bx - ax) * (by - ay) * (bz - az) / m

    sa += volumen
    saa += volumen**2


prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)


print("Volumen estimado =", prom)
print("Desviación =", desv)
print("Volumen exacto =", 16)

cond = (2 * x + 3 * y <= 12) & (z <= y**2 / 2)
Y, X = np.meshgrid(np.linspace(0, 4, 100), np.linspace(0, 6, 100))
Z = Y**2 / 2
yp = np.linspace(0, 4, 100)
zp = np.linspace(0, 8, 100)
YP, ZP = np.meshgrid(yp, zp)
XP = (12 - 3 * YP) / 2

# Gráfico
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
# Techo parabólico
ax.plot_surface(X, Y, Z, alpha=0.4, color="skyblue")
# Plano inclinado
ax.plot_surface(XP, YP, ZP, alpha=0.3, color="gold")
# Puntos aceptados
ax.scatter(x[cond], y[cond], z[cond], s=1, color="red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Volumen limitado por 2x+3y=12 y z=y²/2")
ax.view_init(elev=25, azim=-55)
plt.savefig("Lab08/img/lab/5.png", dpi=300)
plt.show()
