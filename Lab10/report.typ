#import "./lib.typ": code-block, code-block-config, lab-section, summarize-name, unsa-report

#let members = (
  "Jara Mamani Mariel Alisson",
)
#show: unsa-report.with(
  course_name: "Fisica Computacional",
  lab_title: "Laboratorio 10 - Ecuaciones de Lorenz - Grupo B",
  lab_number: "10",
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

  Las ecuaciones de Lorenz describen cómo cambian en el tiempo tres variables relacionadas con el movimiento de un fluido y su temperatura. Se trabaja siempre con las mismas tres constantes y las mismas tres ecuaciones; lo que cambia entre ejercicios es el método numérico usado para resolverlas, las condiciones iniciales o la forma de graficar los resultados.

  #set heading(numbering: "1.a.")

  = Solución por el método de Euler

  \
  *Implementación:* Se fijan las tres constantes del sistema y las condiciones iniciales de las tres variables. Con el método de Euler y un paso de tiempo pequeño se avanza la solución instante a instante, guardando los valores en listas. Al final se organizan cuatro gráficos en una cuadrícula de 2x2: cada plano formado por dos de las tres variables, y un cuarto gráfico que corresponde al atractor de Lorenz.

  *Código fuente:* `src/exe1.py`
  #code-block(file: "src/exe1.py", lang: "python")

  #align(center)[
    #image("img/lab/1.png", width: 90%)
    _Fig. 1: Proyecciones x-y, x-z, y-z y atractor de Lorenz_
  ]

  *Resultados:* En los tres primeros gráficos se distinguen dos regiones donde la trayectoria da vueltas repetidamente (los dos "lóbulos" característicos del sistema), saltando de uno a otro de forma aparentemente irregular. El cuarto gráfico muestra la clásica forma de mariposa del atractor de Lorenz, donde la trayectoria nunca se cierra sobre sí misma ni se sale de una región acotada.
  \

  = Proyecciones en el tiempo y trayectoria completa

  \
  *Implementación:* Se repite la misma simulación con el método de Euler, pero ahora se arman cuatro gráficos en 3D en una cuadrícula de 2x2: tres de ellos combinan dos variables con el tiempo, y el cuarto muestra la trayectoria completa en el espacio de las tres variables.

  *Código fuente:* `src/exe2.py`
  #code-block(file: "src/exe2.py", lang: "python")

  #align(center)[
    #image("img/lab/2.png", width: 90%)
    _Fig. 2: Proyecciones x-y-t, y-z-t, x-z-t y trayectoria x-y-z_
  ]

  *Resultados:* Los tres gráficos que incluyen el tiempo muestran cómo la trayectoria va enrollándose de forma creciente a medida que avanza el tiempo, sin repetirse nunca exactamente. El cuarto gráfico, sin el eje de tiempo, deja ver con más claridad la forma de mariposa completa del atractor, igual que en el ejercicio anterior pero desde otro ángulo.
  \

  = Sensibilidad a las condiciones iniciales

  \
  *Implementación:* Se corren dos simulaciones idénticas con el método de Euler, cambiando únicamente el valor inicial de una de las variables en una cantidad extremadamente pequeña. Ambas trayectorias se grafican juntas en tres gráficos apilados (uno por cada variable contra el tiempo) para poder comparar cómo evolucionan una respecto a la otra.

  *Código fuente:* `src/exe3.py`
  #code-block(file: "src/exe3.py", lang: "python")

  #align(center)[
    #image("img/lab/3.png", width: 80%)
    _Fig. 3: Comparación de dos simulaciones con una condición inicial casi idéntica_
  ]

  *Resultados:* Durante los primeros segundos ambas curvas son prácticamente indistinguibles, ya que la diferencia inicial es diminuta. Sin embargo, pasado cierto tiempo las dos curvas se separan por completo y terminan siguiendo caminos totalmente distintos, aunque ambas se mantienen dentro del mismo rango de valores. Esto evidencia el comportamiento caótico del sistema: un cambio mínimo en las condiciones iniciales termina generando trayectorias completamente diferentes.
  \

  = Comparación entre el método de Euler y el método RK4

  \
  *Implementación:* Se resuelve el mismo sistema de ecuaciones dos veces con las mismas condiciones iniciales: una vez con el método de Euler y otra con el método de Runge-Kutta de cuarto orden (RK4), que evalúa la pendiente en varios puntos intermedios antes de avanzar cada paso. Los resultados de ambos métodos se grafican juntos en varios gráficos apilados para compararlos directamente.

  *Código fuente:* `src/exe4.py`
  #code-block(file: "src/exe4.py", lang: "python")

  #align(center)[
    #image("img/lab/4.png", width: 75%)
    _Fig. 4: Comparación entre el método de Euler y el método RK4_
  ]

  *Resultados:* Al principio ambos métodos coinciden, pero al ser un sistema caótico, la mínima diferencia numérica hace que las trayectorias diverjan rápidamente y salten entre los lóbulos en momentos distintos.

  Visualmente, Euler se desvía de forma más brusca y se queda atascado dando vueltas pequeñas en un mismo lóbulo debido a que calcula cada paso usando solo la pendiente al inicio del intervalo, por lo que el error que se comete en cada paso se parece más a un empujón puntual, casi independiente del error de los pasos anteriores; en cambio, RK4 evalúa la pendiente en varios puntos dentro del mismo paso, partiendo siempre del estado que ya arrastra el error acumulado hasta ese momento; es decir, no agrega un error nuevo e independiente en cada paso, sino que propaga y construye el error del paso actual sobre el error que ya traía de los pasos anteriores, ofreciendo una mayor precisión.
  \
]

#lab-section(title: "CONCLUSIONES Y RECOMENDACIONES")[
  #show heading: set text(weight: "bold")
  #set par(justify: true)

  = CONCLUSIONES

  + El sistema de Lorenz es caótico: aunque las ecuaciones son deterministas, cambios extremadamente pequeños en las condiciones iniciales (o incluso el simple hecho de usar un método numérico distinto) provocan que las trayectorias se separen por completo después de cierto tiempo.
  + A pesar de este comportamiento impredecible punto a punto, la trayectoria siempre queda confinada dentro de la misma región del espacio, formando el característico atractor con forma de mariposa y sus dos lóbulos.
  + Visualizar la misma solución desde distintas combinaciones de variables (planos x-y, x-z, y-z, o incluyendo el tiempo) ayuda a entender mejor la forma del atractor, ya que cada proyección resalta aspectos distintos de la misma trayectoria tridimensional.

  == RECOMENDACIONES

  + Usar un paso de tiempo pequeño en el método de Euler, ya que al tratarse de un sistema caótico los errores de integración se amplifican con rapidez y pueden alejar la solución del comportamiento real del sistema.
  + Al comparar dos simulaciones (por sensibilidad a condiciones iniciales o por método numérico), mantener los mismos ejes y escalas en los gráficos para que la divergencia entre curvas sea fácil de identificar visualmente.
]
