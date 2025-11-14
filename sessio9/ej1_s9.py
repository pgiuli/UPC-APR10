diccionary = {}

def menu():
    return int(input("""
1.Añadir o actualizar términos
2.Traducir
3.Mostrar todos los términos del diccionario
4.Salir
"""))

while True:
    match menu():
        case 1:
            source = input("Introduzca el término en castellano: ")
            translation = input("Introduzca el término en inglés: ")
            diccionary[source] = translation
        case 2:
            print(f"Traducción: {diccionary[input("Introduzca el término a traducir en castellano: ")]}")
        case 3:
            for i in diccionary.keys():
                print(f"{i}:{diccionary[i]}")