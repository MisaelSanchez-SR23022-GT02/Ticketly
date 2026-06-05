from app.models.boleto import Boleto

class BoletoService:
    def __init__(self, funcion_service, sala_service):
        self._contador_id = 1
        self._boletos = []
        self._funcion_service = funcion_service
        self._sala_service = sala_service

    def vender_boleto(self, id_funcion, numero_asiento):

        funcion = next(
            (f for f in self._funcion_service.listar_funciones()
             if f.get_id() == int(id_funcion)),
            None
        )
        if not funcion:
            return "ERROR_FUNCION"

        sala = self._sala_service.buscar_por_id(funcion.get_id_sala())
        if not sala:
            return "ERROR_SALA"

        numero_asiento = int(numero_asiento)

        if numero_asiento < 1 or numero_asiento > sala.get_capacidad():
            return "ERROR_RANGO"

        asientos = sala.get_asientos()
        if asientos[numero_asiento - 1] == 'O':
            return "ERROR_OCUPADO"

        asientos[numero_asiento - 1] = 'O'
        sala._disponibles -= 1

        nuevo_boleto = Boleto(
            self._contador_id,
            funcion.get_id(),
            sala.get_id(),
            numero_asiento
        )
        self._boletos.append(nuevo_boleto)
        self._contador_id += 1
        return nuevo_boleto

    def listar_boletos(self):
        return self._boletos