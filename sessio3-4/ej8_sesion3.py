string = input("Introdueixi una frase: ")

acronym = ""
for word in string.upper().split(" "):
    acronym += word[0]

print(f"Acrònim: {acronym}")