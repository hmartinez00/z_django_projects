import os
from django.db import models
from modules.django_models import create_model
from modules.django_rootes import *
from General_Utilities.control_rutas import setting_routes


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}/{project_name}.settings')
import django
django.setup()

create_model('aplicacion', 'Producto', {
    'nombre': models.CharField(max_length=50),
    'descripcion': models.TextField(),
    'precio': models.DecimalField(max_digits=8, decimal_places=2)
})
