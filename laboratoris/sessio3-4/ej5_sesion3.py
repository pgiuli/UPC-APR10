def factorial(m):
    val = 1
    for i in range(m):
        val *= i+1
    return val

m = int(input("Introdueixi el valor de m: "))

print(f"{m}! = {factorial(m)}")

n = int(input("Introdueixi el valor de n: "))
e = 0
for i in range(n+1):
    e += 1/factorial(i)
print(f"L'aproximació de e amb {n} termes és: {e}")