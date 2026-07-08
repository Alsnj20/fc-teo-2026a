import matplotlib.pyplot as plt
import numpy as np

# Condiciones de simulación
h = 0.0001
tfin = 20
m = 0.2

# COnstantes
K = 0.1
C = 0
F0 = 0
W = 0


t = 0
x = -2.0
vx = 0.0


def axi(x, v, t):
    return (-K * x - C * v + F0 * np.cos(W * t)) / m


def EK(vx):
    return 0.5 * m * vx**2


def EU(x):
    return 0.5 * K * x**2


def ET(ek, eu):
    return ek + eu


# --- Listas para almacenar los resultados ---
px = []
pek = []
peu = []
pet = []

# --- Ciclo de simulación (Método de Euler) ---
for t in np.arange(0, tfin, h):
    ax = axi(x, vx, t)
    vx = vx + h * ax
    x = x + h * vx

    ek = EK(vx)
    eu = EU(x)
    et = ET(ek, eu)
    # Guardar datos
    px.append(x)
    pek.append(ek)
    peu.append(eu)
    pet.append(et)

# --- Gráficas ---
plt.figure(figsize=(12, 8))

# EN UN SOLO GRÁFICo

plt.plot(px, pek, label="Energía Cinética", color="blue")
plt.plot(px, peu, label="Energía Potencial", color="orange")
plt.plot(px, pet, label="Energía Total", color="green")
plt.title("Energía Cinética, Energía Potencial y Energía Total vs Posición")
plt.xlabel("Posición (m)")
plt.ylabel("Energía (J)")
plt.legend()
plt.grid(True)

# Ajustar márgenes y guardar
plt.tight_layout()
plt.savefig("img/lab/exe1/b.png")
plt.show()
