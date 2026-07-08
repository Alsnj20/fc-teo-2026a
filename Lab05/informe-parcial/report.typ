#import "template.typ": project

#show: doc => project(
  title: [
    LÍNEAS EQUIPOTENCIALES Y CAMPO ELÉCTRICO ORTOGONAL PARA UN SISTEMA DE TRES CARGAS
  ],
  authors: (
    "JARA MAMANI, MARIEL ALISSON",
  ),
  course: "FISICA COMPUTACIONAL",
  doc,
)

= Segundo Ejercicio del Parcial

La premisa fundamental del problema exige que el campo eléctrico atraviese todas las curvas de potencial de forma estrictamente perpendicular ($90°$), cumpliendo la condición de ortogonalidad dada por:

$ vec(E) = -nabla V $

A partir de la observación del docente, se evaluaron las dos configuraciones de signos para tres cargas dispuestas en un triángulo isósceles.

En ambos casos se probaron distintas combinaciones de magnitud para las cargas, manteniendo fijas sus posiciones. El resultado fue siempre el mismo dentro de cada opción, sin importar los valores numéricos usados. Esto se debe a que dicha forma depende únicamente de los *signos* de las cargas y no de su magnitud, como se explica más adelante a partir de la fórmula del potencial eléctrico.

== Opción 1: Tres cargas del mismo signo

Con las tres cargas positivas, el potencial total en cualquier punto del plano es:

$ V(x,y) = k sum_(i=1)^3 q_i / r_i , quad r_i = sqrt((x-x_i)^2 + (y-y_i)^2) $

Como todas las cargas ($q_i \/ r_i$ ) son positivas, sus potenciales se suman y nunca se cancelan ($V \neq 0$) en ningún punto finito del plano.En consecuencia, las curvas equipotenciales forman óvalos cerrados individuales que, al alejarse, se fusionan en un único contorno externo que envuelve a las tres cargas., tal como se observa en la @fig-opcion1.

#figure(
  image("img/parcial2-opcion1.png", width: 75%),
  caption: [Equipotenciales (violeta) y líneas de campo eléctrico (gris) para $q_1 = +1.0$ C, $q_2 = +0.8$ C, $q_3 = +0.8$ C.],
) <fig-opcion1>

En toda la figura, las líneas de campo cruzan las curvas violeta en ángulo recto, verificando numéricamente la condición de ortogonalidad. El código fuente utilizado para esta opción es el siguiente:

#figure(
  text(size: 7.5pt, raw(read("./code/parcial21.py"), lang: "python", block: true)),
  caption: [Código fuente de la Opción 1 (`parcial21.py`).
  ],
)

== Opción 2: Dos cargas positivas y una carga negativa

Para esta opción se usa el mismo código de la Opción 1, cambiando solo la línea de definición de las cargas por:

```python
q1, q2, q3 = +0.8, -1.0, +0.8
```
El resultado se muestra en la @fig-opcion2.

#figure(
  image("img/parcial2-opcion2.png", width: 80%),
  caption: [Equipotenciales y líneas de campo eléctrico para $q_1 = +0.8$ C, $q_2 = -1.0$ C, $q_3 = +0.8$ C.],
) <fig-opcion2>

Aquí se observa que la condición de ortogonalidad se sigue cumpliendo. Sin embargo, al introducir una carga negativa, su término $k q_2 / r_2$ se resta en la fórmula en vez de sumarse. Esto obliga a que el potencial total se cancele en ciertas zonas, creando una frontera invisible de potencial cero ($V = 0$) que jamás existiría si todas las cargas compartieran el mismo signo.

Como consecuencia, la topología cambia por completo al introducirse un punto de silla en $V$ (donde el campo es nulo, $\ nabla V = 0$, sin ser máximo ni mínimo). Este cruce por cero rompe la simetría y hace que las curvas equipotenciales dejen de cerrarse en óvalos concéntricos, abriéndose en forma de hipérbolas que aíslan físicamente a la carga negativa de las otras dos.

Por eso, este comportamiento es inviable como reproducción del caso de la Opción 1. Ninguna combinación de magnitudes probada logró que el mapa de la Opción 2 recuperara la topología de un solo contorno cerrado, demostrando que el signo de la carga, y no su valor absoluto, es lo que determina la forma cualitativa del campo.

= Conclusión

Ambas opciones satisfacen matemáticamente la condición de ortogonalidad, ya que las líneas de campo eléctrico siempre intersectan a las curvas equipotenciales a 90° sin importar la distribución de carga. No obstante, únicamente la Opción 1 (mismo signo) reproduce la topología cerrada y unificada esperada para este problema, mientras que la Opción 2 demuestra matemáticamente por qué es imposible obtener un contorno cerrado exterior.
