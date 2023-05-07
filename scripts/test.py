import os
from modules.dir_sel import dir_sel
from General_Utilities.option_list import option_list

key = 'resources'
res = dir_sel(key, 1)
directorio = os.path.abspath(res[0] + '/' + res[1])

ruta_settings = os.path.join(directorio, 'settings.py')

print(ruta_settings)