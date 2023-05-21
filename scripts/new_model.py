import os
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from modules.django_models import ModelGenerator


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'models.py'),
    ]

file_path = ruta_settings[0]

# Creando el modelo
model_name = input('Introduzca el nombre del modelo: ')


res = ModelGenerator(file_path, model_name).model_exists()

print(res)