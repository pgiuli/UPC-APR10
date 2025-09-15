# Declaració de variables i operacions bàsiques.

x = 2
y = 3

res = x + y
print(res) # 5.

frase = "Hola!"

print(type(frase)) # La frase és un string, una sèrie de caràcters.

num = 39.5 # Es defineix com a float.
num_z = int(num) # Evalua a l'int 39.

c1 = 3+2j
c2 = complex(2, -1)
print(c1-c2) # (1+3j)


print(c2.conjugate())
resta = 24 % 3
print(resta == 0)

nom = input()
edat = int("Quants anys tens?") # Ho convertim directament a int per a poder efectuar operacions sobre el valor.
print(f"Fa dos anys tenies {edat-2} anys.") # I can't bring myself to do this without f-strings. It feels wrong and .format() is the devil.