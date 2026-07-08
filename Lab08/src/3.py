import matplotlib.pyplot as plt
import numpy as np

veces = 50
m = 100000

ax, bx = 0, 2
ay, by = -4, 0
az, bz = 0, 6

sa = 0
saa = 0

for k in range(veces):
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)
    z = np.random.uniform(az, bz, m)

    condicion = x**2 / 4 + y**2 / 16 + z**2 / 36 <= 1

    n = np.sum(condicion)

    volumen = n * (bx - ax) * (by - ay) * (bz - az) / m

    sa += volumen
    saa += volumen**2

prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)
m_graf = 15000

x = np.random.uniform(ax, bx, m_graf)
y = np.random.uniform(ay, by, m_graf)
z = np.random.uniform(az, bz, m_graf)

condicion = x**2 / 4 + y**2 / 16 + z**2 / 36 <= 1

u = np.linspace(0, np.pi / 2, 60)
v = np.linspace(np.pi, 2 * np.pi, 60)

u, v = np.meshgrid(u, v)

X = 2 * np.sin(u) * np.cos(v)
Y = 4 * np.sin(u) * np.sin(v)
Z = 6 * np.cos(u)

# Gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax3d = fig.add_subplot(111, projection="3d")
ax3d.scatter(x[condicion], y[condicion], z[condicion], s=2, color="red")
ax3d.set_xlabel("x")
ax3d.set_ylabel("y")
ax3d.set_zlabel("z")
ax3d.set_title("Elipsoide en el octante x>0, y<0, z>0")
plt.savefig("Lab08/img/lab/3.png", dpi=300)
plt.show()
print("Volumen estimado =", prom)
print("Desviación =", desv)
print("Volumen exacto =", 8 * np.pi)
