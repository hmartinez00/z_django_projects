import os
from General_Utilities.control_rutas import setting_routes
from modules.django_rootes import *
from modules.django_modifile import settings
from modules.TextFileManipulator import TextFileManipulator
from General_Utilities.menu import menu_class


file = r'C:\Users\Hector\Documents\0 - A Repositorios GitHub\Devocionales\settings\blackboard\blackboard.txt'

object = TextFileManipulator(file)
menu_class(object)


input('Presione una tecla para continuar: ')

