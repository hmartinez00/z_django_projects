import os
from General_Utilities.option_list import option_list
from ManageDB.sqlite_on_db import selectall_id, show_tables
import unidecode
from modules.django_rootes import *
from General_Utilities.control_rutas import setting_routes


key = 'resources'
path = setting_routes(key)[0]

projects_list   = get_django_projects(path)
project_path    = select_django_project(projects_list)
apps_list       = get_django_apps(project_path)
app_path        = select_django_apps(apps_list)
app_name        = os.path.basename(app_path)

database = os.path.join(project_path, 'db.sqlite3')
db_tables = show_tables(database)

tables = []
for i in db_tables:
    if 'BootStrap5_' in i:
        tables.append(i)

tabla = option_list(tables)

id = 'id'
df = selectall_id(database, tabla, id)['content']
lista = []
for i in df:
    lista.append(unidecode.unidecode(i).replace(' ', '_').lower())

print(lista)

