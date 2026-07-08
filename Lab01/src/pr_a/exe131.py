import matplotlib.pyplot as plt
import numpy as np

# 1. Parámetros de simulación
h=0.1
a=0
t=0
tfin=10

ri = np.array([3, -4,-5]) 
vp = np.array([-2, 4, 6])
vw = np.array([0, -3, 5])
vt = vp + vw

r_actual = ri.copy()
trayectoria = [r_actual.copy()]


for t in np.arange(0, tfin, h):

    # 2. Formulas
    r_actual = r_actual + (vt * h)
    trayectoria.append(r_actual.copy())


trayectoria = np.array(trayectoria)
rf = trayectoria[-1]
dr = rf - ri


# 3. Visualización
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Definir etiquetas con coordenadas para cada vector.// Fomatear decimales a 2 dígitos para mejor legibilidad.
label_ri = f"ri ({ri[0]:.0f}, {ri[1]:.0f}, {ri[2]:.0f})"
label_dr = f"Δr ({dr[0]:.0f}, {dr[1]:.0f}, {dr[2]:.0f})"
label_rf = f"rf ({rf[0]:.0f}, {rf[1]:.0f}, {rf[2]:.0f})"

# 1. Puntos de la trayectoria
# Poner puntos invisibles en los extremos para "estirar" los ejes para evitar solapamiento
ax.scatter([0, ri[0], rf[0]], [0, ri[1], rf[1]], [0, ri[2], rf[2]], alpha=0.0)

# 2. Vector Posición Inicial (ri) - Desde el origen (0,0,0)

ax.quiver(0, 0, 0, ri[0], ri[1], ri[2], color='blue', pivot='tail', label=r'$\vec{r}_i$', arrow_length_ratio=0.5)
ax.text(ri[0]+0.5, ri[1], ri[2], label_ri, color='blue', fontsize=10)

# 3. Vector Desplazamiento (Delta r) - Desde ri hasta rf
ax.quiver(ri[0], ri[1], ri[2], dr[0], dr[1], dr[2], color='red', linestyle='--', label=r'$\Delta \vec{r}$', arrow_length_ratio=0.08)
ax.text(ri[0]+dr[0]/2, ri[1]+dr[1]/2, ri[2]+dr[2]/2, label_dr, color='red', fontsize=10)

# 4. Vector Posición Final (rf) - Desde el origen (0,0,0)
ax.quiver(0, 0, 0, rf[0], rf[1], rf[2], color='green', label=r'$\vec{r}_f$', arrow_length_ratio=0.08)
ax.text(rf[0], rf[1], rf[2], label_rf, color='green', fontsize=10)

# --- CONFIGURACIÓN DE PANTALLA ---
ax.set_xlabel('Eje X (m)')
ax.set_ylabel('Eje Y (m)')
ax.set_zlabel('Eje Z (m)')
ax.set_title('Ejercicio 1.3: Movimiento en 3D con Viento')
ax.legend()

# Resultados por terminal
print(f"Velocidad Resultante: {vt} m/s")
print(f"Posición Final (rf): {rf} m")
print(f"Desplazamiento (dr): {dr} m")

plt.tight_layout()
plt.savefig('TAREA-01/img/pr_a/exe131.png')
plt.show()