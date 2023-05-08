import os
import subprocess
from General_Utilities.control_rutas import setting_routes
from modules.modifile import *


def add_app2(project_name, app_name):

    key = 'resources'
    res = setting_routes(key)[0]

    # Create el listado de directorios
    o_directorio = os.path.abspath(res + '/' + project_name)
    p_directorio = os.path.abspath(o_directorio + '/' + project_name)
    a_directorio = os.path.abspath(o_directorio + '/' + app_name)

    ruta_settings = [
            os.path.join(p_directorio, 'settings.py'),
            os.path.join(p_directorio, 'urls.py'),
            os.path.join(a_directorio, 'urls.py'),
            os.path.join(a_directorio, 'views.py')
        ]   

    # Creando la App. Ejecutar los comandos usando subprocess
    print(f'Creando la aplicacion: {app_name}')
    manage_py_path = os.path.join(o_directorio, "manage.py")
    os.chdir(o_directorio)
    subprocess.run(["python", manage_py_path, "startapp", app_name])
    subprocess.run(["python", manage_py_path, "migrate"])

    # Agregamos la aplicacion
    print(f'Instalando en {project_name}/settings.py')
    print(ruta_settings[0])
    file_path = ruta_settings[0]
    pivot_substring = 'INSTALLED_APPS'
    new_substring = "[\n\t'" + app_name + "',"
    append_substring_to_line(file_path, pivot_substring, new_substring)

    # Instalando la direccion de los templates
    print(f'Instalando la direccion de los templates')
    print(ruta_settings[0])
    file_path = ruta_settings[0]
    pivot_substring = "'DIRS': "
    old_substring = '[]'
    new_substring = '[\n]'
    replace_substring_in_line(file_path, pivot_substring, old_substring, new_substring)

    # Actualizamos urls.py del proyecto
    print(f'Modificando {project_name}/urls.py')
    print(ruta_settings[1])
    pivot_string = 'urlpatterns ='
    element = f"path('{app_name}/', include('{app_name}.urls'))"
    insert_list(ruta_settings[1], pivot_string, element)

    pivot_string = 'from django.urls import path'
    sub_string = 'h, include'
    add_string(ruta_settings[1], pivot_string, sub_string)  

    # Creamos urls.py de la aplicacion
    print(f'Creando {app_name}/urls.py')
    urls_path = ruta_settings[2]
    content = '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
    '''
    if not os.path.isfile(urls_path):
        with open(urls_path, "w") as f:
            f.write(content)