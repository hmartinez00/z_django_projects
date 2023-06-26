import os


# Cintillo de presentacion
print(
    '''
\nPROGRAMACION 1: TELECOMUNICACIONES. UNETI
-------------------------------------------------'''
)

# Ejercicio 1: 
print('\nEjercicio 1: Verificacion de datos para pago ISLR.\n')

user_dates = {
    'numero_de_hijos'   : 'a',
    'edad'              : 'b',
    'sueldo'            : 'c',
}

for i in user_dates:
    user_dates[i] = input(f'Por favor introduzca su {i}: '.replace('_', ' '))

validate_condition = \
    (int(user_dates['edad']) >= 18  ) and \
    (int(user_dates['edad']) <  120 )

condition = \
    (int(user_dates['numero_de_hijos']) > 5     ) and \
    (int(user_dates['edad'])            > 60    ) and \
    (float(user_dates['sueldo'])        < 2500  )

if validate_condition:
    if condition:
        print('\n\nExento de pago ISLR')
    else:
        print('\n\nDebe realizar las gestiones para el pago de su ISLR ante el SENIAT')
else:
    print('\n\nPor favor verifique la edad del usuario.')


# EOF
print('\n\n')