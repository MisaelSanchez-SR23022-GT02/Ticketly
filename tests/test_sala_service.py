from app.services.sala_service import SalaService

def test_crear_sala_asigna_capacidad_correctamente():
    # 1. Preparar
    servicio = SalaService()
    
    # 2. Actuar
    nueva_sala = servicio.crear_sala(50)
    
    # 3. Afirmar
    assert nueva_sala.get_capacidad() == 50
    assert nueva_sala.get_disponibles() == 50
    assert len(servicio.listar_salas()) == 1