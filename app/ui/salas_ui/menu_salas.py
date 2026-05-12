from app.services.sala_service import SalaService
from app.ui.salas_ui.crear_sala_ui import ejecutar_crear_sala
from app.ui.salas_ui.listar_salas_ui import ejecutar_listar
from app.ui.salas_ui.ver_asientos_ui import ejecutar_ver_asientos
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel


console = Console()

def mostrar_menu_salas(service):

    service = SalaService()

    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")

        menu_texto = (
            "[bold cyan]1.[/] Agregar Salas\n"
            "[bold cyan]2.[/] Mostrar Salas\n"
            "[bold cyan]3.[/] Mostrar Asientos\n"
            "[bold cyan]0.[/] Salir"
        )

        console.print(Panel(menu_texto, title="[bold white]MODULO DE SALAS[/]", expand=False))
        
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "0"])

        if opcion == "1":
            ejecutar_crear_sala(service)
        elif opcion == "2":
            ejecutar_listar(service)
            console.print("[bold red]\nPresione Enter para continuar...[/]")
            input()
        elif opcion == "3":
            ejecutar_ver_asientos(service)
        elif opcion == "0":
            break
        else:
            print(" Opcion no valida ")