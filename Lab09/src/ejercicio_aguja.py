import math
import random

import matplotlib.pyplot as plt

m = 200001
veces = 50

sa = 0
saa = 0

px = []
py = []
px_fin = []
py_fin = []
p_color = []

for k in range(veces):
    n_cruces = 0

    temp_px = []
    temp_py = []
    temp_px_fin = []
    temp_py_fin = []
    temp_color = []

    for i in range(m):
        L = 2.5  # Longitud de la aguja

        r = random.random()
        x = L + (10 - 2 * L) * r

        r = random.random()
        y = 0 + (10 - 0) * r

        r = random.random()
        angulo = 0 + (2 * math.pi - 0) * r

        x_fin = x + L * math.cos(angulo)
        y_fin = y + L * math.sin(angulo)

        y_min = min(y, y_fin)
        y_max = max(y, y_fin)

        cruzo = False
        for linea in [0.0, 2.5, 5.0, 7.5, 10.0]:
            if y_min <= linea <= y_max:
                cruzo = True
                break

        if cruzo:
            n_cruces += 1

        if k == veces - 1:
            temp_px.append(x)
            temp_py.append(y)
            temp_px_fin.append(x_fin)
            temp_py_fin.append(y_fin)
            temp_color.append("purple" if cruzo else "limegreen")

    if k == veces - 1:
        px = temp_px
        py = temp_py
        px_fin = temp_px_fin
        py_fin = temp_py_fin
        p_color = temp_color

    if n_cruces > 0:
        pi_estimado = 2 * (m / n_cruces)
    else:
        pi_estimado = 0

    sa += pi_estimado
    saa += pi_estimado**2

prom = sa / veces
desv = math.sqrt(veces * saa - sa**2) / veces

promedio = str(round(prom, 6))
desviacion = str(round(desv, 6))


print(f"Número total de agujas: {m} veces")
print(f"Pi calculado: {promedio} ± {desviacion}")


# Grafica
plt.figure(figsize=(8, 8))

plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0], color="black", linewidth=3)

for linea in [2.5, 5.0, 7.5]:
    plt.axhline(y=linea, color="red", linestyle="-", linewidth=2)

# limite para que no colapse la imagen
limite_graf = min(1000, m)
for i in range(limite_graf):
    if p_color[i] == "purple":
        plt.plot(
            [px[i], px_fin[i]],
            [py[i], py_fin[i]],
            color=p_color[i],
            alpha=0.5,
            linewidth=1.5,
        )

plt.title("Buffon Monte Carlo")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 11)
plt.ylim(-1, 11)

texto_resultado = f"Pi: {promedio} $\\pm$ {desviacion}\n(Real: {math.pi:.6f})"
plt.text(
    0.5,
    10.3,
    texto_resultado,
    fontsize=12,
    bbox=dict(facecolor="white", alpha=0.8, edgecolor="black"),
)

plt.gca().set_aspect("equal", adjustable="box")
plt.show()
