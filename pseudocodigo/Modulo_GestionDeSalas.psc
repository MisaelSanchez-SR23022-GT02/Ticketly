// ALGORITMO PRINCIPAL
// =====================================
Algoritmo GestionDeSalas
    
    Definir contadorSalas, opcion Como Entero
    
    Dimension salaId[10]
    Dimension capacidad[10]
    Dimension disponibles[10]
    Dimension asientos[10,50]
    
    contadorSalas <- 0
    
    Repetir
        
        Escribir "===== GESTION DE SALAS ====="
        Escribir "1. Crear Sala"
        Escribir "2. Mostrar Salas"
        Escribir "3. Ver Asientos"
        Escribir "4. Ocupar Asiento"
        Escribir "5. Salir"
        Leer opcion
        
        Segun opcion Hacer
            
            1:
                CrearSala(salaId, capacidad, disponibles, asientos, contadorSalas)
                
            2:
                MostrarSalas(salaId, capacidad, disponibles, contadorSalas)
                
            3:
                VerAsientos(salaId, capacidad, asientos, contadorSalas)
                
            4:
                OcuparAsiento(salaId, capacidad, disponibles, asientos, contadorSalas)
                
        FinSegun
        
    Hasta Que opcion = 5
    
FinAlgoritmo



	// SUBPROCESOS
	// =====================================
	
	// CREAR SALA
SubProceso CrearSala(salaId Por Referencia, capacidad Por Referencia, disponibles Por Referencia, asientos Por Referencia, contadorSalas Por Referencia)
    
    Definir j Como Entero

    
    Si contadorSalas < 10 Entonces
        
        contadorSalas <- contadorSalas + 1
        
        Escribir "Ingrese ID de la sala:"
        Leer salaId[contadorSalas]
        
        Escribir "Ingrese capacidad (max 50):"
        Leer capacidad[contadorSalas]
        
        Si capacidad[contadorSalas] > 50 Entonces
            capacidad[contadorSalas] <- 50
        FinSi
        
        disponibles[contadorSalas] <- capacidad[contadorSalas]
        
        Para j <- 1 Hasta capacidad[contadorSalas] Hacer
            asientos[contadorSalas, j] <- 0
        FinPara
        
        Escribir "Sala creada correctamente"
        
    SiNo
        Escribir "Limite de salas alcanzado"
    FinSi
    
FinSubProceso


// MOSTRAR SALAS
SubProceso MostrarSalas(salaId, capacidad, disponibles, contadorSalas)
    
    Definir i Como Entero
    
    Si contadorSalas = 0 Entonces
        Escribir "No hay salas registradas"
    SiNo
        
        Para i <- 1 Hasta contadorSalas Hacer
            
            // Validar que la sala exista realmente
            Si capacidad[i] > 0 Entonces
                
                Escribir "Sala ID: ", salaId[i]
                Escribir "Capacidad: ", capacidad[i]
                Escribir "Disponibles: ", disponibles[i]
                Escribir "----------------------"
                
            FinSi
            
        FinPara
        
    FinSi
    
FinSubProceso


// VER ASIENTOS
SubProceso VerAsientos(salaId, capacidad, asientos, contadorSalas)
    
    Definir i, j, idBuscado Como Entero
    Definir encontrado Como Logico
    
    encontrado <- Falso
    
    Escribir "Ingrese ID de la sala:"
    Leer idBuscado
    
    i <- 1
    
    Mientras i <= contadorSalas Y encontrado = Falso Hacer
        
        Si salaId[i] = idBuscado Entonces
            
            encontrado <- Verdadero
            
            Escribir "Asientos (0=Libre, 1=Ocupado):"
            
            Para j <- 1 Hasta capacidad[i] Hacer
                Escribir Sin Saltar asientos[i, j], " "
            FinPara
            
            Escribir ""
            
        FinSi
        
        i <- i + 1
        
    FinMientras
    
    Si encontrado = Falso Entonces
        Escribir "Sala no encontrada"
    FinSi
    
FinSubProceso


// OCUPAR ASIENTO
SubProceso OcuparAsiento(salaId, capacidad, disponibles Por Referencia, asientos Por Referencia, contadorSalas)
    
    Definir i, idBuscado, numeroAsiento Como Entero
    Definir encontrado Como Logico
    
    encontrado <- Falso
    
    Escribir "Ingrese ID de la sala:"
    Leer idBuscado
    
    i <- 1
    
    Mientras i <= contadorSalas Y encontrado = Falso Hacer
        
        Si salaId[i] = idBuscado Entonces
            
            encontrado <- Verdadero
            
            Escribir "Ingrese numero de asiento:"
            Leer numeroAsiento
            
            Si numeroAsiento >= 1 Y numeroAsiento <= capacidad[i] Entonces
                
                Si asientos[i, numeroAsiento] = 0 Entonces
                    asientos[i, numeroAsiento] <- 1
                    disponibles[i] <- disponibles[i] - 1
                    Escribir "Asiento reservado"
                SiNo
                    Escribir "Asiento ocupado"
                FinSi
                
            SiNo
                Escribir "Asiento invalido"
            FinSi
            
        FinSi
        
        i <- i + 1
        
    FinMientras
    
    Si encontrado = Falso Entonces
        Escribir "Sala no encontrada"
    FinSi
    
FinSubProceso
    





