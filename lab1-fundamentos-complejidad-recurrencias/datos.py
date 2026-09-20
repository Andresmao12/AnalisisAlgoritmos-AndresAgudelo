"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 10) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    # TODO: implemente el escenario A.

    generador_aleatorio = random.Random(semilla)
    datos = list(range(1, n + 1))
    generador_aleatorio.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 10) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    # TODO: implemente el escenario B.

    generador_aleatorio = random.Random(semilla)

    cantidad_desordenada = max(1, round(n * 0.02))
    cantidad_ordenada = n - cantidad_desordenada

    datos_ordenados = list(range(n, 0, -1))

    parte_ordenada = datos_ordenados[:cantidad_ordenada]
    parte_desordenada = datos_ordenados[cantidad_ordenada:]

    generador_aleatorio.shuffle(parte_desordenada)

    return parte_ordenada + parte_desordenada



def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # TODO: implemente el escenario C.

    return list(range(1, n + 1))