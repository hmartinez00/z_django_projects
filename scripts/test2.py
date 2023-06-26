import os


# Cintillo de presentacion
print(
    '''
\nPROGRAMACION 1: TELECOMUNICACIONES. UNETI
-------------------------------------------------'''
)



# Ejercicio 1: 
print('''
Ejercicio 1: Verificacion de datos para pago ISLR.
--------------------------------------------------''')
    # Parte 1: Ingreso de datos
user_dates = {
    'numero_de_hijos'   : 'a',
    'edad'              : 'b',
    'sueldo'            : 'c',
}

print('Por favor introduzca los siguientes datos: \n')
for i in user_dates:
    user_dates[i] = input(f'{i}: '.replace('_', ' ').capitalize())

    # Parte 2: Construimos un diccionario para validacion de datos.
val_dates = {
    # Cada clave correspondera a una condicion a evaluar en el
    # proximo bloque de codigo.
    0: [
        # Cada lista estara compuesta por:
            # - Primera entrada de la lista: Una condicion.
            # - Segunda entrada de la lista: El valor que se desea recibir en caso
            # de que la condicion sea falsa.
            # - Tercera entrada de la lista: El valor que se desea recibir en caso
            # de que la condicion sea verdadera.

        (int(user_dates['numero_de_hijos']) < 30),
        'Numero de hijos estadisticamente imposible!',
        None
    ],
    1: [
        (int(user_dates['edad']) > 0 and int(user_dates['edad']) <= 120),
        'Edad fuera de rango!',
        None
    ],
    2: [
        (int(user_dates['edad']) > 18),
        'El contribuyente no puede ser menor de edad!',
        None
    ],

    # ...
    # Aca se pueden agregar otras condiciones de validacion previas
    # Por ejemplo: 
    # es biologicamente imposible que un niño de 10 años 
    # tenga siquiera 1 hijo!
    # o que una persona posea tenga 700 años y tenga 1500 hijos, etc.
    # ...,

    # Aca se agrega la condicion solicitada expresamente
    3: [
            # Se exigen todas estas condiciones segun el enunciado,
            # no solo una o dos, sino Todas sin excepcion, 
            # concentradas en un solo usuario!
            (int(user_dates['numero_de_hijos']) > 5     ) and \
            (int(user_dates['edad'])            > 60    ) and \
            (float(user_dates['sueldo'])        < 2500  )
            # Sin embargo, un usuario con 7 hijos y un sueldo de solo 1000,
            # pero con solo 30 años (<60) tendria que pagar tambien ISLR!
            # solo por no cumplir 1 de las 3 condiciones.
        ,
        'Debe realizar las gestiones para el pago de su ISLR ante el SENIAT',
        'Exento de pago ISLR',
    ]
}

    # Parte 3: Evaluacion de condiciones.
    # Lo haremos mediante un bucle for sobre una lista de
    # condiciones predefinidas en el segmento anterior.
for i in val_dates:

    # Esto es un segmento de codigo deshabilitado solo 
    # para comprobar la validez de las condiciones.
    #
    # if i==3:
    #     print(
    #         (int(user_dates['numero_de_hijos']) > 5     ),
    #         (int(user_dates['edad'])            > 60    ),
    #         (float(user_dates['sueldo'])        < 2500  )
    #     )

    # Aca es donde se ejecutan las comprobaciones
    if val_dates[i][0]==False:
        print('\n' + val_dates[i][1])
        break 
        # En caso de que hayan condiciones falsas el break detendra 
        # el bucle for arrojando donde esta el error!
    else:
        if val_dates[i][2]!=None:
            print('\n' + val_dates[i][2])
        else:
            pass



# Ejercicio 2: 
print('''
Ejercicio 2: Equipos de la LVBP.
--------------------------------------------------''')

    # 1. Definimos la lista
LVBP = [
    'Aguilas del Zulia',
    'Bravos de Margarita',
    'Cardenales de Lara',
    'Caribes de Anzoategui',
    'Leones del Caracas',
    'Navegantes del Magallanes',
    'Tigres de Aragua',
    'Tiburones de La Guaira',
]

encontrado = False

    # 2. Solicitamos los datos al usuario
team = input('Introduzca su equipo favorito: ')

    # 3. Validamos
for i in LVBP:
    if team.lower()==i.lower():
        print(f'Ha seleccionado al glorioso equipo de: {i}!')
        encontrado = True
        break

if not encontrado:
    print("No te gusta la LVBP")



# Ejercicio 3: 
print('''
Ejercicio 3: De donde vienes?
--------------------------------------------------''')

gusto_playa = input("Te gusta la playa? (S/N): ")
gusto_chinchorro = input("Te gusta ir a los chinchorros? (S/N): ")
gusto_rios = input("Te gusta visitar los rios? (S/N): ")

es_oriental = False

while not es_oriental:
    if gusto_playa.lower() == "s" or gusto_chinchorro.lower() == "s" or gusto_rios.lower() == "s":
        print("Usted parece oriental.")
        procedencia = input("Indique su procedencia: ")
        if procedencia.lower() == "nacido" or procedencia.lower() == "criado":
            print("A usted le gusta el oriente!")
            break
    else:
        print("Respuestas:")
        print("Gusto playa:", gusto_playa)
        print("Gusto chinchorro:", gusto_chinchorro)
        print("Gusto rios:", gusto_rios)
        break



# Ejercicio 4: 
print('''
Ejercicio 4: Generadores
--------------------------------------------------''')

def generador_capitales():
    capitales = []
    while True:
        capital = input("Ingrese una capital de estado de Venezuela (o 'salir' para terminar): ")
        if capital.lower() == "salir":
            break
        capitales.append(capital)
        yield capital

generador = generador_capitales()

print("Las primeras 10 capitales ingresadas son:")
for _ in range(10):
    try:
        capital = next(generador)
        print(capital)
    except StopIteration:
        print("Se han ingresado menos de 10 capitales.")
        break


# Ejercicio 5: 
print('''
Ejercicio 5: Generadores
--------------------------------------------------''')

def generador_nombres(nombre1, nombre2, nombre3):
    nombres = [nombre1, nombre2, nombre3]

    for nombre in nombres:
        if len(nombre) >= 7:
            yield nombre[:8]

# Solicitar los nombres al usuario
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")
nombre3 = input("Ingrese el tercer nombre: ")

# Crear una instancia del generador
gen = generador_nombres(nombre1, nombre2, nombre3)

# Imprimir los primeros ocho caracteres de los nombres que cumplen con el requisito
for nombre in gen:
    print(nombre)



# EOF
print('\n\n')