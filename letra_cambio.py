"""este programa cambia la palabra voices por sounds en la cadena de texto """

song =	'''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness	'''		

print(song)

print("\nreemplazamos 'voices' por 'sounds'\n")

print(song[:139],'sounds', song[146:]) # partimos a trozos la cadena de texto, le añadimos el cambio
