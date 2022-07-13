#Este programa compara los valores en una cadena para saber si son alfabeticos

 

 

palabra = input("introduce una palabra: ")

if palabra.isalpha() == False:

    print(" se ha encontrado caracteres no alfabeticos")