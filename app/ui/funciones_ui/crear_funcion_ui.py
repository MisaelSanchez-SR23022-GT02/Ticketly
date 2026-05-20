from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print


console = Console()

def ejecutar_crear(service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    print(Panel.fit("Nueva función, [bold blue]Ingrese los datos que se solicitan![/]"))

    while True:
        id_sala = Prompt.ask("[bold blue]Ingresa la sala: [/]")
        if id_sala is None:
           console.print("[bold red] El ID ingresado no existe.[/]")
        elif id_sala.isdigit():
            break
        console.print("[bold red] El título no puede estar vacío. Inténtalo de nuevo.[/]")

    while True:
        id_peli = Prompt.ask("[bold blue]Ingresa la pelicula: [/]")
        if id_sala is None:
           console.print("[bold red] El ID ingresado no existe.[/]")
        elif id_peli.isdigit():
            break
        console.print("[bold red] La duración es obligatoria.[/]")

    while True:
        hora = Prompt.ask("[bold blue]Ingresa la hora: [/]")
        if hora.strip():
            break
        console.print("[bold red] Debes ingresar una categoría.[/]")

    resultado = service.crear_funcion(id_peli, id_sala, hora)

    if resultado is None:
        console.print("\n" + "-" * 55, style="bright_black")
        console.print("[bold red][!][/] [bold yellow]Error: No se pudo crear la función.[/]")
        console.print("[white]Asegúrese de que el ID de la película y el ID de la sala existan actualmente.[/]")
        console.print("-" * 55, style="bright_black")

        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
    else:
        console.print("-" * 55, style="bright_black")
        console.print(f"[bold green]Funcion creada exitosamente. [/]")
        console.print("-" * 55, style="bright_black")

        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()