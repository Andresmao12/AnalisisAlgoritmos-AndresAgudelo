"""Pruebas de subarreglo.py con assert. Ejecutar: python pruebas.py"""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def suma_tramo(valores, inicio, fin):
    """Suma valores[inicio..fin] para validar que los indices son coherentes."""
    total = 0
    for k in range(inicio, fin + 1):
        total += valores[k]
    return total


def verificar(serie, esperada):
    """Comprueba suma e indices de ambos algoritmos contra `esperada`."""
    copia = list(serie)
    for resultado in (
        subarreglo_fuerza_bruta(serie),
        subarreglo_maximo(serie, 0, len(serie) - 1),
    ):
        i, j, s = resultado
        assert s == esperada, (serie, resultado, esperada)
        assert 0 <= i <= j < len(serie)
        assert suma_tramo(serie, i, j) == s  # los indices respaldan la suma
    assert serie == copia  # no se modifica la lista recibida


# 1. Serie de ocho dias de la situacion problema (suma 17)
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17
verificar(serie, 17)

# 2. Un solo elemento (positivo y negativo)
verificar([7], 7)
verificar([-4], -4)

# 3. Todos negativos
verificar([-8, -3, -6, -2, -9], -2)

# 4. Todos positivos
verificar([4, 1, 7, 3, 2], 17)
assert subarreglo_maximo([4, 1, 7, 3, 2], 0, 4)[:2] == (0, 4)

# 5. El mejor tramo cruza el punto medio (indices 0..7, medio = 3)
cruce = [-5, 1, 6, 4, 5, 3, -9, -2]
assert (0 + 7) // 2 == 3
verificar(cruce, 19)

i, j, s = suma_cruzada(cruce, 0, 3, 7)
assert (i, j, s) == (1, 5, 19)

resultado = subarreglo_maximo(cruce, 0, 7)
assert resultado[0] <= 3 < resultado[1]  # el tramo contiene ambos lados

# 6. Listas aleatorias: ambas funciones deben dar la misma suma
generador = random.Random(2024)
for _ in range(50):
    n = generador.randint(1, 60)
    datos = [generador.randint(-100, 100) for _ in range(n)]
    suma_bruta = subarreglo_fuerza_bruta(datos)[2]
    suma_dyv = subarreglo_maximo(datos, 0, n - 1)[2]
    assert suma_bruta == suma_dyv, (datos, suma_bruta, suma_dyv)

# 7. Listas aleatorias con valores flotantes
for _ in range(20):
    n = generador.randint(1, 40)
    datos = [generador.randint(-1000, 1000) / 10 for _ in range(n)]
    sb = subarreglo_fuerza_bruta(datos)[2]
    sd = subarreglo_maximo(datos, 0, n - 1)[2]
    assert abs(sb - sd) < 1e-9

print("Pruebas finalizadas con exito")
