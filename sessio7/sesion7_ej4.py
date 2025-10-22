from calc import *

menu = """
Calculadora
1.Suma
2.Resta
3.Multiplicación
4.Division
5.Salir
Introduce una opción:
"""

while True:
    match input(menu):

        case "1":
            num1 = float(input("Introduce primer número: "))
            num2 = float(input("Introduce primer número: "))
            Suma(num1, num2, "+").mostrar_resultado()

        case "2":
            num1 = float(input("Introduce primer número: "))
            num2 = float(input("Introduce primer número: "))
            Resta(num1, num2, "-").mostrar_resultado()

        case "3":
            num1 = float(input("Introduce primer número: "))
            num2 = float(input("Introduce primer número: "))
            Mult(num1, num2, "*").mostrar_resultado()

        case "4":
            num1 = float(input("Introduce primer número: "))
            num2 = float(input("Introduce primer número: "))
            Div(num1, num2, "/").mostrar_resultado()

        case "5":
            break
        
        case _:
            print("Opción incorrecta")
