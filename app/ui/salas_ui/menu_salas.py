from app.services.sala_service import SalaService

from app.ui.salas_ui.crear_sala_ui import ejecutar_crear_sala
from app.ui.salas_ui.listar_salas_ui import ejecutar_listar
from app.ui.salas_ui.ver_asientos_ui import ejecutar_ver_asientos

def mostrar_menu_salas():

    service = SalaService()

    while True:
        print("\n--- GESTION DE SALAS --- "  )

        print(" 1. Crear sala ")
        print(" 2. Listar salas ")
        print(" 3. Ver asientos ")
        print(" 0. Volver ")

        opcion = input(" Seleccione: ")

        if opcion == "1":
            ejecutar_crear_sala(service)
        elif opcion == "2":
            ejecutar_listar(service)
        elif opcion == "3":
            ejecutar_ver_asientos(service)
        elif opcion == "0":
            break
        else:
            print(" Opcion no valida ")