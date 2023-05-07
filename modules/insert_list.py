def insert_list(ruta_settings, pivot_string, element):

    # leemos el archivo settings.py
    with open(ruta_settings, 'r') as archivo:
        lineas = archivo.readlines()

    # buscamos la posición de pivot_string
    posicion = None
    for i in range(len(lineas)):
        if pivot_string in lineas[i]:
            posicion = i
            break

    # agregamos la nueva aplicación en la posición deseada
    if posicion is not None:
        lineas[posicion] = lineas[posicion].rstrip()[:-1] + "[\n\t'" + element + "'," + lineas[posicion][-1]
    else:
        print(f'No se encontró la lista {pivot_string} en el archivo indicado.')


    # escribimos las líneas actualizadas en el archivo
    with open(ruta_settings, 'w') as archivo:
        archivo.writelines(lineas)

    print(f'La aplicación se ha agregado correctamente a {pivot_string}.')
