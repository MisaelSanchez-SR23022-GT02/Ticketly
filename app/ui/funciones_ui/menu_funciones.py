from app.ui.funciones_ui.crear_funcion_ui import ejecutar_crear
from app.ui.funciones_ui.listar_funcion_ui import ejecutar_listar
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def mostrar_menu_funcion(service):

    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")

        menu_texto = (
            "[bold cyan]1.[/] Agregar Funcion\n"
            "[bold cyan]2.[/] Mostrar Funcion\n"
            "[bold cyan]0.[/] Salir"
        )

        console.print(Panel(menu_texto, title="[bold white]MODULO DE FUNCIONES[/]", expand=False))
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "0"])

        if opcion == "1":
            ejecutar_crear(service)
        elif opcion == "2":
            ejecutar_listar(service)
            console.print("[bold red]\nPresione Enter para continuar...[/]")
            input()
        elif opcion == "0":
            break
        else:
            print(" Opcion no valida ")