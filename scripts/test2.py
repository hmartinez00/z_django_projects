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



# EOF
print('\n\n')