import matplotlib.pyplot as plt
import numpy as np

# 1. Definir el espacio
xa = np.arange(-3, 3.5, 0.5)
ya = np.arange(-3, 3.5, 0.5)

# Constante de Coulomb y cargas
k = 1.0
q1, q2 = -1.0, -1.0

# Posiciones de las cargas
x1, y1 = 1.0, 1.0
x2, y2 = -1.0, -1.0

# Crear la rejilla de puntos en el plano
x, y = np.meshgrid(xa, ya)

# 2. Calcular los componentes del Campo Eléctrico, para calcular la distancia
Ex = (
    k * q1 * (x - x1) / (((x - x1) ** 2 + (y - y1) ** 2) ** 1.5)
    + k * q2 * (x - x2) / ((x - x2) ** 2 + (y - y2) ** 2) ** 1.5
)

Ey = (
    k * q1 * (y - y1) / ((x - x1) ** 2 + (y - y1) ** 2) ** 1.5
    + k * q2 * (y - y2) / ((x - x2) ** 2 + (y - y2) ** 2) ** 1.5
)

# 3. Graficar el campo vectorial
plt.figure()
plt.quiver(x, y, Ex, Ey)

# Configurar el gráfico
plt.gca().set_aspect("equal", adjustable="box")
plt.title("Campo Eléctrico Vectorial (base.m)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)
plt.show()
