nums = []

print("Introduzca una secuencia de números enteros acabada en -1:")
while True:
    num = int(input("Introduzca un número: "))
    if num == -1:
        break
    else:
        nums.append(num)

print()
print(f"El valor mínimo es: {min(nums)}")
print(f"El valor máximo es: {max(nums)}")