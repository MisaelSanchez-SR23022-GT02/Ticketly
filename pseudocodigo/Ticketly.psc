
//PROCESO PRINCIPAL AUTENTICACION
Proceso Autenticacion
	Definir opcion_deseada Como Entero
	Definir nombre_usuario_guardado, contrasenia_guardada Como Cadena
	Repetir
		Escribir '==Bienvenido=='
		Escribir 'Selecciona la opcion deseada'
		Escribir '1.Iniciar Sesion'
		Escribir '2.Crear Usuario'
		Escribir '0. Salir'
		Leer opcion_deseada
		
		Segun opcion_deseada Hacer 
			1:
				InicioSesion(nombre_usuario_guardado, contrasenia_guardada )
			2:
				CrearCuenta(nombre_usuario_guardado, contrasenia_guardada )
		FinSegun
	Hasta Que  opcion_deseada = 0
FinProceso

//MODULO PARA INICIAR SESION
SubAlgoritmo InicioSesion(nombre_usuario_guardado, contrasenia_guardada )
	
	Borrar Pantalla
	Definir verificar_login Como Logico
	Definir nombre_usuario_ingresado, contrasenia_ingresada Como Cadena
	Definir administrador, contrasenia Como Caracter
	
	administrador <- 'Admin'
	contrasenia <- '1234'
	verificar_login <- Falso
	
	
	Escribir 'Ingrese el nombre de usuario'
	Leer nombre_usuario_ingresado
	Escribir 'Ingrese la contraseña'
	Leer contrasenia_ingresada
	
	Si nombre_usuario_ingresado == administrador Y contrasenia_ingresada == contrasenia Entonces
		verificar_login <- Verdadero
	SiNo
		verificar_login <- Login(nombre_usuario_guardado, contrasenia_guardada, nombre_usuario_ingresado, contrasenia_ingresada)
	FinSi
	
	
	Escribir '-----------------------------------------------'
	Si verificar_login == Verdadero  Entonces
		MenuPrincipal()
	SiNo
		Escribir 'Error: Acceso denegado, usuario o contraseña incorrectos, vuelva a intentarlo!'
	FinSi
	Escribir '-----------------------------------------------'
	Escribir 'Presione enter para volver al menu principal...'
	Esperar Tecla
	Borrar Pantalla
FinSubAlgoritmo


//MODULO PARA CREAR UN NUEVO USUARIO
SubAlgoritmo CrearCuenta (nombre_usuario_guardado Por Referencia, contrasenia_guardada Por Referencia)
	Borrar Pantalla
	Escribir 'Ingrese el nombre de usuario'
	Leer nombre_usuario_guardado
	Escribir 'Ingrese la contrasea'
	Leer contrasenia_guardada
	Escribir '-----------------------------------------------'
	Escribir '¡Usuario creado exitosamente! Puedes iniciar sesion'
	Escribir '-----------------------------------------------'
	Escribir 'Presione enter para volver al menu principal...'
	Esperar Tecla
	Borrar Pantalla
FinSubAlgoritmo


//FUNCION PARA COMPARAR USUARIOS
Funcion resultado <- Login(nombre_usuario_guardado, contrasenia_guardada, nombre_usuario_ingresado, contrasenia_ingresada)
	Si nombre_usuario_ingresado == nombre_usuario_guardado Y contrasenia_ingresada == contrasenia_guardada Entonces
		resultado <- Verdadero
	Sino 
		resultado <- Falso
	Finsi
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
		
		segun opcion_deseada Hacer
			1:
				//ComprarTicket()
		FinSegun
	Hasta Que opcion_deseada = 0
FinSubAlgoritmo


