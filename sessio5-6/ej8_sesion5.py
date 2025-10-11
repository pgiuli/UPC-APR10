def conversor_grados(celsius):
    return celsius*(9/5)+32, celsius+273.15

result = conversor_grados(float(input("Introduce grados celsius: ")))

print(f"El equivalente son {result[0]} grados Farenheit y {result[1]} grados Kelvin")