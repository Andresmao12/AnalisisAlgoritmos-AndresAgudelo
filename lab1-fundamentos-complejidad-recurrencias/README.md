# **Laboratorio 1: Fundamentos, complejidad y recurrencias (Tamiza)**


## Introducción

El análisis de algoritmos permite determinar si una solución no solamente funciona correctamente, sino también si es adecuada para las condiciones en las que debe ejecutarse. En sistemas que manejan grandes cantidades de información, elegir un algoritmo adecuado puede tener un impacto importante en el tiempo de ejecución, el uso de recursos y la capacidad del sistema para cumplir sus restricciones.

En este laboratorio se analiza el caso de la plataforma **Tamiza**, utilizada por la secretaría de Salud para gestionar resultados de pruebas de tamizaje cardiovascular. La plataforma fue creada hace ocho años, cuando el programa cubría 4 municipios y unos 20.000 registros, actualmente debe ordenar 1.200.000 según el índice de riesgo de cada paciente antes de que inicie la jornada del centro de contacto. Actualmente se utiliza **insertion sort**, pero el crecimiento de la cantidad de registros ha provocado que el proceso no termine dentro de la ventana de cuatro horas establecida.

A partir de este problema se estudian las diferencias entre corrección y eficiencia, el comportamiento de los algoritmos ante diferentes tipos de entrada, su complejidad temporal y el impacto que puede tener la elección de un algoritmo en un sistema real.



## Objetivos

### Objetivo general

Analizar el comportamiento y la complejidad de diferentes algoritmos de ordenamiento para determinar su viabilidad en el contexto de la plataforma Tamiza.

### Objetivos específicos

* Diferenciar entre la corrección de un algoritmo y su eficiencia respecto a las restricciones de un sistema.
* Analizar las implicaciones ambientales y éticas relacionadas con la ejecución de algoritmos sobre grandes cantidades de datos.
* Estudiar el comportamiento de insertion sort en el mejor caso, peor caso y caso promedio.
* Implementar y medir los algoritmos utilizando Python.
* Analizar experimentalmente el tiempo de ejecución y el número de comparaciones.
* Comparar teórica y experimentalmente insertion sort y merge sort.

---

## Situación problema

La secretaría de Salud opera un programa de tamizaje cardiovascular en **340 laboratorios e IPS del departamento**. Cada laboratorio envía durante el día los resultados de las pruebas que procesó. Al cierre de la jornada, la plataforma Tamiza tiene acumulados **1.200.000 registros** pendientes de gestión: los resultados de los últimos treinta días que todavía no han sido contactados.

Cada registro trae un **índice de riesgo entre 0 y 1000**, calculado por la plataforma a partir de los valores de laboratorio y de la historia clínica del paciente. **Entre las 2:00 a. m. y las 6:00 a. m. corre un proceso automático que debe ordenar los 1.200.000 registros por índice de riesgo, de mayor a menor, y generar la lista de llamadas del día**. A las 6:00 a. m. el centro de contacto abre y empieza a llamar por esa lista, de arriba hacia abajo: los pacientes con mayor riesgo son contactados primero para citarlos a valoración médica. La ventana del proceso es, por lo tanto, de cuatro horas y no es negociable.

### El problema:
La plataforma fue escrita hace ocho años, cuando el programa cubría **4 municipios y unos 20.000 registros**. El ordenamiento se implementó entonces con insertion sort y nunca se volvió a tocar: siempre funcionó. Con la ampliación del programa a todo el departamento, el proceso empezó a desbordar la ventana. En las últimas semanas, la lista de llamadas ha quedado incompleta tres veces: el proceso no alcanzó a terminar antes de las 6:00 a. m. y el centro de contacto trabajó con una lista parcial, no ordenada por riesgo.

### La decisión sobre la mesa
El área de infraestructura propone **duplicar la capacidad del servidor** —contratar una máquina del doble de velocidad de reloj— **y dejar el software como está**. El argumento es que el algoritmo "ya está probado, lleva ocho años funcionando y entrega el resultado correcto". La secretaría le pide a usted un concepto técnico antes de firmar el contrato.

### Cómo llega el lote de registros 
El equipo de la plataforma le informa que la forma en que llegan los datos depende del canal de origen, y que hay tres escenarios posibles:

| **Escenario** | **Canal de origen** | **Cómo llega el lote de registros** |
|---------------|---------------------|-------------------------------------|
| **A — Aleatorio** | Cargue directo desde el portal web de los laboratorios | Los registros quedan en el orden en que cada laboratorio los subió: sin ninguna relación con el índice de riesgo. |
| **B — Casi ordenado** | Reproceso sobre la lista del día anterior | El 98 % del lote es la lista de ayer, que ya quedó ordenada por riesgo; el 2 % restante son los resultados nuevos del día, que se anexan al final sin ordenar. |
| **C — Orden inverso** | Migración desde el sistema legado de historia clínica | El sistema anterior exporta los registros del índice de riesgo **menor al mayor**, es decir, exactamente al revés de lo que Tamiza necesita. |


# **Parte 1: Analizar el algoritmo antes de comprar hardware**

Primero que todo, debemos tener en cuenta lo siguiente, que un algoritmo sea correcto no significa que produce el resultado esperado. En el caso de Tamiza, **insertion sort es correcto** porque logra ordenar los registros según el índice de riesgo, **pero no podemos decir que es eficiente**, el problema surge cuando debe procesar 1.200.000 registros en la ventana de 4h. Por lo tanto, aunque entregue el resultado correcto, no es viable si no logra terminar dentro de la ventana de cuatro horas establecida por la secretaría.

Ahora bien, antes de invertir en un servidor más rápido es necesario revisar el comportamiento del algoritmo. Insertion sort tiene una complejidad de O(n²), por lo que su cantidad de operaciones crece considerablemente a medida que aumenta el número de registros. Esto ayuda a entender por qué una solución que funcionaba con aproximadamente 20.000 registros ahora tiene dificultades para procesar 1.200.000 dentro de la misma ventana de tiempo.

![alt text](grafica-parte1.png)

Duplicar la velocidad del servidor reduciria el tiempo de ejecución, pero no solucionaría el problema principal. Como ya mencionamos, el algoritmo insertion sort tiene una notacion Big O de n^2, al cambiar el hardware **mejorara el comportamiento, pero seguira siendo n^2**. Y como podemos observar en la grafica, al salirnos lo mas minimo del nuevo margen de 1'200,000 registros, volveremos a tener el mismo problema. Por eso, antes de ampliar la infraestructura, resulta más conveniente evaluar una alternativa de ordenamiento que tenga un mejor comportamiento al trabajar con grandes cantidades de datos.

**Un ejemplo** diferente serían las transacciones interbancarias, desconociendo como funcionan realmente, supongamos que todas las transacciones realizadas el dia 1, deben ser procesadas entre las 06:00h y 10:00h del dia 2, esto siguiendo un orden de bancos ya definidos, por lo cual primero debemos ordenar la lista de transacciones y luego realizarlas. Como problema podemos decir que con el surgimiento de los neobancos y las llaves de Bre-B, el numero de transacciones entre bancos se disparo un 200%. En este caso, un algoritmo puede hacer esta operacion, pero si el incremento hace que nos salgamos de la ventana de tiempo, ya no cumple con lo esperado, y puede que comprar un hardware el doble de potente, lo solucione en este instante, pero si en un mes el numero de transacciones ya no estan 200% arriba, sino un 300% ¿Deberiamos volver a cambiar el hardware? ¿Esto es sostenible a largo plazo?
}


# **Parte 2: Responsabilidad ambiental y ética de la implementación**

Al decidir cual algoritmo utilizar en Tamiza o en cualquier proyecto, **como responsables tecnicos**, debemos tener en cuenta otras cosas ademas de si funciona correctamente y cuánto tiempo tarda, también debemos tener presente las consecuencias que puede tener su ejecución constante. El proceso debe ordenar 1.200.000 registros **diariamente**, y sabemos que un algoritmo que tarde más tiempo también representa un mayor consumo de recursos del servidor, este debe permanecer trabajando durante más tiempo y, por lo tanto, **se consume más energía**. Aunque la diferencia de una sola ejecución pueda parecer pequeña, al repetir el proceso todos los días durante meses o años, ese consumo se acumula y aumenta el impacto ambiental asociado a la operación del sistema.

Desde el punto de vista ético, el problema es todavía más importante porque los datos corresponden a personas y el resultado del ordenamiento determina a quién se contacta primero para recibir su respectiva valoracion. Si el algoritmo tarda demasiado y no termina antes de las 06:00h, algunos pacientes van a quedar fuera de la lista o aparecer en una posición incorrecta. Por ejemplo, un paciente con un **índice de riesgo alto** podría no ser contactado a tiempo para recibir una valoración médica. **En este caso, el costo del error lo asumiría principalmente el paciente** ya que recibira atención más tarde de lo que deberia y terminaria pagando con su salud. La Secretaría y el equipo encargado del sistema también asumirían responsabilidad por no garantizar que el proceso cumpla con las condiciones establecidas.

**Otro posible perjuicio sería para los operadores** del centro de contacto. Si reciben una lista incompleta o desordenada, tendrían que trabajar con información que no representa correctamente la prioridad de los pacientes. Esto puede generar reprocesos, pérdida de tiempo y trabajo adicional, **especialmente si deben revisar nuevamente los registros o corregir manualmente el orden de las llamadas**. En este caso, el operador asume directamente el costo en forma de mayor carga de trabajo, mientras que la Secretaría también tendría que asumir las consecuencias operativas de un sistema que no cumple con su función.

![alt text](mapa-parte2.png)

Ademas, existe una tension entre dos temas que ya mencionamos: terminar a tiempo y garantizar el resultado correcto. no solo basta con encontrar el algoritmo mas rapido, ya que estaria viendose afectada la relacion paciente-secretaria, y como consecuencia de lo ya mencionado (pacientes no reciben su valoracion a tiempo terminan pagando con su salud, secretaria incumple con un acuerdo que existe de por medio) podriamos estar hablando de conflictos entre estos dos actores como perdida de confianza, procesos legales, protestas, etc.

Dicho esto, la elección del algoritmo debe considerar tanto el consumo de recursos como sus consecuencias sobre las personas. En Tamiza, una decisión técnica aparentemente relacionada únicamente con el rendimiento puede terminar afectando la atención que recibe un paciente, el trabajo de los operadores y la responsabilidad de la Secretaría frente al funcionamiento del sistema.

# **Parte 3: Peor caso, mejor caso y caso promedio**



Para analizar el comportamiento de un algoritmo debemos considerar las diferentes formas en las que pueden llegar los datos. Para esto, primero se fija un tamaño de entrada n y se considera el conjunto de todas las entradas posibles que tienen ese mismo tamaño. Sobre este conjunto se analiza cuántas operaciones realiza el algoritmo.

- **Mejor caso:** representa la entrada, de tamaño n, que **requiere la menor cantidad de operaciones** entre todas las entradas posibles ese mismo tamaño.

- **Peor caso:** representa la entrada que **requiere la mayor cantidad de operaciones**. 

- **Caso promedio:** representa el promedio de operaciones que realiza el algoritmo considerando las entradas posibles de tamaño n. Para obtenerlo, se calcula el comportamiento medio sobre ese conjunto de entradas.


Para Tamiza, la ventana de cuatro horas es una restricción estricta y no negociable, por lo que para decidir si un algoritmo puede utilizarse en producción, **definitivamente tomaría como referencia el peor caso**. El sistema debe tener un comportamiento que permita cumplir la restricción incluso cuando los datos lleguen en una condición desfavorable.

> Lo ideal es siempre tomar el peor caso, ya que si en este se comporta como esperamos, en cualquier otra situacion, tambien lo hara.

Para el caso de tamiza tomaremos un tamaño de datos de *n = 1'200.000* que es el que actualmente genera el problema y tomaremos los siguientes casos :

- **Escenario A (Aleatorio):** se aproxima al caso promedio, ya que los registros no tienen una relación previa con el orden que necesita el algoritmo.

- **Escenario B (Ordenado):** se aproxima al mejor caso, porque el 98 % de los registros ya se encuentra en el orden requerido y solamente una pequeña parte necesita ser reorganizada.

- **Escenario C (Orden inverso):** representa el peor caso, porque los registros llegan exactamente en el orden contrario al que necesita producir insertion sort. Esto obliga al algoritmo a realizar la mayor cantidad de desplazamientos y comparaciones.

Esta es la predicción inicial que se utilizará como referencia para comparar posteriormente los resultados experimentales.



# **Parte 4: Complejidad de Merge Sort e Insertion Sort**

> **Proximamente...**



## Estructura del proyecto

```text
curso-analisis-algoritmos/
└── lab1-fundamentos-complejidad-recurrencias/
    ├── README.md
    ├── algoritmos.py
    ├── datos.py
    ├── parte3_casos.py
    ├── parte4_complejidad.py
    │
    └── graficas/
        |-- grafica-parte1.png (Adicional)
        |-- mapa-parte2.png (Adicional)
        ├── parte3_comparaciones.png
        ├── parte3_tiempo.png
        └── parte4_tiempo.png
```



## Requisitos

* Python 3.x
* `matplotlib`

Las dependencias utilizadas en el proyecto se encuentran registradas en `requirements.txt`, de acuerdo con la configuración del entorno del curso.



## Ejecucion del codigo

> **Proximamente...**


## Conclusiones

> **Proximamente...**





## Mis datos

**Estudiante:** Andres Mauricio Agudelo Elorza

**Curso:** Análisis de Algoritmos

**Laboratorio:** Laboratorio Evaluativo 01

**Fecha:** Septiembre de 2026