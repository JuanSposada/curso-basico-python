# este programa calcula el producto escalar de dos vectores

 

v1 = [4, 3, 8, 1]

v2 = [9, 2, 7, 3]

producto = 0

 

print("este es el vector 1: ",v1)

print("este es el vector 2: ",v2)

 

for num1, num2 in zip(v1, v2):

    producto += num1 * num2

   

else: print("este es el producto escalar: ", producto)