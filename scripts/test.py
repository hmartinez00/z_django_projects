from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list
from modules.django_rootes import *
import os


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
print(projects_list)
project_path = select_django_project(projects_list)
print(project_path)

app_name = 'aplicacion'

# Creamos la carpeta de templates
print(f'Creando {app_name}/template/index.html')
urls_path = os.path.join(project_path, app_name, 'template')
os.mkdir(urls_path)
content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    <h1>Inicio</h1>
    
</body>
</html>
'''
urls_path = os.path.join(project_path, app_name, 'template', 'index.html')
if not os.path.isfile(urls_path):
    with open(urls_path, "w") as f:
        f.write(content)