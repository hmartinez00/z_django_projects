import os
import re
import subprocess
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes
from modules.TextFileManipulator import TextFileManipulator


class models:
    """
    Clase para generar modelos en Django.

    :param file_path: Ruta del archivo models.py.
    :param model_name: Nombre del modelo a generar.
    """
    def __init__(
            self, 
            project_path,
            app_name,
            model_name=None
    ):
        """
        Inicializa una instancia de models.

        :param file_path: Ruta del archivo models.py.
        :param model_name: Nombre del modelo a generar.
        """
        self.file_path = os.path.join(project_path, app_name, 'models.py')
        
        lista_modelos = self.get_existing_class()

        if model_name != None:
            self.model_name = model_name
        elif len(lista_modelos) > 0:
            self.model_name = self.change_model()
        else:
            self.model_name = self.add_model_class()

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
            "IntegerField": ["default=0"],
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

        self.fields_connectable_to_models = [
            'ForeignKey',
            'ManyToManyField',
        ]


    def change_model(self):
        '''
        main_description: Conectar modelo.
        '''
        print('Selecciones el modelo que desea conectar:\n')
        lista_modelos = self.get_existing_class()
        self.model_name = option_list(lista_modelos)
        return self.model_name


    def add_model_class(self):
        """
        main_description: Agregar modelo.
        Agrega la definición de la clase del modelo en el archivo models.py.
        Si la clase ya existe, no realiza ninguna acción.
        """
        model_name = input('Introduzca el nombre del modelo: ')
        self.model_name = model_name
        class_str = f"\nclass {self.model_name}(models.Model):\n"
        with open(self.file_path, 'r+') as file:
            content = file.read()
            if class_str not in content:
                file.seek(0, 2)  # Mover el puntero al final del archivo
                file.write(class_str)
        return self.model_name


    def get_existing_class(self):
        '''
        main_description: Listar modelos
        '''
        with open(self.file_path, 'r') as file:
            content = file.read()

        pattern = r"class\s+(\w+)"
        clases = re.findall(pattern, content)
        # print(clases)
        # input('Presione una tecla para continuar: ')
        return clases


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
        # print(fields)
        # input('Presione una tecla para continuar: ')
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
            
        if field_type in self.fields_connectable_to_models:
            print('Seleccione el modelo:\n')
            new_element = option_list(self.get_existing_class())
            new_attributes = []
            for i in attributes:
                if i != 'to':
                    new_attributes.append(i)
                else:
                    new_attributes.append(new_element)
                
                attributes = new_attributes
            
        field_declaration = f"    {field_name} = models.{field_type}({', '.join(attributes)})\n"

        with open(self.file_path, 'r') as file:
            content = file.readlines()

        start_index = None
        end_index = None
        class_found = False

        for i, line in enumerate(content):
            if line.strip().startswith("class ") and line.strip().endswith(":"):
                class_name = line.strip()[6:-1].split("(")[0].strip()
                if class_name == self.model_name:
                    start_index = i
                    class_found = True
            elif class_found and line.strip() == "":
                end_index = i
                break

        if start_index is not None and end_index is not None:
            content.insert(end_index, field_declaration)
        else:
            # Class section not found, adding field at the end of the file
            content.append(field_declaration)

        with open(self.file_path, 'w') as file:
            file.writelines(content)


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
                content = file.readlines()

            start_index = None
            end_index = None
            class_found = False

            for i, line in enumerate(content):
                if line.strip().startswith("class ") and line.strip().endswith(":"):
                    class_name = line.strip()[6:-1].split("(")[0].strip()
                    if class_name == self.model_name:
                        start_index = i
                        class_found = True
                elif class_found and line.strip() == "":
                    end_index = i
                    break
            
            if end_index == None:
                end_index = len(content)
            
            print(start_index, end_index)
            
            if start_index is not None and end_index is not None:
                class_content = content[start_index:end_index]
                print(class_content)
                class_content = list(filter(lambda x: field_name + ' =' not in x, class_content))
                content = content[:start_index] + class_content + content[end_index:]

            with open(self.file_path, 'w') as file:
                file.writelines(content)
        else:
            print('No se elimino ningun campo!')
        
        # Obtener los campos existentes en el modelo
        existing_fields = self.get_existing_fields()
        print("Campos existentes:", existing_fields)
        # input('Presione una tecla para continuar: ')


    def update_admin_file(self):
        '''
        main_description: Actualizar archivo admin.
        '''
        componentes = os.path.normpath(self.file_path).split(os.sep)
        admin_path = os.path.join(*componentes[:-1], 'admin.py').replace(':', ':\\')
        print(admin_path)
        models = self.get_existing_class()
        print(models)
        if len(models) > 0:
            records = ''
            for i in models:
                records = records + f'admin.site.register({i})\n'
            new_content = f'''from django.contrib import admin  
from .models import *

# Register your models here.
{records}
'''
        else:
            new_content = f'''from django.contrib import admin  

            
# Register your models here.
'''
        # replace_file_content(admin_path, new_content)
        admin_object = TextFileManipulator(admin_path)
        admin_object.replace_content(new_content)
        # input('Presione una tecla para continuar: ')


    def all_migrations(self):
        '''
        main_description: Aplicar migraciones.
        Se dirige al directorio raiz del proyecto y ejecuta
        makemigrations y migrate consecutivamente apelando
        al manage.py del proyecto.

        :return: None
        '''
        directorio = os.getcwd()

        componentes = os.path.normpath(self.file_path).split(os.sep)
        app_name = componentes[-2]
        project_path = os.path.join(*componentes[:-2]).replace(':', ':\\')
        print(f'Ejecutando migraciones en: {app_name}')
        os.chdir(project_path)
        subprocess.run(["python", "manage.py", "makemigrations", app_name])
        subprocess.run(["python", "manage.py", "migrate"])
        
        os.chdir(directorio)
        # input('Presione una tecla para continuar: ')


    def add_def_str(self):
        """
        main_description: Agregar metodo str.
        Agregar metodo str.

        :return:
        """

        fields = self.get_existing_fields()
        str_fields = ', '.join(f'{field}=' + '{' + f'self.{field}' + '} ' for field in fields)
        method_name = "__str__"
        method_body = [
            f"out = f'{str_fields}'",
            "return out\n"
        ]

        method_declaration = [
            f"\n    def {method_name}(self):",
            *["        " + line for line in method_body]
        ]

        method_str = "\n".join(method_declaration)
        with open(self.file_path, 'r') as file:
            content = file.readlines()

        start_index = None
        end_index = None
        class_found = False

        for i, line in enumerate(content):
            if line.strip().startswith("class ") and line.strip().endswith(":"):
                class_name = line.strip()[6:-1].split("(")[0].strip()
                if class_name == self.model_name:
                    start_index = i
                    class_found = True
            elif class_found and line.strip() == "":
                end_index = i
                break

        if start_index is not None and end_index is not None:
            content.insert(end_index, method_str)
        else:
            # Class section not found, adding method at the end of the file
            content.append(method_str)

        with open(self.file_path, 'w') as file:
            file.writelines(content)




class views:
    """
    Clase para generar views en Django.

    :param file_path: Ruta del archivo views.py.
    :param view_name: Nombre de la view a generar.
    """
    def __init__(
            self, 
            project_path,
            app_name,
            view_name=None
    ):
        """
        Inicializa una instancia de ViewsGenerator.

        :param file_path: Ruta del archivo views.py.
        :param view_name: Nombre de la view a generar.
        """
        self.file_path = os.path.join(project_path, app_name, 'views.py')

        self.app_name = app_name

        lista_vistas = self.get_existing_def()

        if view_name != None:
            self.view_name = view_name
        elif len(lista_vistas) > 0:
            self.view_name = self.change_view()
        else:
            self.view_name = self.add_view_def()

        self.views_types = self.change_views_types(self.view_name)

        self.object = TextFileManipulator(self.file_path)
        
        componentes = os.path.normpath(self.file_path).split(os.sep)
        urls_path = os.path.join(*componentes[:-1], 'urls.py').replace(':', ':\\')
        self.url_app = TextFileManipulator(urls_path)


    def change_views_types(
            self,
            view_name,
        ):

        views_types = {
            "HttpResponse": f"return HttpResponse('Vista simple {view_name}.')",
            "Template": f"return render(request, '{view_name}.html')",
        }

        return views_types


    def change_view(
            self,
            view_name=None,
    ):
        '''
        main_description: Conectar vista.
        '''
        if view_name==None:
            print('Selecciones el modelo que desea conectar:\n')
            lista_vistas = self.get_existing_def()
            self.view_name = option_list(lista_vistas)
        else:
            self.view_name = view_name
        
        self.views_types = self.change_views_types(self.view_name)
        # print(
        #     self.view_name,
        #     self.views_types
        # )
        # input('Presione una tecla para continuar: ')
        return self.view_name


    def add_view_def(self):
        """
        main_description: Agregar vista.
        Agrega la definición de la funcion de la vista en el archivo views.py.
        Si la vista ya existe, no realiza ninguna acción.
        """
        view_name = input('Introduzca el nombre de la vista: ')
        self.view_name = view_name
        def_str = f"\ndef {self.view_name}(request):\n"
        with open(self.file_path, 'r+') as file:
            content = file.read()
            if def_str not in content:
                file.seek(0, 2)  # Mover el puntero al final del archivo
                file.write(def_str)
        return self.view_name


    def get_existing_def(self):
        '''
        main_description: Listar vistas.
        '''
        with open(self.file_path, 'r') as file:
            content = file.read()

        pattern = r"def\s+(\w+)"
        vistas = re.findall(pattern, content)
        # print(vistas)
        # input('Presione una tecla para continuar: ')
        return vistas  


    def import_HttpResponse(self):
        '''
        main_description: Importa el modulo HttpResponse
        '''
        object = self.object
        content = object.list_content()
        sub_string='from django.http import HttpResponse\n'

        index = object.index_sub_string(
            content=content,
            sub_string=sub_string,
            type_finder=0
        )

        if len(index)==0:
            index = object.index_sub_string(
                content=content,
                sub_string='import',
                type_finder=None
            )

            new_content = object.insert_line(
                section=content,
                position=index[0] + 1,
                new_element="\n"
            )

            new_content = object.insert_line(
                section=content,
                position=index[0] + 1,
                new_element=f"from django.http import HttpResponse"
            )
            
            object.replace_lines_content(new_content)
            print('\t- Importacion de modulo HttpResponse ejecutada.')
        else:
            print('\t- Modulos HttpResponse detectado en el archivo.')


    def add_return(self, view_type=None, view_name=None):
        """
        main_description: Agregar return.
        Agrega un nuevo campo al modelo.

        :param field_type: Tipo de campo a agregar.
                           Si no se proporciona, se solicitará al usuario.
        """
        # print(self.view_name)
        # input('Presione una tecla para continuar: ')

        if not view_type:
            views_list = self.views_types
            view_type = option_list(list(views_list.keys()))
        
        attributes = views_list[view_type]            
        
        return_declaration = f"    {attributes}\n"
        print(return_declaration)
        input('Presione una tecla para continuar: ')

        with open(self.file_path, 'r') as file:
            content = file.readlines()

        start_index = None
        end_index = None
        class_found = False

        for i, line in enumerate(content):
            if line.strip().startswith("def ") and line.strip().endswith(":"):
                class_name = line.strip()[4:-1].split("(")[0].strip()
                if class_name == self.view_name:
                    start_index = i
                    class_found = True
            elif class_found and line.strip() == "":
                end_index = i
                break

        if start_index is not None and end_index is not None:
            content.insert(end_index, return_declaration)
        else:
            # Class section not found, adding field at the end of the file
            content.append(return_declaration)

        with open(self.file_path, 'w') as file:
            file.writelines(content)


    def update_urls_file(self):
        '''
        main_description: Actualizar archivo urls.
        '''
        # Creamos los inputs del proceso.        
        url_app = self.url_app
        content = url_app.list_content()
        if content[-1] == '\n':
            pass
        else:
            content.append('\n')

        inicio = 'urlpatterns = [\n'
        final = '\n'

        sub_string=self.view_name

        # Extraemos el segmento a modificar y el intervalo.
        segment = url_app.segment_num_content(
            content, inicio, final
        )
        section     = segment[0]
        interval    = segment[1]

        # Construimos los contenidos previo y posterior.
        prev_index = [0, interval[0]]
        prev_content = url_app.num_section_content(
            content, prev_index
        )
        post_index = [interval[1], -1]
        post_content = url_app.num_section_content(
            content, post_index
        )

        # Determinamos si la view existe en la lista.
        print(self.view_name)
        condition = url_app.index_sub_string(
            content=section,
            sub_string=sub_string,
            type_finder=None
        )

        print(condition)

        if len(condition)==0:

            # Abrimos un salto de linea.
            # section = url_app.insert_line(
            #     section=section,
            #     position= 1,
            #     new_element="\n"
            # )
            # Insertamos el elemento.
            if self.view_name != 'index':
                new_element=f"\tpath('{self.view_name}/', views.{self.view_name}, name='{self.view_name}'),\n"
            else:
                new_element=f"\tpath('', views.{self.view_name}, name='{self.view_name}'),\n"
            
            section = url_app.insert_line(
                section=section,
                position= 1,
                new_element=new_element
            )

            # Reconstruimos la cadena y reemplazamos en el archivo final.
            new_content = prev_content + section + post_content
            url_app.replace_lines_content(new_content)
        
        else:
            print('\t- Esta view ya se encuentra registrada.')


        # componentes = os.path.normpath(self.file_path).split(os.sep)
        # urls_path = os.path.join(*componentes[:-1], 'urls.py').replace(':', ':\\')
        # print(urls_path)
#         views = self.get_existing_def()
#         print(views)

#         if len(views) > 0:
#             records = ''
#             for i in views:
#                 if i=='index':
#                     records = records + f"\tpath('', views.{i}, name='{i}'),\n"
#                 else:
#                     records = records + f"\tpath('{i}/', views.{i}, name='{i}'),\n"

#             new_content = f'''from django.urls import path
# from . import views

# urlpatterns = [
# {records}
# ]
# '''

#         else:
#             new_content = f'''from django.urls import path
# from . import views

# urlpatterns = [

# ]
# '''

#         self.url_app.replace_content(new_content)
#         input('Presione una tecla para continuar: ')        


    def add_template_view(self):
        '''
        main_description: Agregar template.
        '''
        print('Seleccione la vista:')
        view_name = option_list(self.get_existing_def())

        if view_name!=None:
            # Seleccionamos el template del directorio de templates.
            key0 = 'resources'
            key1 = 'backup_Templates'
            backup_Templates_path = setting_routes(key0)[0] + setting_routes(key1)[0]
            list_Templates = os.listdir(backup_Templates_path)
            print('Seleccione la plantilla:')
            Template = option_list(list_Templates)
            selected_template_path = os.path.join(backup_Templates_path, Template)
            Template_object = TextFileManipulator(selected_template_path)
        
            # Ubicamos la ruta de destino.
            componentes = os.path.normpath(self.file_path).split(os.sep)
            app_path = os.path.join(*componentes[:-1]).replace(':', ':\\')
            templates_path = os.path.join(app_path, 'templates')
            file_path = os.path.join(templates_path, f'{view_name}.html')
            Final_File = TextFileManipulator(file_path)

            new_content = Template_object.show_content().replace('Document', view_name)
            if not os.path.isfile(file_path):
                Final_File.replace_content(new_content)

        input('Presione una tecla para continuar: ')