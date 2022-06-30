def bill_pay(total):
    mdp = input( "metodo de pago? \n \n1. efectivo \n 2. credito\n 3. se me olvido la cartera\n")
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
    elif mdp == '2':
        print("por faciliteme su tarjeta")
        ppn = input("desea agregar propina del 15 % ?") 
        if ppn == 'si':
            total = total + (total * 0.15)
            print(f"con todo y propina se le cobraron: {total}")
        else: 
            print("de aqui no sales hasta que me pagues!!")
            bill_pay()


def show_menu():
    print("este es el menu")
    print("""\t1. cheve... 35 pesos
        2. cubeta... 350 pesos
        3. dollar  
        4. privado .. 200
        5. es todo""")

    
def user_id(name,edad):
    
    print("hola " + name, "de ", + edad, " años")  
    num_user =+ 1
    user_reg = str(num_user) + name + str(edad)
    print(user_reg)

def dollar_exchange():
     print("\nnosotros le podemos cambar sus pesos por billetes de 1 dollar")
     pesos = input("cuantos pesos quiere cambiar?")
     pesos = int(pesos)
     dollar = 20
     billetes = pesos // dollar
     print(f"son: {billetes} billetes de 1 dollar\n")

print("hola mundo")

 
name = input ("Cual es tu nombre?  ")
print("hola " + name)
edad = input("Caul es tu edad? ")
edad= int(edad)
user_id(name, edad)

if edad >= 18 and edad < 99:
    print("\n!bienvenido al Play Boy!!\n")
    id = input("\ntienes identificacion? ")
    if id == 'no':
        print("casi la pegas wer@")
    else: 
        print("""\nPasale! 
Ponte comodo 
y disfruta el show...\n""")
        selector = 0 
        total = 0

        while selector != 5: 
            show_menu()
            selector = int(input("selecciona la opcion que deseas: "))
            
            if selector == 1: 
                cheve = 35
                print( f"\nmuy bien son:{cheve} pesos" )
                total += cheve
                print(f"van ... {total}" )
            elif selector == 2:
                cubeta = 350
                print(f"muy bien son {cubeta} pesos")
                total += cubeta
                print(f"van...{total} pesos")
            elif selector == 3:
                dollar_exchange()
               
            elif selector == 4:
                privado = 200
                print(f"muy bien son {privado} pesos..  " )
                total += privado
                print(f"van... {total} pesos" )
            elif selector == 5:
                print(f" \nmuy bien amigo, el total a pagar es de: {total}")
                bill_pay(total)

               
                    

            else:
                print("esa no es una opcion")

   
  

elif edad > 99:
    print("no puede pasar, puede sufrir un paro cardiaco...")
else:
    print("no puede pasar, prohibida la entrada a menores!")