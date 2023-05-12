import os
import sys
import django
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *



key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)

## Crear Superusuario

# Ruta absoluta del directorio del project_name
PROJECT_DIR = project_path

# Agregar la ruta del project_name al path de python
sys.path.append(PROJECT_DIR)

# Configurar las settings de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_name + '.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario
User.objects.create_superuser(
    username='hmartinez',
    email='hectoralonzomartinez00@gmail.com',
    password='pyp8r5',
)