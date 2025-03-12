class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} de {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y Usuario como valor

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Este libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.usuarios:
            print("El usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")

    def eliminar_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print(f"Usuario con ID {user_id} eliminado de la biblioteca.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro devuelto: {libro} por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, clave) == valor for clave, valor in criterios.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez",
               "Realismo mágico", "987654321")
usuario1 = Usuario("Jose Arizaga", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "123456789")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "123456789")
biblioteca.listar_libros_prestados("U001")
