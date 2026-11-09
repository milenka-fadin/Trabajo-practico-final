# ----- Ejercicio 3A: auditoria con pruebas unitarias -----
import unittest

from .emisiones import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_emision_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(200, 0.5), 100.0)

    def test_consumo_cero(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

    def test_metricas_consumo(self):
        registros = [
            {"planta": "Planta Norte", "consumo_kwh": 1200},
            {"planta": "Planta Sur", "consumo_kwh": 1500},
            {"planta": "Planta Norte", "consumo_kwh": 900},
            {"planta": "Planta Oeste", "consumo_kwh": 1100},
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertAlmostEqual(metricas["total_emisiones"], 1880.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Planta Norte")

    def test_sin_registros(self):
        metricas = obtener_metricas_consumo([])
        self.assertAlmostEqual(metricas["total_emisiones"], 0.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Sin registros")
