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


# Crear una instancia de ModelGenerator
generator = ModelGenerator(file_path, model_name)
print(generator.model_exists())
generator.add_model_class()

generator.add_field()

# Si no existe, agregar la clase del modelo al archivo
# generator.add_field('id', 'AutoField', ['primary_key=True'])
# generator.add_field('name', 'CharField', ["max_length=100"])
# generator.add_field('age', 'IntegerField')

# Obtener los campos existentes en el modelo
existing_fields = generator.get_existing_fields()
print("Campos existentes:", existing_fields)

generator.remove_field()

# # Agregar un nuevo campo al modelo
# if 'email2' not in existing_fields:
#     generator.add_field('email', 'EmailField')

# # Eliminar un campo del modelo
# if 'name2' in existing_fields:
#     generator.remove_field('name2')
