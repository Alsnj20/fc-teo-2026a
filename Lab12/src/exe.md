ok este codigo 62.py, Realice según su número en la relación:
1. Cree la tabla de verdad.
2. No deben haber 8 decisiones, sea óptimo en sus decisiones. Máximo 6 decisiones.
3. Presente en forma gráfica la regla.
4. Fabrique en papel tres líneas para 20 células.

# Autómata Celular Unidimensional - Regla 62

Este documento detalla la resolución teórica, optimización y simulación de la **Regla 62** para un autómata celular unidimensional.

---

## 1. Expresión Booleana y Tabla de Verdad

La regla de evolución asignada está dada por la expresión:

$$F = \bar{a}_{-1}a_1 + a_{-1}\bar{a}_0 + \bar{a}_{-1}a_0$$

Donde:
* $a_{-1}$ representa al vecino izquierdo (`izq`).
* $a_0$ representa a la célula central (`centro`).
* $a_1$ representa al vecino derecho (`der`).

### Tabla de Verdad Completa

Evaluando los 8 estados posibles de la vecindad de 3 células:

| N° | $a_{-1}$ (Izq) | $a_0$ (Centro) | $a_1$ (Der) | $\bar{a}_{-1}$ | $\bar{a}_0$ | $\bar{a}_1$ | Term 1 ($\bar{a}_{-1}a_1$) | Term 2 ($a_{-1}\bar{a}_0$) | Term 3 ($\bar{a}_{-1}a_0$) | Resultado ($F$) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0** | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | **0** |
| **1** | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **1** |
| **2** | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | **1** |
| **3** | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | **1** |
| **4** | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | **1** |
| **5** | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | **1** |
| **6** | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **0** |
| **7** | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |


---

## 2. Comprobación Numérica (Demostración del Número de Regla)

Para verificar que los resultados corresponden a la **Regla 62** de Wolfram, ordenamos el vector de salidas desde el estado 7 al estado 0:

$$\text{Vector de Salidas} = [0, 0, 1, 1, 1, 1, 1, 0]_2$$

Convertimos el número binario $00111110_2$ a su valor equivalente en sistema decimal:

$$0 \cdot 2^7 + 0 \cdot 2^6 + 1 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0$$
$$= 0 + 0 + 32 + 16 + 8 + 4 + 2 + 0 = \mathbf{62}$$

Se demuestra que el comportamiento lógico asignado equivale exactamente a la **Regla 62**.

---

## 3. Análisis de Optimización de Decisiones (Máximo 6 decisiones)

Para implementar el autómata de forma eficiente sin recurrir a evaluar las 8 decisiones condicionales individuales, agrupamos los minitérminos que producen un estado activo (`1`):

1. **Agrupación por Término 1 ($\bar{a}_{-1}a_1$):**
   * Es verdadero cuando $a_{-1} = 0$ y $a_1 = 1$. Cubre las combinaciones `011` y `001` (Casos 3 y 1).
2. **Agrupación por Término 2 ($a_{-1}\bar{a}_0$):**
   * Es verdadero cuando $a_{-1} = 1$ y $a_0 = 0$. Cubre las combinaciones `101` y `100` (Casos 5 y 4).
3. **Agrupación por Término 3 ($\bar{a}_{-1}a_0$):**
   * Es verdadero cuando $a_{-1} = 0$ y $a_0 = 1$. Cubre las combinaciones `011` y `010` (Casos 3 y 2).

Cada uno de esos 3 términos es una "super-condición" que agrupa varios casos a la vez gracias a que ignora la variable que no aparece en el término:Término 1 ($\bar{a}_{-1}a_1$): Significa "Izquierda es 0 y Derecha es 1 (sin importar el Centro)".Esto agrupa automáticamente los casos 0-0-1 y 0-1-1 en una sola pregunta.Término 2 ($a_{-1}\bar{a}_0$): Significa "Izquierda es 1 y Centro es 0 (sin importar la Derecha)".Esto agrupa automáticamente los casos 1-0-0 y 1-0-1 en otra sola pregunta.Término 3 ($\bar{a}_{-1}a_0$): Significa "Izquierda es 0 y Centro es 1 (sin importar la Derecha)".Esto agrupa los casos 0-1-0 y 0-1-1.

Con este análisis, reducimos la lógica a solo **3 decisiones activas** y **1 caso por defecto**, resolviendo la simulación con un máximo de 3 evaluaciones lógicas por celda.

---

## 4. Representación Gráfica de las 8 Sub-reglas

Representación esquemática de la transición de vecindades (donde `[■] = 1` y `[ ] = 0`):

```bash
Regla 7:    Regla 6:    Regla 5:    Regla 4:    Regla 3:    Regla 2:    Regla 1:    Regla 0:
[■ ■ ■]     [■ ■ □]     [■ □ ■]     [■ □ □]     [□ ■ ■]     [□ ■ □]     [□ □ ■]     [□ □ □]
   ↓           ↓           ↓           ↓           ↓           ↓           ↓           ↓   
  [ ]         [ ]         [■]         [■]         [■]         [■]         [■]         [ ]  
  (0)         (0)         (1)         (1)         (1)         (1)         (1)         (0) = rule 62

```
## 5. Simulación en Papel de 20 Células
Para simular la evolución de 20 células bajo la Regla 62, se puede iniciar con una configuración inicial y aplicar las reglas de transición para cada célula en cada paso de tiempo. A continuación, se presenta un ejemplo de cómo podría verse la simulación en papel: Se elije el 7 como aleatorio, y se coloca en la posición central de la primera línea, con las demás células en estado 0.
L1:  _ _ _ _ _ _ ■ _ _ _ _ _ _ _ _ _ _ _ _ _
L2:  _ _ _ _ _ ■ ■ ■ _ _ _ _ _ _ _ _ _ _ _ _
L3:  _ _ _ _ ■ ■ _ _ ■ _ _ _ _ _ _ _ _ _ _ _
L4:  _ _ _ ■ ■ _ ■ ■ ■ ■ _ _ _ _ _ _ _ _ _ _
L5:  _ _ ■ ■ _ ■ ■ _ _ _ ■ _ _ _ _ _ _ _ _ _
