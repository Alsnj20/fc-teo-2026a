import matplotlib.pyplot as plt
import numpy as np

Eyo = 1.0
Ezo = 1.5
desfase = np.pi / 4

k = 1
xf = 10

x = np.linspace(0, xf, 400)

Ey = Eyo * np.cos(k * x)
Ez = Ezo * np.cos(k * x + desfase)

fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, Ey, Ez, linewidth=2)
xv = np.linspace(0, xf, 35)

Eyv = Eyo * np.cos(k * xv)
Ezv = Ezo * np.cos(k * xv + desfase)

ax.quiver(
    xv,
    np.zeros_like(xv),
    np.zeros_like(xv),
    np.zeros_like(xv),
    Eyv,
    Ezv,
    length=1,
    normalize=False,
)

ax.set_xlabel("x")
ax.set_ylabel("Ey")
ax.set_zlabel("Ez")
ax.set_title("Polarización Elíptica de una Onda Electromagnética")
ax.set_xlim(0, xf)
plt.savefig("Lab07/img/lab/5_polarizacion_eliptica.png", dpi=300)
plt.show()
