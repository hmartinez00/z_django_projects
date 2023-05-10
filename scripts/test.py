from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from modules.django_rootes import *


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
print(project_path)
app_list = get_django_apps(project_path)
print(app_list)
# app_name = option_list(app_list)

# print(get_project_and_app_py_files(project_path, app_name))
