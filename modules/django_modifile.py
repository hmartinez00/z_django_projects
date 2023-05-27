

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


    def section_content(self, interval=None):
        '''
        main_description: Mostrar fragmento.
        '''
        
        if interval == None:           
            str_start   = input('Introduzca la cadena de inicio: ')
            str_end     = input('Introduzca la cadena de cierre: ')
            interval    = [str_start, str_end]

        content = self.show_content()
        print(interval)
        start_index = content.index(interval[0])
        print(start_index)
        print(interval[1])
        end_index = content.find(interval[1], interval[0])
        # print(end_index)
        print(start_index, end_index)

        # if end_index == -1:
        #     # No se encontró una línea en blanco adicional, ajustar el índice final
        #     end_index = len(content)
        # class_section = content[start_index:end_index]
        
        # print(class_section)
        input('Presione una tecla para continuar: ')

