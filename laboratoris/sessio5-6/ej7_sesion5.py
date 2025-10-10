def menu():
    print("""
Calculadora
************
Menu
1) Factorial
2) Exponencial
3) Coseno
4) Salir
""")
    return input("Seleccione una opción: ")

def factorial(num):
    i=1
    for h in range(num):
        i*=h+1
    return i

def exponencial(n):
    e = 0
    for i in range(n+1):
        e += 1/factorial(i)
    return e

def cos(x,n):
    cos = 0
    for i in range(n+1):
        cos += ( x**(2*i) / factorial(2*i) )* (-1)**i
    return cos

while True:
    match menu():
        case "1":
                num = int(input("Introduzca un número: "))
                print(f"{num}!={factorial(num)}")
        case "2":
                num = int(input("Introduzca un número: "))
                print(f"exp({num})={exponencial(num)}")
        case "3":
                num = float(input("Introduzca x: "))
                iter = int(input("Introduzca n: "))
                print(f"cos({num})={cos(num, iter)}")
        case "4":
                break
        case _:
              print("Opción incorrecta")