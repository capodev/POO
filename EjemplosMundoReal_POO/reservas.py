class Habitacion:
    def __init__(self, numero, tipo, precio):

        # Inicializa los atributos de una habitación.
        # :param numero: Número de la habitación.
        # :param tipo: Tipo de habitación (e.g., sencilla, doble, suite).
        # :param precio: Precio por noche.

        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True  # Atributo para saber si la habitación está ocupada

    def reservar(self):
        "Marca la habitación como no disponible."
        if self.esta_disponible:
            self.esta_disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        "Marca la habitación como disponible."
        self.esta_disponible = True
        print(f"Habitación {self.numero} liberada con éxito.")


class Cliente:
    def __init__(self, nombre, telefono):

        # Inicializa los atributos del cliente.
        # :param nombre: Nombre del cliente.
        # :param telefono: Teléfono de contacto.

        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        "Representación del cliente como una cadena."
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"


class SistemaReservas:
    def __init__(self):
        "Inicializa el sistema con una lista de habitaciones y reservas."
        self.habitaciones = []
        # Diccionario para almacenar reservas (habitacion -> cliente)
        self.reservas = {}

    def agregar_habitacion(self, habitacion):
        "Agrega una habitación al sistema."
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        "Muestra todas las habitaciones disponibles."
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.esta_disponible:
                print(f"Número: {habitacion.numero}, Tipo: {
                      habitacion.tipo}, Precio: ${habitacion.precio}")

    def realizar_reserva(self, numero_habitacion, cliente):

        # Realiza una reserva para un cliente.
        # :param numero_habitacion: Número de la habitación a reservar.
        # :param cliente: Objeto Cliente que realiza la reserva.

        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.esta_disponible:
                    habitacion.reservar()
                    self.reservas[numero_habitacion] = cliente
                    print(f"Reserva realizada a nombre de {cliente.nombre}.")
                    return
                else:
                    print(f"La habitación {
                          numero_habitacion} no está disponible.")
                    return
        print(f"No se encontró la habitación {numero_habitacion}.")

    def cancelar_reserva(self, numero_habitacion):

        # Cancela una reserva existente.
        # :param numero_habitacion: Número de la habitación reservada.

        if numero_habitacion in self.reservas:
            cliente = self.reservas.pop(numero_habitacion)
            for habitacion in self.habitaciones:
                if habitacion.numero == numero_habitacion:
                    habitacion.liberar()
            print(f"Reserva a nombre de {cliente.nombre} cancelada.")
        else:
            print(f"No existe reserva para la habitación {numero_habitacion}.")


# Ejemplo del uso del sistema de reservas
if __name__ == "__main__":
    # Crear sistema de reservas
    sistema = SistemaReservas()

    # Crear habitaciones y agregarlas al sistema
    sistema.agregar_habitacion(Habitacion(101, "Sencilla", 50))
    sistema.agregar_habitacion(Habitacion(102, "Doble", 80))
    sistema.agregar_habitacion(Habitacion(201, "Suite", 120))

    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "123456789")

    # Mostrar habitaciones disponibles
    sistema.mostrar_habitaciones_disponibles()

    # Realizar una reserva
    sistema.realizar_reserva(102, cliente1)

    # Mostrar habitaciones disponibles después de la reserva
    sistema.mostrar_habitaciones_disponibles()

    # Cancelar una reserva
    sistema.cancelar_reserva(102)

    # Mostrar habitaciones disponibles después de cancelar la reserva
    sistema.mostrar_habitaciones_disponibles()

    # Para este ejemplo mostramos las habitaciones, reservamos una, mostramos habitaciones, cancelamos la reserva y mostramos habitaciones nuevamente.
    #jejeje