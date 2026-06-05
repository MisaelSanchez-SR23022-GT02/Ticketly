from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import box

console = Console()

def imprimir_ticket(boleto):
    table = Table(show_header=False, box=None, padding=(0, 1))

    table.add_column(style="bold bright_white", justify="left")
    table.add_column(style="bold bright_green", justify="left")

    table.add_row("ID BOLETO :", str(boleto.get_id()))
    table.add_row("FUNCION   :", str(boleto.get_id_funcion()))
    table.add_row("SALA      :", str(boleto.get_id_sala()))
    table.add_row("ASIENTO   :", str(boleto.get_numero_asiento()))

    ticket = Panel(
        table,
        title="[reverse bold bright_green] COMPROBANTE DE COMPRA [/]",
        subtitle="[bold dim]VALIDO PARA UNA ENTRADA[/]",
        border_style="bright_green",
        box=box.HEAVY,
        padding=(1, 3),
        expand=False 
    )
    
    console.print(ticket)