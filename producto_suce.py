# Este programa acepta n y realiza un calculo de productos sucesivos

 

n = int(input("dame el numero n:  "))

a = 1

for i in range(1, n +1):

    a *= i**2

    print(a)