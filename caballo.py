# este programa simula el movimiento de un caballo de ajedrez, imprime el recorrido

 

objetivo_x = int(input("dame el valor de x: "))

objetivo_y = int(input("dame el valor de y: "))


x = 0

y = 0

while x < objetivo_x and y < objetivo_y:

    print(f"({x},{y})")

    x += 2

    y += 1

 

    print(f"({x},{y})")

    x += 1

    y += 2