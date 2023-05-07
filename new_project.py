import os
from modules.create_superuser import create_superuser


directorio = os.getcwd()
project_name = 'proyecto_prueba'
app_name = 'aplicacion'

# Create Django project
os.system(f"django-admin startproject {project_name}")

# Create Django app
os.chdir(project_name)
os.system(f"python manage.py startapp {app_name}")
os.system("python .\manage.py migrate")

# Crear Superusuario
create_superuser(directorio, project_name)

# Correr el servidor
os.system('python .\manage.py runserver')