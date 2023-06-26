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
    user_dates[i] = input(f'Por favor intorduzca su {i}: ')

print(user_dates)

# EOF
print('\n\n')