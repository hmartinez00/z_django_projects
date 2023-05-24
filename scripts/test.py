from modules.django_models import ModelGenerator
import inspect
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.menu import get_method_tags, menu_class, request
from General_Utilities.control_rutas import setting_routes
from modules.django_models import ModelGenerator


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

app_name = os.path.basename(app_path)

files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'models.py'),
    ]

file_path = ruta_settings[0]

# Creando el modelo
model_name = input('Introduzca el nombre del modelo: ')

# Crear una instancia de ModelGenerator
generator = ModelGenerator(file_path, model_name)
menu_class(generator)
input('Presione una tecla para continuar: ')