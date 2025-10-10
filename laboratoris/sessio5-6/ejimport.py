from calculos.area import *

def menu():
    print("Calculadora de áreas: ")
    print("1. Área rectángulo")
    print("2. Área cuadrado")
    print("3. Área círculo")
    print("4. Salir")
    opcion = int(input("Selecciona opción: "))
    return opcion

opcion = menu()
while opcion != 4:
    if opcion == 1:
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        res = area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {format(res, '.2f')}")
    elif opcion == 2:
        lado = float(input("Introduce lado cuadrado: "))
        res = area_cuadrado(lado)
        print(f"El área del cuadrado es: {format(res, '.2f')}")
    elif opcion == 3:
        radio = float(input("Introduzca el radio del círculo: "))
        res = area_circulo(radio)
        print(f"El área del círculo es: {format(res, '.2f')}")
    else:
        print("Opción incorrecta")
    opcion = menu()