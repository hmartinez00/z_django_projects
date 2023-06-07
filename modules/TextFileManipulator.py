import os


class TextFileManipulator:
    '''
    Clase para manipular archivos de proyectos Django.

    :param file_path: Ruta del archivo.
    '''
    def __init__(self, file_path):
        '''
        Inicializa una instancia de TextFileManipulator.

        :param file_path: Ruta del archivo.
        '''
        self.file_path = file_path

    
    def show_content(self):
        '''
        main_description: Mostrar contenido.
        '''
        with open(self.file_path, 'r') as f:
            content = f.read()
        
        # print(content)
        # input('Presione una tecla para continuar: ')
        return content

    def list_content(self):
        '''
        main_description: Listar contenido.
        '''
        with open(self.file_path, 'r') as f:
            content = f.readlines()
        
        # print(content)
        # input('Presione una tecla para continuar: ')
        return content


    def num_content(self):
        '''
        main_description: Desplegar contenido enumerado.
        '''
        with open(self.file_path, 'r') as f:
            for i, line in enumerate(f):
                print(i, line)
        
        input('Presione una tecla para continuar: ')


    def replace_content(self, new_content=None):
        '''
        main_description: Reemplazar contenido.
        Reemplaza todo el contenido de un archivo.
        '''
        if new_content == None:
            new_content = input('Introduzca el nuevo contenido: ')
 
        with open(self.file_path, 'w') as f:
            f.write(new_content)


    def replace_lines_content(self, new_content=None):
        '''
        main_description: Reemplazar contenido.
        Reemplaza todo el contenido de un archivo.
        '''
        if new_content == None:
            new_content = input('Introduzca el nuevo contenido: ')

        with open(self.file_path, 'w') as f:
            f.writelines(new_content)


    def section_content(self, content=None, interval=None):
        '''
        main_description: Mostrar fragmento.
        '''
        if content == None:
            content = self.show_content()
        
        if interval == None:           
            str_start   = input('Introduzca la cadena de inicio: ')
            str_end     = input('Introduzca la cadena de cierre: ')
            interval    = [str_start, str_end]

        start_index = content.index(interval[0])
        end_index = content.find(interval[1], start_index)
        if end_index == -1:
            # No se encontró una línea en blanco adicional, ajustar el índice final
            end_index = len(content)
        section = content[start_index:end_index]
        
        # print(section)
        # input('Presione una tecla para continuar: ')
        return section


    # -------------------------------------------
    # En esta seccion definimos los metodos para detectar lineas cnocretas y extraer segmentos de texto.
    # -------------------------------------------


    def index_sub_string(
        self, 
        content=None,
        sub_string=None, 
        type_finder=None
    ):
        '''
        main_description: Extraer indice de linea.
        '''
        if content==None: 
            content = self.list_content()
        
        if sub_string == None:
            sub_string = input('Introduca la subcadena: ')

        index = []
        for i in range(len(content)):
            if type_finder==None:
                if sub_string in content[i]:
                    index.append(i)
            elif type_finder==0:
                if sub_string == content[i]:
                    index.append(i)
            
        # print(index)
        # input('Presione una tecla para continuar: ')
        
        return index


    def num_section_content(
        self, 
        content=None, 
        interval=None
    ):
        '''
        main_description: Mostrar segmento.
        '''
        if content == None:
            content = self.list_content()

        if interval==None:
            str_start   = int(input('Introduzca el numero de linea de inicio:'))
            str_end     = int(input('Introduzca el numero de linea de final:'))
            interval    = [str_start, str_end]

        section = content[interval[0]: interval[1]]

        # print(section)
        # input('Presione una tecla para continuar: ')
        return section


    def segment_num_content(
        self, 
        content=None, 
        inicio=None,
        final=None,
    ):
        '''
        main_description: Mostrar segmento entre cadenas.
        '''
        if content==None:
            content = self.list_content()

        if inicio != final:
            str_start = self.index_sub_string(content=content, sub_string=inicio, type_finder=0)[0]
            new_str_end = []
            for i in self.index_sub_string(content=content, sub_string=final, type_finder=0):
                if i >= str_start:
                    new_str_end.append(i)
            str_end = new_str_end[0]

        elif inicio == final:
            str_start = self.index_sub_string(content=content, sub_string=inicio)[0]
            str_end = str_start + 1

        interval = [str_start, str_end]
        # print(interval)
        section = self.num_section_content(
            content, interval
        )

        # print(section)
        # input('Presione una tecla para continuar: ')
        return section, interval


    def replace_line(
        self,
        index,
        section,
        new_substring
    ):
        '''
        main_description: Reemplazar linea.
        '''
        section[index] = new_substring
        return section


    def insert_line(
        self,
        section,
        position,
        new_element,
    ):
        '''
        main_description: Insertar linea.
        '''

        section.insert(position, new_element)
        return section


    def insert_substring(self, substring=None):
        '''
        main_description: Insertar linea en archivo abierto.
        '''
        file = self.file_path

        # Abrir el archivo en modo de lectura para obtener la posición actual del cursor
        with open(file, 'r') as file_obj:
            current_position = file_obj.tell()

        print(current_position)

        # # Abrir el archivo en modo de escritura para realizar la inserción
        # with open(file, 'w') as file_obj:
        #     file_obj.seek(current_position)  # Mover el cursor a la posición guardada
        #     content = file_obj.read()  # Leer el contenido restante del archivo
        #     # Realizar la inserción de la subcadena en la posición deseada
        #     new_content = content[:current_position] + substring + content[current_position:]
        #     file_obj.write(new_content)

        input('Presione una tecla para continuar: ')

        # file_obj.close()

        # if substring==None:
        #     substring=input('Ingrese la cadena a insertar: ')

        # # Insertar la subcadena en la posición actual del cursor
        # updated_content = content[:current_position] + substring + content[current_position:]

        # # Regresar al principio del archivo y escribir el contenido actualizado
        # file.seek(0)
        # file.write(updated_content)

        # # Mover el cursor al final del contenido insertado
        # file.seek(current_position + len(substring))
        #     # insert_substring(file, 'Subcadena a insertar')


