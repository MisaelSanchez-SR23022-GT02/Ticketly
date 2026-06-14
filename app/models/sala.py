class Sala:
    def __init__(self, id_sala, capacidad):
        self._id = id_sala
        self._capacidad = capacidad
        self._disponibles = capacidad
        self._asientos = [0] * capacidad

    # Getters

    def get_id(self):
        return self._id

    def get_capacidad(self):
        return self._capacidad

    def get_disponibles(self):
        return self._disponibles

    def get_asientos(self):
        return self._asientos