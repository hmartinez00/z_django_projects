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
        find_substring_in_list(files_list, 'admin.py'),
    ]

file_path = ruta_settings[1]
pivot_substring = 'from .models import *'
line_num = find_pivot_substring(file_path, pivot_substring)
print(line_num)
if line_num == None:
    line_num = 1
    add_substring_to_line(file_path, line_num, pivot_substring)

model_name = input('Introduzca el nombre del modelo: ')
file_path = ruta_settings[0]
generator = ModelGenerator(file_path, model_name)
menu_class(generator)
# print(generator.get_existing_class())
# print(generator.update_admin_file())

input('Presione una tecla para continuar: ')