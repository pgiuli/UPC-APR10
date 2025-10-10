a = int(input("Introduzca a: "))
b = int(input("Introduzca b: "))

if a < b:
    a, b = b, a

while a % b != 0:
    residuo = a % b
    a = b
    b = residuo

print(f"El MCD es {b}")