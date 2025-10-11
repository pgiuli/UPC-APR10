year = int(input("Introduzca el año: "))
leap = not year % 4 and year % 100 or not year % 4 and not year % 400
print(f"El año{"" if leap else " no"} es bisiesto")