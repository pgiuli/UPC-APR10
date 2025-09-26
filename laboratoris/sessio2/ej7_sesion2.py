from math import sqrt

a = float(input("Introduzca el valor de a: "))
b = float(input("Introduzca el valor de b: "))
c = float(input("Introduzca el valor de c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("La ecuación no tiene soluciones reales.")
elif discriminant == 0:
    x1 = -b/2*a
    print(f"La solución de ecuación es: {x1}")
else:
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    print(f"Las soluciones de la ecuación son: {x1} y {x2}")
    
