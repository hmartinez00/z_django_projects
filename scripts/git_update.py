import os
from General_Utilities.control_rutas import setting_routes
from Pku_module.Package_update_module import auto_commit
from General_Utilities.option_list import option_list
from Pku_module.Package_update_module import listar_paquetes
from modules.django_rootes import *

# directory = os.getcwd()

# key = 'resources'
# path = setting_routes(key)[0]

# projects_list   = get_django_projects(path)
# project_path    = select_django_project(projects_list)
# apps_list       = get_django_apps(project_path)
# app_path        = select_django_apps(apps_list)

# os.chdir(project_path)
# opciones = os.listdir()
# project = option_list(opciones)
# auto_commit(project)
auto_commit()

# os.chdir(directory)