from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_modifile import TextFileManipulator
from General_Utilities.menu import menu_class
from General_Utilities.option_list import option_list


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

files_list = get_py_files(app_path)

file_path = option_list(files_list)

# Crear una instancia de ModelGenerator
generator = TextFileManipulator(file_path)
menu_class(generator)

input('Presione una tecla para continuar: ')

