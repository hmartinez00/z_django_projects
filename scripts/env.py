import os
import subprocess

def create_virtualenv(project_name):
    # Crear el entorno virtual
    subprocess.run(["mkvirtualenv", project_name])

def create_project(project_name):
    # Crear el proyecto Django
    subprocess.run(["mkproject", project_name])

def delete_project(project_name):
    # Eliminar el proyecto y el entorno virtual asociado
    subprocess.run(["rmvirtualenv", project_name])

# Nombre del proyecto
project_name = input('Introduzca el nombre del proyecto por favor: ')
print(project_name)

create_virtualenv(project_name)
