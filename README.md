# Ticketly: Sistema de Gestión de Cine

Ticketly es una aplicación de consola diseñada para automatizar la reserva y venta de boletos cinematográficos, garantizando una experiencia de usuario fluida y un control administrativo riguroso sobre el aforo de las salas.

---

## Estructura del Proyecto

El sistema está organizado bajo un esquema de **Separación de Responsabilidades**, lo que permite un mantenimiento sencillo y escalabilidad futura:

```
TICKETLY/
├── app/
│   ├── models/                         # Definición de entidades de datos
│   │   ├── __init__.py
│   │   ├── boleto.py                   # Clase modelo para boletos
│   │   ├── funcion.py                  # Clase modelo para funciones
│   │   ├── pelicula.py                 # Clase modelo para películas
│   │   └── sala.py                     # Clase modelo para salas
│   │
│   ├── services/                       # Lógica de negocio y servicios
│   │   ├── __init__.py
│   │   ├── boleto_service.py           # Servicio de venta y gestión de boletos
│   │   ├── funcion_service.py          # Servicio de creación y gestión de funciones
│   │   ├── pelicula_service.py         # Servicio CRUD de películas
│   │   └── sala_service.py             # Servicio de creación y gestión de salas
│   │
│   ├── ui/                             # Capa de interfaz de usuario (consola)
│   │   ├── boletos_ui/                 # Módulo de vistas para boletos
│   │   │   ├── listar_boleto_ui.py     # Vista: listar boletos vendidos
│   │   │   ├── menu_boleto.py          # Menú del módulo de boletos
│   │   │   ├── ticket.py              # Componente: impresión del comprobante
│   │   │   └── vender_boleto_ui.py    # Vista: flujo de venta de boleto
│   │   │
│   │   ├── funciones_ui/               # Módulo de vistas para funciones
│   │   │   ├── crear_funcion_ui.py     # Vista: crear nueva función
│   │   │   ├── listar_funcion_ui.py    # Vista: listar funciones registradas
│   │   │   └── menu_funciones.py      # Menú del módulo de funciones
│   │   │
│   │   ├── peliculas_ui/               # Módulo de vistas para películas
│   │   │   ├── actualizar.py           # Vista: actualizar película existente
│   │   │   ├── crear_ui.py             # Vista: registrar nueva película
│   │   │   ├── eliminar_ui.py          # Vista: eliminar película
│   │   │   ├── listar_ui.py            # Vista: listar catálogo de películas
│   │   │   └── menu_pelicula.py        # Menú del módulo de películas
│   │   │
│   │   ├── salas_ui/                   # Módulo de vistas para salas
│   │   │   ├── __init__.py
│   │   │   ├── crear_sala_ui.py        # Vista: crear nueva sala
│   │   │   ├── listar_salas_ui.py      # Vista: listar salas registradas
│   │   │   ├── ver_asientos_ui.py      # Vista: visualización de asientos de una sala
│   │   │   └── menu_salas.py           # Menú del módulo de salas
│   │   │ 
│   │   └── menu_principal_ui.py        # Menú principal de la aplicación
│   │
│   └── utils/                          # Funciones auxiliares y herramientas
│       ├── asientos_utils.py           # Renderizado visual de la grilla de asientos
│       ├── limpiar_utils.py            # Limpieza de pantalla multiplataforma
│       └── logo_utils.py              # Banner/logo ASCII de la aplicación
│
├── docs/                               # Documentación técnica
│   └── pseudocodigo/
│       └── Ticketly.psc                # Algoritmo original en pseudocódigo (PSeInt)
│
├── tests/                              # Pruebas unitarias del sistema
│   ├── conftest.py                     # Fixtures y configuración compartida de pytest
│   ├── test_boleto_service.py          # Tests del servicio de venta de boletos
│   ├── test_pelicula_service.py        # Tests unitarios del servicio de películas
│   └── test_peliculas_services.py      # Tests adicionales del servicio de películas
│
├── .gitignore
├── main.py                             # Punto de entrada de la aplicación
└── README.md
```

---

## Descripción de Módulos

### `app/models/`

Contiene las clases que representan las entidades del dominio. Cada modelo encapsula sus atributos con getters y setters, centralizando la estructura de la información.

| Archivo | Clase | Descripción |
|---|---|---|
| `pelicula.py` | `Pelicula` | Almacena ID, nombre, duración y categoría de una película. Incluye setters para actualización. |
| `sala.py` | `Sala` | Gestiona ID, capacidad total, asientos disponibles y un arreglo del estado de cada asiento (`0` / `'O'`). |
| `funcion.py` | `Funcion` | Representa la combinación de una película, una sala y un horario. |
| `boleto.py` | `Boleto` | Registra el comprobante de una venta: ID de boleto, función, sala y número de asiento. |

---

### `app/services/`

Núcleo del sistema. Contiene toda la lógica de negocio, validaciones y operaciones sobre los datos en memoria.

| Archivo | Clase | Responsabilidades |
|---|---|---|
| `pelicula_service.py` | `PeliculaService` | CRUD completo de películas. Previene duplicados por nombre. |
| `sala_service.py` | `SalaService` | Creación y búsqueda de salas. Expone `buscar_por_id` y `buscar_sala`. |
| `funcion_service.py` | `FuncionService` | Crea funciones validando que existan la película y la sala referenciadas. Permite listar y eliminar. |
| `boleto_service.py` | `BoletoService` | Orquesta la venta de boletos: valida función, sala, rango de asiento y disponibilidad. Marca el asiento como ocupado (`'O'`) y decrementa el contador de disponibles. |

---

### `app/ui/`

Gestiona la interacción con el usuario mediante menús en consola. Utiliza la librería **[Rich](https://rich.readthedocs.io/en/stable/)** para tablas, paneles con color, prompts validados y el comprobante de compra.

#### `boletos_ui/`
- **`menu_boleto.py`** — Menú principal del módulo con opciones Vender / Listar.
- **`vender_boleto_ui.py`** — Flujo completo de venta: muestra funciones disponibles, renderiza la grilla de asientos y gestiona los errores de validación.
- **`listar_boleto_ui.py`** — Tabla con todos los boletos vendidos en la sesión.
- **`ticket.py`** — Imprime el comprobante de compra con panel estilizado al completar una venta.

#### `funciones_ui/`
- **`menu_funciones.py`** — Menú del módulo con opciones Agregar / Mostrar.
- **`crear_funcion_ui.py`** — Formulario para registrar una nueva función (sala, película, hora).
- **`listar_funcion_ui.py`** — Tabla con todas las funciones registradas.

#### `peliculas_ui/`
- **`menu_pelicula.py`** — Menú del módulo con opciones Agregar / Mostrar / Actualizar / Eliminar.
- **`crear_ui.py`** — Formulario de alta de película con validaciones de campos vacíos.
- **`listar_ui.py`** — Tabla del catálogo de películas.
- **`actualizar.py`** — Formulario de edición con valores por defecto precargados.
- **`eliminar_ui.py`** — Confirmación y eliminación de una película por ID.

#### `salas_ui/`
- **`menu_salas.py`** — Menú del módulo con opciones Agregar / Mostrar / Ver Asientos.
- **`crear_sala_ui.py`** — Formulario de alta de sala con capacidad ajustable (1–50).
- **`listar_salas_ui.py`** — Tabla con ID, capacidad y asientos libres de cada sala.
- **`ver_asientos_ui.py`** — Visualización detallada del estado de asientos de una sala específica.

#### Raíz de `ui/`
- **`menu_principal_ui.py`** — Orquesta la navegación entre los cuatro módulos principales (Películas, Salas, Funciones, Boletos).

---

### `app/utils/`

Herramientas reutilizables transversales a toda la aplicación.

| Archivo | Función principal |
|---|---|
| `asientos_utils.py` | `mostrar_asientos_rapido(sala)` — Renderiza la grilla de asientos en paneles de colores (verde = libre, rojo = ocupado) con 10 columnas. |
| `limpiar_utils.py` | `limpiar_pantalla()` — Limpia la terminal de forma multiplataforma (`cls` en Windows, `clear` en Unix). |
| `logo_utils.py` | `getLogo()` — Retorna el banner ASCII de **TICKETLY** para mostrarse al inicio de cada pantalla. |

---

## Tecnologías

- **Python 3.14.5**
- **[Rich](https://rich.readthedocs.io/en/stable/)** — Interfaz de consola enriquecida (tablas, paneles, colores, prompts).

---

## Ejecución
 
> Los comandos son iguales para **Windows, Linux y macOS**.
 
### 1. Requisitos previos
 
Tener instalado **Python 3.14 o superior**. Se puede verificar con:
 
```bash
python --version
```
---
 
### 2. Clonar el repositorio
 > SSH
```bash
git clone git@github.com:MisaelSanchez-SR23022-GT02/Ticketly.git
```
> HTTP
```bash
https://github.com/MisaelSanchez-SR23022-GT02/Ticketly.git
```
 
---
 
### 3. Ingresar al directorio del proyecto
 
```bash
cd Ticketly
```
 
---
 
### 4. Crear y activar un entorno virtual 
> Recomendado para aislar dependencias del proyecto del resto de tu sistema.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
 
**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
 
> Verán el prefijo `(venv)` en la terminal cuando el entorno esté activo.
 
---
 
### 5. Instalar dependencias
 
```bash
pip install rich
```
 
---
 
### 6. Ejecutar la aplicación
 
```bash
python main.py
```
 
---
 
### 7. Salir del entorno virtual
> Cuando terminen la ejecución, deben colocar el comando `(deactivate)` para salir del entorno virtual.

```bash
deactivate
```
 
---

## Autores

- Bryan Misael Sánchez Ramírez - [@MisaelSanchez-SR23022-GT02](https://github.com/MisaelSanchez-SR23022-GT02)
- Audiel Isaac Terán Morales - [@Audiel007](https://github.com/Audiel007)
- Abner Gabriel Ruiz Martínez - [@rm20102](https://github.com/rm20102)
- Carlos Fernando Rivas Morán - [@FerRvs](https://github.com/FerRvs)