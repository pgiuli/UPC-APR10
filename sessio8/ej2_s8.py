from random import randint

nums = []
test = input("Introduzca un número entre 1 y 10: ")

for _ in range(20):
    nums.append(str(randint(1,10)))

pos = []
count = 0

for i in range(20):
    if nums[i] == test:
        count += 1
        pos.append(str(i+1))

if count > 1:
    print(f"El número aparece {count} veces en la lista en las posiciones {" ".join(pos)}")
elif count == 1:
    print(f"El número aparece {count} vecz en la lista en la posición {" ".join(pos)}")
else:
    print("El número no aparece en la lista")
print(f"Lista: {" ".join(nums)}")