import os
import json

# Tebemos nuestra clase producto que tiene los atributos id_producto, nombre, cantidad y precio


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio,
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id_producto"], data["nombre"], data["cantidad"], data["precio"]
        )

    def __str__(self):
        return f"{self.id_producto}, {self.nombre}, {self.cantidad}, {self.precio}"

# aqui tenemos nuestra clase inventario que tiene los metodos añadir_producto, eliminar_producto, actualizar_producto, buscar_por_nombre, mostrar_productos, guardar_en_archivo y cargar_desde_archivo


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Diccionario para acceso rápido
        self.archivo = archivo
        self.cargar_desde_archivo()
#  en los metodos estamos usando serializacion de objetos para guardar y cargar los datos de los productos en un archivo json

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump([p.to_dict()
                          for p in self.productos.values()], f, indent=4)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
# aqui hacemos uso de la deserializacion de objetos para cargar los datos de los productos desde un archivo json

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()
            return
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = {
                    # aqui hacemos uso del diccionario de comprension para crear un diccionario con los datos de los productos
                    p["id_producto"]: Producto.from_dict(p) for p in data
                }
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo no encontrado o vacío, iniciando con inventario vacío.")

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: ID ya existente.")
            return
        self.productos[id_producto] = Producto(
            id_producto, nombre, cantidad, precio)
        self.guardar_en_archivo()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values() if nombre.lower() in p.nombre.lower()
        ]
        return encontrados if encontrados else "No se encontraron productos."

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def obtener_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# con los archivos Json tenemos mas eficiencia en el manejo de datos y podemos guardar y cargar los datos de los productos de manera mas eficiente
# con la serializacion y deserializacion de objetos podemos guardar y cargar los datos de los productos de manera mas eficiente


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = obtener_entero("ID: ")
            nombre = input("Nombre: ")
            cantidad = obtener_entero("Cantidad: ")
            precio = obtener_flotante("Precio: ")
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = obtener_entero("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = obtener_entero("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(
                id_producto, int(cantidad) if cantidad else None, float(
                    precio) if precio else None
            )
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            print(resultados if isinstance(resultados, str)
                  else "\n".join(map(str, resultados)))
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
# trabajo POO semana 11
