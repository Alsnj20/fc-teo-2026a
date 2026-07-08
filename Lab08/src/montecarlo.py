import matplotlib.pyplot as plt
import numpy as np

# Parámetros iniciales
veces = 50
m = 10000
ax, bx = -2.0, 2.0
ay, by = -3.0, 3.0
sa = 0
saa = 0

# Para almacenar los puntos y graficarlos al final
px_all = []
py_all = []

for k in range(veces):
    n = 0
    # Generamos números aleatorios para m puntos (x e y simultáneamente)
    x = np.random.uniform(ax, bx, m)
    y = np.random.uniform(ay, by, m)

    # Condición: x^2/4 + y^2/9 < 1 (área dentro de la elipse)
    condicion = (x**2 / 4) + (y**2 / 9) < 1

    # Contamos cuántos cumplen la condición
    n = np.sum(condicion)

    # Guardamos los puntos que cumplen para el gráfico
    px_all.extend(x[condicion])
    py_all.extend(y[condicion])

    # Cálculo del área de esta iteración
    area = n * (by - ay) * (bx - ax) / m
    sa += area
    saa += area**2

# Cálculos finales
prom = sa / veces
desv = np.sqrt((veces * saa - sa**2) / veces)

# Visualización
plt.figure(figsize=(8, 8))

plt.scatter(px_all, py_all, s=1, marker=".")
plt.title("Áreas por el método MonteCarlo")
plt.xlabel("x")
plt.ylabel("y")
plt.axis((ax, bx, ay, by))
# plt.axis("equal")

# Mostrar promedio y desviación en el gráfico
plt.text(1.2, by + 0.3, f"Promedio: {prom:.4f}")
plt.text(1.2, by + 0.5, f"+-: {desv:.4f}")

plt.show()

print(f"Promedio: {prom}")
print(f"Desviación: {desv}")
