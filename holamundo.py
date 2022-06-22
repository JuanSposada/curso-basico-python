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
    else: 
        print("pasale, ponte comodo y disfruta el show...")
        selector = 0 
        total = 0
        while selector != 5: 
            total= int(total) 
            print("este es el menu:")
            print("1. cheve  \n2. cubeta\n3. dollar  \n4. privado   \n5. es todo")
            selector = input("selecciona la opcion que deseas: ")
            selector = int(selector)
            if selector == 1: 
                print( "muy bien son 35 pesos")
                total= int(total)
                cheve = 35
                total= cheve + total
                total = str(total)
                print(f"van ... " + total)
            elif selector == 2:
                total= int(total)
                print("muy bien son 350 pesos")
                cubeta = 350
                cubeta= int(cubeta)
                total = cubeta + total
                total = str(total)
                print(f"van..." + total)
            elif selector == 3:
                print("nosotros le podemos cambar sus pesos por billetes de 1 dollar")
                pesos = input("cuantos pesos quiere cambiar?")
                pesos = int(pesos)
                dollar = 20
                billetes = pesos / dollar
                billetes = int(billetes)
                billetes = str(billetes)
                print(f"son: " + billetes, " billetes de 1 dollar")
            elif selector == 4:
                privado = 200
                print("muy bien son 200..  " )
                total = privado + total
                total= str(total)
                print(f"van... " + total)
            elif selector == 5:
                total=str(total)
                print(f" muy bien amigo, el total a pagar es de: "+ total)
                mdp = input( "metodo de pago? \n 1. efectivo \n 2. efectivo\n 3. se me olvido la cartera")
                mdp =int(mdp)
                if mdp == 1:
                    efectivo = input("Con cuanto vas a pagar?")
                    efectivo = int(efectivo)
                    total= int(total)
                    cambio = total - efectivo
                    print(cambio)


            else:
                print("esa no es una opcion")

   
  

elif edad > 99:
    print("pase bajo su propio riesgo...")
else:
    print("no puede pasar, prohibida la entrada a menores!")