import os
from modules.dir_sel import dir_sel
from modules.insert_list import add_string, insert_list


def add_app(nueva_aplicacion, directorio = None):

    if directorio == None:
        key = 'resources'
        res = dir_sel(key, 1)
        directorio = os.path.abspath(res[0] + '/' + res[1])

    ruta_settings = [
            os.path.join(directorio, 'settings.py'),
            os.path.join(directorio, 'urls.py')
        ]

    # Agregamos la aplicacion
    print(ruta_settings[0])
    pivot_string = 'INSTALLED_APPS'
    element = nueva_aplicacion
    insert_list(ruta_settings[0], pivot_string, element)

    # Actualizamos urls.py del proyecto
    print(ruta_settings[1])

    pivot_string = 'urlpatterns ='
    element = f"path('{nueva_aplicacion}/', include('{nueva_aplicacion}.urls'))"
    insert_list(ruta_settings[1], pivot_string, element)

    pivot_string = 'from django.urls import path'
    sub_string = 'h, include'
    add_string(ruta_settings[1], pivot_string, sub_string)
