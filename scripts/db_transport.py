import os
import json
from ManageDB.sqlite_on_db import *
import sys
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')


database = r"C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\db.sqlite3"
ruta_archivo_json = r'C:\Users\admin\Documents\0 - A Repositorios GitHub\z_django_projects\CursoBsw3shools\static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)


tables = list(datos_json.keys())
table = 'BootStrap5_' + tables[0]
# BootStrap5_tutorial_de_bootstrap_5
print(len(tables))
values = datos_json[tables[0]]


for i in range(len(values)):
    renglon = (i,values[i])
    print(renglon)

    insert(database, table, renglon)




# # Establecer la conexión con la base de datos
# conn = sqlite3.connect(database)

# # Crear un cursor para ejecutar consultas
# cursor = conn.cursor()

# # Ejecutar una consulta
# cursor.execute(f'SELECT * FROM {table}')

# # Obtener los resultados de la consulta
# results = cursor.fetchall()

# # Recorrer los resultados
# for row in results:
#     print(row)

# # Cerrar el cursor y la conexión
# cursor.close()
# conn.close()

