import users

user = users.Usuario('', '')
while True:
    user.nombre = input("Introduce nombre usuario: ")
    if user.validar_nombre(user.nombre):
        print("Nombre de usuario correcto")
        break
    else:
        print("Nombre usuario incorrecto, contiene carácteres diferentes de letras o números")

while True:
    user.email = input("Introduce email: ")
    match user.validar_email(user.email):
        case 0: 
            print("Email correcto")
            break
        case -1: print("Email incorrecto. No contiene el carácter @")
        case -2: print("Email incorrecto. No contiene el carácter .")
        case -3: print("Contiene carácteres diferentes de letras o números")

passwd = input("Introduce contraseña: ")
passwd = users.Contrasenya(passwd)
if passwd.es_fuerte():
    print("Contraseña segura")
else:
    print("La contraseña no es lo suficientemente segura. Generando una nueva...")
    passwd = passwd.generar_pass()
    print(f"Nueva contraseña: {passwd.valor}")