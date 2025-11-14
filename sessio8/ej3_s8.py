from libro import Libro

books = []

def menu():
    return int(input("""
1.Dar de alta un libro nuevo en la biblioteca
2.Eliminar libro de la biblioteca
3.Buscar libro biblioteca
4.Mostrar libros biblioteca
5.Salir
"""))


def libro_en_bib(books, isbn):
    for book in books:
        if book.isbn == isbn:
            return book
    return None

while True:
    print("Biblioteca")
    match menu():
        case 1:
            books.append(Libro(input("Introduzca ISBN: "), input("Introduzca nombre: "), input("Introduzca autor: ")))
            print("Libro dado de alta correctamente")
        case 2:
            isbn = input("Introduzca ISBN del libro a eliminar: ")
            for book in books:
                if book.isbn == isbn:
                    books.pop(books.index(book))
                    print("Libro eliminado correctamente")
                    break
            else:
                print("El libro no se puede eliminar porque no está en la biblioteca")  
        case 3:
            isbn = input("Introduzca ISBN del libro a buscar:")
            book = libro_en_bib(books, isbn)
            if book:
                print("Datos del libro")
                print(book)
            else:
                print("El libro no está disponible en la biblioteca")
        case 4:
            for book in books:
                print(book)
        case 5:
            print("Ha salido del gestor de la biblioteca. Hasta pronto.")
            break
