class Pelicula:
    def __init__(self, _id_pelicula, _nombre, _duracion, _categoria):
        self._id_pelicula = _id_pelicula
        self._nombre = _nombre
        self._duracion = _duracion
        self._categoria = _categoria

    def get_id(self):
        return self._id_pelicula
        
    def get_nombre(self):
        return self._nombre
        
    def get_duracion(self):
        return self._duracion
        
    def get_categoria(self):
        return self._categoria
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_duracion(self, duracion):
        self._duracion = duracion

    def set_categoria(self, categoria):
        self._categoria = categoria