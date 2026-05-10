def ejecutar_listar(service):

    salas = service.listar_salas()

    print("\n --- Salas registradas --- ")

    if not salas:
        print(" No hay salas registradas ")

    else:

        print(" Id | Capacidad | Libres ")
        print("---------------------------")

        for sala in salas:

            print(
                sala.get_id(),
                "|",
                sala.get_capacidad(),
                "|",
                sala.get_disponibles()
            )
    input("\n Presione ENTER... ")
