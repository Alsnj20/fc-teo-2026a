import matplotlib.pyplot as plt
import numpy as np

# Parámetros
c = 20
acel = [0] * c
bcel = [0] * c

# Estado inicial: activamos la posición 7
acel[6] = 1

# Gráfica
plt.figure(figsize=(8, 8))
plt.xlim(0, c + 1)
plt.ylim(0, c + 1)
plt.title("Autómata Celular Completo - Regla 62 (Iniciando en Célula 7)")
plt.xlabel("Células")
plt.ylabel("Generaciones")
plt.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.5)
plt.xticks(range(1, c + 1))
plt.yticks(range(1, c + 1))

j = c
mcel = np.zeros((c, c))

# El ciclo corre hasta que j llega a 0 (20 filas completas)
while j > 0:
    mcel[c - j, :] = acel

    for k in range(c):
        if acel[k] == 1:
            plt.plot(k + 1, j, "sk", markersize=14)

    for i in range(c):
        # Condiciones de frontera periódica
        l = i - 1
        r = i + 1
        if l < 0:
            l = c - 1
        if r >= c:
            r = 0

        suma = acel[l] + acel[i] + acel[r]
        bcel[i] = 0

        match suma:
            case 1:
                bcel[i] = 1
            case 2:
                if acel[r] == 1 or acel[i] == 0:
                    bcel[i] = 1
            case _:
                bcel[i] = 0

    acel = bcel.copy()
    j = j - 1

# Muestra el lienzo final en pantalla
plt.show()

plt.figure(figsize=(8, 8))
plt.title("Autómata Celular Completo - Regla 62 (Iniciando en Célula 7)")
plt.xlabel("Células")
plt.ylabel("Generaciones")
plt.imshow(mcel, cmap='gray_r', origin='upper')
plt.savefig("Lab12/img/lab/62.png", dpi=300)
plt.show()
