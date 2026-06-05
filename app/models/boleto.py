class Boleto:
    def __init__(self, _id_boleto, _id_funcion, _id_sala, _numero_asiento):
        self._id_boleto = _id_boleto
        self._id_funcion = _id_funcion
        self._id_sala = _id_sala
        self._numero_asiento = _numero_asiento

    def get_id(self):
        return self._id_boleto

    def get_id_funcion(self):
        return self._id_funcion

    def get_id_sala(self):
        return self._id_sala

    def get_numero_asiento(self):
        return self._numero_asiento
