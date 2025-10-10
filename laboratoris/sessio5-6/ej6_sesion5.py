def menu():
    print("""
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicación
4) División
5) Salir
""")
    return input("Seleccione una opción: ")

while True:
    match menu():
        case "1":
                print(f"La suma es: {int(input("Introduzca un número: ")) + int(input("Introduzca un número: "))}")
        case "2":
                print(f"La suma es: {int(input("Introduzca un número: ")) - int(input("Introduzca un número: "))}")
        case "3":
                print(f"La suma es: {int(input("Introduzca un número: ")) * int(input("Introduzca un número: "))}")
        case "4":
                print(f"La suma es: {int(input("Introduzca un número: ")) / int(input("Introduzca un número: "))}")
        case "5":
                break
        case _:
                print("Opción incorrecta")