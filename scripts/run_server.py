import os
from modules.dir_sel import dir_sel

key = 'resources'
res = dir_sel(key, 0)

os.chdir(res[0])

# Correr el servidor
os.system('python .\manage.py runserver')