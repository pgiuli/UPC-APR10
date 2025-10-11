natural = int(input("Introdueix un nombre natural: "))
output = f"Els divisors de {natural} són: "


for i in range(1, natural):
    if (natural // i) * i == natural:
        output += f"{i}, "
output += str(natural)

print(output)