
# tenemos nuestra clase Libro, que tiene un método prestar()
# este tiene 2 metosdos prestar y devolver
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible  # Encapsulación

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

# Clase derivada para libros digitales que hereda de Libro (Aqui ya estamos aplicando Herencia)
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamano_mb):
        super().__init__(titulo, autor, isbn, disponible=True)
        self.tamano_mb = tamano_mb

    # Sobrescritura de método (polimorfismo)
    def prestar(self):
        print(f"El libro digital '{self.titulo}' ha sido prestado. No afecta su disponibilidad.")

    def mostrar_info(self):
        print(f"Libro Digital: {self.titulo}, Autor: {self.autor}, Tamaño: {self.tamano_mb}MB.")

# tenemos nuestra clase miembro que tiene 2 metodos prestar_libro y devolver_libro
class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print(f"{self.nombre} no puede prestar '{libro.titulo}' porque no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' para devolver.")

# tenemos nuestra clase miembropremium que hereda de miembro
# Clase MiembroPremium
class MiembroPremium(Miembro):
    def __init__(self, nombre='sin_name', id_miembro=4, cuota=100):
        super().__init__(nombre, id_miembro)
        self.cuota = cuota

    def beneficios(self):
        print(f"Miembro Premium: {self.nombre} tiene acceso ilimitado a libros digitales y otros beneficios.")

# Clase Prestamo
class Prestamo:
    def __init__(self, libro, miembro, fecha_prestamo):
        self.libro = libro
        self.miembro = miembro
        self.fecha_prestamo = fecha_prestamo

    def registrar_prestamo(self):
        print(f"Registro: {self.miembro.nombre} prestó '{self.libro.titulo}' el {self.fecha_prestamo}.")

# Creación de libros
libro1 = Libro("1984", "George Orwell", "123456789")
libro_digital1 = LibroDigital("Python Avanzado", "Guido van Rossum", "987654321", 15)


# Creación de miembros
print("\n--- Préstamos de libros físicos ---")
miembro = Miembro("Felix Jimenez",4)
miembro.prestar_libro(libro1)
miembro.devolver_libro(libro1)

print("\n--- Préstamos de libros digitales ---")
libro_digital1.prestar()



# Operaciones


print("\n--- Miembro Premium ---")
miembro_premium = MiembroPremium("FElIX JIMENEZ", 4,200)
miembro_premium.beneficios()
miembro_premium.prestar_libro(libro1)  # El libro '1984' no está disponible.
miembro_premium.prestar_libro(libro_digital1)  # Préstamo exitoso.

print("\n--- Información de libro digital ---")
libro_digital1.mostrar_info()
# este es un ejemplo sencillo de como aplicar los principios de la POO
# por Felix Jimenez , haria mas pero al ser una prueba me da peresita xd
