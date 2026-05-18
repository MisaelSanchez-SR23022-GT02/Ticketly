Algoritmo Ticketly
	
    // --- Peliculas ---
    Definir cantidad_peliculas Como Entero
    Dimension id_peliculas[10], duracion_peliculas[10]
    Dimension titulo_peliculas[10], genero_peliculas[10]
    cantidad_peliculas <- 0
	
    // --- Salas ---
    Definir cantidad_salas Como Entero
    Dimension id_salas[10], capacidad_salas[10], asientos_disponibles_salas[10]
    Dimension matriz_asientos_salas[10, 50]
    cantidad_salas <- 0
	
    // --- Funciones ---
    Definir cantidad_funciones Como Entero
    Dimension id_funciones[20], id_pelicula_por_funcion[20], id_sala_por_funcion[20]
    Dimension horario_funciones[20]
    cantidad_funciones <- 0
	
    // --- Boletos ---
    Definir cantidad_boletos Como Entero
    Dimension id_boletos[100], id_funcion_por_boleto[100], numero_asiento_boleto[100]
    cantidad_boletos <- 0
	
    // --- Variables temporales ---
    Definir opcion_menu, sub_opcion_menu Como Entero
    Definir texto_ingresado, texto_ingresado_secundario Como Caracter
    Definir numero_ingresado, numero_ingresado_secundario, i, j Como Entero
    Definir existe_registro, es_valido Como Logico
	
    Repetir
        Limpiar Pantalla
        Escribir "=================================="
        Escribir "   TICKETLY - BOLETERIA DE CINE"
        Escribir "=================================="
        Escribir " 1. Gestionar Peliculas"
        Escribir " 2. Gestionar Salas"
        Escribir " 3. Gestionar Funciones"
        Escribir " 4. Venta de Boletos"
        Escribir " 5. Salir"
        Escribir "=================================="
        Escribir "Seleccione una opcion: "
        Leer opcion_menu
		
        Segun opcion_menu Hacer
			
            1:
                Repetir
                    Limpiar Pantalla
                    Escribir "--- GESTION DE PELICULAS ---"
                    Escribir "1. Listar peliculas"
                    Escribir "2. Agregar pelicula"
                    Escribir "0. Volver"
                    Escribir "Seleccione: "
                    Leer sub_opcion_menu
					
                    Segun sub_opcion_menu Hacer
                        1:
                            MostrarPeliculas(id_peliculas, titulo_peliculas, duracion_peliculas, genero_peliculas, cantidad_peliculas)
							
                        2:
                            Si cantidad_peliculas >= 10 Entonces
                                Escribir "Error: Limite de 10 peliculas alcanzado."
                                Esperar Tecla
                            Sino
                                Limpiar Pantalla
                                Escribir "--- AGREGAR PELICULA ---"
                                Escribir "Titulo: "
                                Leer texto_ingresado
                                Escribir "Duracion (minutos): "
                                Leer numero_ingresado
                                Escribir "Genero: "
                                Leer texto_ingresado_secundario
								
                                cantidad_peliculas <- cantidad_peliculas + 1
                                id_peliculas[cantidad_peliculas] <- cantidad_peliculas
                                titulo_peliculas[cantidad_peliculas] <- texto_ingresado
                                duracion_peliculas[cantidad_peliculas] <- numero_ingresado
                                genero_peliculas[cantidad_peliculas] <- texto_ingresado_secundario
								
                                Escribir "Pelicula agregada con ID: ", cantidad_peliculas
                                Esperar Tecla
                            FinSi
                    FinSegun
                Hasta Que sub_opcion_menu = 0
            2:
                Repetir
                    Limpiar Pantalla
                    Escribir "--- GESTION DE SALAS ---"
                    Escribir "1. Listar salas"
                    Escribir "2. Agregar sala"
                    Escribir "3. Ver asientos de una sala"
                    Escribir "0. Volver"
                    Escribir "Seleccione: "
                    Leer sub_opcion_menu
					
                    Segun sub_opcion_menu Hacer
                        1:
                            MostrarSalas(id_salas, capacidad_salas, asientos_disponibles_salas, cantidad_salas)
							
                        2:
                            Si cantidad_salas >= 10 Entonces
                                Escribir "Error: Limite de 10 salas alcanzado."
                                Esperar Tecla
                            Sino
                                Limpiar Pantalla
                                Escribir "--- AGREGAR SALA ---"
                                Escribir "Capacidad de la sala (max 50): "
                                Leer numero_ingresado
								
                                Si numero_ingresado > 50 Entonces
                                    numero_ingresado <- 50
                                    Escribir "Capacidad ajustada al maximo: 50"
                                FinSi
                                Si numero_ingresado < 1 Entonces
                                    numero_ingresado <- 1
                                    Escribir "Capacidad ajustada al minimo: 1"
                                FinSi
								
                                cantidad_salas <- cantidad_salas + 1
                                id_salas[cantidad_salas] <- cantidad_salas
                                capacidad_salas[cantidad_salas] <- numero_ingresado
                                asientos_disponibles_salas[cantidad_salas] <- numero_ingresado
								
                                Para j <- 1 Hasta numero_ingresado Hacer
                                    matriz_asientos_salas[cantidad_salas, j] <- 0
                                FinPara
								
                                Escribir "Sala creada con ID: ", cantidad_salas
                                Esperar Tecla
                            FinSi
							
                        3:
                            Escribir "Ingrese el ID de la sala: "
                            Leer numero_ingresado
                            VerAsientos(id_salas, capacidad_salas, matriz_asientos_salas, asientos_disponibles_salas, cantidad_salas, numero_ingresado)
                    FinSegun
                Hasta Que sub_opcion_menu = 0
            3:
                Repetir
                    Limpiar Pantalla
                    Escribir "--- GESTION DE FUNCIONES ---"
                    Escribir "1. Listar funciones"
                    Escribir "2. Agregar funcion"
                    Escribir "3. Actualizar pelicula"
                    Escribir "0. Volver"
                    Escribir "Seleccione: "
                    Leer sub_opcion_menu
					
                    Segun sub_opcion_menu Hacer
                        1:
                            MostrarFunciones(id_funciones, id_pelicula_por_funcion, id_sala_por_funcion, horario_funciones, cantidad_funciones)
							
                        2:
                            Si cantidad_funciones >= 20 Entonces
                                Escribir "Error: Limite de 20 funciones alcanzado."
                                Esperar Tecla
                            Sino
                                Limpiar Pantalla
                                Escribir "--- AGREGAR FUNCION ---"
                                Escribir "ID de pelicula (1 a ", cantidad_peliculas, "): "
                                Leer numero_ingresado
                                es_valido <- Falso
                                Para i <- 1 Hasta cantidad_peliculas Hacer
                                    Si id_peliculas[i] = numero_ingresado Entonces
                                        es_valido <- Verdadero
                                    FinSi
                                FinPara
								
                                Si es_valido = Falso Entonces
                                    Escribir "Error: No existe pelicula con ID ", numero_ingresado
                                    Esperar Tecla
                                Sino
                                    numero_ingresado_secundario <- numero_ingresado
                                    Escribir "ID de sala (1 a ", cantidad_salas, "): "
                                    Leer numero_ingresado
                                    es_valido <- Falso
                                    Para i <- 1 Hasta cantidad_salas Hacer
                                        Si id_salas[i] = numero_ingresado Entonces
                                            es_valido <- Verdadero
                                        FinSi
                                    FinPara
									
                                    Si es_valido = Falso Entonces
                                        Escribir "Error: No existe sala con ID ", numero_ingresado
                                        Esperar Tecla
                                    Sino
                                        Escribir "Horario (ej: 18:00): "
                                        Leer texto_ingresado
										
                                        cantidad_funciones <- cantidad_funciones + 1
                                        id_funciones[cantidad_funciones] <- cantidad_funciones
                                        id_pelicula_por_funcion[cantidad_funciones] <- numero_ingresado_secundario
                                        id_sala_por_funcion[cantidad_funciones] <- numero_ingresado
                                        horario_funciones[cantidad_funciones] <- texto_ingresado
										
                                        Escribir "Funcion creada con ID: ", cantidad_funciones
                                        Esperar Tecla
                                    FinSi
                                FinSi
                            FinSi
                        3:
                            Si cantidad_peliculas = 0 Entonces
                                Escribir "No hay peliculas registradas."
                                Esperar Tecla
                            Sino
                                MostrarPeliculas(id_peliculas, titulo_peliculas, duracion_peliculas, genero_peliculas, cantidad_peliculas)
                                Escribir "Ingrese el ID de la pelicula a actualizar: "
                                Leer numero_ingresado
                                ActualizarPelicula(id_peliculas, titulo_peliculas, duracion_peliculas, genero_peliculas, cantidad_peliculas, numero_ingresado)
                            FinSi                    
                    FinSegun
                Hasta Que sub_opcion_menu = 0
				
            4:
				Limpiar Pantalla
				Escribir "--- VENTA DE BOLETOS ---"
				
				Si cantidad_funciones = 0 Entonces
					Escribir "No hay funciones disponibles."
					Esperar Tecla
				Sino
					MostrarFunciones(id_funciones, id_pelicula_por_funcion, id_sala_por_funcion, horario_funciones, cantidad_funciones)
					
					Escribir "Ingrese ID de la funcion: "
					Leer numero_ingresado
					es_valido <- Falso
					
					Para i <- 1 Hasta cantidad_funciones Hacer
						Si id_funciones[i] = numero_ingresado Entonces
							es_valido <- Verdadero
						FinSi
					FinPara
					
					Si es_valido = Falso Entonces
						Escribir "Error: No existe la funcion con ID ", numero_ingresado
						Esperar Tecla
					Sino
						numero_ingresado_secundario <- numero_ingresado
						
						VerAsientos(id_salas, capacidad_salas, matriz_asientos_salas, asientos_disponibles_salas, cantidad_salas, id_sala_por_funcion[numero_ingresado_secundario])
						
						Escribir "Ingrese numero de asiento: "
						Leer numero_ingresado
						
						indice_sala <- 0
						Para i <- 1 Hasta cantidad_salas Hacer
							Si id_salas[i] = id_sala_por_funcion[numero_ingresado_secundario] Entonces
								indice_sala <- i
							FinSi
						FinPara
						
						Si numero_ingresado < 1 O numero_ingresado > capacidad_salas[indice_sala] Entonces
							Escribir "Error: El asiento ingresado no existe."
							Esperar Tecla
						Sino
							
							Si matriz_asientos_salas[indice_sala, numero_ingresado] = 1 Entonces
								Escribir "Error: El asiento ya esta ocupado."
								Esperar Tecla
							Sino
								
								es_valido <- Verdadero
								Si cantidad_boletos > 0 Entonces
									Para i <- 1 Hasta cantidad_boletos Hacer
										Si id_funcion_por_boleto[i] = numero_ingresado_secundario Y numero_asiento_boleto[i] = numero_ingresado Entonces
											es_valido <- Falso
										FinSi
									FinPara
								FinSi
								
								Si es_valido = Falso Entonces
									Escribir "Error: El asiento ", numero_ingresado, " ya fue vendido para esta funcion."
									Esperar Tecla
								Sino
									
									Si cantidad_boletos >= 100 Entonces
										Escribir "Error: Limite de boletos alcanzado."
										Esperar Tecla
									Sino
										
										matriz_asientos_salas[indice_sala, numero_ingresado] <- 1
										asientos_disponibles_salas[indice_sala] <- asientos_disponibles_salas[indice_sala] - 1
										
										cantidad_boletos <- cantidad_boletos + 1
										id_boletos[cantidad_boletos] <- cantidad_boletos
										id_funcion_por_boleto[cantidad_boletos] <- numero_ingresado_secundario
										numero_asiento_boleto[cantidad_boletos] <- numero_ingresado
										
										Escribir ""
										Escribir "=============================="
										Escribir "       BOLETO VENDIDO"
										Escribir "=============================="
										Escribir " Boleto ID : ", cantidad_boletos
										Escribir " Funcion   : ", numero_ingresado_secundario
										Escribir " Asiento   : ", numero_ingresado
										Escribir "=============================="
										
										Esperar Tecla
										
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
            5:
                Escribir "Hasta luego!"
        FinSegun
    Hasta Que opcion_menu = 5
	
FinAlgoritmo

// SUBPROCESOS PARA MOSTRAR DATOS SOLO DE LECTURA 

SubProceso MostrarPeliculas(arreglo_ids, arreglo_titulos, arreglo_durs, arreglo_generos, cantidad)
    Limpiar Pantalla
    Escribir "--- CATALOGO DE PELICULAS ---"
    Si cantidad = 0 Entonces
        Escribir "No hay peliculas registradas."
    Sino
        Escribir "ID  | TITULO | DUR(min) | GENERO"
        Escribir "----------------------------------------------------"
        Definir i Como Entero
        Para i <- 1 Hasta cantidad Hacer
            Escribir arreglo_ids[i], " | ", arreglo_titulos[i], " | ", arreglo_durs[i], " min | ", arreglo_generos[i]
        FinPara
    FinSi
    Esperar Tecla
FinSubProceso


SubProceso MostrarSalas(arreglo_ids, arreglo_caps, arreglo_disps, cantidad)
    Limpiar Pantalla
    Escribir "--- SALAS REGISTRADAS ---"
    Si cantidad = 0 Entonces
        Escribir "No hay salas registradas."
    Sino
        Escribir "ID | CAPACIDAD | ASIENTOS LIBRES"
        Escribir "-----------------------------------"
        Definir i Como Entero
        Para i <- 1 Hasta cantidad Hacer
            Escribir arreglo_ids[i], " | ", arreglo_caps[i], " | ", arreglo_disps[i]
        FinPara
    FinSi
    Esperar Tecla
FinSubProceso


SubProceso VerAsientos(arreglo_ids, arreglo_caps, arreglo_asientos, arreglo_disps, cantidad, id_buscado)
    Limpiar Pantalla
    Definir i, j Como Entero
    Definir sala_encontrada Como Logico
    sala_encontrada <- Falso
	
    Para i <- 1 Hasta cantidad Hacer
        Si arreglo_ids[i] = id_buscado Entonces
            sala_encontrada <- Verdadero
            Escribir "--- SALA ID: ", arreglo_ids[i], " | Libres: ", arreglo_disps[i], "/", arreglo_caps[i], " ---"
            Escribir "Asientos (0=Libre, 1=Ocupado):"
            Para j <- 1 Hasta arreglo_caps[i] Hacer
                Escribir Sin Saltar "[ ", j, ":", arreglo_asientos[i, j], " ] "
            FinPara
            Escribir ""
        FinSi
        Esperar Tecla
    FinPara
	
    Si sala_encontrada = Falso Entonces
        Escribir "Sala con ID ", id_buscado, " no encontrada."
        Esperar Tecla
    FinSi
FinSubProceso


SubProceso MostrarFunciones(arreglo_ids, arreglo_pelis, arreglo_salas, arreglo_horarios, cantidad)
    Limpiar Pantalla
    Escribir "--- FUNCIONES PROGRAMADAS ---"
    Si cantidad = 0 Entonces
        Escribir "No hay funciones registradas."
    Sino
        Escribir "ID | PELICULA ID | SALA ID | HORARIO"
        Escribir "--------------------------------------"
        Definir i Como Entero
        Para i <- 1 Hasta cantidad Hacer
            Escribir arreglo_ids[i], "  | ", arreglo_pelis[i], " | ", arreglo_salas[i], " | ", arreglo_horarios[i]
        FinPara
    FinSi
    Esperar Tecla
FinSubProceso

SubProceso ActualizarPelicula(arreglo_ids, arreglo_titulos, arreglo_durs, arreglo_generos, cantidad, id_buscado)
    Definir i Como Entero
    Definir indice_encontrado Como Entero
    Definir encontrado Como Logico
    Definir nuevo_titulo, nuevo_genero Como Caracter
    Definir nueva_duracion Como Entero
    
    encontrado <- Falso
    indice_encontrado <- 0
    
    // Validacion: ID existente
    Para i <- 1 Hasta cantidad Hacer
        Si arreglo_ids[i] = id_buscado Entonces
            encontrado <- Verdadero
            indice_encontrado <- i
        FinSi
    FinPara
    
    Si encontrado = Falso Entonces
        Escribir "Error: No existe pelicula con ID ", id_buscado
        Esperar Tecla
    Sino
        Limpiar Pantalla
        Escribir "--- ACTUALIZAR PELICULA ID: ", id_buscado, " ---"
        Escribir "Datos actuales:"
        Escribir "  Titulo  : ", arreglo_titulos[indice_encontrado]
        Escribir "  Duracion: ", arreglo_durs[indice_encontrado], " min"
        Escribir "  Genero  : ", arreglo_generos[indice_encontrado]
        Escribir "--------------------------------------------"
        
        // Validacion: Titulo no vacio
        Repetir
            Escribir "Nuevo titulo (actual: ", arreglo_titulos[indice_encontrado], "): "
            Leer nuevo_titulo
            Si nuevo_titulo = "" Entonces
                Escribir "Error: El titulo no puede estar vacio."
            FinSi
        Hasta Que nuevo_titulo <> ""
        
        // Validacion: Duracion mayor a 0
        Repetir
            Escribir "Nueva duracion en minutos (actual: ", arreglo_durs[indice_encontrado], "): "
            Leer nueva_duracion
            Si nueva_duracion <= 0 Entonces
                Escribir "Error: La duracion debe ser mayor a 0."
            FinSi
        Hasta Que nueva_duracion > 0
        
        // Validacion: Genero no vacio
        Repetir
            Escribir "Nuevo genero (actual: ", arreglo_generos[indice_encontrado], "): "
            Leer nuevo_genero
            Si nuevo_genero = "" Entonces
                Escribir "Error: El genero no puede estar vacio."
            FinSi
        Hasta Que nuevo_genero <> ""
        
        arreglo_titulos[indice_encontrado] <- nuevo_titulo
        arreglo_durs[indice_encontrado] <- nueva_duracion
        arreglo_generos[indice_encontrado] <- nuevo_genero
        
        Escribir "Pelicula actualizada correctamente."
        Esperar Tecla
    FinSi
FinSubProceso