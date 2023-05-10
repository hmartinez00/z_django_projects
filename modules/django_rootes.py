import os


def get_django_projects(path):
    """
    Recibe la ruta del directorio raíz y retorna una lista de todas las carpetas
    de proyectos de Django encontradas en ese directorio.
    """
    django_projects = []
    for dirpath, dirnames, filenames in os.walk(path):
        if 'manage.py' in filenames:
            django_projects.append(dirpath)
    return django_projects


def select_django_project(projects_list):
    """
    Recibe una lista de proyectos de Django y permite seleccionar uno de ellos
    para listar las aplicaciones y los archivos .py.
    """
    print("Seleccione un proyecto de Django para listar sus aplicaciones:")
    for i, project in enumerate(projects_list):
        print(f"{i + 1}. {os.path.basename(project)}")
    while True:
        selection = input("Seleccione el número del proyecto: ")
        if selection.isdigit() and int(selection) in range(1, len(projects_list) + 1):
            return projects_list[int(selection) - 1]
        print("Selección inválida. Intente de nuevo.")


def get_django_apps(project_path):
    """
    Recibe la ruta del proyecto de Django y retorna una lista de todas las
    aplicaciones encontradas dentro de la carpeta del proyecto.
    """
    django_apps = []
    for root, dirs, files in os.walk(project_path):
        for dir in dirs:
            if dir != 'migrations' and dir != '__pycache__':
                init_file = os.path.join(root, dir, '__init__.py')
                if os.path.exists(init_file):
                    django_apps.append(dir)
    return django_apps



def get_py_files(path):
    """
    Recibe la ruta de una carpeta y retorna una lista de todos los archivos .py
    encontrados dentro de esa carpeta.
    """
    py_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py'):
                py_files.append(os.path.join(dirpath, filename))
    return py_files


def get_project_and_app_py_files(project_path, app_name=None):
    """
    Recibe la ruta del proyecto de Django y el nombre opcional de una aplicación
    y retorna una lista de todos los archivos .py encontrados en la carpeta del
    proyecto y en la carpeta de la aplicación.
    """
    app_files = []
    if app_name:
        app_path = None
        # buscar la carpeta de la aplicación en todas las subcarpetas de project_path
        for root, dirs, files in os.walk(project_path):
            if app_name in dirs:
                app_path = os.path.join(root, app_name)
                break
        if app_path:
            app_files = get_py_files(app_path)
    return app_files
