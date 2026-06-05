from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.table import Table

console = Console()

def ejecutar_listar(service):
    peliculas = service.listar_peliculas()

    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")
    
    if not peliculas:
        console.print("-" * 55, style="bright_black")
        console.print(f"[bold red][!][/] [bold yellow]No hay películas registradas...[/]")
        console.print("-" * 55, style="bright_black")
        return
    
    tabla = Table(title="Lista de peliculas")

    tabla.add_column("ID",  style="cyan", no_wrap=True)
    tabla.add_column("Nombre", style="magenta")
    tabla.add_column("Categoria", style="bright_cyan")
    tabla.add_column("Duracion",  style="green")

    for p in peliculas:
        tabla.add_row(str(p.get_id()),
                       p.get_nombre(),
                       p.get_categoria(), 
                       p.get_duracion())
    
    console.print(tabla)