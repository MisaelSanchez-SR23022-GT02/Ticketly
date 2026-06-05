# Ticketly: Sistema de Gestión de Cine

Ticketly es una aplicación diseñada para automatizar la reserva y venta de boletos cinematográficos, garantizando una experiencia de usuario fluida y un control administrativo riguroso sobre el aforo de las salas.

## 1. Estructura del Proyecto

El sistema está organizado bajo un esquema de Separación de Responsabilidades, lo que permite un mantenimiento sencillo y escalabilidad:

```
TICKETLY/
├── app/
│   ├── models/                     # Definición de entidades de datos
│   │   ├── pelicula.py             # Clase modelo para películas
│   │   └── sala.py                 # Clase modelo para salas
│   ├── services/                   # Lógica de negocio y servicios
│   │   ├── pelicula_service.py 
│   │   └── sala_service.py
│   ├── ui/                         # Capa de interfaz de usuario
│   │   ├── peliculas_ui/           # Gestión específica de vistas de películas
│   │   │   ├── crear_ui.py
│   │   │   ├── eliminar_ui.py
│   │   │   ├── listar_ui.py
│   │   │   └── menu_pelicula.py
│   │   ├── salas_ui/               # Gestión específica de vistas de salas
│   │   │   ├── crear_sala_ui.py
│   │   │   ├── listar_sala_ui.py
│   │   │   ├── ver_asientos_ui.py
│   │   │   └── menu_sala.py
│   │   └── menu_principal_ui.py
│   └── utils/                      # Funciones auxiliares y herramientas
│       ├── limpiar_utils.py
│       └── logo_utils.py
├── docs/                           # Documentación técnica
│   └── pseudocodigo/
│       └── Ticketly.psc
├── tests/                          # Pruebas unitarias del sistema
├── .gitignore                      # Archivos ignorados por Git
├── main.py                         # Punto de entrada de la aplicación
└── README.md                       # Documentación principal
```

<<<<<<< HEAD
- `app/models/`: Contiene las clases que representan los datos del sistema, como `pelicula.py`, asegurando que la estructura de la información esté centralizada..
=======
>>>>>>> main
- `app/services/` (Capa de Lógica de Negocio): Es el núcleo del sistema. Aquí reside la lógica para:
  - Verificar la disponibilidad de horarios.
  - Validar que un asiento específico no esté ocupado antes de confirmar la venta.
  - Actualizar el contador de asientos disponibles en tiempo real.
<<<<<<< HEAD
- `app/ui/`: Gestiona la interacción con el usuario mediante menús en consola. Esta capa utiliza la librería **[Rich](https://rich.readthedocs.io/en/stable/)** para mejorar la interfaz gráfica, permitiendo el uso de colores, tablas y estilos avanzados que facilitan la lectura de datos y la navegación por los menús.
- `app/utils/`: Incluye herramientas reutilizables, como el manejo de limpieza de pantalla (`limpiar_utils.py`) y la visualización de elementos gráficos de identidad (`logo_utils.py`).
- `docs/pseudocodigo/`: Contiene la lógica algorítmica inicial (`Ticketly.psc`), sirviendo como plano técnico antes de la implementación final.
- `main.py`: El archivo principal que orquesta el inicio de la aplicación y el despliegue del menú inicial.
=======
- `app/ui/`: Gestiona la interacción con el usuario, mediante menús en consola, capturando los datos necesarios para las transacciones.
- `docs/pseudocodigo/`: Contiene la lógica algorítmica inicial (`Ticketly.psc`), sirviendo como plano técnico antes de la implementación final.
>>>>>>> main

## Autores

- Bryan Misael Sánchez Ramírez - [@MisaelSanchez-SR23022-GT02](https://github.com/MisaelSanchez-SR23022-GT02)
- Audiel Isaac Terán Morales - [@Audiel007](https://github.com/Audiel007)
- Abner Gabriel Ruiz Martínez - [@rm20102](https://github.com/rm20102)
- Carlos Fernando Rivas Morán - [@FerRvs](https://github.com/FerRvs)
