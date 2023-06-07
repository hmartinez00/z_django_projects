import os


datos = {
    'nombre': 'fulanito',
    'apellido': 'de tal',
    'carrera': 'Ingenieria de sofware',
    'seccion': 'A',
    'edo_residencia': 'Guarico',
    'lug_nacimiento': 'Caracas',
    'materias': ['materia1', 'materia2', 'materia3']
}

# -----------------------------------------------
# Ejercicio a: 
# Elaborar una Impresion por pantalla que indique nombre completo,
# en que seccion se encuentra y que carrera de Ingenieria de la
# UNETI esta cursando. 

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
# i. Primera Impresion: Primer Nombre y Primer Apellido
# ii. Segunda Impresion: Lugar de Nacimiento
# iii. Tercera Impresion: Estado de Venezuela donde viven
# actualmente. 

# Resultados:
print('\nEjercicio b:')
print('Nombre completo:'    , datos['nombre']   , datos['apellido'])
print('Lugar de Nacimiento:', datos['lug_nacimiento'])
print('Edo de Residencia'   , datos['edo_residencia'])

# -----------------------------------------------
# Ejercicio c:
# Identificar los ejercicios:
# i. Agregar un comentario antes de cada ejercicio.
# ii. Imprimir por pantalla un título que indique el ejercicio que se
# reflejará en pantalla. 

# Este no es un ejercicio. Corresponde a instrucciones para presentar
# los resultados en pantalla. Se sugiere colocar en el numeral 1 del PDF
# con el resto de la instrucciones previas a los enunciados concretos.


# -----------------------------------------------
# Ejercicio d:
# Elaborar una Lista (colocar un nombre representativo) e imprimirla
# por pantalla que indique las materias que esta cursando
# actualmente en la UNETI. En caso de estar cursando solo una
# materia, agregar al menos dos materias adicionales que le gustaria
# estar cursando.

# Resultados:
print('\nEjercicio d:')
Lista_materia_cursadas = list(datos['materias'])
print(Lista_materia_cursadas)

# -----------------------------------------------
# Ejercicio e:
# A la lista anterior agregar en la posicion 1 la materia: Logica
# Matematica e imprimirla por pantalla. 

# Nota: Las listas comienzan a enumerar desde al posicion 0, de manera que la posicion 1 debe ser obligatoriamente la segunda posicion de la lista si se cuenta usando numeros naturales.

# Resultados:
print('\nEjercicio e:')
new_element = 'Logica Matematica'
position = 1
# el metodo de strings "insert" puede resolver la situacion de forma sencilla.
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

print('Nombre:'             , tupla[0]  )
print('Apellido:'           , tupla[1]  )
print('Seccion: '           , tupla[2]  )
print('Edo de Residencia:'  , tupla[3]  )
print('Valor de la Tupla: ' , tupla     )


# # Otra manera de resolver esto mucho mas compactamente es:
# tupla = [] #Se define primero como una lista
# for i in datos.keys():
#     tupla.append(datos[i])
# tupla = tuple(tupla) # Esto convierte el tipo de dato a tupla, 
# que es lo que se esta pidiendo precisamente.

# # Luego podemos imprimir:
# for i in tupla:
#     print(i)


# -----------------------------------------------
# Ejercicio g:
# Elaborar un diccionario que contenga:
# i. Todos los estados de Venezuela y sus capitales.
# ii. Una clave adicional con su Nombre: y su estado de
# Residencia

# Resultados:
print('\nEjercicio g:')
estados_capitales = {
    'Amazonas'          : 'Puerto Ayacucho',
    'Anzoategui'        : 'Barcelona',
    'Apure'             : 'San Fernando de Apure',
    'Aragua'            : 'Maracay',
    'Barinas'           : 'Barinas',
    'Bolivar'           : 'Ciudad Bolivar',
    'Carabobo'          : 'Valencia',
    'Cojedes'           : 'San Carlos',
    'Delta Amacuro'     : 'Tucupita',
    'Falcon'            : 'Coro',
    'Guarico'           : 'San Juan de los Morros',
    'Lara'              : 'Barquisimeto',
    'Merida'            : 'Merida',
    'Miranda'           : 'Los Teques',
    'Monagas'           : 'Maturin',
    'Nueva Esparta'     : 'La Asuncion',
    'Portuguesa'        : 'Guanare',
    'Sucre'             : 'Cumana',
    'Tachira'           : 'San Cristobal',
    'Trujillo'          : 'Trujillo',
    'Vargas'            : 'La Guaira',
    'Yaracuy'           : 'San Felipe',
    'Zulia'             : 'Maracaibo',
    'Distrito Capital'  : 'Caracas',
}

# Añadiendo clave adicional:
estados_capitales[datos['nombre']] = datos['edo_residencia']

# Imprimir el diccionario completo
print(estados_capitales)

# -----------------------------------------------
# Ejercicio h:
# Elaborar un diccionario donde las claves sean dadas por una lista.
# Elegir cinco estados de Venezuela, donde la posicion 3 tendra
# como clave su nombre y su valor su Estado de residencia. 

# Resultados:
print('\nEjercicio h:')

#Definimos la posicion donde vamos a insertar los datos.
position = 2

# Contruimos las listas con las claves y valores del anterior diccionario
# y cortamos los primeros 5 valores. Eso es lo que se nos ha indicado al 
# pedir seleccionar 5 estados.
claves  = list(estados_capitales.keys())[:5]
valores = list(estados_capitales.values())[:5]

# Redefinimos la 3 posicion segun el conteo de numeros naturales
claves[position]   = datos['nombre']
valores[position]  = datos['edo_residencia']

# Confluimos ambas listas en un solo diccionario mediante el objeto zip
# y convertimos el tipo de datos a diccionario
diccionario = dict(zip(claves, valores))

# Mostramos en pantalla.
print(diccionario)


# -----------------------------------------------
input('Presione una tecla para continuar: ')
