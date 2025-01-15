
# Programa: Cálculo del área de un triángulo
# Funcionalidad: Este programa solicita al usuario la base y la altura de un triángulo,
# calcula su área y muestra el resultado. También verifica si los valores ingresados son válidos.


def calcular_area_triangulo(base: float, altura: float) -> float:

    # Calcula el área de un triángulo dado su base y altura.
    # :param base: Base del triángulo (float).
    # :param altura: Altura del triángulo (float).
    # :return: Área del triángulo (float).

    return (base * altura) / 2


def es_valor_valido(valor: float) -> bool:
    return valor > 0


# Inicio del programa
print("Bienvenido al programa para calcular el área de un triángulo.")

# Solicitar datos al usuario
try:
    base = float(
        input("Por favor, ingresa la base del triángulo (en unidades): "))
    altura = float(
        input("Por favor, ingresa la altura del triángulo (en unidades): "))

    # Verificar si los valores son válidos
    if es_valor_valido(base) and es_valor_valido(altura):
        # Calcular el área del triángulo
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo con base {base} y altura {
              altura} es: {area:.2f} unidades cuadradas.")
    else:
        print("Error: La base y la altura deben ser valores mayores que cero.")
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")

print("Gracias por usar el programa.")

#jejeje se me paso la hora :c