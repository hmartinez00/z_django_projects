import json
from ManageDB.sqlite_on_db import *
import sys


sys.stdout.reconfigure(encoding='utf-8')

def normalizar(string):
    replacements = {
        ' ': '_',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    new_string = ''
    for char in string:
        if char in replacements:
            new_string += replacements[char]
        else:
            new_string += char
    return new_string.lower()


database = r"C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\db.sqlite3"
ruta_archivo_json = r'C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)


tables = list(dict(datos_json).keys())
values = datos_json[tables[0]]

for i in values:
    print(normalizar(i))

