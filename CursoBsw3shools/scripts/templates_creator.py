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


template_dir = os.path.join(app_path, 'templates')
for i in os.listdir(template_dir):
    if str(tabla).replace('BootStrap5_', '').lower() == i.lower():
        for j in lista:
            lesson_dir  = os.path.join(template_dir, i, j)
            lesson_file = os.path.join(lesson_dir, j + '.html')
            if not os.path.exists(lesson_dir):
                os.makedirs(lesson_dir)
            if not os.path.exists(lesson_file):
                with open(lesson_file, 'w') as file:
                    content = '''{% extends "base.html" %}
{% load custom_filters %}
{% block content %}
    <h1>{{ modulo }}</h1>
    <h2>{{ leccion }}</h2>
    {% for i in file_list %}
        <li>
            <a href="{% url 'vistas_clases' modulo leccion i|extract_numbers %}">{{ i }}</a>
        </li>
    {% endfor %}
{% endblock %}                   
'''
                    file.write(content)

