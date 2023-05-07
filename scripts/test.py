import os
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes

key = 'resources'

directory = setting_routes(key)[1]
directorio = os.path.abspath(directory)
os.chdir(directorio)
opciones = os.listdir()
project = option_list(opciones)

directorio = os.path.abspath(directory + '/' + project)
os.chdir(directorio)
print(os.getcwd())