def es_vocal(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

count = 0
word = input("Introduce una palabra: ")
for i in word:
    if es_vocal(i): count+=1
print(f"La palabra {word} tiene {count} vocales")