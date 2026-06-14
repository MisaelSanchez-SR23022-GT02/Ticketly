# Ticketly: Sistema de Gestión de Cine

Ticketly es una aplicación diseñada para automatizar la reserva y venta de boletos cinematográficos, garantizando una experiencia de usuario fluida y un control administrativo riguroso sobre el aforo de las salas.

## 1. Estructura del Proyecto

El sistema está organizado bajo un esquema de Separación de Responsabilidades, lo que permite un mantenimiento sencillo y escalabilidad:

```
ticketly/
│
├── app/                  # Código fuente principal de la aplicación
│   ├── models/           # Modelos de datos
│   ├── services/         # Lógica de aplicación
│   ├── ui/               # Interfaz de usuario
│   └── utils/            # Utilidades y funciones auxiliares
│
├── tests/                              # Pruebas unitarias del sistema
│   ├── conftest.py                     # Fixtures y configuración compartida de pytest
│   ├── test_boleto_service.py          # Tests del servicio de venta de boletos
│   ├── test_pelicula_service.py        # Tests unitarios del servicio de películas
│   └── test_peliculas_services.py      # Tests adicionales del servicio de películas
├── docs/                 # Documentación del proyecto
│   └── pseudocodigo/     # Documentos con pseudocódigo
│       └── Ticketly.psc  # Archivo de pseudocódigo principal
│
├── tests/                # Pruebas unitarias
│
├── .gitignore           # Archivos y directorios ignorados por Git
│
└── README.md             # Documentación principal del repositorio
```

- `app/models/`: Contiene la definición de las entidades principales. Aquí se gestionan los objetos como `Pelicula` entre otros.
- `app/services/` (Capa de Lógica de Negocio): Es el núcleo del sistema. Aquí reside la lógica para:
  - Verificar la disponibilidad de horarios.
  - Validar que un asiento específico no esté ocupado antes de confirmar la venta.
  - Actualizar el contador de asientos disponibles en tiempo real.
- `app/ui/`: Gestiona la interacción con el usuario, mediante menús en consola, capturando los datos necesarios para las transacciones.
- `docs/pseudocodigo/`: Contiene la lógica algorítmica inicial (`Ticketly.psc`), sirviendo como plano técnico antes de la implementación final.

## Autores

- Bryan Misael Sánchez Ramírez - [@MisaelSanchez-SR23022-GT02](https://github.com/MisaelSanchez-SR23022-GT02)
- Audiel Isaac Terán Morales - [@Audiel007](https://github.com/Audiel007)
- Abner Gabriel Ruiz Martínez - [@rm20102](https://github.com/rm20102)
- Carlos Fernando Rivas Morán - [@FerRvs](https://github.com/FerRvs)
