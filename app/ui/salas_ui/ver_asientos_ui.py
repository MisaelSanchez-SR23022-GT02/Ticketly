from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def ejecutar_ver_asientos(service):
    limpiar_pantalla()
    console.print(getLogo(), style="bold blue")

    entrada = Prompt.ask("[bold blue] Ingrese ID de la sala: [/]")
    if not entrada.isdigit():
        console.print("[bold red]Error:[/] Ingrese un número válido.")
        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
        return

    sala = service.buscar_sala(int(entrada))
    if sala is None:
        console.print("[bold red]Error:[/] Sala no encontrada.")
        console.print("[bold red]\nPresione Enter para continuar...[/]")
        input()
        return

    asientos = sala.get_asientos()
    cols = 10

    titulo = Text()
    titulo.append("OCUPADOS", style="bold red")
    titulo.append(f"{'SALA ' + str(sala.get_id()):^30}", style="bold blue")
    titulo.append("DISPONIBLES", style="bold green")

    tabla = Table.grid(padding=(0, 1), expand=True)
    for _ in range(cols):
        tabla.add_column(justify="center")

    fila = []
    for i, estado in enumerate(asientos):
        num = str(i + 1)
        color = "red" if estado == 'O' else "green"
        asiento = Panel(
            Text(num, justify="center", style=f"bold {color}"),
            border_style=color,
            width=6,
            height=3,
        )
        fila.append(asiento)
        if len(fila) == cols or i == len(asientos) - 1:
            while len(fila) < cols:
                fila.append(Text(""))
            tabla.add_row(*fila)
            fila = []

    ancho_panel = (cols * 8) + 6
    console.print(
        Panel(tabla, title=titulo, border_style="blue", padding=(1, 2), width=ancho_panel),
        justify="left"
    )