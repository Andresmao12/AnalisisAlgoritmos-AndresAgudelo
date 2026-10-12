"""Experimento: tiempo de ejecucion vs. tamano de entrada.

Ejecutar: python medicion.py
Genera graficas/tiempo_vs_n.png e imprime la tabla de mediciones.
"""

import os
import random
import statistics
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt 

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo 

SEMILLA = 42
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000, 16000]
RUTA_GRAFICA = os.path.join("graficas", "tiempo_vs_n.png")


def repeticiones_para(n: int) -> int:
    """Devuelve cuantas veces repetir la medicion segun el tamano de la entrada

    Args:
        n: tamano de la entrada.

    Returns:
        Numero de repeticiones; mas para tamanos pequenos, donde un
        solo cronometraje es muy ruidoso.
    """
    if n <= 100:
        return 2000
    if n <= 1000:
        return 20
    if n <= 4000:
        return 5
    return 3


def medir(funcion, *argumentos) -> tuple[float, float]:
    """Cronometra solo la llamada a `funcion` con time.perf_counter().

    Args:
        funcion: algoritmo a medir.
        *argumentos: argumentos con los que se llama.

    Returns:
        Tupla (mediana de los tiempos en segundos, suma devuelta).
    """

    tiempos = []
    suma = 0.0
    repeticiones = repeticiones_para(len(argumentos[0]))
    
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion(*argumentos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        suma = resultado[2]

    return statistics.median(tiempos), suma


def ejecutar_experimento() -> list[tuple[int, float, float]]:
    """Mide ambos algoritmos en cada tamano con la misma lista.

    Returns:
        Lista de tuplas (n, segundos_fuerza_bruta, segundos_dyv).
    """
    
    generador = random.Random(SEMILLA)
    filas = []

    for n in TAMANOS:
        datos = [generador.randint(-100, 100) for _ in range(n)]
        t_bruta, suma_bruta = medir(subarreglo_fuerza_bruta, datos)
        t_dyv, suma_dyv = medir(subarreglo_maximo, datos, 0, n - 1)
        assert suma_bruta == suma_dyv, f"Sumas distintas para n={n}"
        filas.append((n, t_bruta, t_dyv))
        
    return filas


def graficar(filas: list[tuple[int, float, float]]) -> None:
    """Dibuja ambas curvas en los mismos ejes y guarda el PNG.

    Args:
        filas: resultados de ejecutar_experimento().
    """
    ns = [f[0] for f in filas]
    bruta_ms = [f[1] * 1000 for f in filas]
    dyv_ms = [f[2] * 1000 for f in filas]

    plt.figure(figsize=(8, 5.5))
    plt.plot(ns, bruta_ms, "o-", color="tab:red", label="Fuerza bruta")
    plt.plot(ns, dyv_ms, "s-", color="tab:blue", label="Divide y venceras")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Subarreglo maximo: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de la entrada n (numero de dias, escala log)")
    plt.ylabel("Tiempo de ejecucion (milisegundos, escala log)")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    os.makedirs("graficas", exist_ok=True)
    plt.savefig(RUTA_GRAFICA, dpi=150)
    plt.close()


def main() -> None:
    """Corre el experimento, imprime la tabla y guarda la grafica"""

    filas = ejecutar_experimento()
    print(f"{'n':>7} {'fuerza bruta (ms)':>20} {'divide y venceras (ms)':>24}")

    for n, t_bruta, t_dyv in filas:
        print(f"{n:>7} {t_bruta * 1000:>20.4f} {t_dyv * 1000:>24.4f}")

    graficar(filas)
    print(f"Grafica guardada en {RUTA_GRAFICA}")


if __name__ == "__main__":
    main()
