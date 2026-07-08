import matplotlib.pyplot as plt

# 1. Crear el espacio y el lienzo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

origen_x, origen_y, origen_z = 0, 0, 0
vx, vy, vz = 2, 0, 0
Bx, By, Bz = 0, 0, -5
Fmx, Fmy, Fmz = 0, -2, 0

ax.quiver(
    origen_x,
    origen_y,
    origen_z,
    vx,
    vy,
    vz,
    color="green",
    linewidth=3,
    arrow_length_ratio=0.15,
    label=r"Velocidad $\vec{v}$ (2i)",
)

# Flecha Roja para el Campo Magnético
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
    label=r"Campo $\vec{B}$ (-10k)",
)

# Flecha Azul para la Fuerza Magnética
ax.quiver(
    origen_x,
    origen_y,
    origen_z,
    Fmx,
    Fmy,
    Fmz,
    color="blue",
    linewidth=3,
    arrow_length_ratio=0.15,
    label=r"Fuerza $\vec{F}_m$ (-2j)",
)

# 2. Dibujar líneas de los ejes como referencia visual
ax.plot([-3, 3], [0, 0], [0, 0], color="black", linestyle="--", alpha=0.4)  # Eje X (i)
ax.plot([0, 0], [-3, 3], [0, 0], color="black", linestyle="--", alpha=0.4)  # Eje Y (j)
ax.plot([0, 0], [0, 0], [-6, 2], color="black", linestyle="--", alpha=0.4)  # Eje Z (k)

# 3. Configurar los límites del espacio 3D y etiquetas
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-6, 2])

ax.set_xlabel("Eje X (i)")
ax.set_ylabel("Eje Y (j)")
ax.set_zlabel("Eje Z (k)")
ax.set_title("Fuerza de Lorentz usando Quiver 3D")

ax.legend(loc="upper left")
ax.view_init(elev=20, azim=45)
plt.savefig("Lab06/img/lab/1.png", dpi=300, bbox_inches="tight")
plt.show()
