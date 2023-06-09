import os
from modules.django_rootes import *
from General_Utilities.control_rutas import setting_routes
from modules.django_modifile import settings
from modules.django_modifile import urls


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_project(app_list)

