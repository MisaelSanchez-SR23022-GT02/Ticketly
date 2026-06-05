from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

console = Console()

def ejecutar_actualizar(service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    print(Panel.fit("Actualizar Película, [bold blue]Modifique los datos necesarios![/]"))

    id_actualizar = Prompt.ask("[bold blue]Ingresa el ID de la película que deseas actualizar: [/]")
    pelicula = service.buscar_por_id(id_actualizar)

    if not pelicula:
        console.print(f"[bold red]\nNo se encontró ninguna película con el ID {id_actualizar}.[/]")
        console.print("[bold red]Presione Enter para continuar...[/]")
        input()
        return

    console.print(f"\n[bold yellow]Modificando la película:[/] {pelicula.get_nombre()}\n")

    while True:
        nom = Prompt.ask("[bold blue]Nuevo título[/]", default=pelicula.get_nombre())
        if nom.strip():
            break
        console.print("[bold red] El título no puede estar vacío.[/]")

    while True:
        dur = Prompt.ask("[bold blue]Nueva duración[/]", default=pelicula.get_duracion())
        if dur.strip():
            break
        console.print("[bold red] La duración es obligatoria.[/]")

    while True:
        cat = Prompt.ask("[bold blue]Nueva categoría[/]", default=pelicula.get_categoria())
        if cat.strip():
            break
        console.print("[bold red] Debes ingresar una categoría.[/]")

    service.actualizar_pelicula(id_actualizar, nom, dur, cat)

    console.print("-" * 55, style="bright_black")
    console.print(f"[bold green]Película con ID [bold blue]{id_actualizar}[/] actualizada con éxito.[/]")
    console.print("-" * 55, style="bright_black")

    console.print("[bold red]\nPresione Enter para continuar...[/]")
    input()