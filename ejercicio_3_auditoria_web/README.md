# Ejercicio 3 — EcoTech Solutions

TP Final de Python: auditoría unitaria e integración web de emisiones de carbono.

## Requisitos

- Python 3.10 o posterior
- Django (se instala con `requirements.txt`)

## Cómo ejecutarlo en Windows (VS Code)

Abrir la terminal dentro de la carpeta `ejercicio_3_auditoria_web`, que contiene `manage.py`.

```powershell
python -m pip install -r requirements.txt
python manage.py test sustentabilidad
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

Para detener el servidor: `Ctrl+C` en la terminal.

## Estructura

- `sustentabilidad/emisiones.py`: funciones `calcular_emisiones_carbono` y `obtener_metricas_consumo`.
- `sustentabilidad/tests.py`: pruebas unitarias con `unittest.TestCase`.
- `sustentabilidad/views.py`: vista `vista_panel_sustentabilidad` y datos ficticios.
- `sustentabilidad/templates/sustentabilidad/panel.html`: plantilla HTML del panel.
- `ecotech_web/urls.py`: URL que permite acceder al panel.
- `ecotech_web/settings.py`: configuración local de Django.

## Datos de ejemplo

Las cuatro lecturas ficticias suman 4700 kWh. Con el factor de emisión 0.4, las emisiones globales son **1880 kg de CO2**. La planta de mayor consumo acumulado es **Planta Norte**, con 2100 kWh.

No se utilizan datos reales ni servicios externos. La clave incluida en `settings.py` es ficticia y solamente sirve para ejecutar este ejemplo localmente; no se debe desplegar en producción con `DEBUG=True`.
