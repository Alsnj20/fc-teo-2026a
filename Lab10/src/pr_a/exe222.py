import numpy as np
import matplotlib.pyplot as plt

# 1. Constantes y condiciones iniciales
h = 0.001           
t = 0
v0 = 2                  
angulo_deg = 45         
angulo_rad = np.radians(angulo_deg)

# Componentes de la velocidad inicial
vx = v0 * np.cos(angulo_rad)
vy = v0 * np.sin(angulo_rad)
ay = -10         

# Variables de estado inicial para el ciclo
x, y = 0, 0

# Listas para guardar datos
pt, px, py, pvy = [], [], [], []

# 2. Trayectoria
while y >= 0:
    pt.append(t)
    px.append(x)
    py.append(y)
    pvy.append(vy)
    
    # Euler: Actualización directa
    vy = vy + ay * h
    x = x + vx * h
    y = y + vy * h
    t += h

px, py, pt, pvy = np.array(px), np.array(py), np.array(pt), np.array(pvy)

# 3. Análisis de resultados
idx_max = np.argmax(py)
h_max = py[idx_max]
t_h_max = pt[idx_max]
v_max = vx

t_suelo = pt[-1]
x_alcance = px[-1]

# Etiquetas para los puntos clave
txt_hmax = f'H. máx: {h_max:.3f}m\nt={t_h_max:.2f}s'
txt_v_hmax = f'v=0\nt={t_h_max:.2f}s'
txt_res_b = f'$v_x = {vx:.2f} m/s$'
txt_alcance = f'Alcance: {x_alcance:.2f}m' 
txt_suelo = f'T. suelo\nt={t_suelo:.2f}s'

# 4. Visualización
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.gcf().canvas.manager.set_window_title('Laboratorio: Movimiento Parabólico')
fig.suptitle(f'Análisis Cinemático ($v_0={v0}m/s$, $\\theta={angulo_deg}^\circ$)', fontsize=16)


# 1. ACELERACIÓN vs TIEMPO
axs[0,0].plot(pt, [ay]*len(pt), 'r', linewidth=2)
axs[0,0].set_title('Aceleración vs Tiempo (Eje Y)')
axs[0,0].set_ylabel('ay (m/s²)')
axs[0,0].set_xlabel('t (s)')
axs[0,0].set_ylim(ay-2, ay+2)
axs[0,0].grid(True)
# Punto clave: ay constante
axs[0,0].scatter(pt[len(pt)//2], ay, color='black', zorder=5)
axs[0,0].text(pt[len(pt)//2], ay+0.2, f'ay = {ay} m/s²', ha='center', fontweight='bold')

# 2. VELOCIDAD VERTICAL vs TIEMPO
axs[0,1].plot(pt, pvy, 'b', linewidth=2)
axs[0,1].axhline(0, color='black', lw=1)
axs[0,1].set_title('Velocidad Vertical vs Tiempo')
axs[0,1].set_ylabel('vy (m/s)')
axs[0,1].set_xlabel('t (s)')
axs[0,1].grid(True)
# Punto v=0 (Altura máxima)
axs[0,1].plot(pt, pvy, 'b', linewidth=2)
axs[0,1].scatter(t_h_max, 0, color='black', zorder=5)
axs[0,1].text(t_h_max, 0.2, txt_v_hmax, ha='center', fontweight='bold')
# Velocidad horizontal constante
axs[0,1].plot(pt, [vx]*len(pt), 'orange', linestyle='--', linewidth=2, label='$v_x$ (Horizontal)')
axs[0,1].text(0.25, vx - 0.2, txt_res_b, ha='center', fontweight='bold', color='darkorange')


# 3. TRAYECTORIA ESPACIAL (y vs x)
axs[1,0].plot(px, py, 'g', linewidth=2)
axs[1,0].set_title('Trayectoria Espacial (y vs x)')
axs[1,0].set_xlabel('Distancia x (m)')
axs[1,0].set_ylabel('Altura y (m)')
axs[1,0].grid(True)
# Puntos clave: Altura máxima y alcance
axs[1,0].scatter([px[idx_max], x_alcance], [h_max, 0], color='black', zorder=5)
axs[1,0].text(px[idx_max], h_max-0.02, txt_hmax, ha='center', fontweight='bold')
axs[1,0].text(x_alcance-0.05, 0.01, txt_alcance, ha='right', fontweight='bold')

# 4. ALTURA vs TIEMPO
axs[1,1].plot(pt, py, 'm', linewidth=2)
axs[1,1].set_title('Altura vs Tiempo')
axs[1,1].set_xlabel('Tiempo t (s)')
axs[1,1].set_ylabel('Altura y (m)')
axs[1,1].grid(True)
# Puntos clave: t_h_max y t_suelo
axs[1,1].scatter([t_h_max, t_suelo], [h_max, 0], color='black', zorder=5)
axs[1,1].text(t_h_max, h_max-0.01, f'H={h_max:.3f}m', ha='center', fontweight='bold')
axs[1,1].text(t_suelo-0.05, 0.005, txt_suelo, ha='center', fontweight='bold')


# Respodiendo a las preguntas:
print("Resultados:")
# (a) La altura máxima.
print(f"(a) Altura máxima: {h_max:.3f} m")
# (b) La velocidad en esa altura.
print(f"(b) Velocidad en altura máxima: {v_max:.2f} m/s (constante en x)")
# (c) El alcance.
print(f"(c) Alcance horizontal: {x_alcance:.2f} m")
# (d) El tiempo en que llega al suelo.
print(f"(d) Tiempo para llegar al suelo: {t_suelo:.2f} s")


plt.tight_layout() 
plt.savefig('TAREA-01/img/pr_a/exe222.png')
plt.show()