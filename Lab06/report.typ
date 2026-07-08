#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 6 - Campo Magnético - Grupo B",
  lab_number: "06",
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

  #set heading(numbering: "1.a.")

  = Fuerza magnética sobre una carga en movimiento (caso simple)

  \
  *Implementación:* Para una carga negativa que se mueve solo en el eje X, dentro de un campo magnético dirigido en el eje Z, se calcula la fuerza magnética resultante y se dibujan en un mismo gráfico 3D los tres vectores involucrados: velocidad, campo magnético y fuerza, cada uno con su propio color, para poder verificar visualmente la regla de la mano derecha.

  *Código fuente:* `src/1.py`
  #code-block(file: "src/1.py", lang: "python")

  #align(center)[
    #image("img/lab/1.png", width: 80%)
    _Fig. 1: Vectores velocidad, campo magnético y fuerza (caso 1)_
  ]

  *Resultados:* La velocidad apunta en el eje X y el campo magnético en el eje Z negativo; la fuerza resultante aparece perpendicular a ambas, sobre el eje Y negativo. Al ser la carga negativa, la fuerza apunta en sentido contrario al que indicaría la regla de la mano derecha aplicada directamente al producto de velocidad y campo.
  \

  = Fuerza magnética sobre una carga en movimiento (caso general)

  \
  *Implementación:* Se repite el mismo procedimiento del ejercicio anterior, pero ahora con una velocidad y un campo magnético que tienen componentes en los tres ejes. Se calcula la fuerza magnética resultante y se grafican nuevamente los tres vectores en 3D para comparar sus direcciones relativas.

  *Código fuente:* `src/2.py`
  #code-block(file: "src/2.py", lang: "python")

  #align(center)[
    #image("img/lab/2.png", width: 80%)
    _Fig. 2: Vectores velocidad, campo magnético y fuerza (caso general)_
  ]

  *Resultados:* A diferencia del caso anterior, aquí ninguno de los tres vectores queda alineado con un solo eje. Aun así, la fuerza magnética se mantiene perpendicular tanto a la velocidad como al campo magnético, tal como exige la definición de la fuerza magnética, lo cual se aprecia claramente en la vista tridimensional.
  \

  = Campo magnético de corrientes en los vértices de un hexágono

  \
  *Implementación:* Se ubican seis corrientes en los vértices de un hexágono regular, alternando el sentido de la corriente entre vértices consecutivos. Para cada punto de una malla 2D se suma, por superposición, el campo magnético que genera cada corriente. La magnitud se recorta dentro de un rango razonable para que las flechas del gráfico se vean parejas y no se disparen cerca de las corrientes.

  *Código fuente:* `src/3.py`
  #code-block(file: "src/3.py", lang: "python")

  #align(center)[
    #image("img/lab/3.png", width: 80%)
    _Fig. 3: Campo magnético de seis corrientes alternadas en un hexágono_
  ]

  *Resultados:* Alrededor de cada corriente se forma un remolino de flechas, con sentido de giro opuesto entre corrientes vecinas debido a la alternancia de signos. En el centro del hexágono los aportes de las seis corrientes casi se cancelan, quedando un campo mucho más débil que el que se observa junto a cada vértice.
  \

  = Cilindro hueco infinito a partir de corrientes infinitas

  \
  *Implementación:* Se distribuyen 20 corrientes iguales, uniformemente espaciadas, sobre un círculo, simulando la superficie de un cilindro hueco infinito hecho de alambres delgados. Se calcula el campo magnético total por superposición de las 20 corrientes en una malla 2D, tanto dentro como fuera del círculo.

  *Código fuente:* `src/4.py`
  #code-block(file: "src/4.py", lang: "python")

  #align(center)[
    #image("img/lab/4.png", width: 60%)
    _Fig. 4: Campo magnético de un cilindro hueco formado por corrientes_
  ]

  #align(center)[
    #image("img/lab/4_zoom.png", width: 80%)
    _Fig. 5: Zoom del campo magnético de un cilindro hueco formado por corrientes_
  ]



  *Resultados:* Dentro del círculo el campo magnético es prácticamente nulo, ya que las contribuciones de las corrientes de la superficie se cancelan entre sí. Fuera del círculo el campo forma un patrón circular alrededor de todo el cilindro, tal como se espera de una distribución de corriente con simetría cilíndrica.
  \

  = Campo magnético de una espira cuadrada y de un solenoide cuadrado

  \
  *Implementación:* Primero se calcula el campo magnético que produce una sola espira cuadrada a lo largo de su eje, en función de la posición X. Luego se simula un solenoide formado por varias espiras cuadradas iguales colocadas una tras otra, sumando el campo de cada espira para distintas cantidades de espiras (1, 5, 10, 15, 20 y 50), incluyendo el caso pedido de 20 espiras.

  *Código fuente:* `src/5.py`
  #code-block(file: "src/5.py", lang: "python")

  #align(center)[
    #image("img/lab/5.png", width: 80%)
    _Fig. 6: Campo magnético en función de X para solenoides con distinto número de espiras_
  ]

  *Resultados:* Cuantas más espiras tiene el solenoide, mayor es el campo magnético en el centro y más ancha es la región donde el campo se mantiene prácticamente constante (efecto meseta). Con pocas espiras el campo forma un pico angosto, mientras que con 50 espiras se aprecia una meseta amplia y plana, comportamiento que se acerca al de un solenoide ideal.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + La fuerza magnética sobre una carga en movimiento siempre resulta perpendicular tanto a la velocidad como al campo magnético, y su sentido depende del signo de la carga, lo cual se comprobó visualmente en los dos primeros ejercicios mediante la regla de la mano derecha.
  + El principio de superposición también es válido para el campo magnético: al combinar varias corrientes (hexágono, cilindro hueco, solenoide) se pueden lograr desde cancelaciones casi perfectas hasta campos uniformes, dependiendo de cómo se orienten y distribuyan las corrientes.
  + Al aumentar el número de espiras de un solenoide, el campo magnético en su interior se vuelve más intenso y más uniforme, acercándose al comportamiento ideal de un solenoide infinito con una meseta de campo constante.

  == RECOMENDACIONES

  + Recortar o normalizar la magnitud del campo antes de graficarlo con `quiver` cuando hay corrientes puntuales, ya que el campo diverge muy cerca de ellas y puede saturar visualmente el gráfico.
  + Comparar siempre varios casos (distinto número de espiras, corrientes o cargas) en un mismo gráfico cuando sea posible, ya que facilita ver tendencias como el efecto meseta del solenoide.
]
