from caldera import Caldera
from ciudad import Ciudad

city_name = "Barcelona"
ciudad = Ciudad(city_name)


def menu():
    return int(input(
f"""
Análisis calderas de la ciudad de {ciudad.id_ciudad}
1. Añade caldera
2. Listado calderas contaminantes
3. Máxima medición de dióxido de carbono (CO)
4. Mostrar datos calderas
5. Salir
Introduce una opción: """))


while True:
    option = menu()

    if option == 1:
        data = input("Introduce información caldera [ID:CO:temperatura:rendimiento]: ")
        id_c, CO, temperatura, rendimiento = data.split(":")

        caldera = Caldera(id_c, float(CO), float(temperatura), float(rendimiento))
        if ciudad.anyade_caldera(caldera):
            print("Caldera añadida correctamente")
        else:
            print("Una caldera con este identificador ya existe")


    elif option == 2:
        print("Mediciones calderas contaminantes:")
        for caldera in ciudad.calderas_contaminantes():
            print(caldera)

    elif option == 3:
        max_co, ids_calderas_maxco = ciudad.max_CO()
        if len(ids_calderas_maxco) == 1:
            pluralstring = "la caldera"
        elif len(ids_calderas_maxco) > 1:
            pluralstring = "las calderas"
        if ids_calderas_maxco == []:
            print("No hay ninguna caldera en la ciudad")
            continue

        idsstring = " ".join((ids_calderas_maxco))
        string = f"La máxima medición de monóxido de carbono es {max_co}ppm, y ha sido realizado por {pluralstring} {idsstring}"

        print(string)

    elif option == 4:
        print(ciudad)

    elif option == 5:
        print("Hasta pronto!")
        break
    else:
        print("Opción incorrecta.")




