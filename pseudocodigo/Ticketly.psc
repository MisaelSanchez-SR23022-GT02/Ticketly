Algoritmo Ticketly
    Definir opcion, sub_opcion Como Entero
    
    // Arreglos para PEL�CULAS
    Definir cantidad_peliculas Como Entero
    Dimension ids_peli[10], duraciones_peli[10]
    Dimension titulos_peli[10], generos_peli[10]
    cantidad_peliculas <- 0

	    // Arreglos para FUNCIONES
    Definir cantidad_funciones Como Entero
    Dimension ids_funcion[20], ids_peli_funcion[20], salas_funcion[20]
    Dimension horarios_funcion[20]
    cantidad_funciones <- 0
    
    // Arreglos para BOLETOS
    Definir cantidad_boletos Como Entero
    Dimension ids_boleto[100], ids_funcion_boleto[100], asientos_boleto[100]
    cantidad_boletos <- 0
    
    // Variables temporales para lecturas
    Definir lectura_titulo, lectura_genero Como Caracter
    Definir lectura_duracion, lectura_id_funcion, lectura_asiento Como Entero
    
    Repetir
        Limpiar Pantalla
        Escribir "=================================="
        Escribir "    SISTEMA DE BOLETER�A DE CINE"
        Escribir "=================================="
        Escribir "1. Gestionar Pel�culas"
        Escribir "2. Gestionar Salas"
        Escribir "3. Gestionar Funciones"
        Escribir "4. Venta de Boletos"
        Escribir "5. Reportes"
        Escribir "6. Salir"
        Escribir "=================================="
        Leer opcion
        
        Segun opcion Hacer
            1:
                Repetir
                    Limpiar Pantalla
                    Escribir "--- GESTI�N DE PEL�CULAS ---"
                    Escribir "1. Listar pel�culas"
                    Escribir "2. Agregar pel�cula"
                    Escribir "0. Volver"
                    Leer sub_opcion
                    
                    Segun sub_opcion Hacer
                        1: 
                            listar_peliculas(ids_peli, titulos_peli, duraciones_peli, generos_peli, cantidad_peliculas)
                        2: 
                            Limpiar Pantalla
                            Escribir "T�tulo: "
                            Leer lectura_titulo
                            Escribir "Duraci�n (min): "
                            Leer lectura_duracion
                            Escribir "G�nero: "
                            Leer lectura_genero
                            
                            crear_pelicula(ids_peli, titulos_peli, duraciones_peli, generos_peli, cantidad_peliculas, lectura_titulo, lectura_duracion, lectura_genero)
                    FinSegun
                Hasta Que sub_opcion = 0
                
			2: // --- GESTI�N DE SALAS ---
                Escribir "Modulo de Salas"
                Esperar Tecla
                
            3: // --- GESTION DE FUNCIONES ---
                Repetir
                    Limpiar Pantalla
                    Escribir "--- GESTION DE FUNCIONES ---"
                    Escribir "1. Listar funciones"
                    Escribir "2. Agregar funcion"
                    Escribir "0. Volver"
                    Leer sub_opcion
                    
                    Segun sub_opcion Hacer
                        1:
                            listar_funciones(ids_funcion, ids_peli_funcion, horarios_funcion, salas_funcion, cantidad_funciones)
                        2:
                            Limpiar Pantalla
                            Escribir "ID de pelicula: "
                            Leer lectura_id_funcion
                            Escribir "Sala (numero): "
                            Leer lectura_asiento
                            Escribir "Horario (ej: 18:00): "
                            Leer lectura_titulo
                            
                            crear_funcion(ids_funcion, ids_peli_funcion, horarios_funcion, salas_funcion, cantidad_funciones, lectura_id_funcion, lectura_asiento, lectura_titulo)
                    FinSegun
                Hasta Que sub_opcion = 0
                
            4: // --- VENTA DE BOLETOS ---
                Limpiar Pantalla
                Escribir "ID de funcion: "
                Leer lectura_id_funcion
                Escribir "Numero de asiento: "
                Leer lectura_asiento
                
                vender_boleto(ids_boleto, ids_funcion_boleto, asientos_boleto, cantidad_boletos, lectura_id_funcion, lectura_asiento, cantidad_funciones)
				
            6:
                Escribir "Saliendo del sistema..."
        FinSegun
    Hasta Que opcion = 6
FinAlgoritmo

// --- SUBPROCESOS ---

SubProceso listar_peliculas(arreglo_ids, arreglo_titulos, arreglo_duraciones, arreglo_generos, cantidad_total)
    Limpiar Pantalla
    Escribir "--- CAT�LOGO DE PEL�CULAS ---"
    Si cantidad_total = 0 Entonces
        Escribir "No hay pel�culas registradas actualmente."
    Sino
        Escribir "ID | T�TULO | DURACI�N | G�NERO"
        Escribir "--------------------------------"
        Para indice <- 1 Hasta cantidad_total Hacer
            Escribir arreglo_ids[indice], " - ", arreglo_titulos[indice], " (", arreglo_duraciones[indice], " min) [", arreglo_generos[indice], "]"
        FinPara
    FinSi
    Escribir "--------------------------------"
    Escribir "Presione una tecla para volver..."
    Esperar Tecla
FinSubProceso

SubProceso crear_pelicula(arreglo_ids, arreglo_titulos, arreglo_duraciones, arreglo_generos, contador_actual Por Referencia, nuevo_titulo, nueva_duracion, nuevo_genero)
    Si contador_actual < 10 Entonces
        contador_actual <- contador_actual + 1
        arreglo_ids[contador_actual] <- contador_actual
        arreglo_titulos[contador_actual] <- nuevo_titulo
        arreglo_duraciones[contador_actual] <- nueva_duracion
        arreglo_generos[contador_actual] <- nuevo_genero
        Escribir "Pel�cula creada con ID: ", contador_actual
    Sino
        Escribir "Error: No hay espacio para m�s pel�culas (L�mite 10)."
    FinSi
    Esperar Tecla

// FUNCIONES

SubProceso listar_funciones(arreglo_ids, arreglo_ids_peli, arreglo_horarios, arreglo_salas, cantidad_total)
    Limpiar Pantalla
    Escribir "--- FUNCIONES PROGRAMADAS ---"
    Si cantidad_total = 0 Entonces
        Escribir "No hay funciones registradas actualmente."
    Sino
        Escribir "ID | PELICULA | SALA | HORARIO"
        Escribir "--------------------------------"
        Para indice <- 1 Hasta cantidad_total Hacer
            Escribir arreglo_ids[indice], " - Peli ID: ", arreglo_ids_peli[indice], " | Sala: ", arreglo_salas[indice], " | ", arreglo_horarios[indice]
        FinPara
    FinSi
    Escribir "--------------------------------"
    Escribir "Presione una tecla para volver..."
    Esperar Tecla
FinSubProceso

SubProceso crear_funcion(arreglo_ids, arreglo_ids_peli, arreglo_horarios, arreglo_salas, contador_actual Por Referencia, id_pelicula, sala, horario)
    Si contador_actual < 20 Entonces
        contador_actual <- contador_actual + 1
        arreglo_ids[contador_actual] <- contador_actual
        arreglo_ids_peli[contador_actual] <- id_pelicula
        arreglo_salas[contador_actual] <- sala
        arreglo_horarios[contador_actual] <- horario
        Escribir "Funcion creada con ID: ", contador_actual
    Sino
        Escribir "Error: No hay espacio para mas funciones (Limite 20)."
    FinSi
    Esperar Tecla
FinSubProceso

// BOLETOS
SubProceso vender_boleto(arreglo_ids, arreglo_ids_funcion, arreglo_asientos, contador_actual Por Referencia, id_funcion, asiento, total_funciones)
    // Validar que la funcion existe
    Definir funcion_valida Como Logico
    funcion_valida <- Falso
    
    Para i <- 1 Hasta total_funciones Hacer
        Si id_funcion = i Entonces
            funcion_valida <- Verdadero
        FinSi
    FinPara
    
    Si funcion_valida = Falso Entonces
        Escribir "Error: La funcion con ID ", id_funcion, " no existe."
        Esperar Tecla
        Retornar
    FinSi
    
    // Validar que el asiento no este ya vendido en esa funcion
    Definir asiento_ocupado Como Logico
    asiento_ocupado <- Falso
    
    Para j <- 1 Hasta contador_actual Hacer
        Si arreglo_ids_funcion[j] = id_funcion Y arreglo_asientos[j] = asiento Entonces
            asiento_ocupado <- Verdadero
        FinSi
    FinPara
    
    Si asiento_ocupado Entonces
        Escribir "Error: El asiento ", asiento, " ya esta vendido para esta funcion."
    Sino
        Si contador_actual < 100 Entonces
            contador_actual <- contador_actual + 1
            arreglo_ids[contador_actual] <- contador_actual
            arreglo_ids_funcion[contador_actual] <- id_funcion
            arreglo_asientos[contador_actual] <- asiento
            Escribir "=== BOLETO VENDIDO ==="
            Escribir "Boleto ID : ", contador_actual
            Escribir "Funcion ID: ", id_funcion
            Escribir "Asiento   : ", asiento
            Escribir "======================"
        Sino
            Escribir "Error: No hay espacio para mas boletos (Limite 100)."
        FinSi
    FinSi
    Esperar Tecla

FinSubProceso

