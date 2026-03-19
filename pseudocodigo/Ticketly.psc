//PROCESO PRINCIPAL AUTENTICACION
Proceso Autenticacion
	Definir opcion_deseada Como Entero
	Definir nombres_guardados, contrasenias_guardadas Como Cadena
	Definir cantidad_usuarios Como Entero
	
	Dimension nombres_guardados[10]
	Dimension contrasenias_guardadas[10]
	
	cantidad_usuarios <- 1
	nombres_guardados[1] <- 'Admin'
	contrasenias_guardadas[1] <- '1234'
	Repetir
		Escribir '==Bienvenido=='
		Escribir 'Selecciona la opcion deseada'
		Escribir '1.Iniciar Sesion'
		Escribir '2.Crear Usuario'
		Escribir '0. Salir'
		Leer opcion_deseada
		
		Segun opcion_deseada Hacer 
			1:
				InicioSesion(nombres_guardados, contrasenias_guardadas, cantidad_usuarios)
			2:
				CrearCuenta(nombres_guardados, contrasenias_guardadas, cantidad_usuarios)
		FinSegun
	Hasta Que opcion_deseada = 0
FinProceso

//MODULO PARA INICIAR SESION
SubAlgoritmo InicioSesion(nombres_guardados, contrasenias_guardadas, cantidad_usuarios)
	
	Borrar Pantalla
	Definir verificar_login Como Logico
	Definir nombre_usuario_ingresado, contrasenia_ingresada Como Cadena
	
	verificar_login <- Falso
	
	Escribir 'Ingrese el nombre de usuario'
	Leer nombre_usuario_ingresado
	Escribir 'Ingrese la contraseña'
	Leer contrasenia_ingresada
	
	verificar_login <- Login(nombres_guardados, contrasenias_guardadas, cantidad_usuarios, nombre_usuario_ingresado, contrasenia_ingresada)
	
	Escribir '-----------------------------------------------'
	Si verificar_login == Verdadero Entonces
		MenuPrincipal()
	SiNo
		Escribir 'Error: Acceso denegado, usuario o contraseña incorrectos!'
	FinSi
	Escribir '-----------------------------------------------'
	Escribir 'Presione enter para volver al menu principal...'
	Esperar Tecla
	Borrar Pantalla
FinSubAlgoritmo

//MODULO PARA CREAR UN NUEVO USUARIO
SubAlgoritmo CrearCuenta(nombres_guardados Por Referencia, contrasenias_guardadas Por Referencia, cantidad_usuarios Por Referencia)
	Borrar Pantalla
	
	Si cantidad_usuarios >= 10 Entonces
		Escribir 'No se pueden registrar mas usuarios (limite alcanzado)'
	SiNo
		Definir nuevo_nombre, nueva_contrasenia Como Cadena
		
		Escribir 'Ingrese el nombre de usuario'
		Leer nuevo_nombre
		Escribir 'Ingrese la contraseña'
		Leer nueva_contrasenia
		
		cantidad_usuarios <- cantidad_usuarios + 1
		nombres_guardados[cantidad_usuarios] <- nuevo_nombre
		contrasenias_guardadas[cantidad_usuarios] <- nueva_contrasenia
		
		Escribir '-----------------------------------------------'
		Escribir '¡Usuario creado exitosamente! Puedes iniciar sesion'
		Escribir '-----------------------------------------------'
	FinSi
	
	Escribir 'Presione enter para volver al menu principal...'
	Esperar Tecla
	Borrar Pantalla
FinSubAlgoritmo

//FUNCION PARA COMPARAR USUARIOS
Funcion resultado <- Login(nombres_guardados, contrasenias_guardadas, cantidad_usuarios, nombre_usuario_ingresado, contrasenia_ingresada)
	Definir i Como Entero
	resultado <- Falso
	Para i <- 1 Hasta cantidad_usuarios Hacer
		Si nombre_usuario_ingresado == nombres_guardados[i] Y contrasenia_ingresada == contrasenias_guardadas[i] Entonces
			resultado <- Verdadero
		FinSi
	FinPara
FinFuncion

//MENU PRINCIPAL
SubAlgoritmo MenuPrincipal
	Definir opcion_deseada Como Entero
	Limpiar Pantalla
	Repetir
		Escribir 'Seleccione la opcion deseada'
		Escribir '1.Tickets'
		Escribir '2.Funciones'
		Escribir '3.Peliculas'
		Escribir '4.Gestión de Asientos'
		Escribir '0.Salir'
		Leer opcion_deseada
		
		Segun opcion_deseada Hacer
			1:
				//ComprarTicket()
		FinSegun
	Hasta Que opcion_deseada = 0
FinSubAlgoritmo