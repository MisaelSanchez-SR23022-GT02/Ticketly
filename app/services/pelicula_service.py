from app.models.pelicula import Pelicula

class PeliculaService:
    def __init__(self):
        self._contador_id = 1
        self._peliculas = []

    def crear_pelicula(self, nombre, duracion, categoria):
        nueva_pelicula = Pelicula(self._contador_id, nombre, duracion, categoria)
        self._peliculas.append(nueva_pelicula)
        self._contador_id += 1
        return nueva_pelicula

    def listar_peliculas(self):
        return self._peliculas

    def eliminar_pelicula(self, id_pelicula):
        for i, p in enumerate(self._peliculas):
            if p.get_id() == int(id_pelicula):
                return self._peliculas.pop(i)
        return None
    
    def actualizar_pelicula(self, id_pelicula, nuevo_nombre, nueva_duracion, nueva_categoria):
        pelicula = self.buscar_por_id(id_pelicula)
        if pelicula:
            pelicula.set_nombre(nuevo_nombre)
            pelicula.set_duracion(nueva_duracion)
            pelicula.set_categoria(nueva_categoria)
            return pelicula
        return None
    
    def buscar_por_id(self, id_buscado):
        return next((p for p in self._peliculas
                     if p.get_id() == int(id_buscado)), None)