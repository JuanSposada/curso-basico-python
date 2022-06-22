print("hola mundo")
name = input ("Cual es tu nombre?  ")
print("hola " + name)
edad = input("Caul es tu edad? ")
edad = int(edad)
print("hola " + name, "de ", edad, " años")
if edad >= 18 and edad < 99:
    print("\n!bienvenido al Play Boy!!\n")
    id = input("tienes identificacion? ")
    if id == 'no':
        print("casi la pegas wer@")
    else: 
        print("\npasale, ponte comodo y disfruta el show...\n")
        selector = 0 
        total = 0
        while selector != 5: 
            total= int(total) 
            print("este es el menu:")
            print("1. cheve  \n2. cubeta\n3. dollar  \n4. privado   \n5. es todo")
            selector = input("selecciona la opcion que deseas: ")
            selector = int(selector)
            if selector == 1: 
                cheve = 35
                print( f"\nmuy bien son:{cheve} pesos" )
                total= cheve + total
                print(f"van ... {total}" )
            elif selector == 2:
                cubeta = 350
                print(f"muy bien son {cubeta} pesos")
                total = cubeta + total
                print(f"van...{total} pesos")
            elif selector == 3:
                print("\nnosotros le podemos cambar sus pesos por billetes de 1 dollar")
                pesos = input("cuantos pesos quiere cambiar?")
                pesos = int(pesos)
                dollar = 20
                billetes = pesos / dollar
                billetes= int(billetes)                
                print(f"son: {billetes} billetes de 1 dollar\n")
            elif selector == 4:
                privado = 200
                print(f"muy bien son {privado} pesos..  " )
                total = privado + total
                print(f"van... {total} pesos" )
            elif selector == 5:
                print(f" muy bien amigo, el total a pagar es de: {total}")
                mdp = input( "metodo de pago? \n 1. efectivo \n 2. credito\n 3. se me olvido la cartera\n")
                if mdp == '1':
                    efectivo = input("Con cuanto vas a pagar?")
                    efectivo = int(efectivo)
                    cambio = efectivo - total
                    if cambio < 0:
                        print(f"te faltan {cambio} pesos")
                    elif cambio == 0:
                        print("...y la propina??")
                    else:
                        print(f"este es su cambio {cambio} no se olvide de mi propina")

                    print(f"este es su cambio {cambio}")


            else:
                print("esa no es una opcion")

   
  

elif edad > 99:
    print("pase bajo su propio riesgo...")
else:
    print("no puede pasar, prohibida la entrada a menores!")