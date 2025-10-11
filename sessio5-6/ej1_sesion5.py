def es_primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

sequence = []
print("Introduce una secuencia de números, -1 para finalizar.")
while 1:
    x = int(input("Introduce un número: "))
    if x == -1:
        break
    sequence.append(x)

sum = 0
for i in sequence:
    if es_primo(i):
        sum += i

print(f"Suma={sum}")