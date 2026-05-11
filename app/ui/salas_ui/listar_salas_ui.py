from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.table import Table

console = Console()

def ejecutar_listar(service):
    salas = service.listar_salas()

    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    if not salas:
        console.print("-" * 55, style="bright_black")
        console.print(f"[bold red][!][/] [bold yellow]No hay salas registradas...[/]")
        console.print("-" * 55, style="bright_black")
        return
    
    tabla = Table(title="Lista de salas")

    tabla.add_column("ID",  style="cyan", no_wrap=True)
    tabla.add_column("Capacidad", style="magenta")
    tabla.add_column("Libres",  style="green")

    for s in salas:
        tabla.add_row(str(s.get_id()), str(s.get_capacidad()), str(s.get_disponibles()))
    
    console.print(tabla)
