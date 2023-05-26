from modules.django_models import ModelGenerator
import inspect
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.menu import get_method_tags, menu_class, request, option_list
from General_Utilities.control_rutas import setting_routes
from modules.django_models import ModelGenerator


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

app_name = os.path.basename(app_path)

files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'models.py'),
        find_substring_in_list(files_list, 'admin.py'),
    ]

# model_name = input('Introduzca el nombre del modelo: ')
file_path = ruta_settings[0]
# generator = ModelGenerator(file_path, model_name)
generator = ModelGenerator(file_path)
# menu_class(generator)
fields_connectable_to_models = [
    'ForeignKey',
    'ManyToManyField',
]
field_list = generator.field_types
field_type = option_list(list(field_list.keys()))

if field_type in fields_connectable_to_models:
    attributes = field_list[field_type]
    new_element = option_list(generator.get_existing_class())
    print(new_element)
    attributes = [new_element if i == 'to' else i for i in attributes]

    field_declaration = f"    nombre = models.{field_type}({', '.join(attributes)})\n"

print(field_declaration)

input('Presione una tecla para continuar: ')