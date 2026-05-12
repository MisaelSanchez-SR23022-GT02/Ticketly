from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

console = Console()

def ejecutar_crear_sala(service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    print(Panel.fit("Nueva sala, [bold blue]Ingrese los datos que se solicitan![/]"))
    
    
    while True: 
        entrada = Prompt.ask("[bold blue] Capacidad de la sala [bold red](max 50)[/][/]")

        if not entrada.isdigit():
            console.print("[bold red] Opción invalida. Debe ingresar un número.[/]")
            continue 

        capacidad = int(entrada)

    # Validaciones
        if capacidad > 50:
            capacidad = 50
            print(f"[bold blue] Capacidad ajustada al maximo: [bold red]{capacidad}[/][/]")

        if capacidad < 1:
            capacidad = 1
            print(f"[bold blue] Capacidad ajustada al minimo: [bold red]{capacidad}[/][/]")

        nueva_sala = service.crear_sala(capacidad)
        console.print("-" * 55, style="bright_black")
        console.print(f"[bold green]Sala creada con ID:[/] [bold red]{nueva_sala.get_id()}[/]")
        console.print("-" * 55, style="bright_black")

        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
        break
