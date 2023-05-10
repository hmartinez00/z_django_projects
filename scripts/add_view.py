import os
import subprocess
from modules.insert_list import add_string, insert_list
from General_Utilities.control_rutas import setting_routes


def add_view(project_name, app_name):

    key = 'resources'
    res = setting_routes(key)[0]

    # Create el listado de directorios
    o_directorio = os.path.abspath(res + '/' + project_name)
    p_directorio = os.path.abspath(o_directorio + '/' + project_name)
    a_directorio = os.path.abspath(o_directorio + '/' + app_name)

    ruta_settings = [
            os.path.join(p_directorio, 'settings.py'),
            os.path.join(p_directorio, 'urls.py'),
            os.path.join(a_directorio, 'urls.py'),
            os.path.join(a_directorio, 'views.py')
        ]
    
    # Modificamos views.py de la aplicacion
    print(f'Modificando {app_name}/views.py')
    views_path = ruta_settings[3]
    content = '''from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    '''
    with open(views_path, "w") as f:
        f.write(content)