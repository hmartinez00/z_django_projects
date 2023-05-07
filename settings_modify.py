import os

# ruta del archivo settings.py
ruta_settings = os.path.join('proyecto_prueba/proyecto_prueba', 'settings.py')

# definimos la aplicación a agregar
nueva_aplicacion = "aplicacion"

# leemos el archivo settings.py
with open(ruta_settings, 'r') as archivo:
    lineas = archivo.readlines()

# buscamos la posición de INSTALLED_APPS
posicion = None
for i in range(len(lineas)):
    if 'INSTALLED_APPS' in lineas[i]:
        posicion = i
        break

# agregamos la nueva aplicación en la posición deseada
if posicion is not None:
    lineas[posicion] = lineas[posicion].rstrip()[:-1] + "[\n\t'" + nueva_aplicacion + "'," + lineas[posicion][-1]
else:
    print('No se encontró la lista INSTALLED_APPS en el archivo settings.py')


# escribimos las líneas actualizadas en el archivo
with open(ruta_settings, 'w') as archivo:
    archivo.writelines(lineas)

print('La aplicación se ha agregado correctamente a INSTALLED_APPS.')
