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

    print(Panel.fit("Nueva película, [bold blue]Ingrese los datos que se solicitan![/]"))

    while True:
        nom = Prompt.ask("[bold blue]Ingresa el titulo: [/]")
        if nom.strip():
            break
        console.print("[bold red] El título no puede estar vacío. Inténtalo de nuevo.[/]")

    while True:
        dur = Prompt.ask("[bold blue]Ingresa la duración: [/]")
        if dur.strip():
            break
        console.print("[bold red] La duración es obligatoria.[/]")

    while True:
        cat = Prompt.ask("[bold blue]Ingresa la categoria: [/]")
        if cat.strip():
            break
        console.print("[bold red] Debes ingresar una categoría.[/]")

    pelicula_creada = service.crear_pelicula(nom, dur, cat)

    console.print("-" * 55, style="bright_black")
    
    if pelicula_creada is None:
        console.print(f"[bold red]Error: La película [bold yellow]{nom}[/] ya se encuentra registrada en el catálogo.[/]")
    else:
        console.print(f"[bold green]Película [bold red]{nom}[/] creada con éxito.[/]")
        
    console.print("-" * 55, style="bright_black")

    console.print("[bold red]\nPresione Enter para continuar...[/]")
    input()