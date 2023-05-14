import os
import subprocess
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.control_rutas import setting_routes


view_name = 'index'

key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
apps_list = get_django_apps(project_path)
app_path = select_django_apps(apps_list)
app_name = os.path.basename(app_path)
files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'views.py'),
        find_substring_in_list(files_list, 'urls.py'),
    ]

# Actualizamos views.py
print('Actualizamos views.py')
file_path = ruta_settings[0]

print(file_path)
new_content = f'''\n
def {view_name}(request):
    return render(request, '{view_name}.html')
'''
append_to_file(file_path, new_content)
