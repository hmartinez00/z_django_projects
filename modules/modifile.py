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
    # lines[pivot_line] = lines[pivot_line].strip() + new_substring + '\n'
    lines[pivot_line] = lines[pivot_line].rstrip()[:-1] + new_substring + lines[pivot_line][-1]
    with open(file_path, 'w') as f:
        f.writelines(lines)
