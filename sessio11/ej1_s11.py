
def load_figures():
    file = open("figuras.txt", "r")
    count = int(file.readline())

    figures = {}

    for _ in range(count):
        name = file.readline()
        figure = []
        while True:
            line = file.readline()
            if line != "":
                figure.append(line)
            else:
                break
        
        figures[name] = figure
    file.close()
    return figures


print("Cargando fichero figuras.txt ...")

figures = load_figures()
for figure in figures.keys():
    print(figure+"\n")
    for line in figures[figure]:
        print(line)
    print("")