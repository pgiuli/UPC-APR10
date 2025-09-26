string = input("Introdueixi una frase: ")
list = string.split(" ")

words = len(list) - list.count("")
print(f"La frase conté {words} paraules.")

string = input("Introdueixi una frase: ")
word = input("Introdueixi una paraula: ")
words = len(list) - list.count("")
print(f"La frase conté {words} paraules.")
print(f"La frase{"" if word in string else " no"} conté la paraula {word}")