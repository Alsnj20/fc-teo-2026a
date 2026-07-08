import matplotlib.pyplot as plt
import numpy as np

# 1. clear, clf, hold off;
plt.close("all")  # Cierra ventanas anteriores
plt.figure()  # Crea una nueva figura para limpiar pantalla

# % Condiciones Iniciales
t = 0
x_val = 0  # Se usa x_val para no confundir con el iterador x
v = 0.5
tfin = 2000
xi = 0

# % Inicio de la Simulacion onda inicial
n = 0
xf = 6
m = 1

px = []
py = []

# Nota: En MATLAB, '0:.01:xf' incluye el extremo final xf.
# Usamos np.arange y sumamos un pequeño paso para asegurar que incluya xf.
for x in np.arange(0, xf + 0.01, 0.01):
    n = n + 1
    if (x >= 0) and (x <= 3):
        y = +(x - v * t)
    else:
        y = -(x - v * t) + 6

    px.append(x)
    py.append(y)

# % longitud de onda
lo = x  # Guarda el último valor de x de la iteración anterior

# Primera gráfica estática
plt.plot(px, py)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
# En matplotlib, 'hold on' es el comportamiento por defecto hasta que se cierre la figura.

# % periodo
p = lo / v
no = 0

# Bucle principal de simulación temporal
# t va desde p hasta tfin con pasos de p
for t in np.arange(p, tfin + p, p):
    n = 0
    px = []
    py = []
    no = no + 1

    # Bucle espacial variable para el tren de ondas
    start_x = no * lo
    end_x = (no + 1) * lo

    for x in np.arange(start_x, end_x + 0.01, 0.01):
        n = n + 1
        if (x >= no * lo) and (x <= no * lo + lo / 2):
            y = +(x - v * t)
        else:
            y = -(x - v * t) + 6

        px.append(x)
        py.append(y)

    # Graficado de la simulación en movimiento
    plt.plot(px, py, "b")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")

    # Configuración de los límites dinámicos de los ejes (Línea 38 del código original)
    plt.xlim([(no - 2) * (lo - 0.1), (no + 1) * (lo - 0.1)])
    plt.ylim([0, 4])

    # Pausa interactiva para renderizar la animación en tiempo real
    plt.pause(0.05)

# Mantiene la ventana abierta al finalizar
plt.show()
