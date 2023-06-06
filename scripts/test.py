import os
from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)
app_name = os.path.basename(app_path)

# Agregando directorio static
sub_dirs = ['css', 'js', 'img']
for i in sub_dirs:
    urls_path = os.path.join(project_path, 'static', i)
    if os.path.exists(urls_path):
        print(f'\t- Directorio de static/{i} ya existe.')
    else:
        os.makedirs(urls_path)

print(urls_path)


input('Presione una tecla para continuar: ')

