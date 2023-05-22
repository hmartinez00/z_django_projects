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
# new_content = f'''
# def {view_name}(request):
#     return render(request, '{view_name}.html')
# '''
new_content = f'''from django.http import HttpResponse

def {view_name}(request):
    return HttpResponse('Listado de departamentos')
'''
append_to_file(file_path, new_content)

# Actualizamos urls.py de la aplicacion
if view_name != 'index':
    print(f'Modificando urls.py')
    file_path = ruta_settings[1]
    element = f"path('{view_name}/', views.{view_name}, name='{view_name}')"
    pivot_substring = 'urlpatterns = '
    new_substring = "[\n\t" + element + ","
    append_substring_to_line(file_path, pivot_substring, new_substring)


# # Añadir el template
# print('Agregamos el template')
# urls_path = os.path.join(app_path, 'templates')
# if os.path.exists(urls_path):
#     pass
# else:
#     os.mkdir(urls_path)
# file_path = os.path.join(urls_path, f'{view_name}.html')
# new_content = f'''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{view_name}</title>
# </head>
# <body>
#     <h1>{view_name}</h1>
    
# </body>
# </html>
# '''
# if not os.path.isfile(file_path):
#     replace_file_content(file_path, new_content)

# # Ejecutando migraciones
# print(f'Ejecutando migraciones en: {app_name}')
# os.chdir(project_path)
# subprocess.run(["python", "manage.py", "makemigrations", app_name])
# subprocess.run(["python", "manage.py", "migrate"])
