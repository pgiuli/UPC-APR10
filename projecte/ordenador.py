from typing import List


# Asumimos que Comparator y Publicacion están disponibles.

## @brief Clase que ordena una lista de objetos Publicacion utilizando
#  una estrategia de comparación (Comparator) y el algoritmo de la burbuja.
#  @details Esta clase NO modifica la lista original que recibe, sino que devuelve
#  una nueva lista con los elementos ordenados.
class Ordenador:

    ## @brief Constructor de la clase Ordenador.
    #
    #  @param descendente True si la ordenación debe ser en sentido descendente
    #  (mayor a menor), False si debe ser en sentido ascendente (menor a mayor).
    #  @param comparador El Comparator (p.ej., ComparadorAutores, ComparadorFecha)
    #  que se utilizará para ordenar la lista.
    def __init__(self,descendente,comparador):
        self.descendente = descendente
        self.comparador = comparador

    ## @brief Ordena la lista de publicaciones proporcionada utilizando el algoritmo
    #  de la burbuja (Bubble Sort).
    #  @details El método utiliza el comparador definido en el atributo de la
    #  clase y respeta el sentido (ascendente/descendente) del atributo descendente.
    #
    #  Este método NO modifica la lista original pasada como argumento.
    #
    #  @param publicaciones La lista de objetos Publicacion a ordenar.
    #  @return Una <b>nueva</b> lista que contiene las publicaciones ordenadas.
    def ordena(self,publicaciones):
        pubs = publicaciones.copy()

        #Bubble sort implementation:
        for _ in len(pubs):
            for i in range(len(pubs)-1):
                pub1 = pubs[i]
                pub2 = pubs[i+1]
                order = self.comparador.compare(pub1, pub2)
                if order > 0:
                    pubs[i+1] = pub1
                    pubs[i] = pub2
        
        if self.descendente:
            return pubs[::-1]
        return pubs




    # --- Getters y Setters ---

    ## @brief Asigna el comparador.
    #  @param comparador El nuevo comparador a utilizar.
    def set_comparador(self,comparador):
        self.comparador = comparador

    ## @brief Devuelve el valor de descendente.
    #  @return True si es descendente, False si es ascendente.
    def is_descendente(self):
        return self.descendente

    ## @brief Asigna valor a descendente.
    #  @param descendente Nuevo valor de descendente.
    def set_descendente(self,descendente):
        self.descendente = descendente

    ## @brief Obtiene el comparador actual.
    #  @return El Comparator usado para ordenar.
    def get_comparador(self):
        return self.comparador
