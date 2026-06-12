#------------------
#---crear_pelicula-
#__________________

import unittest
from app.models.pelicula import Pelicula
from app.services.pelicula_service import PeliculaService


class TestPeliculaService(unittest.TestCase):

    def setUp(self):
        self.service = PeliculaService()

    def test_crear_pelicula_retorna_pelicula(self):
        """Al crear una película válida debe retornar un objeto Pelicula."""
        pelicula = self.service.crear_pelicula("Inception", 148, "Ciencia Ficción")
        self.assertIsNotNone(pelicula)
        self.assertIsInstance(pelicula, Pelicula)


if __name__ == "__main__":
    unittest.main()