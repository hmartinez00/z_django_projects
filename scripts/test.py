import os
from General_Utilities.control_rutas import setting_routes
# from modules.insert_list import insert_list, add_string
from modules.modifile import *


key = 'resources'
res = setting_routes(key)[0]

project_name = 'proyecto_prueba'
app_name = 'aplicacion'

# Create el listado de directorios
o_directorio = os.path.abspath(res + '/' + project_name)
p_directorio = os.path.abspath(o_directorio + '/' + project_name)
ruta_settings = [
        os.path.join(p_directorio, 'settings.py'),
        os.path.join(p_directorio, 'urls.py'),
    ] 

# Actualizamos urls.py del proyecto
print(f'Modificando {project_name}/urls.py')
print(ruta_settings[1])
# pivot_string = 'urlpatterns ='
# element = f"path('{app_name}/', include('{app_name}.urls'))"
# insert_list(ruta_settings[1], pivot_string, element)

file_path = ruta_settings[1]
pivot_substring = "urlpatterns = ["
new_substring = "[\n\t" + f"path('{app_name}/', include('{app_name}.urls')),"
append_substring_to_line(file_path, pivot_substring, new_substring)


# pivot_string = 'from django.urls import path'
# sub_string = 'h, include'
# add_string(ruta_settings[1], pivot_string, sub_string)  
