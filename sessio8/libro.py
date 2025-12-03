class Libro:
    def __init__(self, isbn, nombre, autor):
        self.isbn = isbn
        self.nombre = nombre
        self.autor = autor
    
    def __str__(self):
        return f"ISBN: {self.isbn}\tNombre: {self.nombre}\tAutor: {self.autor}"