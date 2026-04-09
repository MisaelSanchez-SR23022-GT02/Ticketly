from app.ui.pelicula_ui import menu_peliculas
from app.utils.limpiar_utils import limpiar_pantalla

def mostrar_menu():
    
    while True:
        limpiar_pantalla()
        print("\n--- SISTEMA TICKETLY - MENÚ PRINCIPAL ---")
        print("1. Gestión de Peliculas")
        print("2. Funciones")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_peliculas()
        elif opcion == "2":
           print("")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")