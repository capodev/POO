# vamos a crear una clase sencilla que simule un vehículo, con atributos y métodos básicos.
# la clase tendra su metodo contrucctor y destructor

class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def __del__(self):
        print(f"El vehículo {self.marca} {self.modelo} ha sido eliminado.")

    def mostrar_informacion(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.anio})"

    def sonido(self):
        return "El vehículo emite un sonido genérico."

# Creación de instancias y demostración de la función del programa


if __name__ == "__main__":
    # Instancia de la clase base
    vehiculo = Vehiculo("Genérico", "ModeloX", 2000)
    print(vehiculo.mostrar_informacion())
    print(vehiculo.sonido())
    del vehiculo
    print("Fin del programa")
# En este caso, hemos agregado un método especial __del__ que se ejecuta cuando el objeto es eliminado.
# Este método se conoce como destructor y se utiliza para liberar recursos o realizar tareas de limpieza antes de que el objeto sea eliminado de la memoria.
