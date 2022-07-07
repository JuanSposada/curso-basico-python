# simulador de piedra-papel-tijera


#entrada de datos
print("1. piedra 💎\n2. papel 📰\n3. tijera ✂️\n")
player1 = int(input("jugador 1 - selecciona una opcion: "))
player2 = int(input("jugador 2 - selecciona una opcion: "))

if player1 == player2:
    print("empate")

elif player1 == 1 and player2 == 3:
    print("jugador 1 gana, piedra gana a tijera")
elif player1 == 1 and player2 == 2:
    print("🎉jugador 2 gana 🎉, papel gana a piedra")
elif player1 == 2 and player2 == 1:
    print("🎉jugador 1 gana🎉, papel gana a piedra")
elif player1 == 2 and player2 == 3:
    print("🎉jugador 2 gana🎉, tijera gana papel")
elif player1 == 3 and player2 == 1:
    print("🎉jugador 2 gana🎉, piedra vence a tijera")
elif player1 == 3 and player2 == 2:
    print("jugador 1 gana, tijera gana papel")
else: print("error valores incorrectos!! 💣"   )

    
