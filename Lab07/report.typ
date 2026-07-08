#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 7 - Ondas Viajeras - Grupo B",
  lab_number: "07",
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

  Esta práctica no partió de un enunciado escrito: el docente mostró en la pizarra la forma de cada onda viajera y el trabajo consistió en reproducir esos perfiles mediante simulación, animando cómo se desplaza el perfil en el tiempo. Los primeros cuatro ejercicios corresponden a las ondas mostradas en la pizarra; el quinto (polarización elíptica) fue un ejercicio adicional que no se pidió en pizarra.

  #set heading(numbering: "1.a.")

  = Onda viajera tipo diente de sierra

  \
  *Implementación:* Se define un perfil que sube desde 0 hasta un valor máximo y luego cae bruscamente, repitiéndose de forma periódica. En cada instante de tiempo se recalcula el perfil desplazado (restando a la posición el producto de la velocidad por el tiempo transcurrido) y se actualiza la curva en pantalla, generando el efecto de una onda que viaja hacia la derecha sin cambiar de forma.

  *Código fuente:* `src/1/11.py`
  #code-block(file: "src/1/11.py", lang: "python")

  #align(center)[
    #image("img/lab/1/11_onda_viajera.png", width: 80%)
    _Fig. 1: Onda viajera tipo diente de sierra (última posición de la animación)_
  ]

  *Resultados:* El perfil forma dientes idénticos que se repiten cada unidad de longitud, subiendo de forma abrupta y bajando en línea recta. Al animarlo en el tiempo, el patrón completo se desplaza hacia la derecha manteniendo exactamente la misma forma, tal como corresponde a una onda viajera sin deformación.
  \

  = Onda viajera trapezoidal periódica

  \
  *Implementación:* El perfil se arma por tramos: una parte plana en el valor máximo, una bajada lineal, una parte plana en el valor mínimo y una subida lineal, repitiéndose periódicamente. En cada paso de tiempo se evalúa el tramo correspondiente según la posición desplazada y se redibuja la curva, logrando que el trapecio se desplace en el tiempo.

  *Código fuente:* `src/1/12.py`
  #code-block(file: "src/1/12.py", lang: "python")

  #align(center)[
    #image("img/lab/1/12_onda_viajera.png", width: 80%)
    _Fig. 2: Onda viajera trapezoidal periódica_
  ]

  *Resultados:* Se obtiene una sucesión de trapecios: tramos planos arriba y abajo unidos por rampas lineales. La forma se repite cada dos unidades de longitud y, al avanzar el tiempo, todo el patrón se traslada hacia la derecha conservando la forma trapezoidal.
  \

  = Onda viajera triangular

  \
  *Implementación:* Se construye un perfil en zigzag: sube en línea recta desde un valor mínimo hasta un máximo y luego baja en línea recta de vuelta al mínimo, repitiéndose periódicamente. Igual que en los casos anteriores, se recalcula el tramo activo según la posición desplazada en el tiempo y se actualiza la curva en cada paso.

  *Código fuente:* `src/2/23.py`
  #code-block(file: "src/2/23.py", lang: "python")

  #align(center)[
    #image("img/lab/2/23_onda_viajera.png", width: 80%)
    _Fig. 3: Onda viajera triangular_
  ]

  *Resultados:* El perfil forma una sucesión de triángulos simétricos, alternando entre un valor máximo y un valor mínimo opuesto. Al transcurrir el tiempo, los picos y valles se desplazan hacia la derecha sin perder su forma triangular, como se espera de una onda viajera periódica.
  \

  = Onda viajera tipo pirámide

  \
  *Implementación:* Se define un perfil por tramos con dos pendientes distintas: una subida suave hasta un cuarto de la altura máxima y luego una subida más pronunciada hasta el máximo, seguido por el descenso simétrico. Como en los ejercicios anteriores, el tramo activo se recalcula en cada instante según la posición desplazada en el tiempo.

  *Código fuente:* `src/2/24.py`
  #code-block(file: "src/2/24.py", lang: "python")

  #align(center)[
    #image("img/lab/2/24_onda_tipo_piramide.png", width: 100%)
    _Fig. 4: Onda viajera tipo pirámide_
  ]

  *Resultados:* El perfil resultante muestra picos asimétricos: una subida en dos tramos (uno más suave y otro más empinado) antes de llegar al máximo, y luego la bajada simétrica. Este quiebre de pendiente es justamente lo que le da la forma de "pirámide" escalonada al patrón, que se repite y viaja hacia la derecha con el tiempo.
  \

  = Polarización elíptica de una onda electromagnética (ejercicio adicional)

  \
  *Implementación:* Este ejercicio estaba en la pizarra; se agregó como caso adicional. Se definen dos componentes del campo eléctrico, una en el eje Y y otra en el eje Z, ambas oscilando con la misma frecuencia pero con un desfase entre ellas y con distinta amplitud. Se grafica en 3D la curva que forman ambas componentes a lo largo del eje de propagación, junto con flechas que representan el vector de campo eléctrico en varios puntos.

  *Código fuente:* `src/5.py`
  #code-block(file: "src/5.py", lang: "python")

  #align(center)[
    #image("img/lab/5_polarizacion_eliptica.png", width: 100%)
    _Fig. 5: Polarización elíptica de una onda electromagnética_
  ]

  *Resultados:* Al tener distinta amplitud y un desfase entre las componentes Y y Z, la curva que describe la punta del vector de campo eléctrico, vista de frente, traza una elipse en vez de una línea recta o un círculo. Las flechas confirman que el vector de campo eléctrico gira mientras la onda avanza, cambiando tanto de dirección como de magnitud, lo cual es característico de una polarización elíptica.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + Una onda viajera conserva su forma mientras se desplaza: en todos los perfiles simulados (diente de sierra, trapezoidal, triangular y pirámide) bastó con recalcular el mismo perfil evaluado en una posición desplazada por la velocidad y el tiempo transcurrido para lograr el efecto de traslación.
  + Trabajar el perfil por tramos (con `piecewise` o condiciones lógicas) permite construir formas de onda arbitrarias, incluso con esquinas o cambios de pendiente, algo que sería difícil de lograr con una sola función continua.
  + Cuando dos componentes de un campo oscilante tienen distinta amplitud y un desfase entre sí, el resultado ya no es una oscilación lineal simple sino una trayectoria elíptica, como se observó en el ejercicio de polarización.

  == RECOMENDACIONES

  + Al animar una onda viajera, revisar que el dominio espacial sea lo bastante ancho para mostrar varios periodos completos, de forma que se aprecie claramente la periodicidad del patrón.
]
