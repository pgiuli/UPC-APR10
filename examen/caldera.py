class Caldera:
    def __init__(self, id_c, CO, temperatura, rendimiento):
        self.id_c = id_c
        self.CO = CO
        self.temperatura = temperatura
        self.rendimiento = rendimiento

    def es_contaminante(self):
        return self.CO/self.temperatura > 0.3 or self.rendimiento < 80

    def __str__(self):
        return f"Caldera ID:{self.id_c}\t\t CO={self.CO}ppm\t\t Temperatura={self.temperatura}ºC\t\t Rendimiento={self.rendimiento}%"

