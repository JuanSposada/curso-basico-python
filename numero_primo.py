# este programa calcula si un numero es primo con un ciclo for

 

 

num = int(input("dame un numero: "))

 

if num == 1:

    print("1 no es un numero ni primo ni compuesto")

if num == 2:

    print("Es primo")

for i in range (2, num):

    if num % i == 0:

        print("es numero compuesto")

        break

else: print("es primo")