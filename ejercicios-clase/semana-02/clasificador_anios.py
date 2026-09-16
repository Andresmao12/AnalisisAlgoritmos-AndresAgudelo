"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    # TODO: implemente la lógica usando if / elif / else.

    if anio % 100 == 0 and anio % 400 != 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False



def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    # TODO: implemente la lectura y validación.

    while True:
        try:
                entrada = input("Ingrese una lista de años separados por comas: ")

                anios = [int(anio.strip()) for anio in entrada.split(",")]
                return anios
        except ValueError:
            print("Entrada inválida. Por favor, ingrese solo números enteros separados por comas")


def main() -> None:
    """Punto de entrada del script."""
    # TODO: use leer_anios(), filtre los años bisiestos con una
    # comprensión de listas, e imprima un resumen que incluya al menos
    # la lista de años bisiestos y cuántos hay.

    anios = leer_anios()
    anios_bisiestos = [anio for anio in anios if es_bisiesto(anio)]
    anios_no_bisiestos = [anio for anio in anios if not es_bisiesto(anio)]

    print(f"Años bisiestos: {anios_bisiestos}")
    print(f"Cantidad de años bisiestos: {len(anios_bisiestos)}")
    print(f"Años no bisiestos: {anios_no_bisiestos}")
    print(f"Cantidad de años no bisiestos: {len(anios_no_bisiestos)}")



if __name__ == "__main__":
    main()