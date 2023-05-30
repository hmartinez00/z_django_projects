from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.TextFileManipulator import TextFileManipulator
from General_Utilities.menu import menu_class
from General_Utilities.option_list import option_list
from modules.django_modifile import settings


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)
files_list = get_py_files(app_path)

file_path = option_list(files_list)

# Crear una instancia de ModelGenerator
object = settings(file_path)
menu_class(object)

# app_path = select_django_apps(app_list)
# app_name = os.path.basename(app_path)
# new_dir = f"os.path.join(BASE_DIR, '{app_name}', 'templates'),"
# object.install_template_dir(new_dir)

input('Presione una tecla para continuar: ')

