def factorial(m):
    val = 1
    for i in range(m):
        val *= i+1
    return val

x = float(input("Introdueixi un valor real: "))
n = int(input("Introdueixi un valor natural: "))

cos = 0

for i in range(n+1):
    cos += ( x**(2*i) / factorial(2*i) )* (-1)**i

print(f"cos({x}) = {round(cos,2)}")