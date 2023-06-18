import os
from General_Utilities.control_rutas import setting_routes


key = 'resources'
path = setting_routes(key)[0]

folder = 'cursoBs'
directory = os.path.join(path, folder)

new_file = input('Introduzca el nombre del nuevo archivo: ')

new_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{new_file}</title>

  <!-- BOOTSTRAP -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>

  <link rel="stylesheet" href="css/{new_file}.css">

</head>
<body>

</body>
</html>
'''

html_path = os.path.join(directory, new_file + '.html')
with open(html_path, 'w') as f:
    f.write(new_content)
f.close()

css_path = os.path.join(directory, 'css', new_file + '.css')
with open(css_path, 'w') as f:
    f.write('')
f.close()

dirs = os.listdir(directory)

print(dirs)
