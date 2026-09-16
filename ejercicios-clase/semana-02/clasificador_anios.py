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
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    # TODO: implemente la lectura y validación.
 
 
def main() -> None:
    """Punto de entrada del script."""
    # TODO: use leer_anios(), filtre los años bisiestos con una
    # comprensión de listas, e imprima un resumen que incluya al menos
    # la lista de años bisiestos y cuántos hay.
 
 
if __name__ == "__main__":
    main()