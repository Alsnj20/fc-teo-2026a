#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 5 - Campo y Potencial Eléctrico - Grupo B",
  lab_number: "05",
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

  = Campo eléctrico de cuatro cargas en un rombo

  Las cuatro cargas se ubican en los vértices de un rombo equilátero de 1 cm de lado, colocando cada vértice sobre un eje a la misma distancia del origen (así la distancia entre vértices adyacentes es exactamente 1 cm). Para cada punto de una malla 2D se suma, por superposición, el campo eléctrico que produce cada una de las 4 cargas. Como la magnitud del campo crece mucho cerca de las cargas, el vector resultante se normaliza antes de graficarlo con `quiver`, mostrando solo su dirección.

  == Cargas positivas
  \
  *Implementación:* Las cuatro cargas se fijan en `q1=q2=q3=q4=+1.0 C`. Se recorre cada carga acumulando `Ex_total` y `Ey_total` sobre la malla, se normaliza el vector resultante y se grafica con `quiver`, marcando las cargas con puntos rojos y el rombo con líneas punteadas.

  *Código fuente:* `src/1/a.py`
  #code-block(file: "src/1/a.py", lang: "python")

  #align(center)[
    #image("img/lab/1/1a_cargas_positivas.png", width: 80%)
    _Fig. 1: Campo eléctrico de 4 cargas positivas en un rombo_
  ]

  *Resultados:* Las flechas divergen radialmente desde cada carga, ya que las cuatro son del mismo signo y se repelen entre sí. En el centro del rombo el campo no se anula: por simetría los aportes de las cargas opuestas se cancelan parcialmente, pero el patrón resultante conserva una leve estructura direccional debido a la disposición no colineal de las cargas.
  \

  == Cargas negativas
  \
  *Cargas:* se cambia `q1=q2=q3=q4=-1.0 C` (todas negativas; el resto del código es idéntico al de 1(a)).

  #align(center)[
    #image("img/lab/1/1b_cargas_negativas.png", width: 80%)
    _Fig. 2: Campo eléctrico de 4 cargas negativas en un rombo_
  ]

  *Resultados:* El patrón de flechas es idéntico al de 1(a) pero con sentido invertido: ahora todas apuntan hacia las cargas, ya que el campo converge hacia cada carga negativa. Esto confirma que invertir el signo de todas las cargas solo invierte la dirección del campo eléctrico, sin alterar su geometría.
  \

  == Cargas alternadas
  \
  *Cargas:* `q1=+1.0, q2=-1.0, q3=+1.0, q4=-1.0 C` (signos intercalados en los vértices consecutivos del rombo).

  #align(center)[
    #image("img/lab/1/1c_cargas_alternadas.png", width: 80%)
    _Fig. 3: Campo eléctrico con cargas de signo alternado_
  ]

  *Resultados:* El patrón cambia completamente: se observan líneas de campo saliendo de las cargas positivas y entrando en las negativas, formando remolinos alrededor de cada vértice. En el centro del rombo el campo es más intenso y bien definido que en los casos (a) y (b), pues los aportes de cargas opuestas se suman en lugar de cancelarse.
  \

  = Potencial eléctrico de cuatro cargas en un rombo

  Con las mismas posiciones de las cargas, se calcula el potencial eléctrico que producen las 4 cargas en cada punto de la malla. Los niveles de las curvas de nivel se fijan con los percentiles 1 y 99.7 del potencial para evitar que las singularidades junto a las cargas saturen la escala de colores. Sobre el mismo gráfico se superponen las flechas normalizadas del campo eléctrico, que resultan perpendiculares a las líneas equipotenciales.

  == Cargas positivas
  \
  *Implementación:* Se recorre la lista de cargas acumulando `z += k*qi/r` (potencial) y `Ex_total`, `Ey_total` (campo). Se grafican los contornos de `z` con `contour` y las flechas normalizadas con `quiver` sobre la misma figura.

  *Código fuente:* `src/2/a.py`
  #code-block(file: "src/2/a.py", lang: "python")

  #align(center)[
    #image("img/lab/2/2a_campo_equipotencial.png", width: 80%)
    _Fig. 4: Líneas equipotenciales y campo eléctrico, 4 cargas positivas_
  ]

  *Resultados:* Alrededor de cada carga se forman anillos equipotenciales cerrados y concéntricos, con el potencial decreciendo hacia afuera. Las flechas del campo son siempre perpendiculares a estas curvas y apuntan hacia el exterior, coherente con que las cuatro fuentes son positivas.
  \

  == Cargas negativas
  \
  *Cargas:* `q1=q2=q3=q4=-1.0 C` (mismo código de 2(a), cambiando el signo de las cuatro cargas).

  #align(center)[
    #image("img/lab/2/2b_campo_equipotencial.png", width: 80%)
    _Fig. 5: Líneas equipotenciales y campo eléctrico, 4 cargas negativas_
  ]

  *Resultados:* El potencial es negativo en todo el dominio y crece (se acerca a cero) al alejarse de las cargas. La región central entre las cuatro cargas queda delimitada por un contorno casi cuadrado, donde los potenciales de las cargas vecinas compiten entre sí antes de fundirse en los anillos exteriores comunes.
  \

  == Superficies equipotenciales con cargas intercaladas 3D
  \
  *Implementación:* Se repite el cálculo del potencial para cargas alternadas (`+1,-1,+1,-1`) sobre una malla más fina, recortando los valores extremos para que el relieve sea visible sin que las singularidades dominen la escala vertical. El resultado se grafica como una superficie de alambre (`plot_wireframe`) en 3D en vez de curvas de nivel 2D.

  *Código fuente:* `src/2/c.py`
  #code-block(file: "src/2/c.py", lang: "python")

  #align(center)[
    #image("img/lab/2/2c_relieve_3D.png", width: 70%)
    _Fig. 6: Relieve 3D del potencial con cargas intercaladas_
  ]

  *Resultados:* El relieve muestra dos picos pronunciados (cargas positivas) y dos pozos simétricos (cargas negativas), con una región de silla entre cada par de cargas vecinas de signo opuesto. Esto es justamente la superficie equipotencial esperada para un arreglo de tipo cuadrupolar alternado, muy distinta de los "montes" que se obtendrían si las cuatro cargas fueran del mismo signo.
  \

  = Espira rómbica cargada eléctricamente

  Se distribuye una cantidad fija de cargas puntuales iguales, uniformemente espaciadas, a lo largo de cada uno de los 4 lados de una espira rómbica de 1 cm de lado, interpolando linealmente entre vértices consecutivos. Con la lista resultante de cargas se calculan el potencial (contornos) y el campo eléctrico normalizado (`quiver`) exactamente igual que en los ejercicios anteriores.

  == 8 cargas por lado
  \
  *Implementación:* Se generan 32 cargas positivas (8 por lado) interpolando entre los 4 vértices del rombo. Se acumulan `z`, `Ex_total`, `Ey_total` sobre la malla y se grafican los contornos junto con las flechas normalizadas del campo, además de las posiciones de las cargas individuales.

  *Código fuente:* `src/3/a.py`
  #code-block(file: "src/3/a.py", lang: "python")

  #align(center)[
    #image("img/lab/3/3a_campo_potencial.png", width: 80%)
    _Fig. 7: Espira rómbica con 8 cargas por lado_
  ]

  *Resultados:* Dentro de la espira el campo es prácticamente nulo (las cargas de los lados opuestos se cancelan), mientras que fuera se comporta de forma similar a una única carga puntual grande. Las líneas equipotenciales más internas siguen aproximadamente el contorno romboidal de la espira, y se vuelven circulares a mayor distancia.
  \

  == 16 cargas por lado
  \
  *Cambio:* `num_cargas_por_lado = 16` (64 cargas en total; el resto del código es idéntico al de 3(a)).

  #align(center)[
    #image("img/lab/3/3b_campo_potencial.png", width: 80%)
    _Fig. 8: Espira rómbica con 16 cargas por lado_
  ]

  *Resultados:* La forma general del campo y del potencial es la misma que con 8 cargas por lado, pero al duplicar la densidad de cargas la distribución se vuelve más uniforme: los "escalones" del campo cerca del alambre se suavizan y la región interior de campo casi nulo se define con más precisión, acercándose al caso ideal de una espira con carga continua.
  \

  = Campo y potencial de un alambre recto cargado

  Se modela un alambre recto de 5 cm como 100 cargas puntuales iguales, repartiendo la carga total uniformemente a lo largo del segmento (`q_individual = q_total/num_cargas`). Sobre una malla 2D se calculan el potencial (contornos) y el campo eléctrico normalizado (`quiver`) por superposición de las 100 cargas, igual que en los ejercicios anteriores.

  *Código fuente:* `src/4/a.py`
  #code-block(file: "src/4/a.py", lang: "python")

  #align(center)[
    #image("img/lab/4/4a_campo_potencial.png", width: 80%)
    _Fig. 9: Campo y potencial de un alambre recto de 5 cm_
  ]

  *Resultados:* Las líneas equipotenciales forman óvalos alargados en torno al alambre, más apretadas cerca de los extremos donde se concentra el efecto de "punta". El campo eléctrico es prácticamente perpendicular al alambre en su parte central y se curva hacia los extremos, comportamiento intermedio entre una carga puntual y un alambre infinito.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + El principio de superposición permite construir el campo y el potencial de cualquier arreglo de cargas puntuales sumando las contribuciones individuales, y el signo relativo de las cargas (todas iguales o alternadas) determina completamente la geometría de las líneas de campo y de las superficies equipotenciales.
  + Las líneas equipotenciales y las líneas de campo eléctrico son siempre perpendiculares entre sí, lo cual se verificó visualmente en todos los arreglos simulados (rombo, espira rómbica y alambre recto).
  + Al aumentar el número de cargas puntuales que aproximan una distribución continua (espira rómbica y alambre), el campo y el potencial se vuelven más suaves y uniformes, acercándose al comportamiento ideal de una distribución de carga continua.

  == RECOMENDACIONES

  + Normalizar siempre los vectores de campo antes de graficarlos con `quiver`, ya que su magnitud diverge cerca de las cargas puntuales y puede saturar visualmente el gráfico.
  + Usar percentiles (en vez de el mínimo y máximo absolutos) para fijar los niveles de las curvas de contorno, evitando que las singularidades puntuales dominen la escala de colores.
]
