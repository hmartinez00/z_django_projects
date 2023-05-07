import os
from modules.dir_sel import dir_sel

key = 'resources'
res = dir_sel(key, 1)

print(res)

# Correr el servidor
os.system('python .\manage.py runserver')