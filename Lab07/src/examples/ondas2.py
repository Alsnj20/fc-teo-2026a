import matplotlib.pyplot as plt
import numpy as np

# clc, clear, clf, hold off (En Python se maneja creando una figura nueva)
plt.close("all")  # Cierra ventanas anteriores
plt.figure()  # Crea una nueva figura

# Condiciones Iniciales
t = 0
x = 0
v = 0.5
tfin = 1000
xi = 0

# Inicio de la Simulacion onda inicial
n = 0
xf = 6
m = 1

px = []
py = []

# En Python el límite superior en arange no se incluye,
# sumamos 0.01 para que llegue exactamente a 6 como en MATLAB
for x in np.arange(0, xf + 0.01, 0.01):
    n = n + 1
    if (x >= 0) and (x <= 3):
        y = -(x - v * t)
    else:
        y = -(x - v * t) + 6
    px.append(x)
    py.append(y)

# longitud de onda (En Python, 'x' mantiene el último valor del ciclo)
lo = x

plt.plot(px, py)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")

# periodo
p = lo / v
no = 0

# El ciclo for en Python con saltos se hace con range(inicio, fin + paso, paso)
for t in np.arange(p, tfin + p, p):
    n = 0
    px = []
    py = []
    no = no + 1

    # Calculamos los límites del rango para x
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

    plt.plot(px, py)


plt.xlim([(no - 2) * (lo - 0.1), (no + 1) * (lo - 0.1)])
plt.ylim([0, 4])
plt.pause(0.05)
# Mostrar la gráfica final (equivalente a mantener la ventana abierta)
plt.show()
