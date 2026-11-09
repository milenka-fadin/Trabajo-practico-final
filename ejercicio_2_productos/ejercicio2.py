#----- Modelo de Productos, Excepciones y Persistencia -----#
import json

class StockInvalidoError(Exception):
    pass

# Clase padre
class DispositivoEcológico:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.establecerstock(stock)

    # Setter
    def establecerstock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo")
        else:
            self.__stock = nuevo_stock

    # Getter
    def obtenerstock(self):
        return self.__stock

    # Ficha técnica general
    def ficha_tecnica(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.obtenerstock()}"

    # Convertir objeto a diccionario
    def a_diccionario(self):
        return {
            "tipo": "DispositivoEcológico",
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.obtenerstock()
        }


# Clase hija
class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, precio, stock, potencia):
        super().__init__(nombre, precio, stock)
        self.potencia = potencia

    # Polimorfismo
    def ficha_tecnica(self):
        return f"Panel Solar: {self.nombre}, Precio: ${self.precio}, Stock: {self.obtenerstock()}, Potencia: {self.potencia} W"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["tipo"] = "PanelSolar"
        datos["potencia"] = self.potencia
        return datos


# Gestión de catalgo
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        datos_catalogo = []

        for dispositivo in lista_dispositivos:
            datos_catalogo.append(dispositivo.a_diccionario())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_catalogo, archivo, indent=4, ensure_ascii=False)


#----- Implementacion -----

# Crear dispositivos
dispositivo1 = DispositivoEcológico("Batería ecológica", 15000, 20)
dispositivo2 = PanelSolar("Panel Solar", 25000, 10, 300)
dispositivo3 = PanelSolar("Panel Solar Industrial", 80000, 5, 600)

# Probar excepción 
try:
    dispositivo2.establecerstock(-10)
except StockInvalidoError:
    print("Error controlado: el stock no puede ser negativo")

# Lista de dispositivos
lista_dispositivos = [dispositivo1, dispositivo2, dispositivo3]

# Mostrar fichas tecnicas (polimorfismo)
for dispositivo in lista_dispositivos:
    print(dispositivo.ficha_tecnica())

# Guardar catálogo JSON
gestor = GestorInventario()
gestor.guardar_catalogo_json(lista_dispositivos, "catalogo_ecotech.json")

print("Catálogo guardado correctamente")
