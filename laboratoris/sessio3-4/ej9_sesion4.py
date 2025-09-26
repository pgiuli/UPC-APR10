name = input("Hola! Com et dius? ")
print(f"Bé, {name}, estic pensant en un nombre entre l'1 i el 20.")
print("Tindràs fins a 6 intents per endevinar-lo.")
from random import randint
value = randint(1, 20)

for i in range(6):
    guess = int(input("Endevina, introdueix un nombre: "))
    if guess == value:
        print(f"Enhorabona, {name}! Has endevinat el nombre en {i+1} intents!")
        break
    else:
        print(f"La teva estimació és massa {"baixa" if guess < value else "alta"}")
else:
    print(f"Doncs vaja, no l'has endevinat a temps, el nombre era el {value}.")