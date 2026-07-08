import matplotlib.pyplot as plt
import numpy as np

import magnetico

xa = np.arange(-0.6, 0.61, 0.1)
ya = np.arange(-0.6, 0.61, 0.1)

boolMap = {
    # i x i
    ((1, 0, 0), (1, 0, 0)): (0, 0, 0),
    # i x j
    ((1, 0, 0), (0, 1, 0)): (0, 0, 1),
    # i x k
    ((1, 0, 0), (0, 0, 1)): (0, -1, 0),
    # j x i
    ((0, 1, 0), (1, 0, 0)): (0, 0, -1),
    # j x j
    ((0, 1, 0), (0, 1, 0)): (0, 0, 0),
    # j x k
    ((0, 1, 0), (0, 0, 1)): (1, 0, 0),
    # k x i
    ((0, 0, 1), (1, 0, 0)): (0, 1, 0),
    # k x j
    ((0, 0, 1), (0, 1, 0)): (-1, 0, 0),
    # k x k
    ((0, 0, 1), (0, 0, 1)): (0, 0, 0),
}


def crossPropio(a, b):
    aMap = [0, 0, 0]
    bMap = [0, 0, 0]
    fuerza = [0, 0, 0]
    for h in a:
        for j in b:
            if h != 0 and j != 0:
                aMap = tuple([1 if x == h else 0 for x in a])
                aValue = h
                bMap = tuple([1 if x == j else 0 for x in b])
                bValue = j
                resp = boolMap.get((aMap, bMap), (0, 0, 0))
                for i in range(3):
                    fuerza[i] += resp[i] * aValue * bValue
    return np.array(fuerza)


q = -1
v = np.array([2, -5, 3])
B = np.array([0, 0, 10])
F = q * np.cross(v, B)

ax3d = plt.figure(figsize=(8, 8)).add_subplot(projection="3d")
ax3d.quiver3D(0, 0, 0, v[0], v[1], v[2])
ax3d.quiver3D(0, 0, 0, B[0], B[1], B[2], color="red")
ax3d.quiver3D(0, 0, 0, F[0], F[1], F[2], color="green")
ax3d.set_title("Fuerza de Lorentz")
ax3d.set_xlim([-15, 50])
ax3d.set_ylim([-15, 20])
ax3d.set_zlim([-15, 15])
ax3d.set_xlabel("X")
ax3d.set_ylabel("Y")
ax3d.set_zlabel("Z")

plt.show()
