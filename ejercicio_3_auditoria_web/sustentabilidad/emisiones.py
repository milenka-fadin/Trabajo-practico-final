# ----- Ejercicio 3: calculo y procesamiento de emisiones -----


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula las emisiones a partir del consumo electrico."""
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    """Calcula emisiones globales y determina la planta de mayor consumo."""
    total_emisiones = 0
    consumos_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        total_emisiones += calcular_emisiones_carbono(consumo)
        consumos_por_planta[planta] = consumos_por_planta.get(planta, 0) + consumo

    planta_mayor_consumo = "Sin registros"
    mayor_consumo = -1

    for planta in consumos_por_planta:
        if consumos_por_planta[planta] > mayor_consumo:
            mayor_consumo = consumos_por_planta[planta]
            planta_mayor_consumo = planta

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
    }
