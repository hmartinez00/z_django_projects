import os
from modules.dir_sel import dir_sel
from modules.insert_list import insert_list


def settings_modify(nueva_aplicacion, directorio = None):

    if directorio == None:
        key = 'resources'
        res = dir_sel(key, 1)
        directorio = os.path.abspath(res[0] + '/' + res[1])

    ruta_settings = os.path.join(directorio, 'settings.py')

    print(ruta_settings)

    pivot_string = 'INSTALLED_APPS'
    element = nueva_aplicacion

    insert_list(ruta_settings, pivot_string, element)