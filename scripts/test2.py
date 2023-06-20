import os
import json
from ManageDB.sqlite_on_db import *
import sys

sys.stdout.reconfigure(encoding='utf-8')


database = r"C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\db.sqlite3"
ruta_archivo_json = r'C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)


tables = list(datos_json.keys())
table = tables[0]
print(len(tables))
values = datos_json[tables[0]]


for i in values:
    renglon = (i,)
    print(renglon)

    insert(database, table, renglon)