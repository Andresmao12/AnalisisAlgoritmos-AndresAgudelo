"""Experimentos de medicion: lista enlazada frente a tabla hash."""
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

BUSQUEDAS = 200
SEMILLA = 42


def generar_guias_inexistentes(existentes: set[int], cantidad: int, semilla: int = 7) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo.

    Args:
        numero: entero a evaluar.

    Returns:
        True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano (por encima o por debajo) a un valor.

    Args:
        objetivo: valor de referencia.

    Returns:
        El primo mas cercano a `objetivo`.
    """
    distancia = 0
    while True:
        for candidato in (objetivo - distancia, objetivo + distancia):
            if es_primo(candidato):
                return candidato
        distancia += 1


def generar_guias(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos de diez digitos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def construir(guias: list[int], m: int) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias.

    Args:
        guias: guias a insertar.
        m: numero de casillas de la tabla.

    Returns:
        Una tupla (lista, tabla).
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for indice, guia in enumerate(guias):
        estado = "en bodega" if indice % 2 == 0 else "en reparto"
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Verifica que lista y tabla coinciden en una muestra de existentes.

    Args:
        lista: lista enlazada.
        tabla: tabla hash.
        guias: guias existentes de las que se toma la muestra.
    """
    muestra = random.Random(SEMILLA).sample(guias, min(100, len(guias)))
    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia) is not None


def tiempo_medio(estructura: ListaEnlazada | TablaHash, consultas: list[int]) -> float:
    """Mide el tiempo medio de busqueda (solo las busquedas).

    Args:
        estructura: lista o tabla donde buscar.
        consultas: guias a buscar.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    inicio = time.perf_counter()
    for guia in consultas:
        estructura.buscar(guia)
    fin = time.perf_counter()
    return (fin - inicio) / len(consultas) * 1e6


def experimento_a() -> None:
    """Compara lista y tabla variando n; guarda lista_vs_tabla.png."""
    
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    t_lista: list[float] = []
    t_tabla: list[float] = []
    
    print("Experimento A (busquedas inexistentes, tiempo en us)")
    
    for n in valores_n:
        guias = generar_guias(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        t_lista.append(tiempo_medio(lista, consultas))
        t_tabla.append(tiempo_medio(tabla, consultas))
        print(f"n={n:>6} m={m:>6} alfa={n / m:.2f} " f"lista={t_lista[-1]:.3f} tabla={t_tabla[-1]:.3f}")

    plt.figure(figsize=(7, 4.5))
    plt.plot(valores_n, t_lista, "o-", label="Lista enlazada")
    plt.plot(valores_n, t_tabla, "s-", label="Tabla hash (alfa ~ 2)")
    plt.xlabel("Numero de guias n (unidades)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.title("Busqueda de guias inexistentes: lista vs tabla hash")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga; guarda tiempo_vs_alfa.png."""

    n = 20000
    guias = generar_guias(n)
    consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    alfas_objetivo = [0.25, 0.5, 1, 2, 4, 10]
    alfas: list[float] = []
    tiempos: list[float] = []
    print("Experimento B (n = 20000, tiempo en us)")
    
    for objetivo in alfas_objetivo:
        m = primo_cercano(round(n / objetivo))
        _, tabla = construir(guias, m)
        alfas.append(tabla.factor_carga())
        tiempos.append(tiempo_medio(tabla, consultas))
        print(f"m={m:>6} alfa={alfas[-1]:.2f} tabla={tiempos[-1]:.3f}")
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(alfas, tiempos, "o-", label="Tabla hash, n = 20000")
    plt.xlabel("Factor de carga alfa = n / m (adimensional)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.title("Tiempo de busqueda frente al factor de carga")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    experimento_a()
    experimento_b()
