from modules.create_superuser import create_superuser
from General_Utilities.control_rutas import setting_routes

key = 'resources'

directory = setting_routes(key)[0]

project_name = 'proyecto_prueba'

# Crear Superusuario
create_superuser(directory, project_name)