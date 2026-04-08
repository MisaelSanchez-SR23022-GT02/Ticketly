from models.pelicula import Pelicula

class PeliculaService:
    def __init__(self):
        self._next_id = 1
        self._peliculas = []

    def crear_pelicula(self, nombre, duracion, categoria):
        nueva_pelicula = Pelicula(self._next_id, nombre, duracion, categoria)
        self._peliculas.append(nueva_pelicula)
        self._next_id += 1

    def listar_peliculas(self):
        for pelicula in self._peliculas:
            print(pelicula.describir())
    
    def eliminar_pelicula(self, id_pelicula):
      for pelicula in self._peliculas:
        if pelicula.get_id() == id_pelicula:
            self._peliculas.remove(pelicula)
            return True
      return False