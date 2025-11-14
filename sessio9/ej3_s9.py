text = "Si yo le diera a un general la orden de volar de flor en flor como una mariposa o de escribir una tragedia o de transformarse en ave marina y el general no ejecutase la orden recibida de quién sería la culpa mía o de él"

words = {}

for word in text.split(" "):
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(f"Texto: {text}")

key = input("Introduzca una palabra: ")

if key in words.keys():
    print(f"La palabra {key} aparece {words[key]} {"vez" if words[key] ==1 else "veces"}")
else:
    print(f"La palabra {key} no aparece en el texto")