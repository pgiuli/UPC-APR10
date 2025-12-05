from abc import ABC, abstractmethod



## @brief Función de comparación que impone un orden total sobre una colección de objetos.
#  @details Esta interfaz es el equivalente en Python a java.util.Comparator.
#

class Comparator(ABC):
    ## @brief Compara sus dos argumentos para determinar el orden. NO LO MODIFIQUÉIS
    #  @details Devuelve un entero negativo, cero o un entero positivo si el primer
    #  argumento es menor, igual o mayor que el segundo, respectivamente.
    #
    #  El implementador debe asegurar que el signo de:
    #  compare(x, y) sea opuesto al de compare(y, x).
    #
    #  @param o1 El primer objeto a comparar.
    #  @param o2 El segundo objeto a comparar.
    #  @return Un entero negativo, cero o un entero positivo según si o1 es
    #  menor, igual o mayor que o2.
    @abstractmethod
    def compare(self,o1,o2):
        pass


from typing import Optional,List


# Asumimos que Comparator, Publicacion y Autor están disponibles

## @brief Implementación de Comparator para ordenar objetos Publicacion.
#  @details La comparación se basa en el autor de cada publicación que tenga el
#  apellido lexicográficamente menor (el primero en orden alfabético).
class ComparadorApellidos(Comparator):

    ## @brief Método de utilidad para encontrar el apellido lexicográficamente
    #  menor (el primero alfabéticamente) en la lista de autores de
    #  una publicación.
    #
    #  @param pub La publicación de la cual extraer los autores.
    #  @return El apellido lexicográficamente menor, o None si la
    #  publicación no tiene autores o ningún autor tiene apellido.
    def get_primer_apellido(self,pub):
        autores = pub.get_autores()
        surnames = []
        for autor in autores:
            surnames.append(autor.get_apellidos())
        surname = min(surnames)
        return surname

    ## @brief Compara dos publicaciones basándose en el primer apellido (según orden
    #  alfabético) de sus respectivas listas de autores.
    #  @details Para cada publicación (p1 y p2), primero encuentra el autor cuyo
    #  apellido sea lexicográficamente el menor. Luego, compara esos
    #  dos apellidos resultantes.
    #
    #  @param p1 La primera publicación a comparar.
    #  @param p2 La segunda publicación a comparar.
    #  @return Un valor negativo si el apellido de p1 es anterior,
    #  positivo si es posterior, o 0 si son iguales o si ambas no tienen autores.
    def compare(self,p1,p2):
        p1_surname = get_primer_apellido(p1)
        p2_surname = get_primer_apellido(p2)

        if p1_surname < p2_surname:
            return -1
        elif p2_surname < p1_surname:
            return 1
        else:
            return 0





from typing import Optional


# Asumimos que Comparator y Publicacion están disponibles

## @brief Implementación de Comparator para ordenar objetos Publicacion
#  basándose en su atributo de fecha (formato "AAAAMM").
class ComparadorFechas(Comparator):

    ## @brief Compara dos publicaciones basándose en sus fechas ("AAAAMM").
    #  @details Si ambas fechas (obtenidas de p1 y p2) son distintas de None,
    #  el método retorna un entero negativo si la fecha de p1 es anterior
    #  a la de p2, cero si las fechas son iguales, o un entero positivo
    #  si la fecha de p1 es posterior a la de p2.
    #
    #  El método también maneja los casos en que una o ambas fechas
    #  sean nulas (asumiendo que nulo es "menor" que cualquier fecha).
    #
    #  @param p1 La primera publicación a comparar.
    #  @param p2 La segunda publicación a comparar.
    #  @return Un entero negativo si la fecha de p1 es anterior a la de p2,
    #  cero si las fechas son iguales,
    #  o un entero positivo si la fecha de p1 es posterior a la de p2.
    def compare(self,p1,p2):

        fecha1 = p1.get_fetcha()
        fecha2 = p2.get_fecha()

        if fecha1 is not None and fecha2 is not None:
            return int(fecha1) - int(fecha2)
        else:
            if fecha1 is None and fecha2 is not None:
                return -1
            elif fecha2 is None and fecha1 is not None:
                return 1
            else:
                return 0
