string = input("Introdueix una frase: ")

output = "Text sense espais en blanc: "

for i in string.split(" "):
    if i != "":
        output += i

print(output)