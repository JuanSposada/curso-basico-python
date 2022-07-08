# este programa lee 3 codigos de ejecucion



print(""" introduce las 3 teclas de los comandos:
1. sing out
2. comand palette
3. captura de pantalla \n""")

 

comando_1 = input('introduce la primera tecla: ')

comando_2 = input('introduce la segunda tecla: ')

comando_3 = input('introduce la tercera tecla: ')

 

if comando_1 == 'ctrl' and comando_2 == 'alt' and comando_3 == 'delete':
    print(f'{comando_1} + {comando_2} + {comando_3} = sing out')

elif comando_1 == 'ctrl' and comando_2 =='shift' and comando_3 == 'p':

    print(f'{comando_1} + {comando_2} + {comando_3} = command pallet')

elif comando_1 == 'windows' and comando_2 =='shift' and comando_3 == 's':

    print(f'{comando_1} + {comando_2} + {comando_3} = captura de pantalla')
else: print("error, comando no valido")
