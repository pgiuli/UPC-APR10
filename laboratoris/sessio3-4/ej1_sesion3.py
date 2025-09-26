natural = int(input("Introdueix un nombre natural: "))

sequence = "Seqüència de nombres: "
for i in range(natural):
    sequence += f"{i}, "
sequence += str(natural)
print(sequence)