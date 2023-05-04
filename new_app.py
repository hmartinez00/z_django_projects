import os
import sys
import re
import django
from django.conf import settings
from django.core.management import call_command

ruta = r'C:\Users\Hector\Documents\0 - A Repositorios GitHub\z_django_projects\proyecto'
proyecto = 'proyecto'


# Agregar la ruta del proyecto al path de Python
sys.path.append(ruta)

# Importar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', proyecto + '.settings')
django.setup()
# settings.configure()

# Definir el nombre de la nueva aplicación
nueva_app = 'verificacion'

# Crear el directorio templates si no existe
if not os.path.exists(os.path.join(settings.BASE_DIR, nueva_app, 'templates')):
    os.makedirs(os.path.join(settings.BASE_DIR, nueva_app, 'templates'))
    # Crear un archivo de plantilla básica
    with open(os.path.join(settings.BASE_DIR, nueva_app, 'templates', 'base.html'), 'w') as f:
        f.write('<html><head><title>{% block title %}Título{% endblock %}</title></head><body>{% block content %}{% endblock %}</body></html>')

# Crear la nueva aplicación
# call_command('startapp', nueva_app)

# Agregar la nueva aplicación a la lista INSTALLED_APPS en settings.py
with open(os.path.join(settings.BASE_DIR, proyecto, 'settings.py'), 'r') as f:
    content = f.readlines()

pattern = re.compile(r'INSTALLED_APPS\s*=\s*\[(?P<apps>.*)\]', re.DOTALL)
match = pattern.search(content)
if match:
    apps = match.group('apps').strip()
    new_apps = f"'{nueva_app}',\n    " + apps
    content = pattern.sub(f'INSTALLED_APPS = [{new_apps}]', content)

print(content)

# with open(os.path.join(settings.BASE_DIR, proyecto, 'settings.py'), 'w') as f:
#     f.writelines(content)

# # Crear la nueva vista
# with open(os.path.join(settings.BASE_DIR, nueva_app, 'views.py'), 'w') as f:
#     f.write("from django.shortcuts import render\n\n\ndef nueva_vista(request):\n    return render(request, 'base.html', {'title': 'Título', 'content': 'Contenido de la nueva vista'})")

# # Agregar la nueva vista a urls.py
# with open(os.path.join(settings.BASE_DIR, nueva_app, 'urls.py'), 'w') as f:
#     f.write("from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path('nueva_vista/', views.nueva_vista, name='nueva_vista'),\n]")

# # Ejecutar las migraciones
# call_command('makemigrations')
# call_command('migrate')
