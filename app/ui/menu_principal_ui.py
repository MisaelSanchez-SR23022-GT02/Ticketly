from ui.pelicula_ui import menu_peliculas

def mostrar_menu():
    
    while True:
        print("\n--- TICKETLY - MENÚ PRINCIPAL ---")
        print("1. Gestión de Peliculas")
        print("2. Funciones")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_peliculas()
        elif opcion == "2":
           print("")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")