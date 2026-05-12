from app.ui.peliculas_ui.menu_pelicula import mostrar_menu_peliculas
from app.services.pelicula_service import PeliculaService
from app.ui.salas_ui.menu_salas import mostrar_menu_salas
from app.utils.limpiar_utils import limpiar_pantalla
from app.services.sala_service import SalaService
from app.utils.logo_utils import getLogo
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def mostrar_menu():
    pelicula_service = PeliculaService()
    salas_service = SalaService()
    
    while True:
        limpiar_pantalla()
        console.print(getLogo(), style="bold blue")
        
        menu_texto = (
            "[bold cyan]1.[/] Gestión de Peliculas\n"
            "[bold cyan]2.[/] Gestión de Salas\n"
            "[bold cyan]3.[/] Salir"
        )
        
        console.print(Panel(menu_texto, title="[bold white]MENÚ PRINCIPAL[/]", expand=False))
        
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

        if opcion == "1":
             mostrar_menu_peliculas(pelicula_service)
        if opcion == "2":
             mostrar_menu_salas(salas_service)
        elif opcion == "3":
            console.print("[bold red]Saliendo del sistema...[/]")
            break