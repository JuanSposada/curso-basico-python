
# este programa te da el producto cartesiano de dos cadenas

 

cadena1 = input("ingresa una cadena:  ")

cadena2 = input("ingresa  otra cadena: ")

print("Este es el producto cartesiano: ")

for i in cadena1:

    for j in cadena2:

        print(f"{i}{j}", end= " ")