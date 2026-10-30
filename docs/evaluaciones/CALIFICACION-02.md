# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Andres Mauricio Agudelo · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `67e6ae5`

Muy buen trabajo: su análisis es claro y se apoya en sus propios datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar cerca de n = 50 y lo explica con las constantes ocultas, lo cual coincide con su gráfica.
- Compara con el máximo de un arreglo: dividir no mejora porque combinar cuesta una comparación y el resultado sigue siendo Θ(n).
- Recomienda divide y vencerás y declara que la estimación para 1.000.000 de registros es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Aclarar que el cruce no es un punto exacto: en sus datos las dos curvas están casi pegadas entre n = 50 y n = 100.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` y verifica la condición del caso 2 del método maestro.
- Justifica el Θ(n²) de la fuerza bruta sumando n + (n−1) + … + 1.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos y coinciden entre sí; `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y no modifica la lista.
- Las pruebas cubren todos los casos pedidos, incluido el tramo que cruza el punto medio, con 50 listas aleatorias.
- Las mediciones usan semilla fija, la misma lista para ambos algoritmos y cronometran solo la llamada.

**Lo que puede mejorar:**
- Algunos docstrings no siguen del todo el formato pedido (por ejemplo, no indican que la lista tiene al menos un elemento).

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados, leyenda y nueve tamaños.
- Calcula el factor de crecimiento al duplicar n (≈×4 y ≈×2) y lo contrasta con Θ(n²) y Θ(n log n).

**Lo que puede mejorar:**
- Algunas cifras del texto no coinciden con la gráfica publicada. Por ejemplo, en la gráfica la fuerza bruta en n = 16000 está cerca de 5.000 ms y divide y vencerás cerca de 21 ms, mientras que el informe dice 6.802 y 22,98 ms. Parece que la tabla y la imagen vienen de ejecuciones distintas; conviene regenerar ambas juntas.
- La nota sobre cómo midió no cuenta que repitió las mediciones y usó la mediana, aunque el código lo hace.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, con los archivos y la gráfica con los nombres pedidos.
- Incrusta la gráfica con ruta relativa que funciona y enlaza `subarreglo.py`, `pruebas.py` y `medicion.py`.
- Tiene varios commits descriptivos.

**Lo que puede mejorar:**
- El informe no incluye su nombre completo.
- Faltan las instrucciones para activar el entorno virtual.
- Las instrucciones de reproducción están incompletas: `medicion.py` guarda la gráfica según la raíz del repositorio, así que ejecutarlo dentro de `lab2-divide-y-vencer/` crea una carpeta repetida; hay que indicar desde dónde correrlo. Además, el informe dice que las pruebas imprimen "Todas las pruebas pasaron." pero el mensaje real es otro.
- El informe presenta el título de la estructura, pero no ubica las partes en el orden exacto pedido (las instrucciones de reproducción van al final, no al inicio).

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan siempre la misma suma (también contra una comprobación propia con listas aleatorias) y `medicion.py` corre y genera la gráfica.

## Para el próximo laboratorio
- Ponga su nombre completo y las instrucciones de entorno y ejecución al inicio del informe.
- Genere la tabla y la gráfica en la misma ejecución para que los números coincidan.
- Cite en el análisis los valores que se leen en la gráfica publicada.
- Escriba los *docstrings* completos, con `Args` y `Returns`, y deje dos líneas en blanco entre funciones.
- Cuente en el informe cómo midió (repeticiones y mediana).
