class ModelGenerator:
    def __init__(self, file_path, model_name):
        self.file_path = file_path
        self.model_name = model_name
        self.field_types = {
            "AutoField": [],
            "BigAutoField": [],
            "BigIntegerField": [],
            "BinaryField": [],
            "BooleanField": [],
            "CharField": [],
            "DateField": [],
            "DateTimeField": [],
            "DecimalField": [],
            "DurationField": [],
            "EmailField": [],
            "FileField": [],
            "FilePathField": [],
            "FloatField": [],
            "ForeignKey": ["to", "on_delete"],
            "ImageField": [],
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

    def get_existing_fields(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        start_index = content.index(f"class {self.model_name}")
        end_index = content.index("\n\n", start_index)
        class_content = content[start_index:end_index]
        lines = class_content.split("\n")
        fields = []
        for line in lines:
            line = line.strip()
            if "=" in line:
                field_name = line.split("=")[0].strip()
                fields.append(field_name)
        return fields

    def add_field(self, field_name, field_type, attributes=None):
        if not attributes:
            attributes = []
        field_declaration = f"    {field_name} = models.{field_type}({', '.join(attributes)})"
        with open(self.file_path, 'a') as file:
            file.write(f"\n{field_declaration}")

    def remove_field(self, field_name):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        with open(self.file_path, 'w') as file:
            for line in lines:
                if f"{field_name} =" not in line:
                    file.write(line)
