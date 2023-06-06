import os
from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_modifile import settings


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)

object = settings(project_path)
# Importamos modulo os.
object.import_os()
object = object.object
# Instala la ruta de static en settings.
new_dir = f"os.path.join(BASE_DIR, 'static')"
content = object.list_content()
sub_string="STATICFILES_DIRS = [\n"

index = object.index_sub_string(
    content=content,
    sub_string=sub_string,
    type_finder=0
)

if len(index)==0:
    sub_string="STATIC_URL = 'static/'\n"

    index = object.index_sub_string(
        content=content,
        sub_string=sub_string,
        type_finder=0
    )

    new_content = object.insert_line(
        section=content,
        position=index[0] + 1,
        new_element="\n"
    )

    new_content = object.insert_line(
        section=content,
        position=index[0] + 1,
        new_element=f"STATICFILES_DIRS = [\n\n]"
    )

    object.replace_lines_content(new_content)
    print('\t- Insercion de STATICFILES_DIRS ejecutada.')

print(new_content)


input('Presione una tecla para continuar: ')

