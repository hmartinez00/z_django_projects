import os
from General_Utilities.option_list import option_list
from modules.settings_modify import settings_modify
from modules.dir_sel import dir_sel


key = 'resources'
res = dir_sel(key, 1)
print(res)

opciones = os.listdir()
app_name = option_list(opciones)
print(app_name)

os.chdir('..')
directorio = os.path.abspath(res[0] + '/' + res[1])

settings_modify(app_name, directorio)