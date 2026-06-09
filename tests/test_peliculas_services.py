"""
Tests de PeliculaService - Ticketly
====================================
Cubre: crear, listar, buscar por ID, eliminar, actualizar
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.pelicula_service import PeliculaService


@pytest.fixture
def service():
    """Instancia limpia de PeliculaService para cada test."""
    return PeliculaService()

@pytest.fixture
def servicio_con_pelicula(servicio):
    servicio.crear_pelicula("Inception", 148, "Sci-Fi")
    return servicio


# ─────────────────────────────────────────────
#  CREAR
# ─────────────────────────────────────────────

def test_crear_pelicula_valida(service):
    """crear_pelicula() debe retornar un objeto Pelicula con los datos correctos."""
    p = service.crear_pelicula("Avengers", 181, "Accion")
    assert p is not None
    assert p.get_nombre() == "Avengers"
    assert p.get_duracion() == 181
    assert p.get_categoria() == "Accion"

def test_crear_pelicula_retorna_none_si_nombre_duplicado(service):
    """crear_pelicula() debe retornar None si ya existe una pelicula con el mismo nombre."""
    service.crear_pelicula("Matrix", 136, "Ciencia Ficcion")
    resultado = service.crear_pelicula("matrix", 100, "Drama")  # mismo nombre, distinta capitalización
    assert resultado is None, "No debe crear pelicula con nombre duplicado (case insensitive)"

def test_crear_pelicula_ids_autoincrementales(service):
    """crear_pelicula() debe asignar IDs autoincrementales (1, 2, 3...)."""
    p1 = service.crear_pelicula("Pelicula Uno", 90, "Drama")
    p2 = service.crear_pelicula("Pelicula Dos", 100, "Comedia")
    assert p1.get_id() == 1
    assert p2.get_id() == 2

def test_crear_multiples_peliculas(service):
    """crear_pelicula() debe permitir agregar varias peliculas distintas."""
    service.crear_pelicula("Pelicula A", 80, "Terror")
    service.crear_pelicula("Pelicula B", 90, "Drama")
    service.crear_pelicula("Pelicula C", 100, "Comedia")
    assert len(service.listar_peliculas()) == 3


# ─────────────────────────────────────────────
#  LISTAR
# ─────────────────────────────────────────────

def test_listar_peliculas_vacia(service):
    """listar_peliculas() debe retornar lista vacia si no hay peliculas."""
    assert service.listar_peliculas() == []

def test_listar_peliculas_no_es_none(service):
    """listar_peliculas() nunca debe retornar None."""
    assert service.listar_peliculas() is not None

def test_listar_peliculas_contiene_elementos(service):
    """listar_peliculas() debe contener las peliculas creadas."""
    service.crear_pelicula("El Padrino", 175, "Drama")
    lista = service.listar_peliculas()
    assert len(lista) == 1
    assert lista[0].get_nombre() == "El Padrino"

def test_listar_peliculas_tamanio_aumenta(service):
    """listar_peliculas() debe crecer al agregar peliculas."""
    service.crear_pelicula("Inception", 148, "Ciencia Ficcion")
    service.crear_pelicula("Interstellar", 169, "Ciencia Ficcion")
    assert len(service.listar_peliculas()) == 2


# ─────────────────────────────────────────────
#  BUSCAR POR ID
# ─────────────────────────────────────────────

def test_buscar_por_id_existente(service):
    """buscar_por_id() debe encontrar la pelicula correcta por su ID."""
    p = service.crear_pelicula("Toy Story", 81, "Animacion")
    encontrada = service.buscar_por_id(p.get_id())
    assert encontrada is not None
    assert encontrada.get_id() == p.get_id()
    assert encontrada.get_nombre() == "Toy Story"

def test_buscar_por_id_inexistente_retorna_none(service):
    """buscar_por_id() debe retornar None si el ID no existe."""
    resultado = service.buscar_por_id(999)
    assert resultado is None

def test_buscar_por_id_retorna_pelicula_correcta(service):
    """buscar_por_id() no debe confundir peliculas cuando hay varias."""
    p1 = service.crear_pelicula("Pelicula Uno", 90, "Drama")
    p2 = service.crear_pelicula("Pelicula Dos", 100, "Comedia")
    assert service.buscar_por_id(p1.get_id()).get_nombre() == "Pelicula Uno"
    assert service.buscar_por_id(p2.get_id()).get_nombre() == "Pelicula Dos"


# ─────────────────────────────────────────────
#  ELIMINAR
# ─────────────────────────────────────────────

def test_eliminar_pelicula_existente(service):
    """eliminar_pelicula() debe eliminar la pelicula y retornarla."""
    p = service.crear_pelicula("Pelicula Borrable", 95, "Terror")
    eliminada = service.eliminar_pelicula(p.get_id())
    assert eliminada is not None
    assert eliminada.get_id() == p.get_id()

def test_eliminar_pelicula_ya_no_aparece_en_lista(service):
    """Despues de eliminar, la pelicula no debe aparecer en listar ni en buscar."""
    p = service.crear_pelicula("Pelicula Temporal", 100, "Accion")
    service.eliminar_pelicula(p.get_id())
    assert service.buscar_por_id(p.get_id()) is None
    assert len(service.listar_peliculas()) == 0

def test_eliminar_pelicula_inexistente_retorna_none(service):
    """eliminar_pelicula() debe retornar None si el ID no existe."""
    resultado = service.eliminar_pelicula(999)
    assert resultado is None

def test_eliminar_reduce_tamanio_lista(service):
    """eliminar_pelicula() debe reducir el tamanio de la lista."""
    p1 = service.crear_pelicula("Pelicula 1", 80, "Drama")
    service.crear_pelicula("Pelicula 2", 90, "Comedia")
    antes = len(service.listar_peliculas())
    service.eliminar_pelicula(p1.get_id())
    assert len(service.listar_peliculas()) == antes - 1


# ─────────────────────────────────────────────
#  ACTUALIZAR
# ─────────────────────────────────────────────

def test_actualizar_pelicula_existente(service):
    """actualizar_pelicula() debe modificar correctamente los datos."""
    p = service.crear_pelicula("Titulo Viejo", 90, "Terror")
    actualizada = service.actualizar_pelicula(p.get_id(), "Titulo Nuevo", 110, "Comedia")
    assert actualizada is not None
    assert actualizada.get_nombre() == "Titulo Nuevo"
    assert actualizada.get_duracion() == 110
    assert actualizada.get_categoria() == "Comedia"

def test_actualizar_pelicula_inexistente_retorna_none(service):
    """actualizar_pelicula() debe retornar None si el ID no existe."""
    resultado = service.actualizar_pelicula(999, "Nuevo Nombre", 100, "Drama")
    assert resultado is None

def test_actualizar_no_crea_nueva_pelicula(service):
    """actualizar_pelicula() no debe aumentar el tamanio de la lista."""
    service.crear_pelicula("Pelicula Unica", 100, "Accion")
    antes = len(service.listar_peliculas())
    service.actualizar_pelicula(1, "Pelicula Actualizada", 120, "Drama")
    assert len(service.listar_peliculas()) == antes

def test_actualizar_persiste_en_buscar(service):
    """El cambio de actualizar_pelicula() debe verse al hacer buscar_por_id()."""
    p = service.crear_pelicula("Original", 80, "Drama")
    service.actualizar_pelicula(p.get_id(), "Modificada", 95, "Terror")
    encontrada = service.buscar_por_id(p.get_id())
    assert encontrada.get_nombre() == "Modificada"