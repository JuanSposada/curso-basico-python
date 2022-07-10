# este programa dados 3 valores calcula cual es el minimo

#entrada de datos
valor_1 = int(input("dame un valor: "))
valor_2 = int(input("dame un valor: "))
valor_3 = int(input("dame un valor: "))

 
# condicional para comparar
if (valor_1 < valor_2) and (valor_1 < valor_3):
    print('este es el minimo:', valor_1)
elif valor_2< valor_1 and valor_2 < valor_3:
    print('este es el minimo:', valor_2)
elif valor_3< valor_1 and valor_3 < valor_1:
    print('este es el minimo:', valor_3)
else: print('error!! 💥')
