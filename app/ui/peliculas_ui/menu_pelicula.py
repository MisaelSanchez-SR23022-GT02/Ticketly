from app.ui.peliculas_ui.eliminar_ui import ejecutar_eliminar
from app.ui.peliculas_ui.listar_ui import ejecutar_listar
from app.ui.peliculas_ui.crear_ui import ejecutar_crear
from app.utils.limpiar_utils import limpiar_pantalla
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def mostrar_menu_peliculas(service): 
    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")

        menu_texto = (
            "[bold cyan]1.[/] Agregar Peliculas\n"
            "[bold cyan]2.[/] Mostrar Peliculas\n"
            "[bold cyan]3.[/] Eliminar Peliculas\n"
            "[bold cyan]0.[/] Salir"
        )

        console.print(Panel(menu_texto, title="[bold white]MODULO DE PELICULAS[/]", expand=False))
        
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "0"])

        if opcion == "1":
            ejecutar_crear(service)
        elif opcion == "2": 
            ejecutar_listar(service)
            console.print("[bold red]\nPresione Enter para continuar...[/]")
            input()
        elif opcion == "3": 
            ejecutar_eliminar(service)
        elif opcion == "0": 
            break