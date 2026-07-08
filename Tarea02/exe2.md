# Movimiento de 2 cuerpos
Aplicar el movimiento de 2 cuerpos con datos reales. 

El famoso cuerpo celeste Atlas que vino de algún lugar de la Vı́a Láctea paso por el Sol y luego siguió su camino al infinito. De las diapositivas referente a este tema, considere la constante de gravitación, masa del Sol, radio del Sol y encuentre la
trayectoria de Atlas al pasar por el Sol. 

Hay datos sobre la velocidad de Atlas en Internet. Que tipo de trayectoria es?

## 1.Objetivo
Modelar la trayectoria de atlas que no esta orbitando, sino que pasa cerca del sol y luego se aleja.

## 2. Definición de Variables y Condiciones Iniciales
Para que la simulación sea físicamente verídica, los valores de entrada se han extraído de fuentes oficiales como la **NASA** y el **Ministerio de Ciencia e Innovación (España)**.

### A. Constantes Físicas (Sistema Internacional)
* **G (Constante Gravitacional):** 6.67430e-11 m³/kg·s².
* **M_sol (Masa del Sol):** 1.98847e30 kg.
* **AU (Unidad Astronómica):** 1.496e11 m.
* **R_sol (Radio del Sol):** 6.957e8 m.

### B. Posición Inicial (x, y)
* **x = -6.0 AU**: Ubicamos al cometa a 6 Unidades Astronómicas a la izquierda del Sol. Esto permite visualizar su entrada desde el espacio interestelar (Vía Láctea) hacia el Sistema Solar interior.
* **y = 1.356 AU**: Este valor se conoce como parámetro de impacto. Se elige específicamente porque, según la *NASA*, el perihelio (punto más cercano) de Atlas es de aproximadamente 210 millones de km (cerca de la órbita de Marte). Al poner esta "altura" inicial, garantizamos que el cometa pase a una distancia segura y no choque con el Sol.

### C. Velocidad Inicial (vx, vy)
* **vx = 57,700 m/s**: Esta es la velocidad con la que Atlas viaja antes de ser acelerado intensamente por el Sol. Es una velocidad "hiperbólica", ya que supera los 42.1 km/s (velocidad de escape del Sol a 1 AU).
* **vy = 0 m/s**: Al inicio, el movimiento es puramente horizontal hacia el Sol.

---

## 3. Parámetros de Simulación (Tiempo y Precisión)

La precisión del modelo depende directamente de la configuración del tiempo:

* **Paso de Tiempo (h = 2 horas):** Definido en el código como `3600 * 2`. Un valor de 2 horas es el intervalo óptimo para el **Método de Euler**. Es lo suficientemente pequeño para capturar la aceleración extrema que sufre el cometa cerca del Sol sin generar errores numéricos significativos.
* **Tiempo Total (tfin = 1.2 años):** Definido como `3600 * 24 * 365 * 1.2`. Este periodo permite observar la historia completa del evento: desde que Atlas aparece en el borde del sistema, su aceleración máxima en el perihelio y su posterior alejamiento definitivo.

---

## 4. Implementación del Modelo Físico
Siguiendo la **Diapositiva 7** del curso, la trayectoria no se dibuja como una función estática, sino que se calcula dinámicamente mediante:

1.  **Cálculo de Aceleración (ax, ay):** En cada paso *h*, se calcula la fuerza que ejerce el Sol sobre Atlas:
    ax = -GMx / r³, ay = -GMy / r³
2.  **Actualización de Velocidad y Posición:**
    * v(i+1) = v(i) + a(i) * h
    * x(i+1) = x(i) + v(i+1) * h

Este proceso iterativo permite que el Sol "tire" de Atlas, curvando su línea recta original en una curva de gran energía.

---

## 5. Resultados y Hallazgos
Al ejecutar la simulación, el resultado muestra tres fases claras:
1 **Aproximación:** Atlas entra desde el infinito con velocidad constante.
2 **Interacción (Efecto Honda):** Al acercarse al Sol, la aceleración aumenta drásticamente. El cometa alcanza su velocidad máxima de 246,000 km/h (68.4 km/s) justo en el perihelio (el punto azul).
3. **Escape:** Tras superar el Sol, el cometa comienza a frenarse ligeramente debido a la atracción hacia atrás, pero su velocidad sigue siendo tan alta que se aleja en línea recta hacia los confines de la galaxia.

## Respuesta del Laboratorio
### **¿Qué tipo de trayectoria es?**
Es una **Trayectoria Hiperbólica**.
**Justificación:**
1.  **Excentricidad (e > 1):** Los datos científicos confirman que Atlas tiene una excentricidad de aprox. 6.13.
2.  **Energía:** La velocidad del cometa siempre es mayor a la velocidad de escape local. La gravedad del Sol desvía su camino pero no logra cerrarlo en una elipse.
3.  **Origen:** Al venir de la Vía Láctea y seguir su camino al infinito, se clasifica como un objeto hiperbólico interestelar.

---

## 6. Fuentes Bibliográficas
Los datos numéricos y el contexto científico fueron extraídos de:
1.  **NASA Solar System Exploration (3I/ATLAS):** https://science.nasa.gov/solar-system/comets/3i-atlas/
2.  **Ministerio de Ciencia e Innovación de España:** https://www.ciencia.gob.es/Noticias/2025/octubre/cometa-3I-ATLAS-visita-nuestro-sistema-solar.html
3.  **Diapositivas de Clase:** Material referente al Movimiento de 2 Cuerpos y el Algoritmo de Integración de Euler (Diapositivas 6 y 7).
