"""este programa te da la distancia euclidia entre dos puntos en 2 dimensiones"""
# Entrada de variables
x1 = int(input("ingrese la coordenada x del punto A: "))
y1 = int(input("ingrese la coordenada y del punto A: "))
x2 = int(input("ingrese la coordenada x del punto B: "))
y2 = int(input("ingrese la coordenada y del punto B: "))


# Funcion de la distancia euclidea
distancia_e = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print(f" d(A,B) = {distancia_e}")