import os
import sys
import json


sys.stdout.reconfigure(encoding='utf-8')

def normalizar(value):
    str_string = str(str(value).lower())
    replacements = {
        ' ': '_',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
    }
    new_value = ''
    for char in str_string:
        if char in replacements:
            new_value += replacements[char]
        else:
            new_value += char
    return new_value

directory = os.getcwd()

dir = 'CursoBsw3shools'
os.chdir(dir)
print(os.getcwd())

database = r"db.sqlite3"
ruta_archivo_json = r'static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)

tables = list(dict(datos_json).keys())
values = datos_json[tables[0]]

for i in values:
    print(normalizar(i))


os.chdir(directory)
