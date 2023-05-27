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


    def num_section_content(self, interval=None):
        '''
        main_description: Mostrar segmento.
        '''

        if interval == None:
            str_start   = input('Introduzca el numero de linea de inicio: ')
            str_end     = input('Introduzca el numero de linea de cierre: ')
            interval    = [str_start, str_end]

        content = self.list_content()

        print(interval)


    def section_content(self, interval=None):
        '''
        main_description: Mostrar fragmento.
        '''
        
        if interval == None:           
            str_start   = input('Introduzca la cadena de inicio: ')
            str_end     = input('Introduzca la cadena de cierre: ')
            interval    = [str_start, str_end]

        content = self.show_content()
        start_index = content.index(interval[0])
        end_index = content.find(interval[1], start_index)
        if end_index == -1:
            # No se encontró una línea en blanco adicional, ajustar el índice final
            end_index = len(content)
        class_section = content[start_index:end_index]
        
        print(class_section)
        input('Presione una tecla para continuar: ')
        return class_section
