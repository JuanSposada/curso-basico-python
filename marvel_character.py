"""Este proghrama adivina un personaye de Marvel"""

print("\nResponde las preguntas para adivinar que personaje de MARVEL es: \n")

# Entrada de datos

volar = (input("¿puede volar? (si/no): "))
human = (input("Es humano? (si/no): "))
mask = (input("usa mascara? (si/no): "))
if volar == "si":
    volar = True
elif volar == "no":
    volar = False
if human == "si":
    human = True
elif human == "no":
    human = False
if mask == "si":
    mask = True
elif mask == "no":
    mask = False
if volar and human and mask:
    print("Es Iron Man")
elif volar and human and not mask :
    print("es Capitana Marvel")
elif volar and not human and mask:
    print("es Ronan Accuser")
elif volar and not human and not mask: 
    print("Vision")
elif not volar and human and mask:
    print("es Spiderman")
elif not volar and human and not mask:
    print("es Hulk")
elif not volar and not human and mask:
    print(" es Black Bolt")
elif not volar and not human and not mask:
    print.upper("es Thanos")
else: print("valor incorrecto")

    
