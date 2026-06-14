from app.models.funcion import Funcion

class FuncionService:
    def __init__(self, pelicula_service, sala_service):
        self._contador_id = 1
        self._funciones = []
        self._pelicula_service = pelicula_service
        self._sala_service = sala_service
    
    def crear_funcion(self, id_peli, id_sala, hora):
        peli = self._pelicula_service.buscar_por_id(id_peli)
        if not peli:
            return None 
        sala = self._sala_service.buscar_por_id(id_sala)
        if not sala:
            return None
    
        nueva_funcion = Funcion(self._contador_id, id_peli, id_sala, hora)
        self._funciones.append(nueva_funcion)
        self._contador_id += 1
        return nueva_funcion
    
    def listar_funciones(self):
        return self._funciones
    
    def eliminar_funcion(self, id_funcion):
        for i, f in enumerate(self._funciones):
            if f.get_id() == int(id_funcion):
                return self._funciones.pop(i)