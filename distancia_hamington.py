# este programa calcula la distancia hammington entre dos palabras de la misma longitud

 

print(""" ingresa dos palabras de la misma longitud

para calcular la distancia hammington entre ellas: """)

 

palabra_1 = input("ingresa palabra 1: ")

palabra_2 = input("ingrese palabra 2: ")

 

if len(palabra_1) != len(palabra_2):

    print("error, las palabras tienen diferente longitud")

else:

    i = 0

    j = 0

    while i < len(palabra_1):

        if palabra_1[i] != palabra_2[i]:

            j += 1


        i += 1

    else: print("esta es la distancia hammington", j)    