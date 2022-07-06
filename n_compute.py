"""acepte un entero n y compute el valor de n + nn
+ nnn """

n = input(" ingrese un numero entero: ")
print(n)
n2 = n + n
n3= n2 + n
print(f'{n} + {n2} + {n3}')
n = int(n)
n2 = int(n2)
n3 = int(n3)
print('= ', n + n2 + n3)