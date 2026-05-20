from app.ui.menu_principal_ui import mostrar_menu
from app.services.pelicula_service import PeliculaService
from app.services.sala_service import SalaService
from app.services.funcion_service import FuncionService
from app.ui.menu_principal_ui import mostrar_menu

def main():
    pelicula_service = PeliculaService()
    salas_service = SalaService()
    funcion_service = FuncionService(pelicula_service, salas_service)
    
    mostrar_menu(pelicula_service, salas_service, funcion_service)
    
if __name__ == "__main__":
    main()