class ExpresionHoraria:
    def __init__(self, horas, mins, segs):
        self.horas = horas
        self.mins = mins
        self.segs = segs
    def __str__(self):
        return f"{self.horas}:{"0" + str(self.mins) if self.mins < 10 else self.mins}:{"0" + str(self.segs) if self.segs < 10 else self.segs}"
    def seg_medianoche(self):
        delta = 0
        if self.horas >= 12:
            delta += 3600 * (23-self.horas)
            delta += 60 * (59-self.mins)
            delta += 60 - self.segs
        else:
            delta += 3600 * self.horas
            delta += 60 * self.mins
            delta += self.segs
        return delta