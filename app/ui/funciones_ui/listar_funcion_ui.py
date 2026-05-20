from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.table import Table

console = Console()

def ejecutar_listar(service):
    funciones = service.listar_funciones()

    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    if not funciones:
        console.print("-" * 55, style="bright_black")
        console.print(f"[bold red][!][/] [bold yellow]No hay funciones registradas...[/]")
        console.print("-" * 55, style="bright_black")
        return
    
    tabla = Table(title="Lista de funciones")

    tabla.add_column("ID",  style="cyan", no_wrap=True)
    tabla.add_column("ID_PELICULA", style="magenta")
    tabla.add_column("ID_SALA",  style="green")
    tabla.add_column("HORA",  style="green")

    for f in funciones:
        tabla.add_row(str(f.get_id()), str(f.get_id_pelicula()), str(f.get_id_sala()), f.get_hora_funcion())
    
    console.print(tabla)