"""este programa resulve una ecuancion de segundo grado, dados
los valores de a, b y c"""
#declaracion de variables
a = 4
b = -6
c = 2

#formunla
x1 = (-b + ((b**2) - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - ((b**2) - 4 * a * c) ** 0.5) / (2 * a)

print(x1)
print(x2)