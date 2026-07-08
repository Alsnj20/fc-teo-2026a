#import "./lib.typ": code-block, lab-report, lab-section, table-border-width

#let course-name = "FISICA COMPUTACIONAL"
#let lab-title = "Resolución de la Práctica3: Problemas 3 cuerpos: Laboratorio B"
#let lab-number = "03"
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


    #set heading(numbering: "1.1.1")
    = SOLUCIÓN DE LOS EJERCICIOS PROPUESTOS

    == Ejercicio 1: Primera Circunferencia de radio 1
    *Problema:*
    Graficar una circunferencia con radio $r = 1$ cuyo centro esta en el punto $(+b, -c)$. Elegir b y c a su criterio.

    *Implementación:*
    Comenzamos definiendo las variables y condiciones iniciales, los valores elegidos para b y c son 3 y 2 respectivamente. Pasamos a definir la funciones de aceleración $a_x$ y $a_y$. El paso de tiempo es $h = 0.1$ y $k = 0.1$, empezaremos dibujando el circulo y luego a traves de un for haremos las trayectorias.

    *Código fuente: exe1.py*
    #code-block("src/pr_b/exe1.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe1.png")
      _Figura 1: Gráfico de la primera circunferencia con radio $r = 1$ m_
    ]

    *Resultados:*
    El gráfico muestra trayectorias de partículas que se originan desde el punto $(0, -4)$ con diferentes velocidades iniciales. Como se ve, las trayectorias más lentas (vx pequeño) orbitan cerca de la masa central, formando bucles cerrados alrededor del punto $(3, -2)$. Conforme vx aumenta, las órbitas se abren más, evidenciando que la energía cinética inicial determina el tipo de órbita. La circunferencia negra de radio 1 centrada en $(3, -2)$ representa la masa atractora. Todas las trayectorias divergen hacia la derecha cuando tienen suficiente energía, mostrando el comportamiento característico de órbitas parabólicas e hiperbólicas.
    \

    == Ejercicio 2: Segunda Circunferencia de radio 1
    *Problema:*
    Graficar una circunferencia con radio $r = 1$ cuyo centro esta en el punto $(-b, -c)$.

    *Implementación:*
    Este ejercicio extiende el anterior al agregar una segunda masa puntual en $(-3, -2)$, manteniendo la primera en $(3, -2)$. Se mantienen las funciones $a_x$ y $a_y$. De igual forma dibujamos las dos circunferencias y luego a traves de un for haremos las trayectorias.

    *Código fuente: exe2.py*
    #code-block("src/pr_b/exe2.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe2.png")
      _Figura 2: Gráfico de la segunda circunferencia con radio $r = 1$ m_
    ]

    *Resultados:*
    El gráfico muestra trayectorias en un campo gravitacional de dos masas. Como se ve, las órbitas ahora son asimétricas respecto al eje vertical, favoreciendo trayectorias hacia la derecha donde hay mayor energía potencial combinada. Se observan órbitas complejas alrededor del punto de equilibrio entre las dos masas. Las trayectorias con velocidades bajas permanecen confinadas entre ambas masas, mientras que las de mayor velocidad escapan del sistema. Las dos circunferencias negras en $(3, -2)$ y $(-3, -2)$ marcan los centros de las masas atractoras, haciendo evidente la simetría bilateral del potencial gravitacional.
    \

    == Ejercicio 3: Implemerta las funciones ax y ay
    *Problema:*
    Genere las funciones ax(x, y) y ay(x, y), sabiendo que:

    *Implementación:*
    Para empezar a implementar primero haremos las funciones de aceleración para un sistema de dos cuerpos de acuerdo a la imagen mostrada del laboratorio.
    // Define ax y ay
    $
      a_x (x, y, b_1, c_1, b_2, c_2) =
      - (x - b_1) / ((x - b_1)^2 + (y - c_1)^2)^(3/2)
      - (x - b_2) / ((x - b_2)^2 + (y - c_2)^2)^(3/2)
    $

    $
      a_y (x, y, b_1, c_1, b_2, c_2) =
      - (y - c_1) / ((x - b_1)^2 + (y - c_1)^2)^(3/2)
      - (y - c_2) / ((x - b_2)^2 + (y - c_2)^2)^(3/2)
    $

    Definidas estas funciones, procederemos a mejorar los parámetros de simulación: paso de tiempo $h = 0.3$, rango de velocidades $v_x \in [0.5, 1.5)$, y tiempo final $t_"fin" = 300$ segundos. Se agrega protección contra escape ilimitado deteniendo la simulación si la partícula alcanza $|x| > 20$ o $|y| > 20$.

    *Código fuente: exe3.py*
    #code-block("src/pr_b/exe3.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe3.png")
      _Figura 3: Gráfico de las funciones ax y ay_
    ]

    *Resultados:*
    El gráfico muestra órbitas más complejas alrededor de dos masas. Como se ve, se forman regiones de caoticidad donde pequeñas variaciones en las condiciones iniciales generan trayectorias radicalmente diferentes. Las órbitas oscilan en patrones intrincados entre las dos masas, con bucles múltiples y ciclos de mayor amplitud. Se observan órbitas periódicas y cuasiperiódicas que forman estructuras roseta alrededor del sistema de dos masas en $(3, -2)$ y $(-3, -2)$. Las trayectorias en color naranja que oscilan en el centro demuestran movimiento altamente acoplado donde ambas masas influyen significativamente en la dinámica.
    \

    == Ejercicio 4: No graficar si la partícula colapsa o se escapa
    *Problema:*
    Si las trayectorias llegan a las circunferencias, que no grafique

    *Implementación:*
    Se implementa un sistema de validación de trayectorias que detecta dos condiciones de terminación: colapso y escape. Se añade una condición de colapso verificando si la distancia de la partícula a cualquiera de las dos masas es menor o igual al radio $r = 1$. También se limita el escape lateral con $y > 50$. Solo se grafican trayectorias que ni colapsan ni escapan, permitiendo así visualizar únicamente órbitas ligadas y estables. El paso de tiempo es $h = 0.3$ con $t_"fin" = 100$ segundos y paso de velocidad $k = 0.02$.

    *Código fuente: exe4.py*
    #code-block("src/pr_b/exe4.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe4.png")
      _Figura 4: Gráfico de las trayectorias sin colapsar ni escapar_
    ]

    *Resultados:*
    El gráfico presenta únicamente trayectorias que permanecen ligadas al sistema de dos masas. Como se ve, hay un gran número de trayectorias que se abren radialmente hacia arriba sin llegar a alcanzar $y > 50$. Las órbitas más cerradas y oscilatorias alrededor de las masas son las que ni colapsan ni escapan, conformando una familia discreta de órbitas periódicas. Se observa una cuña de trayectorias que emergen del espacio entre las dos masas, demostrando que la geometría del sistema de dos cuerpos crea canales de movimiento preferentes. Las trayectorias largas y casi rectas indican movimiento de alta energía con deflexión controlada por ambas masas.
    \


    == Ejercicio 5: 4 trayectorias
    *Problema:*
    Encuentre 4 trayectorias

    *Implementación:*
    Se buscan específicamente 4 trayectorias que no sufran colapso ni escape. El algoritmo itera sobre velocidades iniciales $v_x$ usando interpolación lineal entre 0.01 y 3, y al encontrar una trayectoria válida, la almacena con etiqueta y contador. Se incrementa precisión mediante paso temporal más pequeño $h = 0.0025$ y tiempo de simulación prolongado $t_"fin" = 300$ segundos. Las condiciones de validez se mantienen: $|x|, |y| < 50$ y distancia a masas $> r = 1$. Una vez encontradas las 4 trayectorias, el bucle se detiene.

    *Código fuente: exe5.py*
    #code-block("src/pr_b/exe5.py", lang: "python")

    #align(center)[
      #image("img/pr_b/exe5.png")
      _Figura 5: Gráfico de las 4 trayectorias_
    ]

    *Resultados:*
    El gráfico muestra 4 órbitas periódicas y quasiperiódicas alrededor del sistema de dos masas. Como se ve, cada trayectoria posee una firma característica: la trayectoria 1 (azul) ejecuta oscilaciones verticales pronunciadas cruzando entre ambas masas, la trayectoria 2 (naranja) forma órbitas más anchas alrededor del centro del sistema, la trayectoria 3 (verde) describe bucles cerrados sobre la derecha, y la trayectoria 4 (roja) muestra órbitas alargadas. Las cuatro trayectorias convergen cerca del punto de silla entre las masas, demostrando que existen canales de resonancia orbital. La simetría aproximada respecto al eje Y sugiere que el sistema de dos masas equidistantes del origen crea potencial simétrico con familia de órbitas predecibles.
    \

    == Ejercicio 6: Trayectorias y Naves
    *Problema:*
    Una nave se ubica $(x,y)$ y otra en $(x+0.01,y)$. Si ambas tienen las mismas iniciales, dibuje solo dos trayeectorias que correspondan a las dos naves. Considere tiempos largos. Que observa?

    *Implementación:*
    Se implementan dos naves idénticas salvo en posición inicial: Nave A en $(0, 7)$ y Nave B en $(0.01, 7)$, separadas por $Delta x = 0.01$. Ambas tienen velocidad inicial $v_x = 8 times 10^(-7)$, $v_y = 10^(-8)$ (valores cercanos a cero para observar la trayectoria). El paso de tiempo es $h = 0.01$ y la simulación corre durante $t_"fin" = 800$ segundos.

    *Lógica del Ejercicio 6 - Explicación Detallada:*
    La clave de este ejercicio radica en entender que el parámetro que influencia el comportamiento es principalmente $v_x$, no las posiciones iniciales. Aunque se establece una pequeña separación de 0.01 unidades, el valor crítico es que $v_x$ sea cercano a cero. Esta es la razón por la que se puede observar claramente la trayectoria: con $v_x$ pequeño, la partícula no escapa rápidamente del sistema y permanece lo suficiente bajo influencia gravitacional para describir órbitas complejas. Si $v_x$ fuera grande, ambas naves atravesarían rápidamente el sistema sin ser capturadas. Con $v_x$ pequeño, la nave desacelera en la región de las masas, se vuelve en una órbita, y desarrolla una dinámica sensible a pequeñas perturbaciones. La separación inicial de 0.01 es suficientemente pequeña que las dos naves siguen trayectorias prácticamente idénticas al inicio, pero la aceleración no lineal (dependencia proporcional a distancia inversa al cubo) amplifica la diferencia exponencialmente en tiempos largos, generando divergencia caótica.

    *Código fuente: exe6.py*
    #code-block("src/pr_b/exe6.py", lang: "python")
    #align(center)[
      #image("img/pr_b/exe6.png")
      _Figura 6: Gráfico de las trayectorias de las dos naves_
    ]

    *Resultados:*
    El gráfico muestra un fenómeno de caos determinista. Como se ve, ambas naves (azul y rojo) comienzan superpuestas y siguen trayectorias casi idénticas durante los primeros ciclos orbitales alrededor de las dos masas. Las naves orbitan juntas alrededor del punto de equilibrio entre las dos masas en $(3, -2)$ y $(-3, -2)$, ejecutando oscilaciones en espiral. Sin embargo, después de varios ciclos, las trayectorias divergen significativamente: la nave A (azul) forma un bucle más cerrado a la derecha, mientras que la nave B (rojo) desarrolla una órbita más abierta hacia abajo. Esta divergencia exponencial es característica de sistemas caóticos donde pequeñas diferencias iniciales se amplifican por la naturaleza no lineal de las fuerzas gravitacionales. El hecho de que inicialmente sean prácticamente indistinguibles pero terminen muy separadas demuestra la sensibilidad a condiciones iniciales, marca fundamental de la dinámica caótica. La observación es que el sistema de tres cuerpos (las dos masas y la nave) exhibe comportamiento impredecible a largo plazo, validando que perturbaciones minúsculas producen trayectorias radicalmente diferentes.
    \

  ]

  #lab-section("CONCLUSIONES Y RECOMENDACIONES")[
    #show heading: set text(weight: "bold")
    #set par(justify: true)

    = CONCLUSIONES

    + El problema de dos y tres cuerpos en gravitación exhibe comportamiento fundamentalmente distinto del problema de un cuerpo. Mientras que una sola masa central produce órbitas predecibles (elipses, parábolas, hipérbolas), dos masas generan dinámica caótica con órbitas periódicas alternadas con movimiento impredecible. Los ejercicios 1-5 demuestran cómo la arquitectura orbital se vuelve progresivamente más compleja: del sistema simple de una masa (ej. 1) a la complejidad de dos masas (ej. 2-5), donde coexisten órbitas ligadas, escape gravitacional, y resonancias periódicas.

    + El ejercicio 6 demuestra la sensibilidad extrema a condiciones iniciales característica de sistemas caóticos. Dos naves separadas por apenas 0.01 unidades en posición x, siguiendo ecuaciones de movimiento idénticas y deterministas, divergen completamente después de tiempos prolongados. Esto prueba que la integración numérica captura la esencia del caos determinista: predictibilidad a corto plazo con impredecibilidad a largo plazo. El papel crucial de $v_x$ cercano a cero permite que las perturbaciones exponenciales de la dinámica no lineal se desarrollen completamente antes del escape del sistema.

    == RECOMENDACIONES

    + Para futuras prácticas, se recomienda explorar la influencia de la masa relativa de las dos masas centrales en la dinámica orbital. Variar la relación de masas (por ejemplo, una masa mucho mayor que la otra) podría revelar cómo el sistema transita entre comportamiento más predecible (dominancia de una masa) a caos completo (masas comparables). Además, implementar métodos de integración numérica más avanzados (como Runge-Kutta de orden superior) podría mejorar la precisión y permitir simular trayectorias durante tiempos aún más largos sin pérdida significativa de energía, lo que es crucial para estudiar el caos a largo plazo.
  ]
]
