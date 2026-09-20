"""Experimento de mejor, peor y caso promedio para insertion sort."""

import statistics
import time

import matplotlib.pyplot as plt
from pathlib import Path

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir_tiempo(datos: list[int]) -> float:
    """Mide el tiempo que tarda insertion sort en ordenar los datos.

    Args:
        datos: lista de índices de riesgo que será ordenada.

    Returns:
        La mediana de los tiempos de ejecución en segundos.
    """

    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        insertion_sort(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos)


def ejecutar_experimento() -> dict[str, dict[str, list]]:
    """Ejecuta las mediciones para los tres escenarios.

    Returns:
        Diccionario con las comparaciones y tiempos de ejecución
        obtenidos para cada escenario y tamaño de entrada.
    """

    resultados = {
        "A - Aleatorio": {
            "comparaciones": [],
            "tiempos": [],
        },
        "B - Casi ordenado": {
            "comparaciones": [],
            "tiempos": [],
        },
        "C - Inverso": {
            "comparaciones": [],
            "tiempos": [],
        },
    }

    for n in TAMANOS:
        escenarios = {
            "A - Aleatorio": generar_aleatorio(n),
            "B - Casi ordenado": generar_casi_ordenado(n),
            "C - Inverso": generar_inverso(n),
        }

        for nombre, datos in escenarios.items():
            _, comparaciones = insertion_sort(datos)

            tiempo = medir_tiempo(datos)

            resultados[nombre]["comparaciones"].append(comparaciones)
            resultados[nombre]["tiempos"].append(tiempo)

    return resultados


def graficar_comparaciones(
    resultados: dict[str, dict[str, list]],
) -> None:
    """Genera la gráfica de comparaciones.

    Args:
        resultados: diccionario con las comparaciones de cada
            escenario para cada tamaño de entrada.
    """

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Comparaciones entre elementos")
    plt.title("Insertion sort: comparaciones por escenario")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "lab1-fundamentos-complejidad-recurrencias/graficas/parte3_comparaciones.png",
        dpi=300,
    )
    plt.close()


def graficar_tiempos(
    resultados: dict[str, dict[str, list]],
) -> None:
    """Genera la gráfica de tiempo de ejecución.

    Args:
        resultados: diccionario con los tiempos de ejecución de cada
            escenario para cada tamaño de entrada.
    """

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempos"],
            marker="o",
            label=nombre,
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Insertion sort: tiempo por escenario")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "lab1-fundamentos-complejidad-recurrencias/graficas/parte3_tiempo.png",
        dpi=300,
    )
    plt.close()


def imprimir_resultados(
    resultados: dict[str, dict[str, list]],
) -> None:
    """Muestra las mediciones obtenidas en consola.

    Args:
        resultados: diccionario con las comparaciones y tiempos de
            ejecución de cada escenario.
    """

    for nombre, datos in resultados.items():
        print(f"\n{nombre}")

        for i, n in enumerate(TAMANOS):
            comparaciones = datos["comparaciones"][i]
            tiempo = datos["tiempos"][i]

            print(
                f"n={n:5d} | "
                f"comparaciones={comparaciones:10d} | "
                f"tiempo={tiempo:.6f} s"
            )


if __name__ == "__main__":

    Path("lab1-fundamentos-complejidad-recurrencias/graficas").mkdir(exist_ok=True)

    resultados = ejecutar_experimento()

    imprimir_resultados(resultados)
    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)