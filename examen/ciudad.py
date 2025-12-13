class Ciudad:
    def __init__(self, id_ciudad):
        self.id_ciudad = id_ciudad
        self.calderas = {}

    def anyade_caldera(self, caldera):
        if caldera.id_c in self.calderas.keys():
            return False
        self.calderas[caldera.id_c] = caldera
        return True

    def calderas_contaminantes(self):
        contaminantes = []
        for id_c in self.calderas.keys():
            caldera = self.calderas[id_c]
            if caldera.es_contaminante():
                contaminantes.append(caldera)

        return contaminantes

    def max_CO(self):
        max_CO_val = 0
        ids_calderas = []
        for id_c in self.calderas.keys():
            caldera = self.calderas[id_c]
            if caldera.CO > max_CO_val:
                max_CO_val = caldera.CO
                ids_calderas = list()
                ids_calderas.append(caldera.id_c)
            elif caldera.CO == max_CO_val:
                ids_calderas.append(caldera.id_c)

        return max_CO_val, ids_calderas

    def __str__(self):
        outstring = f"""
Ciudad: {self.id_ciudad}
Mediciones Calderas:
"""
        for id_c in self.calderas.keys():
            caldera = self.calderas[id_c]
            outstring += str(caldera)+"\n"
        return outstring