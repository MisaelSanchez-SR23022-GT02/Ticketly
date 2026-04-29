from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print

console = Console()

def ejecutar_eliminar(service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")
    
    print(Panel.fit("Eliminar pelicula, [bold red]Ingrese los datos que se solicitan![/]"))
    
    while True:
        id_p = Prompt.ask("[bold blue]ID de la película a eliminar: [/]")
        
        if not id_p.isdigit():
            console.print("[bold red] El ID debe ser un número entero, inténtalo de nuevo.[/]")
            continue 
        
        id_p = int(id_p)
        eliminada = service.eliminar_pelicula(id_p)
        
        if eliminada:
            console.print("-" * 55, style="bright_black")
            console.print(f"[bold green]Película [bold red]{eliminada.get_nombre()}[/] eliminada con éxito.[/]")
            console.print("-" * 55, style="bright_black")
        else:
            console.print("-" * 55, style="bright_black")
            console.print(f"[bold yellow]Película con ID [bold red]{id_p}[/] no encontrada.[/]")
            console.print("-" * 55, style="bright_black")
            continue

        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
        break