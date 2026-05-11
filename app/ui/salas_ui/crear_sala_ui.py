def ejecutar_crear_sala(service):

    print("\n --- AGREGAR SALA --- ")
    try:

        capacidad = int(
            input(" Capacidad de la sala (max 50): ")
        )

    except ValueError:

        print(" Debe ingresar un numero. ")
        input(" Presione Enter... ")
        return

    # Validaciones

    if capacidad > 50:

        capacidad = 50
        print(" Capacidad ajustada al maximo: 50 ")

    if capacidad < 1:

        capacidad = 1
        print(" Capacidad ajustada al minimo: 1 ")

    nueva_sala = service.crear_sala(capacidad)
    print(f"\n Sala creada con ID: {nueva_sala.get_id()}")
    input("\n Presione ENTER...")
