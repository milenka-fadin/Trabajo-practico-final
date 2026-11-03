#----- Sanitización y Análisis Estadístico de Sensores -----#

def limpiar_registro_sensor(registro_raw) :
    # {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
    sensor_id = registro_raw["sensor_id"]
    sensor_id = sensor_id.strip()

    temperatura = registro_raw["temperatura"]
    temperatura = float(temperatura.replace("C", ""))

    ubicacion = registro_raw.get("ubicacion", "Lugar no registrado")

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio


registro1 = {
        "sensor_id": "Sensor 001",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
}
registro2 = {
        "sensor_id": "Sensor 002",
        "temperatura": "30.2C",
}
registro3 = {
        "sensor_id": "Sensor 003",
        "temperatura": "18.5C",
        "ubicacion": "Planta Sur"
}

registros = [registro1, registro2, registro3]

registros_limpios = [] 

for registro in registros:
    registro_limpio = limpiar_registro_sensor(registro)
    registros_limpios.append(registro_limpio)

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    sensores_alerta = []
    sumatemperatura = 0

    for registro in lista_sensores_limpios:
        if registro["temperatura"] > umbral_temperatura:
            sensores_alerta.append(registro["sensor_id"])

    for registro in lista_sensores_limpios:
        sumatemperatura += registro["temperatura"]

    promedio = sumatemperatura / len(lista_sensores_limpios)

    return sensores_alerta, promedio


umbral_temperatura = 30
sensores_alerta, promedio = generar_resumen_sensores(registros_limpios, umbral_temperatura)

print("Sensores con temperatura mayor al umbral:", sensores_alerta)
print("Promedio de temperatura:", promedio)

