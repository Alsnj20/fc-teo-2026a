import matplotlib.pyplot as plt
import numpy as np

# Constantes del sistema
k=1
m=2
h=0.01
a=0

# Condiciones iniciales
t=0
x=5
v=-2
tfin=10

# Listas para almacenar los resultados
pt = [t]
pv = [v]
px = [x]
pa = [a]

for t in np.arange(0, tfin, h):
    
    # Formulas
    v = v + h*a
    x = x + h*v

    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

# Graficas
plt.figure(figsize=(12, 8))

# Grafica 1: Aceleración vs Tiempo
plt.subplot(2, 2, 1)
plt.plot(pt, pa, label='Aceleración', color='red')
plt.title('Aceleración vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')

plt.grid(True)

# Grafica 2: Velocidad vs Tiempo
plt.subplot(2, 2, 2)
plt.plot(pt, pv, label='Velocidad', color='blue')
plt.title('Velocidad vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Grafica 3: Posición vs Tiempo
plt.subplot(2, 2, 3)
plt.plot(pt, px, label='Posición', color='green')
plt.title('Posición vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Grafica 4: Velocidad vs Posición
plt.subplot(2, 2, 4)
plt.plot(px, pv, label='Fase', color='purple')
plt.title('Posición vs Velocidad')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Ajustar los márgenes para evitar solapamientos
plt.tight_layout()
plt.savefig('TAREA-01/img/pr_a/exe111.png')
plt.show()

