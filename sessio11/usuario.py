class Usuario:
    def __init__(self, nom, telefono, contrasenya):
        self.nom = nom
        self.telefono = telefono
        self.contrasenya = contrasenya

    def __str__(self):
        return f"Nom:{self.nom}\tTelf:{self.telefono}"

