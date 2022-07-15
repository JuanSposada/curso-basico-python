# Este programa identifica si la palabra es isograma

 

palabra = input(" dame una palabra: ")

palabra = list(palabra)

for item in palabra:

    f = palabra.pop(0)

    if (f in palabra) == True:

        print("error")

        break

else: print("es isograma")