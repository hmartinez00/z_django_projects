import os

# Introducimos la ruta
final_dir = input('Introduzca la ruta de destino: ')

# Nombramos el archivo a crear
index = len(os.listdir(final_dir))
file_name = os.path.join(final_dir, f'example{index}.html')

# Creamos el archivo con el contenido
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        content = '''{% extends "base.html" %}
{% load custom_filters %}
{% block content %}

{% endblock %}
'''
        file.write(content)

