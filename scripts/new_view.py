from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_models import views
from General_Utilities.menu import menu_class


view_name = 'index'

key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
apps_list = get_django_apps(project_path)
app_path = select_django_apps(apps_list)
app_name = os.path.basename(app_path)

# Crear una instancia de ModelGenerator
generator = views(project_path, app_name)
menu_class(generator)


input('Presione una tecla para continuar: ')
