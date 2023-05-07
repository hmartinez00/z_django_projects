import os
from General_Utilities.option_list import option_list
from modules.settings_modify import settings_modify
from modules.dir_sel import dir_sel


key = 'resources'
res = dir_sel(key, 1)
print(res[0])

app_name = 'aplicacion'

# Create Django app
os.system(f"python manage.py startapp {app_name}")
os.system("python .\manage.py migrate")

os.chdir('..')
directorio = os.path.abspath(res[0] + '/' + res[1])

print(directorio)
settings_modify(app_name, directorio)