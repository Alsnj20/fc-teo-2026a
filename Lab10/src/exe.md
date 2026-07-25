**Laboratorio 10 – Ecuaciones de Lorenz – Grupo A-B-C-D** **Física Computacional. Ing. de Sistemas**
---

### Ecuaciones de Lorenz

| Ecuaciones de Lorenz | |
| :--- | :--- |
| dx/dt = sigma(y - x) | (a) Elija las condiciones iniciales |
| dy/dt = x(r - z) - y | (b) Determine las gráficas dadas en las diapositi- <br> vas que hicimos clases utilizando la instrucción <br> `subplot(2,2,x)` |
| dz/dt = xy - bz | (c) Aplique el método de Euler. $h = 0.01$ |
---

2. Del mismo código del problema anterior grafique :  
   x - y - t, y - z - t, x - z - t, x - y -z  utilizando la instrucción `subplot(2,2,x)`.

3. **Sensibilidad en las condiciones iniciales** Elegir una condición inicial, por ejemplo $z = 2.5$ y hacer la simulación. Luego elegimos otro valor de $z = 2.500000001 y nuevamente hacemos la simulación. Entonces, presentar en un mismo gráfico las dos simulaciones utilizando la instrucción `subplot(3,1,x)`.

4. Resuelva las ecuaciones de Lorenz, utilizando el método de RK4 y en un mismo gráfico los dos métodos utilizados aplicando la instrucción `subplot(3,1,x)`.
