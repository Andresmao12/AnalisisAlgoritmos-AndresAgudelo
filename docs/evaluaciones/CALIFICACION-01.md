# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Andres Mauricio Agudelo Elorza · **Laboratorio:** Plataforma Tamiza (insertion sort vs. merge sort)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `bfc8b45`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **78 / 100** |
| **Nota (0–5)** | **3.90** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que sea viable, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que duplicar el servidor no cambia el crecimiento cuadrático del algoritmo.
- En la Parte 2 identifica dos perjuicios (el paciente y los operadores) y dice quién asume el costo de cada uno. Relaciona el tiempo de ejecución con el consumo de energía repetido cada día.

**Lo que puede mejorar:**
- El segundo ejemplo (transacciones entre bancos) no dice cuántos datos se procesan; solo habla de un aumento del 200 %. Un ejemplo concreto necesita una cantidad aproximada de datos y la restricción que se rompe.
- La dimensión ambiental se queda en lo general: no estima cuánto tiempo ni cuánta energía se gasta en un año.
- La tensión de que el orden decide a quién se llama primero se menciona, pero no se explica la obligación de que el orden sea exactamente correcto, más allá del tiempo.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Define mejor, peor y caso promedio sobre las entradas de un mismo tamaño n, justifica usar el peor caso para decidir y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro, identificando a, b y f(n) y concluyendo `Θ(n log n)`.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- El cálculo de insertion sort "línea a línea" quedó incompleto: no se indica cuántas veces se ejecuta cada línea del ciclo interno ni se suman los costos. Pasa directo a mejor y peor caso.
- La verificación del caso 2 del método maestro es muy corta; falta escribir con claridad la condición que se comprueba.
- La predicción se plantea con n = 1.200.000, pero el experimento llega solo hasta 6400; conviene hablar del mismo tamaño que se mide.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), trabajan sobre una copia, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. Para una lista ya en el orden pedido, insertion sort hace `n - 1` comparaciones, como debe ser.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y usan semilla.
- Hay docstrings y tipos en casi todo.

**Lo que puede mejorar:**
- Hay faltas de estilo: líneas en blanco de más, espacios al final de línea y archivos sin salto de línea final.
- `medir_tiempo` en `parte4_complejidad.py` no tiene tipo para el parámetro `algoritmo`, y ese archivo no tiene descripción al inicio.
- Los scripts solo funcionan si se ejecutan desde la carpeta raíz del repositorio, porque las rutas de las gráficas están escritas así.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos que C es el peor caso, B el mejor y A queda en medio. Contrasta con la predicción.
- En 4.2 describe lo que hace cada curva y lo conecta con `n²` y `n log n`.
- En 4.3 recomienda merge sort, declara las extrapolaciones como estimación (cerca de 12 horas para insertion sort y unos 5 segundos para merge sort) y responde a la propuesta del servidor.

**Lo que puede mejorar:**
- Las cifras de la sección "Conclusiones" (por ejemplo 0,927 s, 58 veces y 9,05 horas) no coinciden con las de la Parte 4 y 4.3 (1,22 s, 72,7 veces y 11,95 horas), ni con las gráficas publicadas. Parecen de otra corrida; el informe debe tener números consistentes.
- El análisis de la Parte 3.2 es muy breve y sin cifras; los datos solo aparecen al final.
- Para el servidor del doble de velocidad usa una reducción "hipotética" del 50 %; falta citar la gráfica y el tamaño del que sale el dato.
- La mejora por hardware se descarta, pero no se explica por qué con merge sort sí cabría con holgura en la ventana frente al margen que queda.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio, los cuatro archivos `.py` y las tres gráficas pedidas están donde deben, y las imágenes se ven desde el informe.
- Hay siete commits con mensajes descriptivos, su nombre y pasos para reproducir.

**Lo que puede mejorar:**
- Las partes prácticas no enlazan su código: faltan los enlaces a `parte3_casos.py` y `parte4_complejidad.py` al inicio de la Parte 3 y la Parte 4, y a `datos.py`; `algoritmos.py` solo aparece como texto o enlace a un fragmento.
- Las instrucciones de ejecución mezclan rutas de Windows y piden estar en dos carpetas distintas, lo que confunde.
- El informe repite el enunciado largo del caso y trae tres gráficas adicionales; el informe debe ser más directo.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en pruebas con listas aleatorias, casi ordenadas e inversas, y los scripts corren y generan las gráficas cuando se ejecutan desde la raíz del repositorio.

## Para el próximo laboratorio
- Enlace en el informe cada archivo `.py` al inicio de la parte que lo usa.
- Después de cada corrida final, copie al informe solo los números de las gráficas publicadas, para que todo coincida.
- Complete el conteo línea a línea mostrando cuántas veces se ejecuta cada línea y sumando.
- Dé un segundo ejemplo con cantidad de datos y restricción, y estime energía o tiempo acumulado.
- Revise el estilo del código (líneas en blanco, espacios sobrantes, tipos en todas las funciones).
