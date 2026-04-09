from app.services.pelicula_service import PeliculaService
from app.utils.limpiar_utils import limpiar_pantalla
import time
service = PeliculaService()

def menu_peliculas():
    opcion = ""

    while opcion != "0":
        limpiar_pantalla()
        print("\n--- TICKETLY - GESTION PELICULAS ---")
        print("1. Crear peliculas")
        print("2. Listar peliculas")
        print("3. Eliminar peliculas")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            nombre = input("Nombre: ")
            duracion = input("Duración: ")
            categoria = input("Categoría: ")

            service.crear_pelicula(nombre, duracion, categoria)

        elif opcion == "2": 
            limpiar_pantalla()   
            print("Lista de peliculas:")
            print("-" * 50)
            service.listar_peliculas() 
            print("-" * 50)
            time.sleep(1) 
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            limpiar_pantalla()
            id_pelicula = input("ID de la película: ")
            service.eliminar_pelicula(int(id_pelicula))

        elif opcion == "0":
            print("Saliendo del programa.")

        else:
            print("Opción no válida.")