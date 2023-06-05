import os


def find_pivot_substring(file_path, pivot_substring):
    """
    Busca la posición de la substring de pivoteo en el archivo.

    Args:
        file_path (str): Ruta del archivo.
        pivot_substring (str): Subcadena a buscar.

    Returns:
        int: El número de línea en el que se encontró la subcadena de pivoteo.

    Raises:
        ValueError: Si la subcadena de pivoteo no se encuentra en el archivo.
    """
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith(pivot_substring):
                return i
       # raise ValueError(f'La substring de pivoteo "{pivot_substring}" no fue encontrada en el archivo.')


def replace_file_content(file_path, new_content):
    """
    Reemplaza todo el contenido del archivo con un nuevo contenido.

    Args:
        file_path (str): Ruta del archivo.
        new_content (str): Contenido nuevo que reemplazará al contenido existente.

    Returns:
        None
    """
    with open(file_path, 'w') as f:
        f.write(new_content)


def replace_substring_in_line(file_path, pivot_substring, old_substring, new_substring):
    """
    Reemplaza una subcadena en la línea donde se encuentra la substring de pivoteo.

    Args:
        file_path (str): Ruta del archivo.
        pivot_substring (str): Subcadena que indica en qué línea se realizará el reemplazo.
        old_substring (str): Subcadena que se reemplazará.
        new_substring (str): Nueva subcadena que reemplazará a la antigua.

    Returns:
        str: Si la antigua subcadena no se encuentra en la línea, se retorna "No se puede hacer la sustitución".
    """
    pivot_line = find_pivot_substring(file_path, pivot_substring)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    line = lines[pivot_line]
    if old_substring not in line:
        return 'No se puede hacer la sustitución'
    if new_substring not in line:
        line = line.replace(old_substring, new_substring)
        lines[pivot_line] = line
        with open(file_path, 'w') as f:
            f.writelines(lines)

def append_substring_to_line(file_path, pivot_substring, new_substring):
    """
    Añade una subcadena en la línea donde se encuentra la substring de pivoteo.

    Args:
        file_path (str): Ruta del archivo.
        pivot_substring (str): Subcadena que indica en qué línea se realizará la adición.
        new_substring (str): Nueva subcadena que se agregará a la línea.

    Returns:
        None
    """
    pivot_line = find_pivot_substring(file_path, pivot_substring)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines[pivot_line] = lines[pivot_line].rstrip()[:-1] + new_substring + lines[pivot_line][-1]
    with open(file_path, 'w') as f:
        f.writelines(lines)

def add_substring_to_line(filepath, line_num, substring):
    """
    Agrega una subcadena a una línea específica de un archivo de texto.

    Args:
        filepath (str): Ruta del archivo de texto.
        line_num (int): Número de línea a la que se agregará la subcadena.
        substring (str): Subcadena que se agregará a la línea.

    Returns:
        - True si la subcadena se agregó correctamente a la línea especificada.
        - False si el número de línea está fuera del rango de líneas del archivo.
    """

    with open(filepath, 'r') as f:
        lines = f.readlines()

    # check if line_num is within the range of lines
    if line_num < 0 or line_num > len(lines):
        return False

    else:
        line = lines[line_num]
        print(line)

        # check if substring already exists in line
        if substring not in line:

            # add substring to line
            line = line.rstrip('\n') + substring + '\n'
            lines[line_num] = line

            # write updated lines to file
            with open(filepath, 'w') as f:
                f.writelines(lines)

            return True

def append_to_file(file_path, text):
    with open(file_path, 'r') as file:
        content = file.read()
    if text in content:
        print(f"El modelo ya existe en el archivo.")
    else:
        with open(file_path, 'a') as file:
            file.write(text)

def import_module_to_file(file_path, module_name):
    """
    Esta función importa un módulo en un archivo Python si aún no ha sido importado.
    Busca en el archivo si ya hay una importación del módulo especificado y, si es así,
    no hace nada. Si no se encuentra ninguna importación, la función agrega una nueva línea
    de importación en la posición adecuada en el archivo.

    Args:
        file_path (str): La ruta del archivo donde se importará el módulo.
        module_name (str): El nombre del módulo que se importará.

    Returns:
        None
    """

    # Check if module already imported
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(f"import {module_name}") or line.startswith(f"from {module_name}"):
                print(f"Module {module_name} already imported in {file_path}")
                return

    # Find the line number to insert the new import statement
    insert_line = -1
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_line = i
    insert_line += 1

    # Insert the new import statement
    new_line = f"import {module_name}\n"
    lines.insert(insert_line, new_line)

    # Write the updated file contents
    with open(file_path, 'w') as f:
        f.writelines(lines)
        print(f"Module {module_name} imported to {file_path} successfully")


def swap_lines(file_path, target_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_index = None
    for i, line in enumerate(lines):
        if line.strip() == target_line:
            line_index = i
            break

    if line_index is None or line_index == len(lines) - 1:
        # No se encontró la línea o es la última línea, no se puede intercambiar
        return

    # Intercambiar las líneas
    lines[line_index], lines[line_index + 1] = lines[line_index + 1], lines[line_index]

    with open(file_path, 'w') as file:
        file.writelines(lines)
