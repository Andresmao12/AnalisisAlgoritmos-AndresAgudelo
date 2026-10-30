"""Pruebas con assert para ListaEnlazada y TablaHash."""
import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado")

# 1. Busqueda exitosa e infructuosa en la lista y en la tabla
lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in ((1000000010, "en bodega"), (1000000024, "en reparto"), 
                     (1000000017, "en bodega"), (1000000005, "entregado")):
    
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert lista.buscar(99) is None
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000005) == "entregado"
assert tabla.buscar(99) is None

# 2. Colision forzada con m = 7: 10, 24 y 17 caen en la casilla 3
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(17) == "en bodega"
assert tabla.casillas[3].tamano == 3

# 3. Factor de carga
assert tabla.factor_carga() == 3 / 7

# 4. Veinte colecciones aleatorias: lista y tabla coinciden
for semilla in range(20):
    azar = random.Random(semilla)
    n = azar.randint(1, 300)
    guias = azar.sample(range(10**9, 10**10), n)
    lista = ListaEnlazada()
    tabla = TablaHash(azar.choice((7, 11, 53, 101)))

    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    conjunto = set(guias)

    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia) is not None
        
    for _ in range(50):
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in conjunto:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

print("Todas las pruebas pasaron.")
