import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_id_producto(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"{self.__id_producto},{self.__nombre},{self.__cantidad},{self.__precio}"

    @staticmethod
    def from_string(producto_str):
        id_producto, nombre, cantidad, precio = producto_str.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.__productos = []
        self.__archivo = archivo
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.__archivo, 'w') as f:
                for producto in self.__productos:
                    f.write(str(producto) + "\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.__archivo):
            open(self.__archivo, 'w').close()
            return
        try:
            with open(self.__archivo, 'r') as f:
                self.__productos = [Producto.from_string(line) for line in f]
        except FileNotFoundError:
            print("Archivo no encontrado, iniciando con inventario vacío.")
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if any(p.get_id_producto() == id_producto for p in self.__productos):
            print("Error: ID ya existente.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.__productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("Producto añadido con éxito al Inventario.")

    def eliminar_producto(self, id_producto):
        self.__productos = [
            p for p in self.__productos if p.get_id_producto() != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía en el Inventario.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.__productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado en el Inventario.")
                return
        print("Producto no encontrado en el Inventario.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.__productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados if encontrados else "No se encontraron productos en el Inventario."

    def mostrar_productos(self):
        if not self.__productos:
            print("Inventario vacío.")
        else:
            for producto in self.__productos:
                print(producto)


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
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(
                cantidad) if cantidad else None, float(precio) if precio else None)
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
