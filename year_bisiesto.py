"""dado un año, el programa calcula si es bisiesto o no lo es"""

# entrada de datos

year = int(input('ingese un año para saber si es bisiesto: '))

# condicional
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('el año es bisiesto')
else: print('este año NO es bisiesto')