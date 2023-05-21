import os
from modules.django_rootes import *
from modules.modifile import *
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


def create_model(file_path, model_name):

    field_dict = {
        "ForeingKey": [
                'model_name2',
                'on_delete=models.CASCADE',
            ],
        "CharField": [
                'max_lenght=50',
            ],
        "IntegerField": [
                'default=0',
            ],
        "DateField": [],
        "ManyToManyField": [
                'single_var',
            ],
    }


    with open(file_path, 'r+') as f:
        content = f.read()
        
        # Verificar si la clase ya existe en el archivo
        if model_name in content:
            print(f"El modelo {model_name} ya existe en el archivo.")
            return
        
        # Crear la definición del modelo
        model_def = f"\n\nclass {model_name}(models.Model):\n"
        for field, args in field_dict.items():
            field_args = ', '.join(args)
            model_def += f"    {field}({field_args})\n"
        
        # Agregar la definición del modelo al archivo
        f.write(model_def)
        
    print(f"El modelo {model_name} ha sido agregado al archivo.")



key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

files_list = get_py_files(app_path)

# Create el listado de directorios
ruta_settings = [
        find_substring_in_list(files_list, 'models.py'),
    ]

file_path = ruta_settings[0]

# Creando el modelo
model_name = input('Introduzca el nombre del modelo: ')

# Actualizando el archivo models.py de la app
# var_name = input('Introduzca el nombre de la variable: ')
var_list = {
    "ForeingKey": [
            'model_name2',
            'on_delete=models.CASCADE',
        ],
    "CharField": [
            'max_lenght=50',
        ],
    "IntegerField": [
            'default=0',
        ],
    "DateField": [],
    "ManyToManyField": [
            'single_var',
        ],
}


# Ejemplo de uso
# create_model(file_path, model_name)



# Definimos la clase
class_def = f"class {model_name}(models.Model)"
new_content = '\n\n' + class_def + ': '
# # Seleccionamos el tipo de campo y extraemos sus atributos
# var_type = option_list(list(var_list.keys()))
# var_attrs = var_list[var_type]
# # Definimos el campo
# var_def = f'{var_name} = models.{var_type}(' + ', '.join(var_attrs) + ')'
# pivot_substring = class_def
# new_substring = ':\n\t' + var_def
# target_line = var_def

append_to_file(file_path, new_content)
# append_substring_to_line(file_path, pivot_substring, new_substring)
# swap_lines(file_path, target_line)