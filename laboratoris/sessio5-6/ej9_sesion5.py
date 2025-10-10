def fib(n):
    res =["0", "1"]
    for _ in range(n-1):
        res.append(str(int(res[len(res)-2])+int(res[len(res)-1])))
    return res

n = int(input("Introduzca un número natural: "))
print(f"Fibonacci ({n})= {" ".join(fib(n))}")