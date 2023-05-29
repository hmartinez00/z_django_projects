from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_modifile import TextFileManipulator
from General_Utilities.menu import menu_class
from General_Utilities.option_list import option_list


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

files_list = get_py_files(app_path)

file_path = option_list(files_list)

# Crear una instancia de ModelGenerator
generator = TextFileManipulator(file_path)
# menu_class(generator)

content = generator.list_content()

inicio = 'TEMPLATES = [\n'
final = '\n'

segment = generator.segment_num_content(
    content, inicio, final
)

section = segment[0]
interval = segment[1]

index = generator.index_sub_string(
    content=section,
    sub_string="        'DIRS': [],\n", 
    type_finder=0
)

if len(index)!=0:
    section = generator.replace_line(
        index=index[0],
        section=section,
        new_substring="        'DIRS': [\n"
    )

    section = generator.insert_line(
        section=section,
        position=index[0] + 1,
        new_element="\n\t\t],\n"
    )

else:
    index = generator.index_sub_string(
        content=section,
        sub_string="        'DIRS': [\n", 
        type_finder=0
    )

    section = generator.insert_line(
        section=section,
        position=index[0] + 1,
        new_element="\t\t\t'ruta_template/'"
    )

print(section)

input('Presione una tecla para continuar: ')

