import os
from modules.TextFileManipulator import TextFileManipulator


class settings:
    '''
    Clase para manipular archivo settings.py de Django.

    :param project_path: Ruta del proyecto.
    '''
    def __init__(
            self, 
            project_path
    ):
        '''
        Inicializa una instancia de settings.

        :param project_path: Ruta del proyecto.
        '''
        project_name = os.path.basename(project_path)
        file_path = os.path.join(project_path, project_name, 'settings.py')        
        self.file_path = file_path
        self.object = TextFileManipulator(self.file_path)


    def import_os(self):
        '''
        main_description: Importa el modulo os
        '''
        object = self.object
        content = object.list_content()
        sub_string='import os\n'

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
                new_element=f"import os"
            )
            
            object.replace_lines_content(new_content)
            print('\t- Importacion de modulo os ejecutada.')
        else:
            print('\t- Modulos os detectado en el archivo.')


        # input('Presione una tecla para continuar: ')


    def install_app(
        self,
        app_name=None
    ):
        '''
        main_description: Instalar en INSTALLED_APPS.
        '''
        # Creamos los inputs del proceso.        
        object = self.object
        content = object.list_content()
        inicio = 'INSTALLED_APPS = [\n'
        final = '\n'

        if app_name==None:
            app_name = input('Introduzca la ruta al directorio de templates: ')

        sub_string=app_name

        # Extraemos el segmento a modificar y el intervalo.
        segment = object.segment_num_content(
            content, inicio, final
        )
        section     = segment[0]
        interval    = segment[1]

        # Construimos los contenidos previo y posterior.
        prev_index = [0, interval[0]]
        prev_content = object.num_section_content(
            content, prev_index
        )
        post_index = [interval[1], -1]
        post_content = object.num_section_content(
            content, post_index
        )

        # Determinamos si la app existe en la lista.
        condition = object.index_sub_string(
            content=section,
            sub_string=sub_string,
            type_finder=None
        )

        print(condition)

        if len(condition)==0:

            # Abrimos un salto de linea.
            section = object.insert_line(
                section=section,
                position= 1,
                new_element="\n"
            )
            # Insertamos el elemento.
            section = object.insert_line(
                section=section,
                position= 1,
                new_element=f"\t'{app_name}',"
            )

            # Reconstruimos la cadena y reemplazamos en el archivo final.
            new_content = prev_content + section + post_content
            object.replace_lines_content(new_content)
        
        else:
            print('\t- Esta app ya se encuentra instalada en la lista INSTALLED_APPS.')


    def install_template_dir(
        self,
        new_dir=None
    ):
        '''
        main_description: Instalar directorio en TEMPLATE.
        Inserta un nuevo elemento en la lista TEMPLATE para hacer la instalacion segun los protocolos de Django.
        
        :params:
        :returns: 
        '''
        # Creamos los inputs del proceso.        
        object = self.object
        content = object.list_content()
        inicio = 'TEMPLATES = [\n'
        final = '\n'

        if new_dir==None:
            new_dir = input('Introduzca la ruta al directorio de templates: ')

        sub_string=new_dir

        index = object.index_sub_string(
            content=content,
            sub_string=sub_string,
            type_finder=None
        )

        if len(index)==0:

            # Extraemos el segmento a modificar y el intervalo.
            segment = object.segment_num_content(
                content, inicio, final
            )
            section     = segment[0]
            interval    = segment[1]

            # Construimos los contenidos previo y posterior.
            prev_index = [0, interval[0]]
            prev_content = object.num_section_content(
                content, prev_index
            )
            post_index = [interval[1], -1]
            post_content = object.num_section_content(
                content, post_index
            )

            # Extraemos el indice del renglon de pivoteo
            # dentro del segmento de trabajo y modificamos
            # para ajustar la condiciones de insercion.
            index = object.index_sub_string(
                content=section,
                sub_string="        'DIRS': [],\n", 
                type_finder=0
            )

            if len(index)!=0:
                section = object.replace_line(
                    index=index[0],
                    section=section,
                    new_substring="        'DIRS': [\n"
                )

                section = object.insert_line(
                    section=section,
                    position=index[0] + 1,
                    new_element="\t\t],\n"
                )

            # Aseguradas las condiciones de insercion
            # ejecutamos las operaciones:
            index = object.index_sub_string(
                content=section,
                sub_string="        'DIRS': [\n", 
                type_finder=0
            )
                # Abrimos un salto de linea.
            section = object.insert_line(
                section=section,
                position=index[0] + 1,
                new_element="\n"
            )
                # Insertamos el elemento.
            section = object.insert_line(
                section=section,
                position=index[0] + 1,
                new_element=f"\t\t\t{new_dir},"
            )

            # Reconstruimos la cadena y reemplazamos en el archivo final.
            new_content = prev_content + section + post_content
            object.replace_lines_content(new_content)
        
        else:
            print('\t- El directorio ya esta registrado en la lista de TEMPLATES.')


    def install_static_dir(self):
        '''
        main_description: Instalar directorio en STATICFILES.
        Crea la lista STATICFILE e Inserta un nuevo elemento segun los protocolos de Django.
        
        :params:
        :returns: 
        '''
        # Importamos modulo os.
        self.import_os()
        object = self.object
        # Instala la ruta de static en settings.
        new_dir = f"os.path.join(BASE_DIR, 'static')"
        content = object.list_content()

        index = object.index_sub_string(
            content=content,
            sub_string=new_dir,
            type_finder=None
        )

        if len(index)==0:

            sub_string="STATICFILES_DIRS = [\n"

            index = object.index_sub_string(
                content=content,
                sub_string=sub_string,
                type_finder=0
            )

            if len(index)==0:
                sub_string="STATIC_URL = 'static/'\n"

                index = object.index_sub_string(
                    content=content,
                    sub_string=sub_string,
                    type_finder=0
                )

                new_content = object.insert_line(
                    section=content,
                    position=index[0] + 1,
                    new_element="\n"
                )

                new_content = object.insert_line(
                    section=content,
                    position=index[0] + 1,
                    new_element="]"
                )

                new_content = object.insert_line(
                    section=content,
                    position=index[0] + 1,
                    new_element=f"STATICFILES_DIRS = [\n"
                )

                index = [index[0] + 1]


            new_content = object.insert_line(
                section=content,
                position=index[0] + 1,
                new_element=f"\t{new_dir},\n"
            )

            object.replace_lines_content(new_content)
            print('\t- Insercion de STATICFILES_DIRS ejecutada.')

        else:
            print('\t- Directorio static detectado en el archivo.')


class urls:
    '''
    Clase para manipular archivo urls.py de Django.

    :param project_path: Ruta del proyecto.
    '''
    def __init__(
        self, 
        project_path,
        app_name,
    ):
        '''
        Inicializa una instancia de urls.

        :param project_path: Ruta del proyecto.
        :app_name: Nombre de la app con cuyo urls.py se desea conectar.
        '''
        self.app_name = app_name
 
        project_name = os.path.basename(project_path)
        url_project_path = os.path.join(project_path, project_name, 'urls.py')        
        url_app_path = os.path.join(project_path, self.app_name, 'urls.py')        
        self.url_project_path = url_project_path
        self.url_app_path = url_app_path
   
        self.url_project = TextFileManipulator(self.url_project_path)
        self.url_app = TextFileManipulator(self.url_app_path)


    def import_include(self):
        '''
        Importa la funcion include en la zona de importacion de modulos.
        '''
        url_project = self.url_project
        content = url_project.list_content()
        sub_string='from django.urls import path, include\n'

        index = url_project.index_sub_string(
            content=content,
            sub_string=sub_string,
            type_finder=0
        )

        if len(index)==0:
            sub_string = 'from django.urls import path'

            index = url_project.index_sub_string(
                content=content,
                sub_string=sub_string,
                type_finder=None
            )

            new_content = url_project.replace_line(
                index=index[0],
                section=content,
                new_substring=f"{sub_string}, include\n"
            )
            print(new_content[index[0]])
            
            url_project.replace_lines_content(new_content)
            print('\t- Importacion de la funcion include ejecutada.')
        else:
            print('\t- Funcion include detectada en el archivo.')


    def reg_url_app_project(self):
        '''
        main_description: Instalar en urlpatterns.
        '''
        # Creamos los inputs del proceso.        
        url_project = self.url_project
        content = url_project.list_content()
        if content[-1] == '\n':
            pass
        else:
            content.append('\n')

        inicio = 'urlpatterns = [\n'
        final = '\n'

        sub_string=self.app_name

        # Extraemos el segmento a modificar y el intervalo.
        segment = url_project.segment_num_content(
            content, inicio, final
        )
        section     = segment[0]
        interval    = segment[1]

        # Construimos los contenidos previo y posterior.
        prev_index = [0, interval[0]]
        prev_content = url_project.num_section_content(
            content, prev_index
        )
        post_index = [interval[1], -1]
        post_content = url_project.num_section_content(
            content, post_index
        )

        # Determinamos si la app existe en la lista.
        condition = url_project.index_sub_string(
            content=section,
            sub_string=sub_string,
            type_finder=None
        )

        print(condition)

        if len(condition)==0:

            # Abrimos un salto de linea.
            section = url_project.insert_line(
                section=section,
                position= 1,
                new_element="\n"
            )
            # Insertamos el elemento.
            section = url_project.insert_line(
                section=section,
                position= 1,
                new_element=f"\tpath('{self.app_name}/', include('{self.app_name}.urls')),"
            )

            # Reconstruimos la cadena y reemplazamos en el archivo final.
            new_content = prev_content + section + post_content
            url_project.replace_lines_content(new_content)
        
        else:
            print('\t- Esta app ya se encuentra registrada.')


    def reg_url_app_app(self):
        '''
        Crea el archivo urls.py de la app.
        '''
        print(f'Creando {self.app_name}/urls.py')
        content = '''from django.urls import path
from . import views

urlpatterns = [

]
'''
    # path('', views.index, name='index'),
        self.url_app.replace_content(content)
