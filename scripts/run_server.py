import os
from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)

os.chdir(project_path)

# Correr el servidor
os.system('python .\manage.py runserver')