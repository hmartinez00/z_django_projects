from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.TextFileManipulator import TextFileManipulator
from General_Utilities.menu import menu_class
from General_Utilities.option_list import option_list
from modules.django_modifile import settings
from modules.django_modifile import urls


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
project_name = os.path.basename(project_path)
file_path = os.path.join(project_path, project_name, 'settings.py')
print(project_path)

app_name = 'appEmpresaDjango'

print(f'Importando funcion include.')
object = urls(project_path, app_name)
object.import_include()
object.reg_url_app_project()

input('Presione una tecla para continuar: ')

