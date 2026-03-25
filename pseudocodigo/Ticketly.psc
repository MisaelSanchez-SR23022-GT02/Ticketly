Algoritmo Ticketly
    Definir opcion, sub_opcion Como Entero
    
    // Arreglos para PELÍCULAS
    Definir cantidad_peliculas Como Entero
    Dimension ids_peli[10], duraciones_peli[10]
    Dimension titulos_peli[10], generos_peli[10]
    cantidad_peliculas <- 0
    
    // Variables temporales para lecturas
    Definir lectura_titulo, lectura_genero Como Caracter
    Definir lectura_duracion, lectura_id_funcion, lectura_asiento Como Entero
    
    Repetir
        Limpiar Pantalla
        Escribir "=================================="
        Escribir "    SISTEMA DE BOLETERÍA DE CINE"
        Escribir "=================================="
        Escribir "1. Gestionar Películas"
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
                    Escribir "--- GESTIÓN DE PELÍCULAS ---"
                    Escribir "1. Listar películas"
                    Escribir "2. Agregar película"
                    Escribir "0. Volver"
                    Leer sub_opcion
                    
                    Segun sub_opcion Hacer
                        1: 
                            listar_peliculas(ids_peli, titulos_peli, duraciones_peli, generos_peli, cantidad_peliculas)
                        2: 
                            Limpiar Pantalla
                            Escribir "Título: "
                            Leer lectura_titulo
                            Escribir "Duración (min): "
                            Leer lectura_duracion
                            Escribir "Género: "
                            Leer lectura_genero
                            
                            crear_pelicula(ids_peli, titulos_peli, duraciones_peli, generos_peli, cantidad_peliculas, lectura_titulo, lectura_duracion, lectura_genero)
                    FinSegun
                Hasta Que sub_opcion = 0
                
			2: // --- GESTIÓN DE SALAS ---
                Escribir "Modulo de Salas"
                Esperar Tecla
                
            3: // --- GESTIÓN DE FUNCIONES ---
                Escribir "Modulo de Funciones"
                Esperar Tecla
                
            4: // --- VENTA DE BOLETOS ---
                Escribir "=== VENTA DE BOLETOS ==="
				
            6:
                Escribir "Saliendo del sistema..."
        FinSegun
    Hasta Que opcion = 6
FinAlgoritmo

// --- SUBPROCESOS ---

SubProceso listar_peliculas(arreglo_ids, arreglo_titulos, arreglo_duraciones, arreglo_generos, cantidad_total)
    Limpiar Pantalla
    Escribir "--- CATÁLOGO DE PELÍCULAS ---"
    Si cantidad_total = 0 Entonces
        Escribir "No hay películas registradas actualmente."
    Sino
        Escribir "ID | TÍTULO | DURACIÓN | GÉNERO"
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
        Escribir "Película creada con ID: ", contador_actual
    Sino
        Escribir "Error: No hay espacio para más películas (Límite 10)."
    FinSi
    Esperar Tecla
FinSubProceso