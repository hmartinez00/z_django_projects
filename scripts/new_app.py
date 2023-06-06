import os
import subprocess
from modules.django_rootes import *
from General_Utilities.control_rutas import setting_routes
from modules.django_modifile import settings
from modules.django_modifile import urls


app_name = 'appEmpresaDjango'

key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)


# 1. Creando la App. Ejecutar los comandos usando subprocess
print(f'Creando la aplicacion: {app_name}')
os.chdir(project_path)
subprocess.run(["python", "manage.py", "startapp", app_name])
# subprocess.run(["python", "manage.py", "migrate"])


# 2. Instala la app, crea el directorio de templates e instala el directorio.
# Crear una instancia de settings, 
object = settings(project_path)
print(f'Instalando la app en settings.py.')
object.install_app(app_name)
print(f'Instalando la direccion de los templates.')
# Importamos modulo os.
object.import_os()
# Instala la ruta de templates en settings.
new_dir = f"os.path.join(BASE_DIR, '{app_name}', 'templates')"
object.install_template_dir(new_dir)
# Creamos el directorio de templates de la app.
print('Creando el directorio templates de la app.')
app_path = os.path.join(project_path, app_name)
urls_path = os.path.join(app_path, 'templates')
if os.path.exists(urls_path):
    print('\t- Directorio de templates ya existe.')
else:
    os.mkdir(urls_path)


# 3. Actualizamos urls.py del proyecto
# Crear una instancia de urls, 
object = urls(project_path, app_name)
print(f'Modificando urls.py\nImportando funcion include.')
# Importamos funcion include.
object.import_include()
# Instalamos en urlpatterns.
print(f'Registro en urlpatterns.')
object.reg_url_app_project()


# 4. Creamos el archivo urls.py de la aplicacion
object.reg_url_app_app()

os.chdir(path)


input('Presione una tecla para continuar: ')