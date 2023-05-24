from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_models import ModelGenerator
from General_Utilities.menu import menu_class


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

# print(file_path)
# # Obtener todos los componentes de la ruta como una lista
# componentes = os.path.normpath(file_path).split(os.sep)
# print(componentes[-2])
# project_path2 = os.path.join(*componentes[:-2])
# print(project_path2)
# input('Presione una tecla para continuar: ')

# Creando el modelo
model_name = input('Introduzca el nombre del modelo: ')

# Crear una instancia de ModelGenerator
generator = ModelGenerator(file_path, model_name)
menu_class(generator)

# print(generator.model_exists())
# generator.add_model_class()

# # Si no existe, agregar la clase del modelo al archivo
# generator.add_field('id', 'AutoField', ['primary_key=True'])
# generator.add_field('name', 'CharField', ["max_length=100"])
# generator.add_field('age', 'IntegerField')
