def es_par(num):
    return bool(not num % 2)

num = input("Introduce un número: ")
sum = 0
for i in num:
    if es_par(int(i)): sum += int(i)

print(f"La suma de los dígitos pares de {num} es {sum}")