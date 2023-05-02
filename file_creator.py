import os

location = r"C:\Users\Hector\Documents\0 - A Repositorios GitHub\z_django_projects\file.txt"
string = "Hola! Aca mi primer script desarrollado por ChatGPT directamente!"

# Revisar si el archivo ya existe
if os.path.exists(location):
    # Si el archivo existe, abrirlo en modo escritura y escribir la cadena de texto
    with open(location, "w") as file:
        file.write(string)
else:
    # Si el archivo no existe, crearlo y escribir la cadena de texto
    with open(location, "x") as file:
        file.write(string)
        
# Imprimir el contenido del archivo
with open(location, "r") as file:
    print(file.read())
