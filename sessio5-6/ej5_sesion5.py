width, char = int(input("Anchura del triángulo: ")), input("Carácter para dibujar triángulo: ")
for i in range(width+1):
    print(char*i)
for i in range(1,width).__reversed__():
    print(char*i)