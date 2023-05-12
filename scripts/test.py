from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from modules.django_rootes import *
import os


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
print(projects_list)
project_path = select_django_project(projects_list)
print(project_path)

apps_list = get_django_apps(project_path)
print(apps_list)
app_path = select_django_apps(apps_list)
print(app_path)

files_list = get_py_files(app_path)
print(files_list)

file = find_substring_in_list(files_list, 'settings.py')
print(file)