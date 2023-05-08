def add_string(ruta_settings, pivot_string, sub_string):

    # leemos el archivo settings.py
    with open(ruta_settings, 'r') as archivo:
        lineas = archivo.readlines()

    # buscamos la posición de pivot_string
    posicion = None
    for i in range(len(lineas)):
        if pivot_string in lineas[i]:
            posicion = i
            break

    # agregamos la nueva sub_string
    if posicion is not None:
        if sub_string not in lineas[posicion]:
            lineas[posicion] = lineas[posicion].rstrip()[:-1] + sub_string + lineas[posicion][-1]
        else:
            pass
    else:
        print(f'No se encontró la cadena pivote {pivot_string} en el archivo indicado.')


    # escribimos las líneas actualizadas en el archivo
    with open(ruta_settings, 'w') as archivo:
        archivo.writelines(lineas)

    print(f'La subcadena se ha agregado correctamente!')



def insert_list(ruta_settings, pivot_string, element):

    sub_string = "[\n\t'" + element + "',"
    add_string(ruta_settings, pivot_string, sub_string)
    