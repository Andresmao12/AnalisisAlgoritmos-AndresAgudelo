import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento.

    Args:
        algoritmo: función de ordenamiento que se desea medir.
        datos: lista de datos que será ordenada.

    Returns:
        La mediana de los tiempos de ejecución en segundos.
    """
    
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos)


def ejecutar_experimento() -> dict[str, list[float]]:
    """Mide ambos algoritmos sobre el escenario A.

    Returns:
        Diccionario con los tiempos de ejecución de Insertion Sort
        y Merge Sort para cada tamaño de entrada.
    """
    
    resultados = {
        "Insertion Sort": [],
        "Merge Sort": [],
    }

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos,
        )

        resultados["Insertion Sort"].append(tiempo_insertion)
        resultados["Merge Sort"].append(tiempo_merge)

    return resultados


def graficar_tiempos(resultados: dict[str, list[float]]) -> None:
    """Genera la gráfica comparativa de tiempos.

    Args:
        resultados: diccionario con los tiempos de ejecución de ambos
            algoritmos para cada tamaño de entrada.
    """

    for nombre, tiempos in resultados.items():
        plt.plot(
            TAMANOS,
            tiempos,
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos: Insertion Sort vs Merge Sort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "lab1-fundamentos-complejidad-recurrencias/"
        "graficas/parte4_tiempo.png",
        dpi=300,
    )

    plt.close()


def imprimir_resultados(resultados: dict[str, list[float]]) -> None:
    """Muestra los tiempos obtenidos.

    Args:
        resultados: diccionario con los tiempos de ejecución de ambos
            algoritmos para cada tamaño de entrada.
    """

    for nombre, tiempos in resultados.items():
        print(f"\n{nombre}")

        for n, tiempo in zip(TAMANOS, tiempos):
            print(
                f"n={n:5d} | "
                f"tiempo={tiempo:.6f} s"
            )


if __name__ == "__main__":
    resultados = ejecutar_experimento()

    imprimir_resultados(resultados)
    graficar_tiempos(resultados)