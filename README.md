# Pre-entrega Automation Testing

Proyecto de automatización de pruebas funcionales sobre el sitio de práctica [Sauce Demo](https://www.saucedemo.com), desarrollado con Python, PyTest y Selenium WebDriver.

**Curso:** Talento Tech - Automation QA
**Comisión:** 26221
**Autor:** Ariel Oliva

## Propósito del proyecto

El objetivo es validar de forma automática las funcionalidades principales de un e-commerce de prueba, aplicando buenas prácticas de testing automatizado: pruebas independientes, código auxiliar reutilizable y generación de reportes con los resultados de cada ejecución.

Casos de prueba cubiertos:

| Archivo | Descripción |
|---|---|
| `tests/test_login.py` | Inicio de sesión con credenciales válidas. |
| `tests/test_carrito.py` | Agregado de un producto al carrito. |
| `tests/test_navegacion.py` | Verificación de que, tras iniciar sesión, se muestran los elementos principales de la interfaz: Titulo, carrito y menú hamburguesa. |

## Tecnologías utilizadas

- Python 3.12.3
- PyTest
- Selenium WebDriver
- pytest-html (generación del reporte HTML)
- Google Chrome

## Estructura del proyecto

```
.
├── tests/
│   ├── test_carrito.py
│   ├── test_login.py
│   └── test_navegacion.py
├── utils/
│   └── iniciarSesion.py
├── reporte.html
└── README.md
```

- `tests/`: casos de prueba.
- `utils/`: funciones auxiliares reutilizables por los tests (por ejemplo, el inicio de sesión).
- `reporte.html`: reporte de la última ejecución.

## Requisitos previos

- Python 3.12 o superior.
- Google Chrome instalado en el equipo.
- Conexión a internet (las pruebas se ejecutan contra https://www.saucedemo.com).

## Instalación de dependencias

1. Clonar el repositorio:

```bash
git clone https://github.com/Ariel3748/pre-entrega-automation-testing-Ariel-Oliva
cd pre-entrega-automation-testing-Ariel-Oliva
```


2. Instalar las dependencias:

```bash
pip install pytest selenium pytest-html
```

## Ejecución de las pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest
```

Ejecutar las pruebas y generar el reporte HTML:

```bash
python -m pytest --html=reporte.html --self-contained-html
```

Al finalizar, se genera el archivo `reporte.html` en la raíz del proyecto, que puede abrirse con cualquier navegador. La opción `--self-contained-html` incluye los estilos dentro del mismo archivo, de modo que puede compartirse sin archivos adicionales.

