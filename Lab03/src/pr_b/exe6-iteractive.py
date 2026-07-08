import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURACIÓN DE PARÁMETROS ---
r = 1.0
h = 0.01
tfin = 800
x0, y0 = 0.0, -7.0
vx0, vy0 = 0.04264, 0.0

# PRUEBA2: Choques con 2da circunferencia
# h = 0.01
# tfin = 800
# x0, y0 = 0.0, 7.0
# vx0, vy0 = 0.00000080, 0.00000001


b1, c1 = 3, -2
b2, c2 = -3, -2


# --- MÓDULOS DE FÍSICA ---
def calcular_aceleraciones(x, y):
    """Calcula la aceleración neta en x e y debido a ambas masas."""
    den1 = ((x - b1) ** 2 + (y - c1) ** 2) ** (1.5)
    den2 = ((x - b2) ** 2 + (y - c2) ** 2) ** (1.5)

    if den1 == 0 or den2 == 0:
        return 0.0, 0.0

    ax = (-(x - b1) / den1) - ((x - b2) / den2)
    ay = (-(y - c1) / den1) - ((y - c2) / den2)
    return ax, ay


def paso_euler(x, y, vx, vy):
    """Realiza un paso de integración numérica."""
    ax_net, ay_net = calcular_aceleraciones(x, y)
    vx_new = vx + ax_net * h
    vy_new = vy + ay_net * h
    x_new = x + vx_new * h
    y_new = y + vy_new * h
    return x_new, y_new, vx_new, vy_new


# --- CONFIGURACIÓN VISUAL ---

plt.ion()  # Activar modo interactivo
fig, ax_vis = plt.subplots(figsize=(9, 9))
ax_vis.set_xlim(-10, 10)
ax_vis.set_ylim(-10, 10)
ax_vis.set_aspect("equal")
ax_vis.grid(True)

# Dibujar masas fijas
theta = np.linspace(0, 2 * np.pi, 100)
ax_vis.plot(b1 + np.cos(theta), c1 + np.sin(theta), "k", linewidth=2)
ax_vis.plot(b2 + np.cos(theta), c2 + np.sin(theta), "k", linewidth=2)

# Crear objetos de trayectoria vacíos
(linea_a,) = ax_vis.plot([], [], "b", label="Nave A (x)", alpha=0.8)
(linea_b,) = ax_vis.plot([], [], "r", label="Nave B (x + 0.01)", alpha=0.8)
ax_vis.legend()

# --- BUCLE PRINCIPAL (SIMULACIÓN SIMULTÁNEA) ---

# Estados iniciales
xa, ya, vxa, vya = x0, y0, vx0, vy0
xb, yb, vxb, vyb = x0 + 0.01, y0, vx0, vy0

txa, tya = [xa], [ya]
txb, tyb = [xb], [yb]

print("Simulando... Cierra la ventana para detener.")

for t in np.arange(0, tfin, h):
    # Calcular siguiente paso para ambas naves
    xa, ya, vxa, vya = paso_euler(xa, ya, vxa, vya)
    xb, yb, vxb, vyb = paso_euler(xb, yb, vxb, vyb)

    # Guardar trayectorias
    txa.append(xa)
    tya.append(ya)
    txb.append(xb)
    tyb.append(yb)

    seMueveA = True
    seMueveB = True

    if seMueveA:
        xa, ya, vxa, vya = paso_euler(xa, ya, vxa, vya)
        txa.append(xa)
        tya.append(ya)
        # Si choca
        if (
            np.sqrt((xa - b1) ** 2 + (ya - c1) ** 2) <= r
            or np.sqrt((xa - b2) ** 2 + (ya - c2) ** 2) <= r
        ):
            print(f"Colisión detectada para Nave A en t = {t:.2f}")
            seMueveA = False

    if seMueveB:
        xb, yb, vxb, vyb = paso_euler(xb, yb, vxb, vyb)
        txb.append(xb)
        tyb.append(yb)
        # Si choca
        if (
            np.sqrt((xb - b1) ** 2 + (yb - c1) ** 2) <= r
            or np.sqrt((xb - b2) ** 2 + (yb - c2) ** 2) <= r
        ):
            print(f"Colisión detectada para Nave B en t = {t:.2f}")
            seMueveB = False

    # Actualizar animación cada 30 pasos para mayor fluidez
    if int(t / h) % 30 == 0:
        linea_a.set_data(txa, tya)
        linea_b.set_data(txb, tyb)
        plt.pause(0.001)

    if not seMueveA and not seMueveB:
        print("Ambas naves han colisionado. Deteniendo simulación.")
        break

plt.ioff()  # Desactivar modo interactivo
print("Simulación terminada.")
plt.savefig("img/pr_b/exe6-iteractive.png", dpi=300)
plt.show()
