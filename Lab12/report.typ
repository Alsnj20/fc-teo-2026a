#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 12 - Autómata Celular Unidimensional - Regla 62 - Grupo B",
  lab_number: "12",
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

  Un autómata celular unidimensional es un modelo discreto compuesto por una línea de celdas, cada una con un estado binario (0 o 1). En cada generación, el nuevo estado de cada celda depende exclusivamente del estado de su vecino izquierdo, sí misma y su vecino derecho.

  #set heading(numbering: "1.a.")

  = Expresión booleana y tabla de verdad

  \
  *Enunciado:* Determinar la expresión booleana que representa la Regla 62 y construir su tabla de verdad completa, verificando que el número de regla corresponde al valor decimal obtenido del vector de salidas ordenado.

  *Desarrollo:* La regla de evolución asignada corresponde a la expresión booleana:

  $F = macron(a)_(−1) a_1 + a_(−1) macron(a)_0 + macron(a)_(−1) a_0$

  donde $a_(−1)$ representa al vecino izquierdo, $a_0$ a la celda central y $a_1$ al vecino derecho. Evaluando las 8 combinaciones posibles de la vecindad de tres celdas se obtiene la siguiente tabla de verdad:

  #align(center)[
    #table(
      columns: 11,
      fill: (x, y) => if y == 0 { rgb("#DEDEDE") } else { none },
      stroke: 0.5pt + rgb("cccccc"),
      align: center,

      // Encabezados
      table.cell(inset: 0.4em)[#set text(weight: "bold"); N°],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $a_(-1)$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $a_0$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $a_1$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $macron(a)_(-1)$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $macron(a)_0$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $macron(a)_1$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $macron(a)_(-1) a_1$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $a_(-1) macron(a)_0$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $macron(a)_(-1) a_0$],
      table.cell(inset: 0.4em)[#set text(weight: "bold"); $=$],

      [*0*], [0], [0], [0], [1], [1], [1], [0], [0], [0], [*0*],
      [*1*], [0], [0], [1], [1], [1], [0], [1], [0], [0], [*1*],
      [*2*], [0], [1], [0], [1], [0], [1], [0], [0], [1], [*1*],
      [*3*], [0], [1], [1], [1], [0], [0], [1], [0], [1], [*1*],
      [*4*], [1], [0], [0], [0], [1], [1], [0], [1], [0], [*1*],
      [*5*], [1], [0], [1], [0], [1], [0], [0], [1], [0], [*1*],
      [*6*], [1], [1], [0], [0], [0], [1], [0], [0], [0], [*0*],
      [*7*], [1], [1], [1], [0], [0], [0], [0], [0], [0], [*0*],
    )
  ]

  Para verificar el número de regla, se ordena el vector de salidas desde el estado 7 al estado 0:

  $text("Vector de Salidas") = [0, 0, 1, 1, 1, 1, 1, 0]_2$

  Convirtiendo el número binario $00111110_2$ a decimal:

  $0 · 2^7 + 0 · 2^6 + 1 · 2^5 + 1 · 2^4 + 1 · 2^3 + 1 · 2^2 + 1 · 2^1 + 0 · 2^0 = 32 + 16 + 8 + 4 + 2 = bold(62)$

  *Resultados:* Se confirma que el comportamiento lógico asignado equivale exactamente a la Regla 62 de Wolfram.
  \

  = Optimización de decisiones

  \
  *Enunciado:* Reducir la implementación del autómata a un máximo de 6 decisiones condicionales, sin evaluar las 8 combinaciones de forma individual.

  *Desarrollo:* En lugar de comparar los tres vecinos celda por celda (lo que requeriría evaluar las 8 combinaciones posibles de $2^3$), se suma directamente el estado de la vecindad: $s = a_(−1) + a_0 + a_1$. El resultado numérico indica cuántas celdas están activas, reduciendo el problema a 4 escenarios posibles ($s = 0, 1, 2$ o $3$).

  A partir de la tabla de verdad, se identifican los patrones de salida para cada valor de $s$:

  - *Caso $s = 1$ (población baja):* Representa las vecindades [1-0-0], [0-1-0] y [0-0-1]. En la Regla 62, la presencia de una única celda activa siempre es suficiente para generar vida en la siguiente generación. Sin importar la posición de esa celda, el resultado asignado es 1.

  - *Caso $s = 2$ (población media):* Representa las vecindades [1-0-1], [0-1-1] y [1-1-0]. La regla se vuelve selectiva: las combinaciones [1-0-1] y [0-1-1] producen 1, mientras que [1-1-0] produce 0.

  - *Caso $s = 0$ y $s = 3$ (por defecto):* Cuando $s = 0$ no hay celdas vivas alrededor, por lo que la celda permanece inactiva. Cuando $s = 3$ hay sobrepoblación total, lo que también resulta en estado 0. Ambos casos se capturan en la cláusula `else`.

  Con este análisis, la lógica se reduce a tres condiciones.
  \

  = Representación gráfica de las 8 sub-reglas

  \
  *Enunciado:* Presentar en forma gráfica la transición de vecindades que define la Regla 62, mostrando cada una de las 8 sub-reglas con su resultado correspondiente.

  *Desarrollo:* Se utiliza una representación esquemática donde $[■]$ indica estado activo (1) y $[□]$ indica estado inactivo (0). Cada fila muestra la vecindad de entrada y la celda central resultante:

  \
  #align(center)[
    #block(width: 90%)[
      #set text(size: 9pt)
      #set par(leading: 0.7em)
      ```
      Regla 7:    Regla 6:    Regla 5:    Regla 4:    Regla 3:    Regla 2:    Regla 1:    Regla 0:
      [■ ■ ■]     [■ ■ □]     [■ □ ■]     [■ □ □]     [□ ■ ■]     [□ ■ □]     [□ □ ■]     [□ □ □]
         ↓           ↓           ↓           ↓           ↓           ↓           ↓           ↓
        [ ]         [ ]         [■]         [■]         [■]         [■]         [■]         [ ]
        (0)         (0)         (1)         (1)         (1)         (1)         (1)         (0)
      ```
    ]
  ]

  \

  *Resultados:* Las sub-reglas 1 a 5 producen estado activo (1), mientras que las sub-reglas 0, 6 y 7 producen estado inactivo (0).

  #set par(justify: true)
  = Simulación de tres líneas para 20 células

  \
  *Enunciado:* Simular manualmente la evolución de una línea de 20 células bajo la Regla 62 durante tres generaciones sucesivas.

  *Desarrollo:* Se elige como configuración inicial una única celda activa en la posición 7 (las demás en estado 0). Se aplica la Regla 62 a cada celda considerando sus vecinos, con conectividad circular (la celda 1 tiene como vecino izquierdo a la celda 20, y la celda 20 tiene como vecino derecho a la celda 1). Las tres primeras generaciones resultan:
  \
  ```
  L1:  _ _ _ _ _ _ ■ _ _ _ _ _ _ _ _ _ _ _ _ _
  L2:  _ _ _ _ _ ■ ■ ■ _ _ _ _ _ _ _ _ _ _ _ _
  L3:  _ _ _ _ ■ ■ _ _ ■ _ _ _ _ _ _ _ _ _ _ _
  L4:  _ _ _ ■ ■ _ ■ ■ ■ ■ _ _ _ _ _ _ _ _ _ _
  ```
  \
  *Resultados:* A partir de una célula aislada, la Regla 62 genera un patrón que se expande simétricamente hacia ambos lados. En la segunda línea aparecen tres celdas activas contiguas, y en la tercera el patrón se bifurca, mostrando dos grupos separados por celdas inactivas. Este crecimiento progresivo y la aparición de estructuras espaciales es característico de las reglas de Wolfram clasificadas como "complejas".
  \

  = Código fuente y simulación computacional

  \
  *Implementación:* Se implementa el autómata celular en Python utilizando una matriz de 20×20 para almacenar las 20 generaciones sobre las 20 celdas. Se establece como condición inicial una celda activa en la posición 7. En cada generación se evalúa la Regla 62 mediante la optimización por suma descrita en el item2. La visualización se realiza con `matplotlib`, representando las celdas activas como cuadros negros sobre una cuadrícula.

  *Código fuente:* `src/62.py`
  #code-block(file: "src/62.py", lang: "python")

  #align(center)[
    #image("img/lab/62.png", width: 65%)
    _Fig. 1: Autómata celular completo — Regla 62 con condición inicial en la célula 7_
  ]

  *Resultados:* La imagen muestra la evolución completa del autómata durante 20 generaciones. El patrón resultante exhibe un crecimiento triangular con bifurcaciones simétricas respecto a la posición inicial. Las regiones oscuras (celdas activas) forman una estructura que se ramifica hacia los bordes, mientras que las regiones claras (celdas inactivas) generan triángulos invertidos característicos.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + La Regla 62 genera un patrón de crecimiento simétrico con bifurcaciones que se expanden hacia los bordes del espacio celular.
  + La optimización mediante suma de estados reduce las 8 evaluaciones condicionales individuales a 2 decisiones y 1 caso por defecto, manteniendo la corrección lógica del autómata.
  + La simulación computacional confirma el resultado teórico obtenido en papel, validando tanto la tabla de verdad como la implementación optimizada.

  == RECOMENDACIONES

  + Verificar manualmente las primeras generaciones del autómata antes de ejecutar la simulación completa, para detectar errores en la implementación de la regla o en las condiciones de frontera.
  + Al implementar condiciones de frontera periódicas, asegurar que los índices de los vecinos se ajusten correctamente al rango $[0, N-1]$ mediante la operación módulo, evitando accesos fuera de los límites del arreglo.
]
