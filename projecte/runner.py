from caosdeuso import Controlador
from gestordatos import GestorDeDatos
from comparadores import *
from buscadores import *
from ordenador import Ordenador



# Asumimos que todas las clases anteriores (Controlador, GestorDeDatos,
# Ordenador, Comparadores, Buscadores, Exceptions) están importadas.

## @brief Clase que ejecuta un escenario de prueba predefinido en memoria.
class EjecutorDesdeMemoria:

    ## @brief Constructor.
    #  @details Crea el atributo resultado como una lista vacía.
    def __init__(self):
        self.resultado = []

    ## @brief Obtiene la lista de resultados acumulados.
    #  @return Lista de strings con el toString() de las publicaciones encontradas.
    def get_resultado(self):
        strings = []
        for result in self.resultado:
            strings.append(str(result))
        return strings
    ## @brief Ejecuta el escenario de prueba completo de búsqueda y ordenación.
    #
    #  @details El proceso detallado es el siguiente:
    #  1. Creará un objeto Controlador.
    #  2. Obtendrá las publicaciones invocando al método
    #     GestorDeDatos.cargar_publicaciones_de_prueba().
    #  3. Añadirá estas publicaciones al Controlador.
    #
    #  4. Realizará una búsqueda de publicaciones por el nombre "Geoffrey Hinton".
    #
    #  5. Generará una lista con las publicaciones encontradas ordenadas por
    #     fecha en sentido ascendente.
    #  6. Para cada publicación de la lista generará un String invocando al
    #     método __str__() y lo añadirá al atributo resultado.
    #  7. Generará una lista con las publicaciones encontradas ordenadas por
    #     fecha en sentido descendente.
    #  8. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #  9. Generará una lista con las publicaciones encontradas ordenadas por
    #     autor en sentido ascendente.
    #  10. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #  11. Generará una lista con las publicaciones encontradas ordenadas por
    #     autor en sentido descendente.
    #  12. Para cada publicación de la lista generará un String y lo añadirá al resultado.
    #
    #  13. Realizará una búsqueda de publicaciones por las siguientes palabras
    #     clave: "neural networks" y "optimization" (una sola búsqueda: se buscan
    #     publicaciones que contengan ambos valores).
    #  14. Repetirá los pasos 5 a 12 para la lista de publicaciones obtenidas.
    #
    #  15. Realizará una búsqueda de publicaciones cuya fecha de publicación
    #     esté dentro del intervalo "197001" y "198012".
    #  16. Repetirá los pasos 5 a 12 para la lista de publicaciones obtenidas.
    #
    #  @note PODÉIS DEFINIROS AQUEL(LOS) MÉTODO(S) ADICIONAL(ES) QUE
    #  CONSIDERÉIS OPORTUNO PARA ORGANIZAR EL CÓDIGO DE ESTA CLASE.

    def get_all_sort_type_list(self, publist):
        resultado = []
        
        comparador = ComparadorFechas()
        ordenador = Ordenador(False, comparador)
        sorted_pubs = ordenador.ordena(publist)
        
        for pub in sorted_pubs:
            resultado.append(pub.__str__())

        ordenador = Ordenador(True, comparador)
        sorted_pubs = ordenador.ordena(publist)
        
        for pub in sorted_pubs:
            resultado.append(pub.__str__())

        comparador = ComparadorApellidos()
        ordenador = Ordenador(False, comparador)
        sorted_pubs = ordenador.ordena(publist)

        for pub in sorted_pubs:
            resultado.append(pub.__str__())
        
        ordenador = Ordenador(True, comparador)
        sorted_pubs = ordenador.ordena(publist)

        for pub in sorted_pubs:
            resultado.append(pub.__str__())

        return resultado

    def ejecuta(self):
        controller = Controlador()
        pubs = GestorDeDatos.cargar_publicaciones_de_prueba()
        for pub in pubs.keys():
            controller.add_publicacion(pubs[pub])


        buscador = BuscadorPorNombres()
        buscador.add_nombre("Geoffrey Hinton")
        publist = buscador.busca(controller.get_publicaciones())
        
        self.resultado.extend(self.get_all_sort_type_list(publist))
        
        buscador = BuscadorPorPalabrasClave()
        buscador.add_palabra("neural networks")
        buscador.add_palabra("optimization")
        publist = buscador.busca(controller.get_publicaciones())
        
        self.resultado.extend(self.get_all_sort_type_list(publist))
        
        buscador = BuscadorPorIntervalo("197001", "198012")
        publist = buscador.busca(controller.get_publicaciones())
        
        self.resultado.extend(self.get_all_sort_type_list(publist))




        

if __name__ == "__main__":
    ejecutor = EjecutorDesdeMemoria()
    ejecutor.ejecuta()
