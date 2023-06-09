import os
import json
from ManageDB.sqlite_on_db import *
import sys
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')


database = r"CursoBsw3shools\db.sqlite3"
ruta_archivo_json = r'CursoBsw3shools\static\estructura_curso.json'

with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)


tables = list(datos_json.keys())
table = 'BootStrap5_' + tables[4]
print(len(tables))
values = datos_json[tables[4]]


for i in range(len(values)):
    renglon = (values[i], 1, 'a')
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

