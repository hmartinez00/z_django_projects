import os
from General_Utilities.control_rutas import setting_routes

project_name = 'proyecto_prueba'

key = 'resources'
directorio = setting_routes(key)[0]

os.chdir(directorio)
print(os.getcwd())

# Create Django project
os.system(f"django-admin startproject {project_name}")