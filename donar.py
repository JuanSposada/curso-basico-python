#este programa acepta los datos de una persona y le indica si es apto para donar

print(" \n Hola este programa te indicara si eres apto para donar \
    por favor ingresa tus datos: \n") 

edad = int(input('edad? '))

peso = int(input('peso? '))

pulso = int(input('pulso? '))

plaquetas = int(input('plaquetas?'))

 

if (edad > 18 and edad < 65) and (peso > 50) and (pulso > 50 and pulso < 110) and (plaquetas > 150000):

    print('Apto para donar 🤟')

else: print('no apto para donar ⚡')