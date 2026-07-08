#import "./lib.typ": code-block, lab-report, lab-section, table-border-width

#let course-name = "FISICA COMPUTACIONAL"
#let lab-title = "Resolución de la Práctica 2: Movimiento en una, dos y tres dimensiones: Variante B"
#let lab-number = "02"
#let instructor-name = "Prof. Edwin Agapito Llamoca Requena"
#let member-list = (
  "Jara Mamani Mariel Alisson",
)

#lab-report(
  course-name: course-name,
  lab-title: lab-title,
  lab-number: lab-number,
  instructor-name: instructor-name,
  member-list: member-list,
  sem-code: "VII",
)[
  #lab-section("RESULTADOS Y PRUEBAS", align-mode: left + top)[
    #show heading: set text(weight: "bold")
    #set par(justify: true)


    = SOLUCIÓN DE LOS EJERCICIOS PROPUESTOS
    = VARIANTE A

    #set heading(numbering: "1.1.1")
    #show heading.where(level: 3): set text(weight: "bold")

    = $arrow(a) = 0$, no hay aceleración
    == Velocidad Constante en una Dimensión

    === Problema
    Sea una partícula, cuya posición inicial es $t_0 = 0$, $x_0 = 5$ m con $v_x = -2$ m/s. Determine la posición de la partícula para $t = 10$ s. Utilice el tamaño de paso $h = 0.01$. Hacia donde se dirige la partícula.

    \
    *Implementación:* Se definieron las variables iniciales `x=5`, `v=-2`, `a=0`, `h=0.01`. Se utilizó un ciclo `for` para calcular la posición en cada instante `t` con el paso `h` establecido y se grafico según lo que se pide.

    *Código fuente: exe111.py*
    #code-block("src/pr_a/exe111.py", 
    lang: "python")

    #align(center)[
      #image("img/pr_a/exe111.png")
      _Figura 1: Gráficos de a-t, v-t, x-t, v-x_
    ]

    *Resultados:* En el gráfico `a-t` se observa una línea horizontal en `a=0` porque la aceleración es nula. En `v-t` se observa una línea recta con pendiente cero debido a que la velocidad es constante. En `x-t` se observa una línea recta con pendiente negativa porque la partícula se mueve hacia la izquierda. En `v-x` se observa un punto único porque la velocidad no cambia. Concluyendo que la pertícula se dirige hacia la izquierda.

    

    === 
    La posición inicial de una partícula se ubica en $x_0 = 5$ m y $t_0 = 0$ con velocidad $v_x = -3$ m/s. Después de 3 s, adquiere una velocidad $v_x = 2$ m/s transcurriendo 2 s más. Encuentre la posición final de la partícula. Utilice tamaño de paso $h = 0.1$.

    *Implementación:* Se definieron las condiciones iniciales `x=5`, `v=-3`, `h=0.1`. Se utilizó un ciclo `for` con una condición para cambiar la velocidad cuando `t > 3` s.

    *Código fuente: ej1.1.2.py*
    #code-block("src/pr_a/exe112.py", lang: "python")

    #image("img/pr_a/exe112.png")

    *Descripción:* En el gráfico `a-t` se observa una línea horizontal porque la aceleración es cero. En `v-t` se observa un escalón debido al cambio de velocidad en `t=3s`. En `x-t` se observa un cambio de pendiente cuando la velocidad cambia de dirección. En `v-x` se observa una línea horizontal en cada intervalo.

    ---

    === Una partícula parte del reposo desde $vec(r) = (3 hat(i) + 4 hat(j))$ m con $vec(v) = -(2 hat(i) + 4 hat(j))$ m/s. Encuentre su posición final y el desplazamiento cuando $t = 5$ s.

    *Implementación:* Se definieron los vectores posición inicial `ri` y velocidad `v` con paso `h=0.1`. Se utilizó un ciclo para actualizar la posición usando la fórmula vectorial. Se representó los vectores `ri`, `rf` y `Δr` usando `quiver`.

    *Código fuente: ej1.2.1.py*
    #code-block("src/pr_a/exe121.py", lang: "python")

    #image("img/pr_a/exe121.png")

    *Descripción:* En el gráfico se observa la trayectoria de la partícula con los vectores de posición inicial (azul), desplazamiento (rojo) y posición final (verde).

    ---

    === Una partícula parte del reposo desde $vec(r) = (3 hat(i) + 4 hat(j))$ m con una velocidad $vec(v) = -(4 hat(i) + 3 hat(j))$ m/s. Cuando inicia su movimiento se presenta una velocidad del viento $vec(v)_v = (3 hat(i) - 5 hat(j))$ m/s. Encuentre su posición final y el desplazamiento cuando $t = 10$ s.

    *Implementación:* Se calculó la velocidad resultante `vt = vp + vw`. Se utilizó un ciclo para actualizar la posición con la fórmula vectorial y se representó los vectores usando `quiver`.

    *Código fuente: ej1.2.2.py*
    #code-block("src/pr_a/exe122.py", lang: "python")

    #image("img/pr_a/exe122.png")

    *Descripción:* Se observa la trayectoria con vectores `ri`, `rf` y `Δr` considerando la velocidad del viento.

    ---
    === Una partícula parte del reposo desde $vec(r) = (3 hat(i) + 4 hat(j) + 5 hat(k))$ m con $vec(v) = -(2 hat(i) + 4 hat(j) + 6 hat(k))$ m/s. Cuando inicia su movimiento se presenta una velocidad del viento $vec(v)_v = (3 hat(j) - 5 hat(k))$ m/s. Encuentre su posición final y el desplazamiento cuando $t = 10$ s.

    *Implementación:* Se calculó la velocidad resultante `vt = vp + vw` en 3D. Se representó los vectores `ri`, `rf` y `Δr` usando `quiver` en proyección 3D.

    *Código fuente: ej1.3.1.py*
    #code-block("src/pr_a/exe131.py", lang: "python")

    #align(center)[
      #image("img/pr_a/exe131.png")
      _Figura 1 — Panel de variables del depurador mostrando `size = 3` (valor incorrecto)._
    ]


    *Descripción:* Se observa la trayectoria en 3D con los vectores de posición inicial, desplazamiento y posición final.

    ---

    === Una pelota se lanza con $v_y = 10$ m/s desde $y = 2$ m. Determine la altura máxima, cuando la velocidad sea cero, el tiempo donde llega a la altura máxima, el tiempo donde pasa por $y = 2$ y el tiempo en que llega al suelo.

    *Implementación:* Se definieron las condiciones iniciales `y=2`, `vy=10`, `ay=-10`, `h=0.01`. Se utilizó un ciclo `while` que continúa hasta que `y < 0`. Se calculó la altura máxima usando `np.argmax`.

    *Código fuente: ej2.1.1.py*
    #code-block("src/pr_a/exe211.py", lang: "python")

    #image("img/pr_a/exe211.png")

    *Resultados:*
    #table(
      columns: (auto, auto, auto),
      [*Parámetro*], [*Valor*], [*Unidad*],
      [Altura máxima], [7.00], [m],
      [Tiempo altura máx], [1.00], [s],
      [Tiempo pasa y=2], [2.00], [s],
      [Tiempo suelo], [2.45], [s],
    )

    *Descripción:* En `a-t` se observa una línea horizontal en `ay=-10` porque la gravedad es constante. En `v-t` se observa una línea recta con pendiente negativa porque la velocidad disminuye debido a la gravedad. En `y-t` se observa una parábola porque la pelota sube y baja. En `v-y` se observa una línea porque la velocidad depende de la altura.

    ---

    // === Una pelota se lanza desde el suelo con una velocidad de $v = 2$ m/s con un ángulo de $30^{\circ}$ con la horizontal. Determine la altura máxima, la velocidad en esa altura, el alcance y el tiempo en que llega al suelo.

    *Implementación:* Se calculó las componentes de velocidad inicial `vx = v0*cos(θ)`, `vy = v0*sin(θ)`. Se usó un ciclo `while` con `vy` decreciente debido a la gravedad.

    *Código fuente: ej2.2.1.py*
    #code-block("src/pr_a/exe222.py", lang: "python")

    #image("img/pr_a/exe222.png")

    *Resultados:*
    #table(
      columns: (auto, auto, auto),
      [*Parámetro*], [*Valor*], [*Unidad*],
      [Altura máxima], [0.10], [m],
      [Velocidad en H máx], [1.41], [m/s],
      [Alcance], [0.40], [m],
      [Tiempo suelo], [0.28], [s],
    )

    *Descripción:* En `a-t` se observa `ay=-10` constante. En `vy-t` se observa una línea con pendiente negativa. En `y-x` se observa una parábola porque es un movimiento parabólico. En `y-t` se observa una parábola.

    ---

    // === Una pelota se lanza desde el suelo con una velocidad de $2$ m/s con un ángulo de $30^{\circ}$ con la horizontal. Determine la altura máxima, la velocidad en esa altura, el alcance y el tiempo en que llega al suelo.

    *Implementación:* Se usaron las componentes vectoriales de velocidad `(vx, vy, vz)`. Se aplicó gravedad solo en eje Z `(az=-10)`. Se representó la trayectoria 3D y se calculó el desplazamiento horizontal.

    *Código fuente: ej2.3.1.py*
    #code-block("src/pr_a/exe223.py", lang: "python")

    #image("img/pr_a/exe223.png")

    *Resultados:*
    #table(
      columns: (auto, auto, auto),
      [*Parámetro*], [*Valor*], [*Unidad*],
      [Altura máxima], [2.25], [m],
      [Tiempo H máx], [0.60], [s],
      [Alcance horizontal], [6.12], [m],
      [Tiempo suelo], [1.15], [s],
    )

    *Descripción:* En `vz-t` se observa una línea con pendiente negativa. En `z-t` se observa una parábola. En `distancia-t` se observa una línea recta porque la magnitud horizontal es constante.

  ]

  #lab-section("CONCLUSIONES Y RECOMENDACIONES")[
    #show heading: set text(weight: "bold")
    #set par(justify: true)

    = CONCLUSIONES

    + 

    + 

    + 

    == RECOMENDACIONES

    + 

    + 

    + 
  ]
]
