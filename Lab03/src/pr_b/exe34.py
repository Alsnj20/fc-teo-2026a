import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 8, "lines.linewidth": 0.8})
plt.figure(figsize=(8, 8))

# Datos iniciales
r = 1.0
h = 0.01      
tfin = 100
    
# Circunferencia 1
b1 , c1 = 3 ,-2

theta = np.linspace(0, 2*np.pi, 100)
x_circ = b1 + np.cos(theta)
y_circ = c1 + np.sin(theta)
plt.plot(x_circ, y_circ, 'black', linewidth=2, label=f"Masa1 en ({b1}, {c1})")

# Circunferencia 2
b2 , c2 = -3, -2
x_circ2 = b2 + np.cos(theta)
y_circ2 = c2 + np.sin(theta)
plt.plot(x_circ2, y_circ2, 'black', linewidth=2, label=f"Masa2 en ({b2}, {c2})")

def ax(x, y, xc1, yc1, xc2, yc2):
    # Masa 1: Distancias y Radio
    den1 = ((x - xc1)**2 + (y - yc1)**2)**(3/2)
    # Masa 2: 
    den2 = ((x - xc2)**2 + (y - yc2)**2)**(3/2)
    if den1 == 0 or den2 == 0:
        return 0.0
    
    return (-(x - xc1) / den1) - ((x - xc2) / den2)

def ay(x, y, xc1, yc1, xc2, yc2):
    # Masa 1: Distancias y Radio
    den1 = ((x - xc1)**2 + (y - yc1)**2)**(3/2)
    # Masa 2: Distancias y Radio
    den2 = ((x - 
             xc2)**2 + (y - yc2)**2)**(3/2)

    if den1 == 0 or den2 == 0:
        return 0.0
    return (-(y - yc1) / den1) - ((y - yc2) / den2)

for vx0 in np.arange(0.5, 1.5, 0.1):
    x, y = 0.0, 0.0
    vx, vy = vx0, 0
    
    px = [x]
    py = [y]
    
    # seFugo = False
    
    for t in np.arange(0, tfin, h):        
        
        vx += ax(x, y, b1, c1, b2, c2) * h
        vy += ay(x, y, b1, c1, b2, c2) * h
        x  += vx * h
        y  += vy * h
        
        if np.sqrt((x - b1)**2 + (y - c1)**2) <= r or np.sqrt((x - b2)**2 + (y - c2)**2) <= r:
            break
        if y > 50:
            break
        
        px.append(x)
        py.append(y)
        
        if abs(x) > 20 or abs(y) > 20:
            break
        
        
    plt.plot(px, py)

# Configuración de la gráfica
plt.title("Laboratorio 3 - Ejercicio 1")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()