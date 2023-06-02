from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_models import models
from General_Utilities.menu import menu_class


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)
app_name = os.path.basename(app_path)

# Crear una instancia de ModelGenerator
generator = models(project_path, app_name)
menu_class(generator)

# print(generator.model_exists())
# generator.add_model_class()

# # Si no existe, agregar la clase del modelo al archivo
# generator.add_field('id', 'AutoField', ['primary_key=True'])
# generator.add_field('name', 'CharField', ["max_length=100"])
# generator.add_field('age', 'IntegerField')
