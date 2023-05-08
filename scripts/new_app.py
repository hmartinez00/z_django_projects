import os
from modules.add_app import add_app
from modules.dir_sel import dir_sel


key = 'resources'
res = dir_sel(key, 0)

project_name = res[1]
app_name = 'aplicacion'

add_app(project_name, app_name)