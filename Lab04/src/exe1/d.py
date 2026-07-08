import matplotlib.pyplot as plt
import numpy as np

# Condiciones de simulación
h = 0.001
tfin = 20
m = 0.2

# COnstantes
K = 0.1
C = 0
F0 = 0
W = 0


t = 0
x = 1
vx = 0.6


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


px = []
pvx = []
pax = []

for t in np.arange(0, tfin, h):
    ax = axi(x, vx, t)
    vx = vx + ax * h
    x = x + vx * h

    # Guardar datos
    px.append(x)
    pvx.append(vx)
    pax.append(ax)

# --- Gráficas ---
plt.figure(figsize=(12, 8))
plt.plot(np.arange(0, tfin, h), px, label="Posición (x)", color="black")
plt.plot(np.arange(0, tfin, h), pvx, label="Velocidad (vx)", color="green")
plt.plot(np.arange(0, tfin, h), pax, label="Aceleración (ax)", color="red")
plt.title("Posición, Velocidad y Aceleración vs Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()


# Ajustar márgenes y guardar
plt.tight_layout()
plt.savefig("img/lab/exe1/d.png", dpi=300)
plt.show()
