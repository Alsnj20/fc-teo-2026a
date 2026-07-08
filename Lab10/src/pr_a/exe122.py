import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
h=0.1
a=0
# Condiciones iniciales
t=0
tfin=10

ri = np.array([3, -4]) 
vp = np.array([-4, 3])
vw = np.array([3,-5])
vt = vp + vw

r_actual = ri.copy()
trayectoria = [r_actual.copy()]


for t in np.arange(0, tfin, h):

    # Formulas
    r_actual = r_actual + (vt * h)
    trayectoria.append(r_actual.copy())


trayectoria = np.array(trayectoria)
rf = trayectoria[-1]
dr = rf - ri

# Visualización
plt.figure(figsize=(8, 8))

# 1. Dibujar los puntos de la trayectoria
plt.plot(trayectoria[:, 0], trayectoria[:, 1], 'k.', markersize=5, label='Puntos Trayectoria')

# 2. Vector Posición Inicial (ri) - Desde el origen (0,0)
plt.quiver(0, 0, ri[0], ri[1], angles='xy', scale_units='xy', scale=1, color='blue', label='$r_i$', width=0.01)

# 3. Vector Desplazamiento (Delta r) - Desde ri hasta rf
plt.quiver(ri[0], ri[1], dr[0], dr[1], angles='xy', scale_units='xy', scale=1, color='red', label='$\Delta r$', width=0.01) 

# 4. Vector Posición Final (rf) - Desde el origen (0,0)
plt.quiver(0, 0, rf[0], rf[1], angles='xy', scale_units='xy', scale=1, color='green', label=r'$r_f$', alpha=0.5, width=0.008)

# Graficación
plt.grid(True)
plt.axis('equal')
plt.title('Ejercicio 1.2.1 - Trayectoria y Vectores')
plt.xlabel('Eje X (m)')
plt.ylabel('Eje Y (m)')
plt.legend()

print(f"Posición Final (rf): {rf}")
print(f"Desplazamiento (Δr): {dr}")

plt.tight_layout()
plt.savefig('TAREA-01/img/pr_a/exe122.png')
plt.show()