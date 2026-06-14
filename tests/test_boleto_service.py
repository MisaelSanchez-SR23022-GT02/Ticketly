import pytest
from app.services.pelicula_service import PeliculaService
from app.services.sala_service import SalaService
from app.services.funcion_service import FuncionService
from app.services.boleto_service import BoletoService
from app.models.boleto import Boleto

@pytest.fixture
def servicios():
    pelicula_service = PeliculaService()
    sala_service = SalaService()
    funcion_service = FuncionService(pelicula_service, sala_service)
    boleto_service = BoletoService(funcion_service, sala_service)

    pelicula_service.crear_pelicula("Inception", "148", "Sci-Fi")
    sala_service.crear_sala(3)
    funcion_service.crear_funcion(1, 1, "18:00")

    return boleto_service, funcion_service, sala_service


def test_vender_boleto_exitoso(servicios):
    boleto_service, _, _ = servicios
    resultado = boleto_service.vender_boleto(1, 1)

    assert isinstance(resultado, Boleto)
    assert resultado.get_id() == 1
    assert resultado.get_id_funcion() == 1
    assert resultado.get_numero_asiento() == 1


def test_vender_boleto_ocupa_asiento(servicios):
    boleto_service, _, sala_service = servicios
    sala = sala_service.buscar_por_id(1)
    disponibles_antes = sala.get_disponibles()

    boleto_service.vender_boleto(1, 2)

    assert sala.get_asientos()[1] == 'O'
    assert sala.get_disponibles() == disponibles_antes - 1


def test_vender_boleto_funcion_inexistente(servicios):
    boleto_service, _, _ = servicios
    assert boleto_service.vender_boleto(99, 1) == "ERROR_FUNCION"


def test_vender_boleto_asiento_fuera_de_rango(servicios):
    boleto_service, _, _ = servicios
    assert boleto_service.vender_boleto(1, 99) == "ERROR_RANGO"


def test_vender_boleto_asiento_cero(servicios):
    boleto_service, _, _ = servicios
    assert boleto_service.vender_boleto(1, 0) == "ERROR_RANGO"


def test_vender_boleto_asiento_ocupado(servicios):
    boleto_service, _, _ = servicios
    boleto_service.vender_boleto(1, 1)
    assert boleto_service.vender_boleto(1, 1) == "ERROR_OCUPADO"


def test_listar_boletos_acumula(servicios):
    boleto_service, _, _ = servicios
    boleto_service.vender_boleto(1, 1)
    boleto_service.vender_boleto(1, 2)
    assert len(boleto_service.listar_boletos()) == 2