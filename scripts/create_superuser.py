import os
import sys
import django
from modules.dir_sel import dir_sel
from General_Utilities.control_rutas import setting_routes


key = 'resources'
directorio = setting_routes(key)[0]
project_name = dir_sel(key, 0)[1]

# Create el listado de directorios
o_directorio = os.path.abspath(directorio + '/' + project_name)
p_directorio = os.path.abspath(o_directorio + '/' + project_name)
# a_directorio = os.path.abspath(o_directorio + '/' + app_name)

ruta_settings = [
        os.path.join(p_directorio, 'settings.py'),
        os.path.join(p_directorio, 'urls.py'),
        # os.path.join(a_directorio, 'urls.py'),
        # os.path.join(a_directorio, 'views.py')
    ] 


## Crear Superusuario

# Ruta absoluta del directorio del project_name
PROJECT_DIR = o_directorio

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