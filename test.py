import os

directorio = os.getcwd()
print(directorio)

os.chdir('proyecto_prueba')
directorio = os.getcwd()

print(directorio)