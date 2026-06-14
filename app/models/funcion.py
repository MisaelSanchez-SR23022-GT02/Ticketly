class Funcion:
    def __init__(self, _id_funcion, _id_pelicula, _id_sala, _hora_funcion):
        self._id_funcion = _id_funcion
        self._id_pelicula = _id_pelicula
        self._id_sala = _id_sala
        self._hora_funcion = _hora_funcion

    def get_id(self):
         return self._id_funcion
        
    def get_id_pelicula(self):
        return self._id_pelicula 
        
    def get_id_sala(self):
        return self._id_sala
        
    def get_hora_funcion(self):
        return self._hora_funcion