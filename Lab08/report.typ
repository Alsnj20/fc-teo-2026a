#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 8 - Método Montecarlo - Grupo B",
  lab_number: "08",
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

  En todos los ejercicios se usa el mismo procedimiento de Monte Carlo: se generan muchos puntos al azar dentro de un rectángulo o caja que contiene por completo a la figura de interés, se cuenta qué fracción de esos puntos cae dentro de la región buscada, y esa fracción se multiplica por el área o volumen de la caja para estimar el área o volumen de la figura. Repitiendo este proceso varias veces (50 corridas) se obtiene además una desviación que indica qué tan confiable es la estimación.

  #set heading(numbering: "1.a.")

  = Área entre una parábola y una recta

  \
  *Implementación:* Se generan puntos al azar dentro de un rectángulo que envuelve la región formada por la parábola y la recta dadas. Se separan los puntos que caen entre ambas curvas y se calcula el área como la fracción de puntos aceptados multiplicada por el área del rectángulo. Este proceso se repite 50 veces para promediar el resultado y estimar su desviación.

  *Código fuente:* `src/1.py`
  #code-block(file: "src/1.py", lang: "python")

  #align(center)[
    #image("img/lab/1_monte_carlo.png", width: 75%)
    _Fig. 1: Área entre una parábola y una recta por el método de Monte Carlo_
  ]

  *Resultados:* La nube de puntos aceptados llena exactamente la región encerrada entre la parábola y la recta, confirmando visualmente que la condición usada para filtrar los puntos es correcta. El área estimada resultó muy cercana al valor exacto calculado de forma analítica, con una desviación pequeña respecto al promedio de las 50 corridas.
  \

  = Área entre dos parábolas

  \
  *Implementación:* Se generan puntos al azar dentro de un rectángulo que cubre la región entre las dos parábolas dadas. Se aceptan los puntos que quedan entre ambas curvas y, como en el ejercicio anterior, se estima el área repitiendo el proceso 50 veces.

  *Código fuente:* `src/2.py`
  #code-block(file: "src/2.py", lang: "python")

  #align(center)[
    #image("img/lab/2.png", width: 75%)
    _Fig. 2: Área entre las curvas y=x² y y=x³/3_
  ]

  *Resultados:* Los puntos aceptados quedan concentrados en la región angosta entre ambas curvas, que se cierra exactamente en los puntos de intersección (0,0) y (3,9). El área estimada coincide de cerca con el valor exacto, dentro del margen de la desviación calculada.
  \

  = Volumen de un octante de un elipsoide

  \
  *Implementación:* Se generan puntos al azar dentro de una caja rectangular que cubre el octante donde x es positivo, y es negativo y z es positivo. Se acepta un punto si cumple la ecuación del elipsoide, y el volumen se estima igual que en los ejercicios de área, pero usando el volumen de la caja en vez del área del rectángulo.

  *Código fuente:* `src/3.py`
  #code-block(file: "src/3.py", lang: "python")

  #align(center)[
    #image("img/lab/3.png", width: 75%)
    _Fig. 3: Puntos dentro del octante del elipsoide_
  ]

  *Resultados:* La nube de puntos aceptados forma un octante de elipsoide bien definido, denso cerca del origen y que se va adelgazando hacia los bordes curvos de la superficie. El volumen estimado por Monte Carlo resultó muy cercano al volumen exacto calculado a partir de los semiejes del elipsoide.
  \

  = Área entre una exponencial y un logaritmo

  \
  *Implementación:* Antes de aplicar Monte Carlo, se calculan los puntos donde se cruzan la curva exponencial y la curva logarítmica dadas, usando el método de Newton-Raphson, ya que no tienen una intersección que se pueda despejar directamente. Con esos límites se arma la caja de muestreo y se repite el mismo procedimiento de generar puntos, aceptar los que quedan entre ambas curvas y estimar el área.

  *Código fuente:* `src/4.py`
  #code-block(file: "src/4.py", lang: "python")

  #align(center)[
    #image("img/lab/4.png", width: 75%)
    _Fig. 4: Área entre las curvas y=e^(x-3) y y=ln(x)_
  ]

  *Resultados:* Los puntos de intersección encontrados con Newton-Raphson coinciden exactamente con los cruces visibles entre la curva exponencial y la logarítmica. Los puntos aceptados por Monte Carlo llenan de forma pareja la región delgada encerrada entre ambas curvas, confirmando que los límites de integración usados fueron los correctos.
  \

  = Volumen limitado por un plano inclinado y un cilindro parabólico

  \
  *Implementación:* Se generan puntos al azar dentro de una caja que cubre el primer octante. Se acepta un punto si queda del lado correcto del plano inclinado y por debajo de la superficie del cilindro parabólico al mismo tiempo, y se estima el volumen de la misma forma que en el ejercicio del elipsoide.

  *Código fuente:* `src/5.py`
  #code-block(file: "src/5.py", lang: "python")

  #align(center)[
    #image("img/lab/5.png", width: 75%)
    _Fig. 5: Volumen limitado por el plano inclinado y el cilindro parabólico_
  ]

  *Resultados:* Los puntos aceptados se concentran en la cuña que queda por debajo de ambas superficies, formando una figura que se angosta hacia donde el plano y el cilindro se cruzan. El volumen estimado por Monte Carlo resultó consistente con el valor exacto calculado de forma analítica.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + El método de Monte Carlo permite estimar áreas y volúmenes de figuras irregulares sin necesidad de resolver una integral de forma analítica, bastando con saber si un punto cae o no dentro de la región de interés.
  + Repetir el muestreo varias veces y promediar los resultados permite no solo obtener una estimación más estable, sino también calcular una desviación que indica qué tan confiable es esa estimación.
  + Cuando los límites de integración no se pueden despejar de forma algebraica (como en la intersección entre una exponencial y un logaritmo), se puede recurrir a un método numérico como Newton-Raphson para encontrarlos antes de aplicar Monte Carlo.

  == RECOMENDACIONES

  + Elegir una caja o rectángulo de muestreo lo más ajustado posible a la figura de interés, ya que una caja demasiado grande hace que se desperdicien muchos puntos fuera de la región y el resultado se vuelva menos preciso.
  + Graficar siempre los puntos aceptados sobre la figura junto con las curvas o superficies que la limitan, ya que es la forma más directa de verificar que la condición usada para filtrar los puntos es correcta.
]
