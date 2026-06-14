from app.ui.boletos_ui.vender_boleto_ui import ejecutar_vender
from app.ui.boletos_ui.listar_boleto_ui import ejecutar_listar
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def mostrar_menu_boletos(boleto_service, funcion_service, sala_service):

    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")

        menu_texto = (
            "[bold cyan]1.[/] Vender Boleto\n"
            "[bold cyan]2.[/] Mostrar Boletos Vendidos\n"
            "[bold cyan]0.[/] Salir"
        )

        console.print(Panel(menu_texto, title="[bold white]MODULO DE BOLETOS[/]", expand=False))
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "0"])

        if opcion == "1":
            ejecutar_vender(boleto_service, funcion_service, sala_service)
        elif opcion == "2":
            ejecutar_listar(boleto_service)
            console.print("[bold red]\nPresione Enter para continuar...[/]")
            input()
        elif opcion == "0":
            break
