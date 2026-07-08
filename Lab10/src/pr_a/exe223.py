import numpy as np
import matplotlib.pyplot as plt

# 1. Constantes y condiciones iniciales
h = 0.001           
t = 0

# Velocidad inicial vectorial v = (3i + 4j + 5k)
vx, vy, vz = 3, 4, 5    
az = -10

# Variables de estado inicial
x, y, z = 0, 0, 1

# Listas para guardar datos
pt, px, py, pz, pvz = [], [], [], [], []

# 2. Trayectoria (Simulación hasta tocar suelo z >= 0)
while z >= 0:
    pt.append(t)
    px.append(x)
    py.append(y)
    pz.append(z)
    pvz.append(vz)
    
    # Euler: Actualización
    # vx y vy no cambian porque no hay aceleración en X ni Y
    vz = vz + az * h
    x = x + vx * h
    y = y + vy * h
    z = z + vz * h
    t += h

# Conversión a arrays
px, py, pz, pt, pvz = np.array(px), np.array(py), np.array(pz), np.array(pt), np.array(pvz)

# 3. Análisis de resultados
idx_max = np.argmax(pz)
h_max = pz[idx_max]
t_h_max = pt[idx_max]

v_en_hmax = np.sqrt(vx**2 + vy**2)

t_suelo = pt[-1]
alcance_horizontal = np.sqrt(px[-1]**2 + py[-1]**2)

# Etiquetas
txt_hmax = f'H. máx: {h_max:.2f}m\nt={t_h_max:.2f}s'
txt_suelo = f'Suelo\nt={t_suelo:.2f}s'
txt_vel_b = f'V en H.máx = {v_en_hmax:.2f} m/s'

# 4. Visualización
fig = plt.figure(figsize=(14, 10))
plt.gcf().canvas.manager.set_window_title('Laboratorio: Proyectil 3D')

# --- SUBPLOT 1: TRAYECTORIA 3D (Para demostrar la parábola) ---
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot(px, py, pz, 'g', linewidth=3)
ax1.set_title('Trayectoria 3D (Demostración de Parábola)')
ax1.set_xlabel('Eje X (m)')
ax1.set_ylabel('Eje Y (m)')
ax1.set_zlabel('Altura Z (m)')
ax1.scatter(px[idx_max], py[idx_max], h_max, color='red', s=50) # Punto más alto

# --- SUBPLOT 2: VELOCIDAD VERTICAL (vz) vs TIEMPO ---
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(pt, pvz, 'b', linewidth=2)
ax2.axhline(0, color='black', lw=1)
ax2.set_title('Velocidad Vertical (vz) vs Tiempo')
ax2.set_ylabel('vz (m/s)')
ax2.grid(True)
ax2.scatter(t_h_max, 0, color='black')
ax2.text(t_h_max, 0.5, txt_vel_b, ha='center', fontweight='bold', color='blue')

# --- SUBPLOT 3: ALTURA (z) vs TIEMPO ---
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(pt, pz, 'm', linewidth=2)
ax3.set_title('Altura (z) vs Tiempo')
ax3.set_xlabel('t (s)')
ax3.set_ylabel('z (m)')
ax3.grid(True)
ax3.scatter([t_h_max, t_suelo], [h_max, 0], color='black')
ax3.text(t_h_max, h_max - 0.2, txt_hmax, ha='center', fontweight='bold')

# --- SUBPLOT 4: DISTANCIA HORIZONTAL vs TIEMPO ---
distancia_horizontal = np.sqrt(px**2 + py**2)
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(pt, distancia_horizontal, 'orange', linewidth=2)
ax4.set_title('Distancia Horizontal vs Tiempo')
ax4.set_xlabel('Tiempo (s)')
ax4.set_ylabel('Distancia (m)')
ax4.scatter(t_suelo, alcance_horizontal, color='black')
ax4.text(t_suelo-0.2, alcance_horizontal - 0.5, txt_suelo, ha='center', fontweight='bold', color='orange')
ax4.grid(True)

plt.tight_layout()

# Respuestas:
print(f"(a) La trayectoria es parabólica en el plano de movimiento.")
print(f"(b) Velocidad en z=1 m: vz = {pvz[0]:.2f} m/s")
print(f"(c) El alcance horizontal es de {alcance_horizontal:.2f} m")
print(f"(d) Tiempo hasta el suelo: {t_suelo:.2f} s")

plt.savefig('TAREA-01/img/pr_a/exe223.png')
plt.show()