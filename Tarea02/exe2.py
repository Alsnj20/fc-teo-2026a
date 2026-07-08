import matplotlib.pyplot as plt
import numpy as np

"""
2 Movimiento de 2 cuerpos
Aplicar el movimiento de 2 cuerpos con datos reales. El famoso cuerpo celeste Atlas que vino de alg´un lugar de la V´ıa L´actea paso por el Sol y luego sigui´o su camino al infinito. De las diapositivas referente a este tema, considere la constante de gravitaci´on, masa del Sol, radio del Sol y encuentre la
trayectoria de Atlas al pasar por el Sol. Hay datos sobre la velocidad de Atlas en Internet. Que tipo
de trayectoria es?
"""

# 1. CONSTANTES FÍSICAS UNIVERSALES
G = 6.67430e-11
M_SOL = 1.98847e30
R_SOL = 6.957e8
AU = 1.496e11

# Factor para la aceleracion
GM = G * M_SOL

# 2. CONDICIONES INICIALES (Atlas viniendo desde lejos)
x = -6 * AU
y = 1.356 * AU
vx = 57700.0  # Velocidad de aproximación (57.7 km/s)
vy = 0.0

h = 3600 * 2  # Paso de tiempo: 2 horas
tfin = 3600 * 24 * 365 * 1.2  # Simulación por 1.2 años


# 3. FUNCIONES DE ACELERACIÓN
def ax(x, y):
    r = np.sqrt(x**2 + y**2)
    return -GM * x / (r**3)


def ay(x, y):
    r = np.sqrt(x**2 + y**2)
    return -GM * y / (r**3)


# 4. SIMULACIÓN
px, py = [x], [y]

distancia_minima = float("inf")
punto_perihelio = (0, 0)
v_perihelio_detectada = 0

for t in np.arange(0, tfin, h):
    r_actual = np.sqrt(x**2 + y**2)

    # Detectar el punto más cercano (Perihelio)
    if r_actual < distancia_minima:
        distancia_minima = r_actual
        punto_perihelio = (x, y)
        v_perihelio_detectada = np.sqrt(vx**2 + vy**2)

    vx += ax(x, y) * h
    vy += ay(x, y) * h
    x += vx * h
    y += vy * h

    px.append(x)
    py.append(y)

# 5. GRÁFICA
plt.figure(figsize=(12, 7))
px_au = np.array(px) / AU
py_au = np.array(py) / AU

plt.plot(0, 0, "yo", markersize=15, label="Sol")
plt.plot(px_au, py_au, "r-", alpha=0.7, label="Trayectoria de 3I/ATLAS")

peri_x_au = punto_perihelio[0] / AU
peri_y_au = punto_perihelio[1] / AU
plt.scatter(
    peri_x_au,
    peri_y_au,
    color="blue",
    s=100,
    zorder=5,
    label="Perihelio (Aproximación máxima)",
)

plt.title("Trayectoria Hiperbólica de 3I/ATLAS cruzando el Sistema Solar")
plt.xlabel("Eje X (AU)")
plt.ylabel("Eje Y (AU)")
plt.xlim(-5)
plt.grid(False)
plt.legend()
plt.gca().set_aspect("equal")
plt.savefig("trayectoria_atlas.png", dpi=300)
plt.show()


# Si llego a ser orbita
