from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from General_Utilities.option_list import option_list


key = 'resources'
path = setting_routes(key)[0]

projects_list = get_django_projects(path)
project_path = select_django_project(projects_list)
app_list = get_django_apps(project_path)
app_path = select_django_apps(app_list)

files_list = get_py_files(app_path)

file_path = option_list(files_list)


# file_path = r'C:\Users\Hector\Documents\0 - A Repositorios GitHub\z_django_projects\empresaDjango\empresaDjango\settings.py'

def analyze_settings_file(filename):
    import ast
    from codegen import to_source
    # Abrir y leer el archivo
    with open(filename, "r") as file:
        source_code = file.read()

    # Analizar el código fuente en un AST
    tree = ast.parse(source_code)

    # Variables de bandera
    target_settings_found = False

    # Recorrer el AST en busca de nodos específicos
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                target = node.targets[0].id
                if target == "TEMPLATES":
                    # Ejemplo de análisis específico para la configuración de la base de datos
                    target_settings  = node.value

                    # Buscar el diccionario que contiene la clave 'DIRS'
                    for target_element in target_settings.elts:
                        if isinstance(target_element, ast.Dict):
                            for i, key in enumerate(target_element.keys):
                                if isinstance(key, ast.Str) and key.s == 'DIRS':
                                    # Modificar el valor asociado a la clave 'DIRS'
                                    target_element.values[i] = ast.List(
                                        elts=[ast.Str(s='/ruta/a/mis/templates')],
                                        ctx=ast.Load()
                                    )
                                    # Marcar la variable de bandera como verdadera
                                    target_settings_found = True
                                    break

                    break

    # Verificar si se encontró la configuración de TEMPLATES y se realizó la modificación
    if target_settings_found:
        # Convertir el AST actualizado a una cadena de texto
        updated_code = to_source(tree)

        # Guardar los cambios en el archivo settings.py
        with open(filename, "w") as file:
            file.write(updated_code)

        print("Configuración de TEMPLATES actualizada y guardada en el archivo settings.py.")
    else:
        print("No se encontró la configuración de TEMPLATES en el archivo.")


# Ejemplo de uso
settings_file = file_path
analyze_settings_file(settings_file)

input('\nPresione una tecla para continuar: ')
