import sys
from dominio import *

# Asumimos que Autor, Publicacion, Libro y ArticuloEnRevista están disponibles.

## @brief Clase de utilidad para leer (parsear) un archivo de texto
#  y cargar los datos de publicaciones en un mapa.
class LectorPublicaciones:
    # Delimitadores definidos en el formato
    # Nota: En Python split() usa literales por defecto, no regex,
    # por lo que no hace falta escapar el pipe (|) a menos que usemos el módulo re.
    _DELIM_CAMPO = ";"
    _DELIM_LISTA = "|"
    _DELIM_AUTOR = ":"

    ## @brief Lee un archivo de texto estructurado y lo convierte en un mapa de
    #  objetos Publicacion.
    #  @details Toda la información de una única publicación debe estar en una sola línea.
    #  Los datos de la publicación estarán separados por delimitadores.
    #
    #  A continuación se listan dichos delimitadores:
    #  - **Delimitador de Campo Principal (atributo):** `;` (Punto y coma)
    #  - **Delimitador de Listas (para autores o palabras clave):** `|` (Barra vertical)
    #  - **Delimitador de nombre, apellido de Autor:** `:` (Dos puntos)
    #
    #  ### Formato de Línea LIBRO
    #
    #      TIPO;ID;TITULO;FECHA_AAAAMM;AUTORES;PALABRAS_CLAVE;EDITORIAL
    #
    #  Donde TIPO es "LIBRO".
    #
    #  - **Ejemplo AUTORES:** `"Robert C.:Martin:N/A|Erich:Gamma:N/A"`
    #  - **Ejemplo PALABRAS_CLAVE:** `"design|patterns|gof|oop"`
    #
    #  Ejemplo de línea para Libro:
    #      "LIBRO;LIB-003;Design Patterns...;199410;Erich:Gamma:N/A|...;design|patterns;Addison-Wesley"
    #
    #  @param nombre_archivo El path (ruta) y nombre del archivo a leer.
    #  @return Un diccionario (Dict[str, Publicacion]) donde la clave es el ID de la
    #  publicación.
    @staticmethod
    def leer(nombre_archivo):
        file = open(nombre_archivo, "r")
        pubs = {}
        while True:
            line = file.readline()[:-1]
            if line == "": break

            if line.split(";")[0] == "LIBRO":
                obj, id, title, date, raw_authors, raw_keywords, editorial = line.split(";")
            if line.split(";")[0] == "ARTICULO":
                obj, id, title, date, raw_authors, raw_keywords, revista, impact = line.split(";")

            raw_authors = raw_authors.split("|")
            authors = []
            for au in raw_authors:
                name, surname, institution = au.split(":")
                if institution == "N/A": institution = None
                author = Autor(name, surname, institution)
                authors.append(author)
            
            keywords = raw_keywords.split("|")


            if obj == "LIBRO":
                pubs[id] = Libro(title, id, authors, keywords, date, editorial)
            elif obj == "ARTICULO":
                pubs[id] = ArticuloEnRevista(title, id, authors, keywords, date, float(impact), revista)
        
        return pubs

if __name__ == "__main__":
    lector = LectorPublicaciones
    pubs = LectorPublicaciones.leer("publicaciones.txt")
    for pub in pubs.keys():
        print(pub)
        for author in pubs[pub].get_autores():
            print(author.get_id())