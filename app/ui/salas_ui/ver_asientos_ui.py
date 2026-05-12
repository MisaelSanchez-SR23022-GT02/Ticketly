def ejecutar_ver_asientos(service):
    try:
        id_sala = int(
            input(" Ingrese Id de sala: ")
        )

    except ValueError:

        print(" Debe ingresar un numero. ")
        input(" Presione ENTER... ")
        return
    sala = service.buscar_sala(id_sala)

    if sala is None:

        print(" Sala no encontrada. ")
        input(" Presione ENTER... ")
        return

    print(
        f"\n --- SALA {sala.get_id()} "
        f" | Libres: {sala.get_disponibles()}/{sala.get_capacidad()} ---"
    )

    asientos = sala.get_asientos()
    for i in range(len(asientos)):
        print(f"[ { i+1 }: { asientos[i] } ]", end = "")

    print()
    input("\n Presione ENTER... ")