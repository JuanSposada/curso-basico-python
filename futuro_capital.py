"""este programa calcula el futuro capital de una cantidad de dinero a partir
del capital inicial, el interes y el tiempo"""

#entrada de datos
capital_inicial = int(input("ingrese el capital inicial: ")) 
interes = float(input("ingrese el interes: "))
tiempo = int(input("durante cuantos años? "))

interes /= 100

capital_final = (capital_inicial * interes * tiempo) + capital_inicial
print(capital_final)