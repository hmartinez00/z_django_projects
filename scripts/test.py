import sys

# Establecer la codificación de entrada y salida
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

datos = {
    'nombre': 'fulanito',
    'apellido': 'de tal',
    'carrera': 'Ingenieria de sofware',
    'seccion': 'A',
    'lug_nacimiento': 'Caracas',
    'edo_residencia': 'Guarico',
    'materias': ['materia1', 'materia2', 'materia3']
}

# -----------------------------------------------
# Ejercicio a: 
# Elaborar una Impresión por pantalla que indique nombre completo,
# en que sección se encuentra y que carrera de Ingeniería de la
# UNETI está cursando. 

# Resultados:
print('\nEjercicio a:')
print(
    f'''
    Nombre completo:\t{datos['nombre']} {datos['apellido']}
    Carrera en Curso:\t{datos['carrera']}
    '''
)

# -----------------------------------------------
# Ejercicio b: 
# Elaborar tres impresiones (tres instrucciones print distintas) por
# pantalla que indiquen:
# i. Primera Impresión: Primer Nombre y Primer Apellido
# ii. Segunda Impresión: Lugar de Nacimiento
# iii. Tercera Impresión: Estado de Venezuela donde viven
# actualmente. 

# Resultados:
print('\nEjercicio b:')
print(datos['nombre'], datos['apellido'])
print(datos['lug_nacimiento'])
print(datos['edo_residencia'])

# -----------------------------------------------
# Ejercicio d:
# Elaborar una Lista (colocar un nombre representativo) e imprimirla
# por pantalla que indique las materias que está cursando
# actualmente en la UNETI. En caso de estar cursando sólo una
# materia, agregar al menos dos materias adicionales que le gustaría
# estar cursando.

# Resultados:
print('\nEjercicio d:')
Lista_materia_cursadas = list(datos['materias'])
print(Lista_materia_cursadas)

# -----------------------------------------------
# Ejercicio e:
# A la lista anterior agregar en la posición 1 la materia: Lógica
# Matemática e imprimirla por pantalla. 

# Nota: Las listas comienzan a enumerar desde al posicion 0, de manera que la posicion 1 debe ser obligatoriamente la segunda posicion de la lista si se cuenta usando numeros naturales.

# Resultados:
print('\nEjercicio e:')
new_element = 'Lógica Matemática'
position = 1
Lista_materia_cursadas.insert(position, new_element)
print(Lista_materia_cursadas)

# -----------------------------------------------
# Ejercicio f:
# Elaborar e imprimir por pantalla una Tupla que contenga:
# i. Empaquetado de los campos: Nombre, Apellido, Seccion,
# Estado Residencia.
# ii. Imprimir cada valor de variable por pantalla (usando print) y
# luego imprimir la tupla completa 

# Resultados:
print('\nEjercicio f:')
tupla = (
    datos['nombre'], 
    datos['apellido'],
    datos['seccion'],
    datos['edo_residencia'],
)

print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla)

# -----------------------------------------------
# Ejercicio g:
# Elaborar un diccionario que contenga:
# i. Todos los estados de Venezuela y sus capitales.
# ii. Una clave adicional con su Nombre: y su estado de
# Residencia

# Resultados:
print('\nEjercicio g:')
estados_capitales = {
    'Amazonas': 'Puerto Ayacucho',
    'Anzoátegui': 'Barcelona',
    'Apure': 'San Fernando de Apure',
    'Aragua': 'Maracay',
    'Barinas': 'Barinas',
    'Bolívar': 'Ciudad Bolívar',
    'Carabobo': 'Valencia',
    'Cojedes': 'San Carlos',
    'Delta Amacuro': 'Tucupita',
    'Falcón': 'Coro',
    'Guárico': 'San Juan de los Morros',
    'Lara': 'Barquisimeto',
    'Mérida': 'Mérida',
    'Miranda': 'Los Teques',
    'Monagas': 'Maturín',
    'Nueva Esparta': 'La Asunción',
    'Portuguesa': 'Guanare',
    'Sucre': 'Cumaná',
    'Táchira': 'San Cristóbal',
    'Trujillo': 'Trujillo',
    'Vargas': 'La Guaira',
    'Yaracuy': 'San Felipe',
    'Zulia': 'Maracaibo',
    'Distrito Capital': 'Caracas'
}

# Imprimir el diccionario completo
print(estados_capitales)

# -----------------------------------------------
# Ejercicio h:
# Elaborar un diccionario donde las claves sean dadas por una lista.
# Elegir cinco estados de Venezuela, donde la posición 3 tendrá
# como clave su nombre y su valor su Estado de residencia. 

# Resultados:
print('\nEjercicio h:')
claves = ['clave1', 'clave2', datos['nombre'], 'clave4', 'clave5']
valores = ['valor1', 'valor2', datos['edo_residencia'], 'valor4', 'valor5']

diccionario = dict(zip(claves, valores))
print(diccionario)


# -----------------------------------------------
input('Presione una tecla para continuar: ')

