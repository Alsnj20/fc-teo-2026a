import matplotlib.pyplot as plt
import numpy as np

# 1. Grid definition
xa = np.arange(-0.6, 0.61, 0.1)
ya = np.arange(-0.6, 0.61, 0.1)

# 2. Parameters: Electric currents
B1 = +1
B2 = +1

# Wire positions (wires 3 and 4 are defined but unused in the original code)
x1, x2, x3, x4 = +1, -1, 0.5, -0.5
y1, y2, y3, y4 = +1, -1, -0.5, +0.5

# 3. Meshgrid
x, y = np.meshgrid(xa, ya)

# 4. Denominators for distance squared from wires 1 and 2
d1 = (x - x1) ** 2 + (y - y1) ** 2
d2 = (x - x2) ** 2 + (y - y2) ** 2

# Avoid potential division by zero
d1 = np.where(d1 == 0, 1e-9, d1)
d2 = np.where(d2 == 0, 1e-9, d2)

# 5. Magnetic field components (corrected formulas from Matlab)
Bx = -B1 * (y - y1) / d1 - B2 * (y - y2) / d2
By = +B1 * (x - x1) / d1 + B2 * (x - x2) / d2

# 6. Visualization
plt.figure(figsize=(8, 8))
# Draw parameters
plt.scatter([x1, x2], [y1, y2], color="red", s=100, label="Wires")
plt.quiver(x, y, Bx, By, color="purple", pivot="middle", scale=10)
plt.axis("square")
plt.grid(True, linestyle="--", alpha=0.5)
plt.title("Campo Magnético de Hilos Conductores")
plt.xlabel("x")
plt.ylabel("y")
# plt.xlim([-1, 1])
# plt.ylim([-1, 1])
plt.xlim([-0.7, 0.7])
plt.ylim([-0.7, 0.7])
plt.show()
