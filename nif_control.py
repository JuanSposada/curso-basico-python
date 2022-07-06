"""este programa calcula el digito de control de un nif"""

# entrada de variables

nif = int(input('ingrese su nif (8 digitos)'))

resto = nif % 23

letras_control = 'TRWAGMYFPDXBNJZSQVHLCKE'
print(f'este es su nif con digito de contro: {nif}{letras_control[resto]}')