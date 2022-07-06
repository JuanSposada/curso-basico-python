"""dada una plabra, calcula la longitud de la misma y la multiplica
por el numero de vocales de la palabra"""

# entrada de datos
word = input('ingrese una palabra: ')
word_len = len(word)
vowels = (word.count('a') + word.count('e') \
    + word.count('i') + word.count('o') + word.count('u'))
print('este es el resultado: ',word_len * vowels)