import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
plt.figure(figsize=(8, 8))
n = 0
h = 0.01
k = 0.05
tfin = 30

# Funciones de aceleración
def ax(x, y):
    return -x / ((x**2 + y**2)**(3/2))

def ay(x, y):
    return -y / ((x**2 + y**2)**(3/2))

# Bucle externo: Variacion de la velocidad inicial en el eje Y
for vy in np.arange(0.01, 3 + k, k):
    vx = 0.0
    y = -4.0
    x = 0.0
    n = 0
    # vy = vy_init
    
    # Listas para almacenar la trayectoria (px, py)
    px = [x]
    py = [y]
    
    # Bucle interno: Evolución temporal
    for t in np.arange(0, tfin + h, h):
        n += 1
        # Actualización de velocidades
        vx = vx + ax(x, y) * h
        vy = vy + ay(x, y) * h
        
        # Actualización de posiciones
        x = x + vx * h
        y = y + vy * h
        
        # Guardar posiciones
        px.append(x)
        py.append(y)
    
    # Graficar cada trayectoria
    # Aumentar el tamaño de los puntos para mejor visualización
    plt.plot(px, py, markersize=5, label=f'vy={vy:.2f}', marker='o')

# Configuración final de la gráfica
plt.title("Trayectorias - Lab 02")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
# plt.axhline(0, color='green', linewidth=2)
# plt.axvline(0, color='red', linewidth=2)
plt.show()