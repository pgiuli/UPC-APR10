username = input("Introdueixi el nom d'usuari: ")
password = input("Introdueixi la contrasenya: ")

uservalid = 5 < len(username) < 13 and username.isalnum()
passvalid = len(password) == 8 and password.isalnum() and password.find(" ") == -1

if uservalid and passvalid:
    print("Nom d'usuari i contrasenya correctes")
elif uservalid:
    print("Contrasenya incorrecta")
elif passvalid:
    print("Nom d'usuari incorrecte")
else:
    print("Nom d'usuari i contrasenya incorrectes.")
