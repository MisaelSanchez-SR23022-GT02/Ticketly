from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from app.ui.boletos_ui.ticket import imprimir_ticket
from app.utils.asientos_utils import mostrar_asientos_rapido

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import print

console = Console()

def ejecutar_vender(boleto_service, funcion_service, sala_service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    funciones = funcion_service.listar_funciones()
    if not funciones:
        console.print("-" * 55, style="bright_black")
        console.print("[bold red][!][/] [bold yellow]No hay funciones registradas. Agregue una función primero.[/]")
        console.print("-" * 55, style="bright_black")
        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
        return

    tabla_funciones = Table(title="Funciones Disponibles")
    tabla_funciones.add_column("ID", style="cyan", no_wrap=True)
    tabla_funciones.add_column("ID Película", style="magenta")
    tabla_funciones.add_column("ID Sala", style="green")
    tabla_funciones.add_column("Hora", style="yellow")
    tabla_funciones.add_column("Asientos Libres", style="bright_green")

    for f in funciones:
        sala = sala_service.buscar_por_id(f.get_id_sala())
        libres = str(sala.get_disponibles()) if sala else "N/A"
        tabla_funciones.add_row(
            str(f.get_id()),
            str(f.get_id_pelicula()),
            str(f.get_id_sala()),
            f.get_hora_funcion(),
            libres
        )

    console.print(tabla_funciones)

    print(Panel.fit("Venta de boleto, [bold blue]Ingrese los datos que se solicitan![/]"))

    while True:
        id_funcion = Prompt.ask("[bold blue]Ingresa el ID de la función: [/]")
        if not id_funcion.isdigit():
            console.print("[bold red] El ID debe ser un número entero.[/]")
            continue

        funcion = next(
            (f for f in funciones if f.get_id() == int(id_funcion)),
            None
        )
        if not funcion:
            console.print(f"[bold red] No existe una función con ID {id_funcion}. Inténtalo de nuevo.[/]")
            continue
        break


    sala = sala_service.buscar_por_id(funcion.get_id_sala())

    if sala:
        console.print()
        mostrar_asientos_rapido(sala)
        console.print(
            f"[bold white]Sala {sala.get_id()}[/] — "
            f"Capacidad: [bold cyan]{sala.get_capacidad()}[/]  |  "
            f"Disponibles: [bold green]{sala.get_disponibles()}[/]  |  "
            f"Ocupados: [bold red]{sala.get_capacidad() - sala.get_disponibles()}[/]"
        )
        console.print()

    while True:
        num_asiento = Prompt.ask("[bold blue]Ingresa el número de asiento: [/]")
        if not num_asiento.isdigit():
            console.print("[bold red] El número de asiento debe ser un entero.[/]")
            continue
        break

    resultado = boleto_service.vender_boleto(id_funcion, num_asiento)

    console.print()
    console.print("-" * 55, style="bright_black")

    if resultado == "ERROR_FUNCION":
        console.print("[bold red][!][/] [bold yellow]Error: La función especificada no existe.[/]")
    elif resultado == "ERROR_SALA":
        console.print("[bold red][!][/] [bold yellow]Error: La sala asociada a la función no existe.[/]")
    elif resultado == "ERROR_RANGO":
        console.print(
            f"[bold red][!][/] [bold yellow]Error: El asiento [bold red]{num_asiento}[/] "
            f"no existe en esta sala (capacidad: {sala.get_capacidad()}).[/]"
        )
    elif resultado == "ERROR_OCUPADO":
        console.print(
            f"[bold red][!][/] [bold yellow]Error: El asiento [bold red]{num_asiento}[/] "
            f"ya está ocupado.[/]"
        )
    else:
       limpiar_pantalla()
       console.print(getLogo(), style="bold blue")
       imprimir_ticket(resultado) 
        
    console.print("[bold red]\nPresione Enter para continuar...[/]")
    input()
