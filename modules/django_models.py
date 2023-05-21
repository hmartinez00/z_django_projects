import re
from General_Utilities.option_list import option_list


class ModelGenerator:
    def __init__(self, file_path, model_name):
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
        with open(self.file_path, 'r') as file:
            content = file.read()
        return self.model_name in content

    def add_model_class(self):
        class_str = f"\nclass {self.model_name}(models.Model):\n"
        with open(self.file_path, 'r+') as file:
            content = file.read()
            if class_str not in content:
                file.seek(0, 2)  # Mover el puntero al final del archivo
                file.write(class_str)

    def get_existing_fields(self):
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


    def modules_actions(self):
        while True:
            # Mostrar opciones y solicitar entrada al usuario
            print("1. Insertar Campo")
            print("2. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                # Realizar la acción
                print("Insertando Campo")
                self.add_field()

            elif opcion == "2":
                # Salir del ciclo
                print("Saliendo del programa...")
                break

            else:
                # Opción inválida
                print("Opción inválida. Por favor, selecciona una opción válida.")
