import os
import subprocess
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.control_rutas import setting_routes


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
apps_list = get_django_apps(project_path)
app_path = select_django_apps(apps_list)
files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'views.py'),
        find_substring_in_list(files_list, 'urls.py'),
    ]

print(ruta_settings)

# # Creando la App. Ejecutar los comandos usando subprocess
# print(f'Creando la aplicacion: {app_name}')
# os.chdir(project_path)
# subprocess.run(["python", "manage.py", "startapp", app_name])
# subprocess.run(["python", "manage.py", "migrate"])
