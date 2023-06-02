from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from General_Utilities.menu import menu_class
from General_Utilities.option_list import option_list
from modules.django_modifile import settings
from modules.django_modifile import urls
from modules.django_models import views


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)
app_name = os.path.basename(app_path)

object = views(project_path, app_name)
menu_class(object)


input('Presione una tecla para continuar: ')

