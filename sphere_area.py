"""Este programa te da el area de una esfera en base al radio"""

PI = 3.14159265359  # declaracion de constante
radius= int(input("Ingrese el radio de la esfera: ")) # entrada del radio por el usuario

# formula para calcular el area de la esfera
volumen = 4/3 * PI * (radius ** 3)
print(volumen)
