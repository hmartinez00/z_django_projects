import os
import re
import subprocess
from General_Utilities.option_list import option_list


class ModelGenerator:
    """
    Clase para generar modelos en Django.

    :param file_path: Ruta del archivo models.py.
    :param model_name: Nombre del modelo a generar.
    """
    def __init__(self, file_path, model_name):
        """
        Inicializa una instancia de ModelGenerator.

        :param file_path: Ruta del archivo models.py.
        :param model_name: Nombre del modelo a generar.
        """
        self.file_path = file_path
        self.model_name = model_name
        self.field_types = {
            "AutoField": ["primary_key=True"],
            "BigAutoField": ["primary_key=True"],
            "BigIntegerField": [],
            "BinaryField": [],
            "BooleanField": ["default=False"],
            "CharField": ["max_length=100"],
            "DateField": [],
            "DateTimeField": ["auto_now_add=True"],
            "DecimalField": ["max_digits=8", "decimal_places=2"],
            "DurationField": [],
            "EmailField": [],
            "FileField": ["upload_to='archivos/'"],
            "FilePathField": [],
            "FloatField": [],
            "ForeignKey": ["to", "on_delete=models.CASCADE"],
            "ImageField": ["upload_to='imagenes/'"],
            "IntegerField": [],
            "ManyToManyField": ["to"],
            "NullBooleanField": [],
            "OneToOneField": ["to", "on_delete"],
            "PositiveBigIntegerField": [],
            "PositiveIntegerField": [],
            "PositiveSmallIntegerField": [],
            "SlugField": [],
            "SmallAutoField": [],
            "SmallIntegerField": [],
            "TextField": [],
            "TimeField": [],
            "URLField": [],
            "UUIDField": [],
        }

    def model_exists(self):
        """
        main_description: Verificar existencia.
        Verifica si el modelo ya existe en el archivo models.py.

        :return: True si el modelo existe, False en caso contrario.
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
        return self.model_name in content

    def add_model_class(self):
        """
        main_description: Agregar modelo.
        Agrega la definición de la clase del modelo en el archivo models.py.
        Si la clase ya existe, no realiza ninguna acción.
        """
        class_str = f"\nclass {self.model_name}(models.Model):\n"
        with open(self.file_path, 'r+') as file:
            content = file.read()
            if class_str not in content:
                file.seek(0, 2)  # Mover el puntero al final del archivo
                file.write(class_str)

    def get_existing_fields(self):
        """
        main_description: Verificar existencia de campos.
        Obtiene la lista de campos existentes en el modelo.

        :return: Lista de campos existentes en el modelo.
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
        start_index = content.index(f"class {self.model_name}")
        end_index = content.find("\n\n", start_index)
        if end_index == -1:
            # No se encontró una línea en blanco adicional, ajustar el índice final
            end_index = len(content)
        class_section = content[start_index:end_index]
        fields = re.findall(r'\w+\s*=\s*models\.', class_section)
        fields = [field.replace(' = models.', '') for field in fields]
        return fields

    def add_field(self, field_name=None, field_type=None, attributes=None):
        """
        main_description: Agregar campos.
        Agrega un nuevo campo al modelo.

        :param field_name: Nombre del campo a agregar.
                           Si no se proporciona, se solicitará al usuario.
        :param field_type: Tipo de campo a agregar.
                           Si no se proporciona, se solicitará al usuario.
        :param attributes: Atributos adicionales para el campo.
        """
        if not attributes:
            attributes = []
        
        if not field_name:
            field_name = input("Ingrese el nombre del campo: ")

        if not field_type:
            field_list = self.field_types
            field_type = option_list(list(field_list.keys()))
            attributes = field_list[field_type]
            
        field_declaration = f"    {field_name} = models.{field_type}({', '.join(attributes)})\n"
        
        with open(self.file_path, 'a') as file:
            file.write(f"{field_declaration}")
        
        # Obtener los campos existentes en el modelo
        existing_fields = self.get_existing_fields()
        print("Campos existentes:", existing_fields)

    def remove_field(self, field_name=None):
        """
        main_description: Remover campos.
        Elimina un campo del modelo.

        :param field_name: Nombre del campo a eliminar.
                           Si no se proporciona, se solicitará al usuario.
                           Si se selecciona 'No borrar ningun campo!', no se realizará ninguna acción.
        """
        if field_name is None:
            existing_fields = self.get_existing_fields()
            existing_fields.append('No borrar ningun campo!')
            field_name = option_list(existing_fields)
        
        if field_name != 'No borrar ningun campo!':
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            with open(self.file_path, 'w') as file:
                for line in lines:
                    if f"{field_name} =" not in line:
                        file.write(line)
        else:
            print('No se elimino ningun campo!')
        
        # Obtener los campos existentes en el modelo
        existing_fields = self.get_existing_fields()
        print("Campos existentes:", existing_fields)

    def all_migrations(self):
        '''
        main_description: Aplicar migraciones.
        '''
        componentes = os.path.normpath(self.file_path).split(os.sep)
        app_name = componentes[-2]
        project_path = os.path.join(*componentes[:-2])
        print(project_path)
        print(f'Ejecutando migraciones en: {app_name}')
        os.listdir()
        os.chdir(project_path)
        input('Presione una tecla para continuar: ')
        # subprocess.run(["python", "manage.py", "makemigrations", app_name])
        # subprocess.run(["python", "manage.py", "migrate"])