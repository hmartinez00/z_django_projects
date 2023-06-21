import os
import json
from ManageDB.sqlite_on_db import *
import sys
from unidecode import unidecode
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')

def replace_spaces(value):
    new_value = value\
        .replace(' ', '_')\
        .replace('á', 'a')\
        .replace('é', 'e')\
        .replace('í', 'i')\
        .replace('ó', 'o')\
        .replace('ú', 'u').lower()
        
    return new_value


database = r"CursoBsw3shools\db.sqlite3"
ruta_archivo_json = r'CursoBsw3shools\static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)

tables = list(datos_json.keys())
values = []
for i in datos_json[tables[0]]:
    values.append(replace_spaces(i))

print(tables, values)