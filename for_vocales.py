# Dada una palabra, este programa calcula cuantas vocales tiene

 

palabra = input("ingresa palabra: ")

i= 0

for letra in palabra:

    if letra == "a":

        i += 1

    elif letra == "e":

        i += 1

    elif letra == "i":

        i += 1

    elif letra == "o":

        i += 1

    elif letra == 'u':

        i += 1

print("esta es la cantidad de vocales que tiene tu palabra: ", i)       

