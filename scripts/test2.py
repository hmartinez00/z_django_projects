import ast

file_path = r'C:\Users\Hector\Documents\0 - A Repositorios GitHub\z_django_projects\empresaDjango\empresaDjango\settings.py'

def analyze_settings_file(filename):
    # Abrir y leer el archivo
    with open(filename, "r") as file:
        source_code = file.read()

    # Analizar el código fuente en un AST
    tree = ast.parse(source_code)

    # Recorrer el AST en busca de nodos específicos
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                target = node.targets[0].id
                if target == "DATABASES":
                    # Ejemplo de análisis específico para la configuración de la base de datos
                    database_settings = node.value
                    print("Configuración de la base de datos encontrada:")
                    print(ast.dump(database_settings))

# Ejemplo de uso
settings_file = file_path
analyze_settings_file(settings_file)
