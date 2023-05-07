import os
from General_Utilities.control_rutas import setting_routes
from modules.settings_modify import settings_modify


key = 'resources'
directory = setting_routes(key)[1]

project_name = 'proyecto_prueba'

directorio = os.path.abspath(directory)
os.chdir(directorio)
print(os.getcwd())

# Create Django project
os.system(f"django-admin startproject {project_name}")