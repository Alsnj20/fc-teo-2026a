import matplotlib.pyplot as plt
import numpy as np

# 1. Definición del espacio (35x35 mantiene una excelente densidad de flechas)
xa = np.linspace(-0.7, 0.7, 35)
ya = np.linspace(-0.7, 0.7, 35)
x, y = np.meshgrid(xa, ya)

# 2. Configurar el Hexágono de alambres
R = 0.4
theta = np.linspace(0, 2 * np.pi, 7)[:-1]

x_w = R * np.cos(theta)
y_w = R * np.sin(theta)

Q = np.array([1, -1, 1, -1, 1, -1])
Bx = np.zeros_like(x)
By = np.zeros_like(y)

# 3. Calcular el campo magnético
for xw, yw, curr in zip(x_w, y_w, Q):
    d_i = (x - xw) ** 2 + (y - yw) ** 2
    d_i = np.where(d_i < 1e-4, 1e-4, d_i)
    Bx += -curr * (y - yw) / d_i
    By += curr * (x - xw) / d_i

magnitud = np.sqrt(Bx**2 + By**2)
magnitud_segura = np.where(magnitud == 0, 1e-9, magnitud)

Ux = Bx / magnitud_segura
Uy = By / magnitud_segura

max_deseado = np.percentile(magnitud, 75)
min_deseado = max_deseado * 0.22

magnitud_estetica = np.clip(magnitud, min_deseado, max_deseado)

Bx_estetico = Ux * magnitud_estetica
By_estetico = Uy * magnitud_estetica

plt.figure(figsize=(9, 9))
plt.scatter(0, 0, color="black", s=100, label="Centro")
plt.scatter(x_w, y_w, color="purple", s=100, label="Alambres")
plt.quiver(
    x,
    y,
    Bx_estetico,
    By_estetico,
    color="purple",
    pivot="middle",
    scale=140,
    width=0.0026,
    headwidth=3.5,
    headlength=4.5,
)
plt.axis("square")
plt.title("Hexágono de Alambres Conductores (Centro Optimizado)")
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.xlim([-0.7, 0.7])
plt.ylim([-0.7, 0.7])
plt.legend(loc="upper right", framealpha=0.9)
plt.savefig("Lab06/img/lab/3.png", dpi=300, bbox_inches="tight")

try:
    plt.show()
except Exception as e:
    print("No se pudo mostrar el gráfico interactivo:", e)
