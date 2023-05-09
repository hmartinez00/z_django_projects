import os


def find_pivot_substring(file_path, pivot_substring):
    """
    Busca la posición de la substring de pivoteo en el archivo.
    """
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if pivot_substring in line:
                return i
    raise ValueError(f'La substring de pivoteo "{pivot_substring}" no fue encontrada en el archivo.')


def replace_file_content(file_path, new_content):
    """
    Reemplaza todo el contenido del archivo con un nuevo contenido.
    """
    with open(file_path, 'w') as f:
        f.write(new_content)


def replace_substring_in_line(file_path, pivot_substring, old_substring, new_substring):
    """
    Reemplaza una subcadena en la línea donde se encuentra la substring de pivoteo.
    """
    pivot_line = find_pivot_substring(file_path, pivot_substring)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines[pivot_line] = lines[pivot_line].replace(old_substring, new_substring)
    with open(file_path, 'w') as f:
        f.writelines(lines)


def append_substring_to_line(file_path, pivot_substring, new_substring):
    """
    Añade una subcadena en la línea donde se encuentra la substring de pivoteo.
    """
    pivot_line = find_pivot_substring(file_path, pivot_substring)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines[pivot_line] = lines[pivot_line].rstrip()[:-1] + new_substring + lines[pivot_line][-1]
    with open(file_path, 'w') as f:
        f.writelines(lines)

def add_substring_to_line(filepath, line_num, substring):
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
            line = line.rstrip('\n') + ' ' + substring + '\n'
            lines[line_num] = line

            # write updated lines to file
            with open(filepath, 'w') as f:
                f.writelines(lines)

            return True

def import_module_to_file(file_path, module_name):
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

