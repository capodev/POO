# aqui tenemos la clase producto con sus respectivos getter y setters para acceder a los atributos de la clase producto
# luego tenemos la clase inventario que tiene una lista de productos y metodos para añadir, eliminar, actualizar, buscar y mostrar productos
class Producto:
    # la clase producto tiene un constructor que recibe los atributos id_producto, nombre, cantidad y precio
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
        return f"ID: {self.__id_producto}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: ${self.__precio:.2f}"


class Inventario:
    # la clase inventario tiene un constructor que inicializa una lista vacia de productos

    def __init__(self):
        self.__productos = []
# metodo para añadir un producto a la lista de productos, recibe los atributos id_producto, nombre, cantidad y precio

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if any(p.get_id_producto() == id_producto for p in self.__productos):
            print("Error: ID ya existente.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.__productos.append(nuevo_producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        self.__productos = [
            p for p in self.__productos if p.get_id_producto() != id_producto]
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.__productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.__productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados if encontrados else "No se encontraron productos."

    def mostrar_productos(self):
        if not self.__productos:
            print("Inventario vacío.")
        else:
            for producto in self.__productos:
                print(producto)

# menu para interactuar con el inventario


def menu():
    inventario = Inventario()
    while True:
        # menu con las opciones para interactuar con el inventario
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
