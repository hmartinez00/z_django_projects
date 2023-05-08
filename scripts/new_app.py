import os
from modules.add_app import add_app
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
add_app(app_name, directorio)