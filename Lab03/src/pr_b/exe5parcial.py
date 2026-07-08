import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# 1. GENERACIÓN DE DATOS (MÉTODO DE EULER / DISCRETO)
# =====================================================================
dt = 0.01  # Paso de tiempo
t_tramo1 = np.arange(0, 2, dt)  # de t=0 a t=2 (sin incluir el 2 exacto)
t_tramo2 = np.arange(2, 4 + dt, dt)  # de t=2 a t=4

# Tramo 1: v = -20 m/s, x empieza en -10 m
v1 = np.full_like(t_tramo1, -20.0)
x1 = -10.0 + v1 * t_tramo1  # x(t) = x0 + v*t -> va de -10 a -50

# Tramo 2: v = +10 m/s, x empieza en -50 m (posición al final del tramo 1)
v2 = np.full_like(t_tramo2, 10.0)
x2 = -50.0 + v2 * (t_tramo2 - 2.0)  # x(t) = -50 + 10*(t - 2) -> va de -50 a -30

# Unimos los tramos para las líneas continuas
# (Nota: No los unimos directamente en una sola línea para evitar que Matplotlib
# dibuje una diagonal sólida en el salto; el salto lo haremos a mano)

# =====================================================================
# 2. GRAFICAR EL ESPACIO DE FASES (v vs x)
# =====================================================================
plt.figure(figsize=(8, 6))

# Dibujamos el Tramo 1 (Línea horizontal a v = -20)
plt.plot(x1, v1, color="blue", linewidth=2.5, label="Tramo 1 (t: 0s a 2s)")

# Dibujamos el Salto en x = -50 (Línea discontinua vertical)
# Va desde v = -20 hasta v = 10
plt.plot(
    [-50, -50],
    [-20, 10],
    color="red",
    linestyle="--",
    linewidth=2,
    label="Salto instantáneo (t = 2s)",
)

# Dibujamos el Tramo 2 (Línea horizontal a v = 10)
plt.plot(x2, v2, color="green", linewidth=2.5, label="Tramo 2 (t: 2s a 4s)")

# Añadimos flechas para indicar el sentido del movimiento en el espacio de fases
plt.annotate(
    "",
    xy=(-30, -20),
    xytext=(-20, -20),
    arrowprops=dict(arrowstyle="->", color="blue", lw=2),
)
plt.annotate(
    "",
    xy=(-40, 10),
    xytext=(-45, 10),
    arrowprops=dict(arrowstyle="->", color="green", lw=2),
)

# =====================================================================
# 3. DETALLES ESTÉTICOS DEL GRÁFICO
# =====================================================================
plt.title("Espacio de Fases $v - x$", fontsize=14, fontweight="bold")
plt.xlabel("Posición $x$ (m)", fontsize=12)
plt.ylabel("Velocidad $v$ (m/s)", fontsize=12)

# Configuramos los límites de los ejes para que se vea holgado y limpio
plt.xlim(-60, 0)
plt.ylim(-30, 20)

# Dibujamos las líneas de los ejes coordenados (x=0 e y=0) si entran en el rango
plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
plt.axvline(0, color="black", linewidth=0.8, linestyle=":")

# Activamos la cuadrícula (grid) similar a las de tus laboratorios
plt.grid(True, linestyle="--", alpha=0.6)

# Mostramos la leyenda para identificar cada parte
plt.legend(loc="best")

# Mostramos el gráfico en pantalla
plt.show()
