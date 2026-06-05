from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.table import Table

console = Console()

def ejecutar_listar(service):
    boletos = service.listar_boletos()

    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    if not boletos:
        console.print("-" * 55, style="bright_black")
        console.print("[bold red][!][/] [bold yellow]No hay boletos vendidos aún...[/]")
        console.print("-" * 55, style="bright_black")
        return

    tabla = Table(title="Boletos Vendidos")

    tabla.add_column("ID Boleto", style="cyan", no_wrap=True)
    tabla.add_column("ID Función", style="magenta")
    tabla.add_column("ID Sala", style="green")
    tabla.add_column("Asiento", style="yellow")

    for b in boletos:
        tabla.add_row(
            str(b.get_id()),
            str(b.get_id_funcion()),
            str(b.get_id_sala()),
            str(b.get_numero_asiento())
        )

    console.print(tabla)
