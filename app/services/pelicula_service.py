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