import matplotlib.pyplot as plt
import numpy as np

# 1. Constantes del sistema
h = 0.01
ay=-10

# Condiciones iniciales
t=0
y=2
vy=10

# Listas para guardar datos
pt = [t]
py = [y]
pvy = [vy]
pa = [ay]

# 2. TRAYECTORIA (Simulación hasta que llega al suelo y < 0)
while y >= 0:
      
    # Fórmulas
    vy = vy + (h * ay)
    y = y + (h * vy)
    t = t + h
    
    # Guardar datos
    pt.append(t)
    py.append(y)
    pvy.append(vy)
    pa.append(ay)


pt, py, pvy, pa = np.array(pt), np.array(py), np.array(pvy), np.array(pa)

# 3. ANÁLISIS DE RESULTADOS
idx_max = np.argmax(py)
h_max = py[idx_max]
t_h_max = pt[idx_max]
t_suelo = pt[-1]


# Punto donde regresa ay y=2
idx_y2 = np.argmin(np.abs(py[pt > 0.5] - 2)) + np.where(pt > 0.5)[0][0]
t_y2= pt[idx_y2]

# 4. VISUALIZACIÓN
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.gcf().canvas.manager.set_window_title('Laboratorio 2: Caída Libre')


# 1. ACELERACIÓN vs TIEMPO
axs[0,0].plot(pt, pa, 'r', linewidth=2)
axs[0,0].set_title('Aceleración vs Tiempo')
axs[0,0].set_ylabel('ay (m/s²)')
axs[0,0].set_xlabel('t (s)')
axs[0,0].grid(True)
# Punto ay=-10
axs[0,0].scatter(pt[len(pt)//2], -10, color='black')
axs[0,0].text(pt[len(pt)//2], -9.95, 'ay = -10 m/s²', fontweight='bold') 

# 2. VELOCIDAD vs TIEMPO
axs[0,1].plot(pt, pvy, 'b', linewidth=2)
axs[0,1].set_title('Velocidad vs Tiempo')
axs[0,1].set_ylabel('v (m/s)')
axs[0,1].set_xlabel('t (s)')
axs[0,1].grid(True)
# Punto v=0
axs[0,1].scatter(t_h_max, 0, color='black', zorder=5)
axs[0,1].text(t_h_max, 1, f'v=0\nt={t_h_max:.1f}s', ha='center', fontweight='bold')

# 3. ALTURA vs TIEMPO
axs[1,0].plot(pt, py, 'g', linewidth=2)
axs[1,0].set_title('Altura vs Tiempo')
axs[1,0].set_ylabel('y (m)')
axs[1,0].set_xlabel('t (s)')
axs[1,0].grid(True)
# Puntos clave y-t
axs[1,0].scatter([t_h_max, t_y2, t_suelo], [h_max, 2, 0], color='black', zorder=5)
axs[1,0].text(t_h_max, 6.2, f'Máx: {h_max:.2f}m\nTM={t_h_max:.2f}s', ha='center', fontweight='bold')

axs[1,0].text(t_y2, 2.3, f'y=2\nt={t_y2:.2f}s', ha='center', fontweight='bold')
axs[1,0].text(t_suelo, 0.3, f'Suelo\nt={t_suelo:.2f}s', ha='center', fontweight='bold')

# 4. VELOCIDAD vs ALTURA
axs[1,1].plot(py, pvy, 'm', linewidth=2)
axs[1,1].set_title('Velocidad vs Altura')
axs[1,1].set_xlabel('y (m)')
axs[1,1].set_ylabel('v (m/s)')
axs[1,1].grid(True)
# Punto de retorno
axs[1,1].scatter(h_max, 0, color='black', zorder=5)
axs[1,1].text(6.1, 0, f'y={h_max:.2f}m\nv=0', ha='center', fontweight='bold')

# Respondiendo a las preguntas:
print("\nResultados:")
# (a) La altura máxima.
print(f"(a) Altura máxima: {h_max:.2f} m")
# (b) Cuando la velocidad sea cero.
print(f"(b) Velocidad cero en t = {t_h_max:.2f}s")
# (c) El tiempo donde llega a la altura máxima.
print(f"(c) Tiempo para altura máxima: {t_h_max:.2f} s")
# (d) El tiempo donde pasa por y = 2.
print(f"(d) Tiempo para y=2: {t_y2:.4f} s")
# (e) El tiempo en que llega al suelo.
print(f"(e) Tiempo para llegar al suelo: {t_suelo:.4f} s")

plt.tight_layout()
plt.savefig('TAREA-01/img/pr_a/exe211.png')
plt.show()