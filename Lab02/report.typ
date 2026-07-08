#import "./lib.typ": code-block, lab-report, lab-section, table-border-width

#let course-name = "FISICA COMPUTACIONAL"
#let lab-title = "Resolución de la Práctica 2: Laboratorio B"
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

    #set heading(numbering: "1.1.1")

    == Ejercicio 1: Circunferencia de radio 3
    *Problema:*
    Graficar una circunferencia con radio $r = 3$ cuyo centro esta en el origen.

    *Implementación:* Se definieron las funciones de aceleración ax y ay que calculan la aceleración gravitatoria. Se utilizó el método de Euler para integrar las ecuaciones de movimiento con un paso temporal h = 0.01. Las trayectorias se inicializaron desde el punto (0, -3) con diferentes velocidades iniciales en el eje x (vx0 variando de 0.5 a 1.5). Debido al comportamiento de la condiciones iniciales, se dibujaron múltiples trayectorias alrededor de una circunferencia de radio r = 3 con centro en el origen.

    *Código fuente: exe1.py*
    #code-block("src/pr_b/exe1.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe1.png")
      _Figura 1: Gráfico de la circunferencia con radio $r = 3$ m_
    ]

    *Resultados:* En el gráfico se observa la circunferencia de radio 3 con centro en el origen (0,0). Las trayectorias de partículas siguen órbitas que pasan cerca de la circunferencia, algunas completan revoluciones y otras escapan. El patrón muestra cómo diferentes velocidades iniciales producen diferentes tipos de trayectorias alrededor del centro gravitatorio.

    \

    == Ejercicio 2: Omision grafica en r <= 3
    *Problema:*
    Cuando la trayectoria llegue a $r = sqrt((x-1)^2 + y^2) <= 3$ que no grafique pero debe continuar la simulación.

    *Implementación:* Se-modificó la función ax(x,y) para que calculate la aceleración considerando el centro en (1,0) según la fórmula -(x-1)/r³. Se agregó la condición de omisión gráfica dentro del bucle: cuando la distancia al centro sea menor o igual a r (sqrt((x-1)²+y²) <= 3), se deja de agregar puntos a la trayectoria (usando break) pero la simulación continúa para las demás partículas. Esto permite que las partículas que chocan no se grafiquen dentro del círculo.

    *Código fuente: exe2.py*
    #code-block("src/pr_b/exe2.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe2.png")
      _Figura 2: Grafico de la trayectoria omitiendo r <= 3 m_
    ]


    *Descripción:* El gráfico muestra múltiples trayectorias evitando el interior del círculo de radio 3 con centro en (1,0). Como se puede observar, las líneas no penetran en el área sombreada del círculo, lo que indica que la condición de omisión funciona correctamente. Las partículas que chocan contra el obstáculo se detienen en el borde sin ser graficadas en el interior.



    == Ejercicio 3: Parabolas, Elipses e Hiperbolas
    *Problema:*
    Grafique en un misma ventana, dos parábolas, dos elipses y dos hiperbolas


    *Implementación:* Se-modificó la función ax(x,y) para que calculara la aceleración considerando el centro en (0,1) en lugar de (0,0). Se implementó la clasificación de trayectorias basándose en el comportamiento: las parábolas tienen velocidad baja y chocan con el obstáculo circular (r <= 3), las elipses tienen velocidad media y permanecen en órbita cerca del centro (distancia final <= 20), y las hiperbolas tienen velocidad alta y escapan del sistema. Se almacenaron las primeras dos trayectorias de cada tipo para graficarlas.

    *Código fuente: exe3.py*
    #code-block("src/pr_b/exe3.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe3.png")
      _Figura 3: Dos parábolas, dos elipses y dos hiperbolas en una misma ventana_
    ]


    *Descripción:* El gráfico muestra dos parábolas de color naranja que representan las trayectorias de baja velocidad que chocan con el obstáculo circular. Se observa también dos elipses de color morado que corresponden a las órbitas estables donde la partícula gira alrededor del centro sin chocar ni escapar. Las dos hipérbolas de color azul claro representan las trayectorias de alta velocidad que escapan del campo gravitatorio. Como se puede observar, las parábolas son las más cortas porque terminan en colisión, las elipses son cerradas y recurrentes, y las hipérbolas se abren y se alejan del centro.

    \

    == Ejercicio 4: Repetición con vx = vy
    *Problema:*
    Repita el paso anterior para vx = vy . Debe notarse claramente el efecto de vx


    *Implementación:* Se-agregó la condición para que la velocidad inicial en y sea igual a la velocidad inicial en x (vy = vx0), de modo que las partículas partan con velocidad diagonal. Se-modificaron los puntos de guardado usando variables individuales (parabola_choque_1_x, parabola_choque_1_y, etc.) en lugar de listas para almacenar las dos parábolas, dos elipses y dos hipérbolas. El límite de escape se aumentó a 70 para permitir que las hiperbolas se observen mejor.

    *Código fuente: exe4.py*
    #code-block("src/pr_b/exe4.py", lang: "python")


    #align(center)[
      #image("img/pr_b/exe4.png", width: 40%)
      _Figura 4: Dos parábolas, dos elipses y dos hiperbolas en una misma ventana con vx = vy_

    ]


    *Descripción:* El gráfico se observa cómo al hacer vy = vx, las trayectorias ahora tienen un componente diagonal desde el inicio. Las parábolas de color naranja siguen chocando con el obstáculo pero con un ángulo diferente. Las elipses de color morado muestran órbitas más simétricas debido a la velocidad inicial diagonal. Las hipérbolas de color azul claro escapan del sistema con trayectorias más amplias. Como se ve, el efecto de vx = vy produce trayectorias más simétricas y balanceadas en comparación con el ejercicio anterior donde solo se tenía vx.
  ]

  #lab-section("CONCLUSIONES Y RECOMENDACIONES")[
    #show heading: set text(weight: "bold")
    #set par(justify: true)

    = CONCLUSIONES

    + Se demostró que la simulación gravitatoria puede producir diferentes tipos de trayectorias (parábolas, elipses, hipérbolas) dependiendo de la velocidad inicial de la partícula. Las partículas con baja velocidad chocan (parábolas), las de velocidad media orbitan (elipses), y las de alta velocidad escapan (hipérbolas).

    + El método de Euler funciona correctamente para integrar las ecuaciones de movimiento en problemas gravitatorios, permitiendo visualizar las órbitas y sus transiciones. Sin embargo, para simulaciones de larga duración pueden acumularse errores numéricos que afectan la precisión.

    + El cambio de vy = vx produce trayectorias más simétricas debido a que la partícula comienza con un componente diagonal, mostrando el efecto de la dirección inicial en la forma de la órbita.


    == RECOMENDACIONES

    + Es importante ajustar adecuadamente los parámetros de tiempo (h) y el número máximo de iteraciones para evitar errores de overflow o tiempos de cómputo excesivos.

    + Se recomienda validar los resultados con valores teóricos knownos (como el período de una órbita circular) para asegurar la correcta implementación del modelo físico.
  ]
]
