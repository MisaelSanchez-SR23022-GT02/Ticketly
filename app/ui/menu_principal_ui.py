from app.ui.peliculas_ui.menu_pelicula import mostrar_menu_peliculas
from app.ui.funciones_ui.menu_funciones import mostrar_menu_funcion
from app.ui.boletos_ui.menu_boleto import mostrar_menu_boletos
from app.ui.salas_ui.menu_salas import mostrar_menu_salas
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def mostrar_menu(pelicula_service, salas_service, funcion_service, boleto_service):

    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")

        menu_texto = (
            "[bold cyan]1.[/] Gestión de Películas\n"
            "[bold cyan]2.[/] Gestión de Salas\n"
            "[bold cyan]3.[/] Gestión de Funciones\n"
            "[bold cyan]4.[/] Venta de Boletos\n"
            "[bold cyan]5.[/] Salir"
        )

        console.print(Panel(menu_texto, title="[bold white]MENÚ PRINCIPAL[/]", expand=False))

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5"])

        if opcion == "1":
            mostrar_menu_peliculas(pelicula_service)
        elif opcion == "2":
            mostrar_menu_salas(salas_service)
        elif opcion == "3":
            mostrar_menu_funcion(funcion_service)
        elif opcion == "4":
            mostrar_menu_boletos(boleto_service, funcion_service, salas_service)
        elif opcion == "5":
            console.print("[bold red]Saliendo del sistema...[/]")
            break