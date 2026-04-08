from services.pelicula_service import PeliculaService
import time
service = PeliculaService()

def menu_peliculas():
    opcion = ""

    while opcion != "0":
        print("\n--- TICKETLY - GESTION PELICULAS ---")
        print("1. Crear peliculas")
        print("2. Listar peliculas")
        print("3. Eliminar peliculas")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            duracion = input("Duración: ")
            categoria = input("Categoría: ")

            service.crear_pelicula(nombre, duracion, categoria)

        elif opcion == "2":   
            print("Lista de peliculas:")
            print("-" * 50)
            service.listar_peliculas() 
            print("-" * 50)
            time.sleep(1) 
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            id_pelicula = input("ID de la película: ")
            service.eliminar_pelicula(int(id_pelicula))

        elif opcion == "0":
            print("Saliendo del programa.")

        else:
            print("Opción no válida.")