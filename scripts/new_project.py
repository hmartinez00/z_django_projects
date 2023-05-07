import os
from General_Utilities.control_rutas import setting_routes
from modules.settings_modify import settings_modify


key = 'resources'

directory = setting_routes(key)[1]

project_name = 'proyecto_prueba'
app_name = 'aplicacion'

directorio = os.path.abspath(directory)
os.chdir(directorio)
print(os.getcwd())

# Create Django project
os.system(f"django-admin startproject {project_name}")

directorio = os.path.abspath(directory + '/' + project_name)
os.chdir(directorio)
print(os.getcwd())

# Create Django app
os.system(f"python manage.py startapp {app_name}")
os.system("python .\manage.py migrate")

settings_modify(app_name)