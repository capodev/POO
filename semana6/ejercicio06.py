# Aqui estamnos  aplicando conceptos de POO en Python

# Clase base que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_informacion(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.anio})"

    def sonido(self):
        return "El vehículo emite un sonido genérico."

# Clase derivada que representa un automóvil, hereda de Vehiculo


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.__puertas = puertas  # Atributo privado

    # Método para acceder al atributo privado
    def obtener_puertas(self):
        return self.__puertas

    # Método sobrescrito (polimorfismo)
    def sonido(self):
        return "El automóvil emite un sonido característico: ¡Bip Bip!"

# Clase derivada que representa una motocicleta, hereda de Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    # Método sobrescrito (polimorfismo)
    def sonido(self):
        return "La motocicleta emite un sonido característico: ¡Vroom Vroom!"


# Creación de instancias y demostración de la funcion del programa
if __name__ == "__main__":
    # Instancia de la clase base
    vehiculo = Vehiculo("Genérico", "ModeloX", 2000)
    print(vehiculo.mostrar_informacion())
    print(vehiculo.sonido())

    # Instancia de la clase Automovil (herencia y encapsulación)
    auto = Automovil("Toyota", "Corolla", 2022, 4)
    print(auto.mostrar_informacion())
    print(f"Número de puertas: {auto.obtener_puertas()}")
    print(auto.sonido())  # Ejemplo de polimorfismo

    # Instancia de la clase Motocicleta (herencia y polimorfismo)
    moto = Motocicleta("Yamaha", "R1", 2023, 1000)
    print(moto.mostrar_informacion())
    print(moto.sonido())  # Ejemplo de polimorfismo
    #tarea semana 06