from expresionHoraria import ExpresionHoraria

vals = input("Introduzca primera hora: ").split(":")
time1 = ExpresionHoraria(int(vals[0]), int(vals[1]), int(vals[2]))
vals = input("Introduzca segunda hora: ").split(":")
time2 = ExpresionHoraria(int(vals[0]), int(vals[1]), int(vals[2]))
print(f"La expresión horaria más cercana a media noche: {time1.__str__() if time1.seg_medianoche() < time2.seg_medianoche() else time2.__str__()}")