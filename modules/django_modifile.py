from modules.TextFileManipulator import TextFileManipulator


class settings:
    '''
    Clase para manipular archivo settings.py de Django.

    :param file_path: Ruta del archivo settings.py.
    '''
    def __init__(self, file_path):
        '''
        Inicializa una instancia de settings.

        :param file_path: Ruta del archivo settings.py.
        '''
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
            print('Importacion de modulo os ejecutada.')
        else:
            print('Modulos os detectado en el archivo.')


        input('Presione una tecla para continuar: ')


    def install_template_dir(
        self,
        new_dir=None
    ):
        '''
        main_description: Insertar en TEMPLATE.
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
            type_finder=0
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
