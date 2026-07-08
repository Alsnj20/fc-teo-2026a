import matplotlib.pyplot as plt

# Crear el espacio y el lienzo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

origen_x, origen_y, origen_z = 0, 0, 0
vx, vy, vz = 3, 5, 6
Bx, By, Bz = -10 / 2, 2 / 2, 1 / 2
Fmx, Fmy, Fmz = -0.7 * 1.5, -6.3 * 1.5, -5.6 * 1.5

ax.quiver(
    origen_x,
    origen_y,
    origen_z,
    vx,
    vy,
    vz,
    color="green",
    linewidth=3,
    arrow_length_ratio=0.12,
    label=r"Velocidad $\vec{v}$ (3i + 5j + 6k)",
)

# Flecha Roja para el Campo Magnético (B)
ax.quiver(
    origen_x,
    origen_y,
    origen_z,
    Bx,
    By,
    Bz,
    color="red",
    linewidth=3,
    arrow_length_ratio=0.15,
    label=r"Campo $\vec{B}$ (-10i + 2j + 1k)",
)

# Flecha Azul para la Fuerza Magnética (Fm)
ax.quiver(
    origen_x,
    origen_y,
    origen_z,
    Fmx,
    Fmy,
    Fmz,
    color="blue",
    linewidth=3,
    arrow_length_ratio=0.12,
    label=r"Fuerza $\vec{F}_m$ (0.7i - 6.3j - 5.6k)",
)

# Dibujar líneas de los ejes como referencia visual (líneas punteadas)
ax.plot([-8, 8], [0, 0], [0, 0], color="black", linestyle="--", alpha=0.3)  # Eje X (i)
ax.plot([0, 0], [-8, 8], [0, 0], color="black", linestyle="--", alpha=0.3)  # Eje Y (j)
ax.plot(
    [0, 0], [0, 0], [-10, 10], color="black", linestyle="--", alpha=0.3
)  # Eje Z (k)

ax.set_xlim([-8, 8])
ax.set_ylim([-8, 8])
ax.set_zlim([-10, 10])
ax.set_xlabel("Eje X (i)")
ax.set_ylabel("Eje Y (j)")
ax.set_zlabel("Eje Z (k)")
ax.set_title("Fuerza de Lorentz en 3D (Ejercicio 2)")
ax.legend(loc="upper left")
ax.view_init(elev=25, azim=60)
plt.savefig("Lab06/img/lab/2.png", dpi=300, bbox_inches="tight")
plt.show()
