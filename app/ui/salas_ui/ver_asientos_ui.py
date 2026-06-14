from app.utils.asientos_utils import mostrar_asientos_rapido 
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt

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

    mostrar_asientos_rapido(sala)