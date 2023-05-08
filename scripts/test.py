import os
from General_Utilities.control_rutas import setting_routes
from modules.insert_list import insert_list, add_string


key = 'resources'
res = setting_routes(key)[0]

project_name = 'proyecto_prueba'
app_name = 'aplicacion'

# Create el listado de directorios
o_directorio = os.path.abspath(res + '/' + project_name)
p_directorio = os.path.abspath(o_directorio + '/' + project_name)
ruta_settings = [
        os.path.join(p_directorio, 'settings.py'),
    ] 

# Instalando la direccion de los templates
print(f'Instalando la direccion de los templates')
print(ruta_settings[0])
pivot_string = "'DIRS': []"
element = f"[os.path.join(BASE_DIR, '{app_name}', 'templates')],"
add_string(ruta_settings[0], pivot_string, element)