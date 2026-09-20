"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente el algoritmo contando cada comparacion
    # entre dos elementos de la lista.


    datos_ordenados = datos.copy()
    comparaciones = 0

    for i in range(1, len(datos_ordenados)):

        clave = datos_ordenados[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if datos_ordenados[j] >= clave:
                break

            datos_ordenados[j + 1] = datos_ordenados[j]
            j -= 1

        datos_ordenados[j + 1] = clave

    return (datos_ordenados, comparaciones)



def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """

    # TODO: implemente dividir, conquistar y combinar, contando
    # cada comparacion realizada dentro de la mezcla.
    
    datos_ordenados = datos.copy()

    if len(datos_ordenados) <= 1:
        return datos_ordenados, 0

    mitad = len(datos_ordenados) // 2

    izquierda, comparaciones_izquierda = merge_sort(
        datos_ordenados[:mitad]
    )

    derecha, comparaciones_derecha = merge_sort(
        datos_ordenados[mitad:]
    )

    resultado = []
    i = 0
    j = 0
    comparaciones_merge = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones_merge += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    comparaciones = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_merge
    )

    return resultado, comparaciones