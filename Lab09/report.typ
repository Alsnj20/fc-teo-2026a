#import "./lib.typ": code-block, lab-report, lab-section, table-border-width

#let course-name = "FISICA COMPUTACIONAL"
#let lab-title = "Laboratorio 4 - Movimiento Oscilatorio - Grupo B"
#let lab-number = "04"
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

    #set heading(numbering: "1.a.")


    = Sistema Masa-Resorte sin Fricción
    Un resorte con $k = 0.1 "N/m"$ unido a una masa $m = 0.2 "kg"$ se mueve horizontalmente en un medio donde no hay fricción. Si las condiciones iniciales son $x = -2$ y $v_x = 0$, grafique

    == Gráficos x-t, v-t, a-t y v-x en subplots
    \
    *Implementación:*
    Se define la masa m = 0.2 kg y la constante del resorte k = 0.1 N/m. Las condiciones iniciales son posición inicial x = -2 m y velocidad inicial vx = 0. Se utiliza el método de Euler con un paso de tiempo h = 0.01 s para integrar las ecuaciones de movimiento durante un tiempo total de 20 s. Se calculan la aceleración, velocidad y posición en cada paso de tiempo. Finalmente, se crean cuatro subplots en una sola figura: posición vs tiempo, velocidad vs tiempo, aceleración vs tiempo y velocidad vs posición (espacio de fase).

    *Código fuente:* `src/exe1/a.py`
    #code-block("src/exe1/a.py", lang: "python")

    #align(center)[
      #image("img/lab/exe1/a.png", width: 80%)
      _Fig. 1: Gráficos de posición, velocidad, aceleración y espacio de fase vs tiempo_
    ]

    *Resultados:*
    El gráfico muestra las cuatro gráficas solicitadas. En la gráfica de posición vs tiempo se observa un movimiento oscilatorio armónico simple con amplitud constante de 2 m y período de aproximadamente 2π segundos. La velocidad y aceleración también oscilan de forma sinusoidal con el mismo período pero desfasadas 90° y 180° respectivamente. El espacio de fase velocidad vs posición forma una elipse cerrada, indicando conservación de energía.
    \

    == Energías U-x, K-x, E-x en un solo gráfico
    \
    *Implementación:*
    Se define la masa m = 0.2 kg, constante del resorte k = 0.1 N/m y sin fricción (C = 0). Las condiciones iniciales son x = -2 m y vx = 0. Se utiliza el método de Euler con paso de tiempo muy pequeño h = 0.0001 s para mayor precisión en el cálculo de energía. En cada paso se calculan: energía cinética K = ½mv², energía potencial U = ½kx² y energía total E = K + U. Se grafican las tres energías en función de la posición x en un solo gráfico.

    *Código fuente:* `src/exe1/b.py`
    #code-block("src/exe1/b.py", lang: "python")

    #align(center)[
      #image("img/lab/exe1/b.png", width: 80%)
      _Fig. 2: Energías cinética, potencial y total vs posición_
    ]

    *Resultados:*
    El gráfico muestra las tres energías en función de la posición. La energía total (línea verde) se mantiene constante en todo el recorrido, confirmando la conservación de energía en el sistema sin fricción. La energía cinética (azul) y potencial (naranja) oscilan de manera complementaria: cuando la posición está en los extremos (x = ±2), la velocidad es cero y la energía es toda potencial; cuando pasa por el centro (x = 0), toda la energía es cinética.
    \

    == Espacio de fase tridimensional v-x-t
    \
    *Implementación:*
    Se utilizan los mismos parámetros del ejercicio anterior: m = 0.2 kg, k = 0.1 N/m, sin fricción, condiciones iniciales x = -2 m, vx = 0. Se integra con método de Euler durante 60 segundos para observar varias oscilaciones completas. Se almacenan los valores de posición, velocidad y tiempo en arrays. Se crea una gráfica tridimensional usando projection="3d" de matplotlib, donde el eje X representa la velocidad, el eje Y la posición y el eje Z el tiempo.

    *Código fuente:* `src/exe1/c.py`
    #code-block("src/exe1/c.py", lang: "python")

    #align(center)[
      #image("img/lab/exe1/c.png", width: 80%)
      _Fig. 3: Espacio de fase tridimensional posición-velocidad-tiempo_
    ]

    *Resultados:*
    El gráfico tridimensional muestra una trayectoria en forma de hélice que se proyecta como una elipse en el plano horizontal. Como se ve, la amplitud de la oscilación se mantiene constante a lo largo del tiempo, y la trayectoria no converge hacia el centro sino que forma bucles cerrados repetitivos, lo cual es característica del movimiento armónico simple sin fricción.
    \
    == Trayectorias x-t, v-t, a-t en un solo gráfico
    \
    *Implementación:*
    Se definen los mismos parámetros que en los ejercicios anteriores. Se integra con método de Euler durante 20 segundos con paso h = 0.01 s. Se almacenan posición, velocidad y aceleración en arrays. Se crea un solo gráfico con tres subplots superpuestos: posición vs tiempo, velocidad vs tiempo y aceleración vs tiempo, cada uno con su propia escala y color para facilitar la visualización.

    *Código fuente:* `src/exe1/d.py`
    #code-block("src/exe1/d.py", lang: "python")

    #align(center)[
      #image("img/lab/exe1/d.png", width: 80%)
      _Fig. 4: Trayectorias de posición, velocidad y aceleración vs tiempo_
    ]

    *Resultados:*
    El gráfico muestra las tres trayectorias superpuestas. La posición oscila entre -2 y 2 m. La velocidad oscila entre -1.25 y 1.25 m/s, alcanzando su máximo cuando la posición pasa por el centro (x=0). La aceleración oscila entre -0.5 y 0.5 m/s², siendo máxima en los extremos de la posición (x=±2) y cero en el centro.
    \


    = Sistema Masa-Resorte en Medio Friccionante
    Un resorte con $k = 0.1 "N/m"$ unido a una masa $m = 2 "kg"$ se mueve horizontalmente en un medio friccionante. Encuentre la constante c de tal manera que el resorte con su masa pase por $v_x=0$ diez veces. Si las condiciones iniciales $x = -2$ y $v_x = 0$, grafique

    == Gráficos x-t, v-t, a-t y v-x en cuatro gráficos utilizando subplots
    \
    *Implementación:*
    Se define la masa m = 2 kg, constante del resorte k = 0.1 N/m y se busca la constante de fricción c tal que el sistema pase por vx=0 diez veces. Se prueba con diferentes valores de c hasta encontrar el adecuado (c ≈ 0.19999 Ns/m). Con estas condiciones iniciales, se integra con método de Euler durante 150 segundos con paso h = 0.01 s. Se almacenan posición, velocidad y aceleración en arrays. Se crean cuatro subplots: posición vs tiempo, velocidad vs tiempo, aceleración vs tiempo y espacio de fase velocidad vs posición.


    *Código fuente:* `src/exe2/a.py`
    #code-block("src/exe2/a.py", lang: "python")

    #align(center)[
      #image("img/lab/exe2/a.png", width: 80%)
      _Fig. 5: Gráficos de posición, velocidad, aceleración y espacio de fase con fricción_
    ]

    *Resultados:*
    El gráfico muestra las cuatro gráficas del sistema con fricción. Se observa que la amplitud de la oscilación disminuye progresivamente con el tiempo (movimiento subamortiguado). El sistema cruza por x=0 exactamente 10 veces como se pedía. En el espacio de fase, la trayectoria forma una espiral que converge hacia el origen, indicando la pérdida gradual de energía debido a la fricción.
    \

    == Espacio de fase tridimensional v-x-t
    \
    *Implementación:*
    Se utilizan los mismos parámetros del ejercicio anterior: m = 2 kg, k = 0.1 N/m, C = 0.199999 Ns/m, condiciones iniciales x = -2 m, vx = 0. Se integra con el método de Euler durante 200 segundos y se almacenan los valores de posición, velocidad y tiempo. Se crea una gráfica tridimensional donde los ejes representan posición, velocidad y tiempo respectivamente.

    *Código fuente:* `src/exe2/b.py`
    #code-block("src/exe2/b.py", lang: "python")

    #align(center)[
      #image("img/lab/exe2/b.png", width: 80%)
      _Fig. 6: Espacio de fase tridimensional con fricción_
    ]

    *Resultados:*
    El gráfico tridimensional muestra una trayectoria en forma de espiral que se va cerrando hacia el centro a medida que avanza el tiempo. A diferencia del caso sin fricción que formaba una hélice abierta, aquí la espiral converge hacia el origen, lo cual evidencia que la energía mecánica se disipa gradualmente debido a la fricción del medio.
    \


    = Sistema Masa-Resorte con/sin Fuerza Externa
    Un resorte con $k = 0.1 "N/m"$ unido a una masa $m = 0.5$ se mueve horizontalmente en un medio $c = 0.15 "Ns/m"$ donde hay fricción. Luego actúa una fuerza externa cuya amplitud $F_0 = 0.01 "N"$ y $w = 0.2 "rad/s"$. Si las condiciones iniciales son $x = -1$ y $v_x =0$, grafique

    == Comparativa: Simulación sin fuerza externa vs con fuerza externa
    \
    *Implementación:*
    Se define un sistema con masa m = 0.5 kg, constante del resorte k = 0.1 N/m, coeficiente de fricción c = 0.15 Ns/m. Se consideran dos casos: (1) sin fuerza externa (F0 = 0), (2) con fuerza externa de amplitud F0 = 0.01 N y frecuencia angular w = 0.2 rad/s. Las condiciones iniciales son x = -1 m y vx = 0. Se utiliza el método de Euler con paso h = 0.01 s durante 100 s. Se realizan dos simulaciones independientes y se grafican ambas curvas de posición vs tiempo en un mismo gráfico para comparar su comportamiento.

    *Código fuente:* `src/exe3/a.py`
    #code-block("src/exe3/a.py", lang: "python")

    #align(center)[
      #image("img/lab/exe3/a.png", width: 80%)
      _Fig. 7: Comparación de posición vs tiempo con y sin fuerza externa_
    ]

    *Resultados:*
    El gráfico muestra claramente la diferencia entre ambos casos. Sin fuerza externa (línea roja discontinua), el sistema pierde energía rápidamente debido a la fricción y la oscilación se amortigua hasta detenerse. Con fuerza externa (línea azul continua), el sistema alcanza un estado estacionario donde oscila indefinidamente con amplitud constante, ya que la fuerza externa compensa la energía perdida por fricción.
    \

    == Gráficos x-t, v-t, a-t y v-x en subplots con/sin fuerza externa
    \
    *Implementación:*
    Se utilizan los mismos parámetros del ejercicio anterior (m = 0.5 kg, k = 0.1 N/m, c = 0.15 Ns/m, F0 = 0.01 N, w = 0.2 rad/s). Se realizan dos simulaciones simultáneas: una con fuerza externa y otra sin ella. Se calculan posición, velocidad y aceleración para ambos casos en cada paso de tiempo. Se crean cuatro subplots en una figura 2x2: posición vs tiempo, velocidad vs tiempo, aceleración vs tiempo y espacio de fase v-x. En cada subplot se representan ambas simulaciones con diferentes colores y tipos de línea para facilitar la comparación.

    *Código fuente:* `src/exe3/b.py`
    #code-block("src/exe3/b.py", lang: "python")

    #align(center)[
      #image("img/lab/exe3/b.png", width: 80%)
      _Fig. 8: Comparación de posición, velocidad, aceleración y espacio de fase_
    ]

    *Resultados:*
    El gráfico muestra las cuatro variables cinemáticas para ambos casos. En las gráficas de posición, velocidad y aceleración, se observa que el sistema sin fuerza externa (líneas discontinuas) decae hacia cero, mientras que el sistema con fuerza externa (líneas continuas) mantiene oscilaciones de amplitud constante. En el espacio de fase, el caso sin fuerza externa converge al origen, mientras que el caso con fuerza externa describe una trayectoria compleja pero estable.
    \
    == Espacio de fase tridimensional v-x-t con/sin fuerza externa
    \
    *Implementación:*
    Se utilizan los mismos parámetros anteriores (m = 0.5 kg, k = 0.1 N/m, c = 0.05 Ns/m - valor diferente al original para mejor visualización, F0 = 0.01 N, w = 0.2 rad/s). Se realizan dos simulaciones: una con fuerza externa y otra sin ella. Se almacenan los valores de posición, velocidad y tiempo para cada caso. Se crea una gráfica tridimensional con projection="3d" donde se representan ambas trayectorias en el espacio fase-tiempo con diferentes colores para distinguir cada caso.

    *Código fuente:* `src/exe3/c.py`
    #code-block("src/exe3/c.py", lang: "python")

    #align(center)[
      #image("img/lab/exe3/c.png", width: 80%)
      _Fig. 9: Espacio de fase tridimensional con y sin fuerza externa_
    ]

    *Resultados:*
    El gráfico tridimensional muestra dos trayectorias diferentes. La trayectoria azul (con fuerza externa) forma una especie de cilindro o tubo que no converge al centro, representando el estado estacionario de oscilación forzada. La trayectoria naranja (sin fuerza externa) forma una espiral que converge hacia el origen, representando el sistema amortiguado sin excitación externa. Esto ilustra claramente cómo la fuerza externa mantiene la oscilación del sistema.
    \

    == Ubicación el lugar donde la fuerza externa toma acción
    \
    *Implementación:*
    Este ejercicio tiene como objetivo determinar el punto exacto donde la fuerza externa comienza a influir significativamente en el sistema. La lógica del código es la siguiente: se realizan dos simulaciones simultáneas con los mismos parámetros (m = 0.5 kg, k = 0.1 N/m, c = 0.15 Ns/m, condiciones iniciales x = -1 m, vx = 0), pero en una se incluye la fuerza externa (F0 = 0.01 N, w = 0.2 rad/s) y en la otra no (F0 = 0). En cada paso de tiempo se calcula la diferencia entre las posiciones de ambos sistemas: diff(t) = x_con_fuerza(t) - x_sin_fuerza(t).

    El código espera los primeros 5 segundos para que el sistema se estabilice y luego busca el punto donde el signo de la diferencia cambia (es decir, cuando diff(t) pasa de positivo a negativo o viceversa). Esto indica que las dos trayectorias se cruzan y a partir de ese momento la influencia de la fuerza externa se vuelve notoria. Cuando se detecta este cruce, se marca el punto con un círculo rojo en la gráfica.

    *Código fuente:* `src/exe3/d.py`
    #code-block("src/exe3/d.py", lang: "python")

    #align(center)[
      #image("img/lab/exe3/d.png", width: 80%)
      _Fig. 10: Ubicación donde la fuerza externa toma acción_
    ]

    *Resultados:*
    El gráfico muestra las dos curvas de posición vs tiempo. La línea azul representa el sistema con fuerza externa y la línea roja el sistema sin fuerza externa. El punto marcado con un círculo rojo indica el momento exacto donde ambas curvas se cruzan y la fuerza externa comienza a dominar el comportamiento del sistema. Como se observa, inicialmente ambas curvas son casi idénticas, pero después del punto de cruce, la curva con fuerza externa diverge y mantiene oscilaciones mientras la otra decae.
    \

    = Figuras de Lissajous

    Para graficar las figuras de Lissajous. Sean las ecuaciones
    \
    \
    $a_x = -k_1/m_1 x$ y $a_y = -k_2/m_2 y$.
    \
    \
    - varie $k_1/m_1=l^2$ para $l = 1, 2, 3,...$. Si $m_1 = 1$, entonces $k_1 = l^2$. Si $l=1$, entonces $k_1 = 1$.
    - varie $k_2/m_2=n^2$ para $n = 1, 2, 3,...$. Si $m_2 = 1$, entonces $k_2 = n^2$. Si $n=1$, entonces $k_2 = 1$.

    Grafique las figuras de Lissajous para los siguientes casos:

    1. Trayectorias base con condiciones iniciales dadas $x=1$, $v_x=2.36$, $y=1$, $v_y=0.0$
    2. Fabrique para cada cosas con las mismas condiciones iniciales.
    - (a) Caso l = 1, n = 2
    - (b) Caso l = 1, n = 3
    - (c) Caso l = 2, n = 3
    - (d) Caso l = 3, n = 4
    - (e) Caso l = 3, n = 5
    - (f) Caso l = 4, n = 5
    - (g) Caso l = 5, n = 6

    \
    *Implementación:*
    Para graficar las figuras de Lissajous, se considera un sistema de dos osciladores armónicos desacoplados en las direcciones x e y. Las ecuaciones de movimiento son: $a_x = -k_1/m_1x$ y $a_y = -k_2/m_2y$. Se fijan las masas $m_1 = m_2 = 1$. Las relaciones $k/m$ se variaron según los valores de l y n: para l=1,2,3,... se tiene k_1 = l²; para n=1,2,3,... se tiene k_2 = n².
    Las condiciones iniciales son: x = 1 m, vx = 2.36 m/s, y = 1 m, vy = 0 m/s. Se utiliza el método de Euler con paso h = 0.01 s para integrar ambas ecuaciones simultáneamente. Se generan figuras para los casos: (a) l=1, n=2, (b) l=1, n=3, (c) l=2, n=3, (d) l=3, n=4, (e) l=3, n=5, (f) l=4, n=5, (g) l=5, n=6. Se crea una cuadrícula de subplots 3x3 para mostrar todas las figuras en una sola figura.

    *Código fuente:* `src/exe4/4.py`
    #code-block("src/exe4/4.py", lang: "python")

    #align(center)[
      #image("img/lab/exe4/4_lissajous_figures.png", width: 90%)
      _Fig. 11: Figuras de Lissajous para diferentes valores de l y n_
    ]

    *Resultados:*
    El gráfico muestra las siete figuras de Lissajous para diferentes relaciones de frecuencia. Cada figura representa la trayectoria en el plano xy del sistema bidimensional. Como se observa, cuando la relación entre las frecuencias es un número racional simple (como 1:2, 1:3, 2:3), las figuras forman curvas cerradas y simétricas. La complejidad de la figura aumenta a medida que los valores de l y n aumentan, formando patrones cada vez más intrincados que reflejan la relación entre las frecuencias de oscilación en ambas direcciones.
    \
  ]

  #lab-section("CONCLUSIONES Y RECOMENDACIONES")[
    #show heading: set text(weight: "bold")
    #set par(justify: true)

    = CONCLUSIONES

    + Se demostró que en un sistema sin fricción, la energía total se conserva perfectamente, manifestándose en un espacio de fase de bucle cerrado.
    + La incorporación de un medio friccionante provoca la disipación de la energía mecánica, evidenciado por el decaimiento exponencial de la amplitud y la convergencia al origen en el espacio de fase.
    + La acción de una fuerza externa armónica contrarresta la pérdida por fricción, llevando al sistema a un régimen estacionario de oscilación que depende enteramente de la fuerza impulsora.

    == RECOMENDACIONES

    + Utilizar siempre pasos de integración pequeños (h) en métodos numéricos como Euler para reducir el error de aproximación acumulado en simulaciones largas.
    + Analizar los problemas desde distintas perspectivas gráficas, como el espacio de fase y la energía, para una comprensión holística del comportamiento del sistema físico.
  ]
]
