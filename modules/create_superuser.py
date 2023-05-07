import os
import sys
import django


def create_superuser(directorio, proyecto):
    # Ruta absoluta del directorio del proyecto
    PROJECT_DIR = os.path.abspath(directorio + '/' + proyecto)

    # Agregar la ruta del proyecto al path de python
    sys.path.append(PROJECT_DIR)

    # Configurar las settings de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', proyecto + '.settings')
    django.setup()

    from django.contrib.auth.models import User

    # Crear superusuario
    User.objects.create_superuser(
        username='hmartinez',
        email='hectoralonzomartinez00@gmail.com',
        password='pyp8r5',
    )