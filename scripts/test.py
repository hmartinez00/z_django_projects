import os
from modules.dir_sel import dir_sel
from modules.insert_list import add_string, insert_list


key = 'resources'
res = dir_sel(key, 1)
directorio = os.path.abspath(res[0] + '/' + res[1])

nueva_aplicacion = 'aplicacion'

ruta_settings = [
        os.path.join(directorio, 'settings.py'),
        os.path.join(directorio, 'urls.py')
    ]

print(ruta_settings)

print(ruta_settings[1])

pivot_string = 'urlpatterns ='
element = f"path('{nueva_aplicacion}/', include('{nueva_aplicacion}.urls'))"
insert_list(ruta_settings[1], pivot_string, element)