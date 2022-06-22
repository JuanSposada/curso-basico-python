print("hola mundo")
name = input ("Cual es tu nombre?  ")
print(f"hola " + name)
edad = input("Caul es tu edad? ")
edad = int(edad)
print(f"hola " + name, "de ", edad, " años")
if edad >= 18 and edad < 99:
    print("!bienvenido al Play Boy!!")
    id = input("tienes identificacion? ")
    if id == 'no':
        print("casi la pegas wer@")
    else: print("pasale, ponte comodo y disfruta el show...")
    print("desea cambio de billetes de 1 dollar?")
    print("nosotros le podemos cambar")
    pesos = input("cuantos pesos quiere cambiar?")
    pesos = int(pesos)
    dollar = 20
    billetes = pesos / dollar
    billetes = int(billetes)
    billetes = str(billetes)
    print(f"son: " + billetes, " billetes de 1 dollar")
elif edad > 99:
    print("pase bajo su propio riesgo...")
else:
    print("no puede pasar, prohibida la entrada a menores!")