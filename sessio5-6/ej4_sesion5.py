def imp_hist(num):
    print("*"*num)

for i in input("Introduzca los valores del histograma separados por un espacio en blanco: ").split(" "):
    imp_hist(int(i))