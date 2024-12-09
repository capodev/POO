# vamos a crear un algritmo que calcule el promedio semanal del clima de forma de programacion tradicional

# definimos un array para los dias de la semana
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# vamos a crear una funcion que permita ingresar 7 numeros por teclado y los almacene en un array
def ingresar_temperaturas():
    temperaturas = []
    for dia in dias:
        temperatura = int(input(f"Ingrese la temperatura del dia {dia}: "))
        temperaturas.append(temperatura)
# aqui en el return dejaremos como salida el array de temperaturas
    return temperaturas


# creamos la funcion que calcule el promedio de las ingresar_temperaturas
# pero este recibe ya las temperaturas calculadas antes, le hacemos el recorrido en el for y sumamos cada temperatura
def promedio_temperatura(temperaturas):
    suma = 0
    for temperatura in temperaturas:
        suma += temperatura
    return suma / len(temperaturas)
# asignamos a la variable suma_total el resultado de la funcion promedio_temperatura que a su vez ya recibe las temperaturas entradas por teclado
suma_total = promedio_temperatura(ingresar_temperaturas())

# imprimimos el resultado del promedio de las temperaturas de la semana
# le agregamos round para redondear el resultado a 2 decimales
print(f"El promedio del clima de la semana es: {round(suma_total,2)}")
# desarrollado por felix Jimenez, Sigan viendo