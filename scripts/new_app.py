import os
import subprocess
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.control_rutas import setting_routes
from modules.django_modifile import settings


app_name = 'appTiendaDjango'

key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)
app_path = os.path.join(project_path, project_name)
files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'settings.py'),
        find_substring_in_list(files_list, 'urls.py'),
    ]   

# Creando la App. Ejecutar los comandos usando subprocess
print(f'Creando la aplicacion: {app_name}')
os.chdir(project_path)
subprocess.run(["python", "manage.py", "startapp", app_name])
# subprocess.run(["python", "manage.py", "migrate"])



# Instalando la app, creando el directorio de templates e
# instalando el directorio.

# Crear una instancia de settings, 
object = settings(project_path)
print(f'Instalando la app en settings.py.')
object.install_app(app_name)
print(f'Instalando la direccion de los templates.')
# Importamos modulo os.
object.import_os()
new_dir = f"os.path.join(BASE_DIR, '{app_name}', 'templates')"
object.install_template_dir(new_dir)
print('Creando el directorio templates de la app.')
app_path = os.path.join(project_path, app_name)
urls_path = os.path.join(app_path, 'templates')
if os.path.exists(urls_path):
    print('\t- Directorio de templates ya existe.')
else:
    os.mkdir(urls_path)

input('Presione una tecla para continuar: ')


# Actualizamos urls.py del proyecto
print(f'Modificando urls.py')
print(ruta_settings[1])
file_path = ruta_settings[1]
pivot_substring = 'from django.urls import path'
old_substring = pivot_substring
new_substring = 'from django.urls import path, include'
replace_substring_in_line(file_path, pivot_substring, old_substring, new_substring)
element = f"path('{app_name}/', include('{app_name}.urls'))"
pivot_substring = 'urlpatterns = '
new_substring = "[\n\t" + element + ","
append_substring_to_line(file_path, pivot_substring, new_substring)

# Creamos urls.py de la aplicacion
ruta_settings.append(
        os.path.join(project_path, app_name, 'urls.py')
    )

print(f'Creando {app_name}/urls.py')
urls_path = ruta_settings[2]
content = '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
'''
if not os.path.isfile(urls_path):
    with open(urls_path, "w") as f:
        f.write(content)

os.chdir(path)