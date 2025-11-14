from usuario import Usuario

def menu():
    return int(input("""
Menú gestión usuarios:
1.Registrar usuario
2.Dar de baja usuario
3.Mostrar usuarios
4.Buscar usuario
5.Salir
Introduzca una opción: """))

users = {}

while 1:
    match menu():
        case 1:
            email = input("Introduce email del usuario a dar de alta: ")
            nom = input("Introduce nombre: ")
            telf = input("Introduce teléfono: ")
            passwd = input("Introduce contraseña: ")
            users[email] = Usuario(nom, telf, passwd)
        case 2:
            email = input("Introduce email del usuario a dar de baja: ")
            if email in users.keys():
                del users[email]
                print("Usuario dado de baja correctamente")
            else:
                print("El usuario no existe")
        case 3:
            print("Listado de usuarios:")
            for email in users.keys():
                print(f"Email: {email}    {users[email]}")
        case 4:
            email = input("Introduce email del usuario: ")
            if email in users.keys():
                print(f"Email: {email}    {users[email]}")
            else:
                print("No existe ningún usuario con dicho email")
        case 5:
            print("Ha salido de la aplicación")
            break
        case _:
            print("Opción incorrecta.")