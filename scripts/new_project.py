import os
from General_Utilities.control_rutas import setting_routes
from modules.django_modifile import settings


project_name = 'miProyecto'

key = 'resources'
directorio = setting_routes(key)[0]

os.chdir(directorio)
print(os.getcwd())

# Create Django project
os.system(f"django-admin startproject {project_name}")

# Agregando directorio static files
project_path = os.path.join(directorio, project_name)

sub_dirs = ['css', 'js', 'img']
for i in sub_dirs:
    urls_path = os.path.join(project_path, 'static', i)
    if os.path.exists(urls_path):
        print(f'\t- Directorio de static/{i} ya existe.')
    else:
        os.makedirs(urls_path)

# Instalando static en settings
object = settings(project_path)
object.install_static_dir()
