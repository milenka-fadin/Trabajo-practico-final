# ----- Ejercicio 3B: vista de Django -----
from django.shortcuts import render

from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # Registros ficticios autorizados por la consigna del TP.
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 1500},
        {"planta": "Planta Norte", "consumo_kwh": 900},
        {"planta": "Planta Oeste", "consumo_kwh": 1100},
    ]

    contexto = obtener_metricas_consumo(registros)

    return render(request, "sustentabilidad/panel.html", contexto)
