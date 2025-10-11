import random
import string

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def validar_nombre(self, nom):
        return nom.isalnum()

    def validar_email(self, mail):
        if not "@" in mail:
            return -1
        elif not "." in mail:
            return -2
        elif not mail.replace("@", "a").replace(".", "a").isalnum():
            return -3
        else: return 0

class Contrasenya:
    def __init__(self, valor):
        self.valor = valor
        self.long = len(valor)
    
    def es_fuerte(self):
        uppcount = 0
        lowcount = 0
        numcount = 0
        for char in self.valor:
            if char.isupper(): uppcount += 1
            if char.islower(): lowcount += 1
            if char.isdigit(): numcount += 1
        return uppcount >= 2 and lowcount >= 1 and numcount >= 5
    
    def generar_pass(self):
        val = ''
        for _ in range(2):
            val += random.choice(string.ascii_uppercase)
        for _ in range(5):
            val += random.choice(string.digits)
        val += random.choice(string.ascii_lowercase)
        passwd = []
        for i in val: passwd.append(i)
        random.shuffle(passwd)
        val = ''.join(passwd)
        return Contrasenya(val)
        