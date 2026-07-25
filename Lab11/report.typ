#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 11 - Secciones de Poincaré - Grupo B",
  lab_number: "11",
  instructor_name: "Prof. Edwin Agapito Llamoca Requena",
  members: members,
  members_abbr_full_names: members.map(name => summarize-name(name, positions: (0, 2), separator: ",")).join(" - "),
)

#set image(width: 70%)
#set list(indent: 2pt)


#lab-section(title: "RESULTADOS Y PRUEBAS")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)
  = SOLUCIÓN DE LOS EJERCICIOS PROPUESTOS

  La sección de Poincaré es una técnica que permite estudiar la dinámica de un sistema registrando el estado de las variables (posición y velocidad) únicamente en instantes separados por un periodo fijo. De este modo, una trayectoria continua en el espacio de fases se reduce a un conjunto discreto de puntos cuya distribución revela si el movimiento es periódico, cuasiperiódico o caótico. En este laboratorio se aplican los métodos de Euler y Runge-Kutta de cuarto orden (RK4) a distintos osciladores y se construyen las secciones de Poincaré correspondientes.

  #set heading(numbering: "1.a.")

  = Oscilador no lineal conservativo — Método de Euler

  \
  *Implementación:* Se define el oscilador con aceleración $a = x - x^3$, que corresponde a un sistema conservativo con un potencial de doble pozo. Se establecen las condiciones iniciales $x_0 = sqrt(2)$ y $v_0 = 0$, y se avanza la solución mediante el método de Euler con un paso de tiempo $h = 0.0001$ durante 30 segundos. En cada iteración se actualizan la posición y la velocidad a partir de la aceleración evaluada en el instante actual. Los valores se almacenan en listas y se organizan cuatro gráficos en una cuadrícula de 2×2: posición contra tiempo, velocidad contra tiempo, aceleración contra tiempo y la trayectoria tridimensional $x$-$v$-$t$.

  *Código fuente:* `src/exe1.py`
  #code-block(file: "src/exe1.py", lang: "python")

  #align(center)[
    #image("img/lab/exe1.png", width: 90%)
    _Fig. 1: Diagramas x-t, v-t, a-t y trayectoria x-v-t del oscilador $a = x - x^3$_
  ]

  *Resultados:* La posición oscila entre valores positivos y negativos de manera no sinusoidal, con estancias prolongadas cerca de los puntos de equilibrio estable ($x = plus.minus 1$) y transiciones rápidas entre ambos pozos. La velocidad alcanza sus valores máximos durante dichas transiciones y se anula en los extremos de la oscilación. La aceleración presenta picos pronunciados en los cruces por la zona inestable ($x = 0$), donde la fuerza restauradora cambia de signo. En el gráfico tridimensional se distingue una órbita cerrada en el plano $x$-$v$ que se extiende a lo largo del eje temporal, confirmando que el sistema es conservativo y la trayectoria es periódica.
  \

  = Oscilador amortiguado — Método RK4

  \
  *Implementación:* Se incorpora un término de amortiguamiento lineal al oscilador, resultando en la ecuación $a = x - x^3 - c v$ con $c = 0.05$. Se emplea el método de Runge-Kutta de cuarto orden (RK4) con un paso $h = 0.005$ durante 60 segundos. Se ejecutan dos simulaciones con condiciones iniciales distintas: $(x_0 = 0, v_0 = -1.2)$ y $(x_0 = 0, v_0 = 1.2)$, para observar la convergencia hacia cada uno de los dos pozos de potencial. Los resultados se presentan en cinco gráficos: tres diagramas temporales ($x$-$t$, $v$-$t$, $a$-$t$) y dos trayectorias tridimensionales $x$-$v$-$t$ correspondientes a cada condición inicial.

  *Código fuente:* `src/exe2.py`
  #code-block(file: "src/exe2.py", lang: "python")

  #align(center)[
    #image("img/lab/exe2.png", width: 95%)
    _Fig. 2: Diagramas temporales y trayectorias x-v-t del oscilador amortiguado $a = x - x^3 - c v$_
  ]

  *Resultados:* En los diagramas temporales se aprecia cómo la amplitud de las oscilaciones decrece progresivamente debido a la disipación de energía introducida por el término de amortiguamiento. La posición converge hacia uno de los puntos de equilibrio estable ($x = +1$ o $x = -1$) dependiendo de la condición inicial. Las trayectorias tridimensionales muestran espirales que se enrollan hacia adentro a medida que avanza el tiempo: la espiral derecha corresponde a la condición inicial que conduce al pozo en $x = +1$, y la espiral izquierda al pozo en $x = -1$. El método RK4 proporciona una integración estable y precisa a lo largo de todo el intervalo de simulación.
  \

  = Sección de Poincaré del oscilador de Duffing forzado

  \
  *Implementación:* Se resuelve el oscilador de Duffing forzado, cuya ecuación de movimiento es $a = b x - d x^3 - c v + f cos(omega t)$, con los parámetros $b = 1$, $d = 1$, $c = 0.24$, $f = 0.68$ y $omega = 1.7$. Se emplea el método RK4 y se muestrea el estado del sistema una vez por cada periodo de la fuerza externa ($T = 2 pi \/ omega$), dividiendo cada periodo en $m = 20$ subpasos de integración. La simulación se extiende durante $10000$ segundos para acumular suficientes puntos en la sección de Poincaré. Para evitar que la posición angular se desborde, se aplica una corrección modular al rango $[-pi, pi]$.

  *Código fuente:* `src/exe3.py`
  #code-block(file: "src/exe3.py", lang: "python")

  #align(center)[
    #image("img/lab/exe3.png", width: 75%)
    _Fig. 3: Sección de Poincaré del oscilador de Duffing forzado_
  ]

  *Resultados:* La sección de Poincaré muestra un conjunto de puntos con una estructura geométrica definida, formando curvas que se pliegan y entrecruzan en el plano $x$-$v$. Esta distribución no aleatoria de los puntos es la firma de un atractor extraño, característico del comportamiento caótico del oscilador de Duffing bajo los parámetros seleccionados. Se distinguen dos regiones principales de acumulación de puntos, correspondientes a los dos pozos de potencial del sistema, conectadas por bandas de transición que evidencian los saltos entre ambos pozos.
  \

  = Sección de Poincaré del movimiento armónico simple

  \
  *Implementación:* Se modela el movimiento armónico simple (MAS) con la ecuación $a = -(k\/m) x$, empleando los parámetros $k = 0.1$ y $m = 200$, lo que determina una frecuencia angular $omega = sqrt(k\/m)$. Se aplica el método RK4 con condiciones iniciales $x_0 = 1$ y $v_0 = 0$. El muestreo de Poincaré se realiza una vez por cada periodo natural del oscilador ($T = 2 pi \/ omega$), subdividiendo cada periodo en $n_"sub" = 100$ subpasos de integración. La simulación se ejecuta durante $100$ segundos.

  *Código fuente:* `src/exe4.py`
  #code-block(file: "src/exe4.py", lang: "python")

  #align(center)[
    #image("img/lab/exe4.png", width: 70%)
    _Fig. 4: Sección de Poincaré del movimiento armónico simple_
  ]

  *Resultados:* La sección de Poincaré se reduce a un único punto en el plano $x$-$v$, ubicado en la posición inicial $(x = 1, v approx 0)$. Este resultado es consistente con la teoría: dado que el periodo de muestreo coincide exactamente con el periodo natural del oscilador, el sistema retorna al mismo estado en cada instante de muestreo. La presencia de un solo punto confirma que el movimiento armónico simple es estrictamente periódico, y su sección de Poincaré es un punto fijo en el espacio de fases.
  \

  = Sección de Poincaré del movimiento subamortiguado

  \
  *Implementación:* Se modela un oscilador armónico subamortiguado con la ecuación $a = -(k\/m) x - (c\/m) v$, utilizando $k = 0.1$, $m = 200$ y $c = 0.15$. Se calculan la frecuencia natural $omega_0 = sqrt(k\/m)$, el coeficiente de atenuación $alpha = c\/(2m)$ y la frecuencia amortiguada $omega_1 = sqrt(omega_0^2 - alpha^2)$. El muestreo se realiza una vez por cada periodo amortiguado $T_1 = 2 pi \/ omega_1$, con $n_"sub" = 20$ subpasos de integración por periodo. Se simulan 30 periodos completos a partir de las condiciones iniciales $x_0 = 1$ y $v_0 = 1$.

  *Código fuente:* `src/exe5.py`
  #code-block(file: "src/exe5.py", lang: "python")

  #align(center)[
    #image("img/lab/exe5.png", width: 75%)
    _Fig. 5: Sección de Poincaré del movimiento subamortiguado_
  ]

  *Resultados:* Los puntos de la sección de Poincaré forman una secuencia que converge progresivamente hacia el origen del plano $x$-$v$, trazando una curva que se acerca al punto $(0, 0)$. Cada punto sucesivo se encuentra más cerca del equilibrio que el anterior, lo que refleja la pérdida continua de energía mecánica debida al amortiguamiento. A diferencia del MAS, donde la sección es un punto fijo, aquí la sección muestra una sucesión de puntos que se acumula en el atractor del sistema: el punto de reposo. Este patrón confirma que el movimiento subamortiguado es no periódico en sentido estricto, ya que la amplitud decrece en cada ciclo.
  \

  = Sección de Poincaré del oscilador $a = x - x^3 - c v$ con periodo estimado

  \
  *Implementación:* Se retoma el oscilador $a = x - x^3 - c v$ con $c = 0.1$. Para determinar la frecuencia de muestreo adecuada, primero se resuelve el caso conservativo ($c = 0$) con condiciones iniciales $x_0 = 0.5$ y $v_0 = 0$ mediante RK4, detectando los instantes en que la velocidad cruza por cero para medir el periodo natural $T$ del movimiento acotado dentro de un pozo de potencial. A partir de ese periodo se define $omega = 2 pi \/ T$. Luego se ejecuta la simulación del oscilador amortiguado con el mismo paso de tiempo $h = T \/ n_"sub"$ durante 50 periodos, registrando la posición y la velocidad en cada paso para construir la sección de Poincaré.

  *Código fuente:* `src/exe6.py`
  #code-block(file: "src/exe6.py", lang: "python")

  #align(center)[
    #image("img/lab/exe6.png", width: 75%)
    _Fig. 6: Sección de Poincaré del oscilador $a = x - x^3 - c v$ con frecuencia estimada_
  ]

  *Resultados:* La sección de Poincaré presenta un patrón en espiral que converge hacia el punto de equilibrio estable del pozo derecho ($x approx 1, v approx 0$). Los puntos exteriores de la espiral corresponden a los primeros periodos de la simulación, cuando la amplitud aún es considerable, y los puntos interiores a los periodos finales, cuando la disipación ya ha reducido sustancialmente la energía del sistema. La forma espiral indica que el oscilador pierde energía de manera gradual y que cada retorno al instante de muestreo ocurre con una amplitud ligeramente menor. A diferencia del caso puramente conservativo, donde la sección sería un punto fijo, el amortiguamiento genera esta estructura convergente que evidencia la naturaleza disipativa del sistema.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + La sección de Poincaré es una herramienta eficaz para clasificar el comportamiento dinámico de un oscilador: un punto fijo indica movimiento periódico (MAS), una secuencia convergente indica movimiento disipativo (subamortiguado), y un conjunto de puntos con estructura geométrica compleja indica caos (Duffing forzado).
  + El oscilador conservativo $a = x - x^3$ exhibe órbitas cerradas en el espacio de fases y su sección de Poincaré, muestreada al periodo natural, se reduce a un único punto; al añadir amortiguamiento, la sección se transforma en una espiral convergente hacia el punto de equilibrio estable.
  + El oscilador de Duffing forzado, bajo los parámetros $c = 0.24$, $f = 0.68$ y $omega = 1.7$, produce un atractor extraño en su sección de Poincaré, lo que confirma la presencia de caos determinista en el sistema.

  == RECOMENDACIONES

  + Emplear el método RK4 en lugar del método de Euler para simulaciones de largo plazo, ya que su mayor precisión por paso evita la acumulación de errores que pueden distorsionar la sección de Poincaré.
  + Descartar los primeros periodos de la simulación (transitorio) al construir la sección de Poincaré de sistemas forzados, para asegurar que los puntos registrados correspondan exclusivamente al régimen estacionario del atractor.
  + Al estimar el periodo de muestreo a partir de la detección de cruces por cero, utilizar interpolación lineal entre los pasos de integración adyacentes para obtener una aproximación más precisa del instante de cruce.
]
