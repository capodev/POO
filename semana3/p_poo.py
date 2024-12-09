# vamos a crear un algritmo que calcule el promedio semanal del clima con POO

class Clima:
    # definimos un array para los dias de la semana
    # ENCAPSULACION  __dias es una variable privada LA CUAL NO SE PUEDE ACCEDER DESDE FUERA DE LA CLASE podemos hacer getter y setter para acceder a ella
    __dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    temperaturas = []
    # esta funcion pide los valores por teclado
    def ingresar_temperaturas(self):
        for dia in self.__dias:
            temperatura = int(input(f"Ingrese la temperatura del dia {dia}: "))
            self.temperaturas.append(temperatura)
    # calcula los promedios del array para su resultado
    def promedio_temperatura(self):
        suma = 0
        for temperatura in self.temperaturas:
            suma += temperatura
        suma = round(suma / len(self.temperaturas), 2)
        return print(f"El promedio del clima de la semana es: {suma}")


clima = Clima()
clima.ingresar_temperaturas()
clima.promedio_temperatura()
# en este ejemplo al ser muy corto no APLICACREMOS LOS PRINCIPIOS DE ABSTRACCION, POLIMORFISMO NI HERENCIA SOLO ENCAPSULACION
# en este ejemplo hicimos casi lo mismo que en p Estructurada pero en clases
# podriamos hacer que la clase reciba un array ya con los datos de clima en el constructor o declararle uno con los datos en fin