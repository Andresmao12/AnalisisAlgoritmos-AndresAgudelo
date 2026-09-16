def calcular_promedio(lista: list[int]) -> float:
    """
    Calcula el promedio de una lista de enteros

    Args:
        lista: Lista de enteros 
    
    Returns:
        float: El promedio de los elementos en la lista
    """

    suma = 0

    for elemento in lista:
        suma += elemento
    return suma / len(lista)



def main() -> None:
    lista = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista)

    print(promedio)


if __name__ == "__main__":
    main()