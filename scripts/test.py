import os
from modules.django_rootes import *
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes
from General_Utilities.menu import menu_class
from modules.django_modelsviews import models


# key = 'resources'
# path = setting_routes(key)[0]

app_list = list(project_settings()['Apps'].keys())
app_name = option_list(app_list)

print(app_name)

# projects_list   = get_django_projects(path)
# project_path    = select_django_project(projects_list)
# project_name    = os.path.basename(project_path)
# app_list        = get_django_apps(project_path)
# app_path        = select_django_project(app_list)
# app_name        = os.path.basename(app_path)


# object = models(project_path, app_name)
# menu_class(object)

# input('Presiones una tecla para continuar: ')