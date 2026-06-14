from app.models.sala import Sala

class SalaService:
    def __init__(self):
        self._contador_id = 1
        self._salas = []

    # Crear Sala
    def crear_sala(self, capacidad):
        nueva_sala = Sala(self._contador_id, capacidad)
        self._salas.append(nueva_sala)
        self._contador_id += 1
        return nueva_sala


    # Listar Sala
    def listar_salas(self):
        return self._salas

    # Buscar sala

    def buscar_sala(self, id_sala):
        for sala in self._salas:
            if sala.get_id() == id_sala:
                return sala

        return None
    
    def buscar_por_id(self, id_buscado):
        return next((s for s in self._salas
                     if s.get_id() == int(id_buscado)), None)